"""
RouterLang Deploy Module
=========================
Pushes generated per-device config files to real network devices via NAPALM.

Supported vendors:
    cisco      — NAPALM driver: ios
    junos      — NAPALM driver: junos
    openconfig — NOT directly deployable via NAPALM (JSON format, use RESTCONF)

Deployment modes:
    normal     — diff then apply if changes exist
    dry-run    — diff only, never apply anything

Credentials are read from a credentials.ini file:

    [defaults]
    username = admin
    password = secret
    ssh_port = 22

Usage (from main.py):
    python main.py my_network.rl --generate --deploy --ipam ipam.csv
    python main.py my_network.rl --generate --deploy --dry-run --ipam ipam.csv
    python main.py my_network.rl --generate --deploy --creds credentials.ini --ipam ipam.csv

Requirements:
    pip install napalm
"""

import os
import sys
import configparser
from datetime import datetime

# ── ANSI colours (same as main.py) ────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GREY   = "\033[90m"
WHITE  = "\033[97m"


# ===============================================================================
# Credentials loader
# ===============================================================================

def load_credentials(creds_path: str = "credentials.ini") -> dict:
    """
    Load SSH credentials from a .ini file.

    Expected format:
        [defaults]
        username = admin
        password = secret
        ssh_port = 22

    Falls back to prompting the user if the file is not found.
    NEVER hardcode credentials — always use this file or environment variables.
    """
    creds = {"username": "", "password": "", "ssh_port": 22}

    if creds_path and os.path.isfile(creds_path):
        cfg = configparser.ConfigParser()
        cfg.read(creds_path)
        section = "defaults" if cfg.has_section("defaults") else cfg.sections()[0] if cfg.sections() else None
        if section:
            creds["username"] = cfg.get(section, "username", fallback="")
            creds["password"] = cfg.get(section, "password", fallback="")
            creds["ssh_port"] = cfg.getint(section, "ssh_port", fallback=22)

    # Fall back to prompting if anything is missing
    if not creds["username"]:
        creds["username"] = input("  SSH username: ").strip()
    if not creds["password"]:
        import getpass
        creds["password"] = getpass.getpass("  SSH password: ")

    return creds


# ===============================================================================
# NAPALM driver map
# ===============================================================================

# Maps RouterLang vendor names to NAPALM driver names
_NAPALM_DRIVERS = {
    "cisco": "ios",
    "junos": "junos",
}


def _get_napalm_driver(vendor: str):
    """Return the NAPALM driver class for the given vendor string."""
    try:
        import napalm
    except ImportError:
        print(f"\n  {RED}✗  NAPALM is not installed.{RESET}")
        print(f"  {GREY}Run: pip install napalm{RESET}\n")
        sys.exit(1)

    driver_name = _NAPALM_DRIVERS.get(vendor.lower())
    if driver_name is None:
        raise ValueError(
            f"Vendor '{vendor}' is not supported for direct deployment. "
            f"Supported: {', '.join(_NAPALM_DRIVERS.keys())}. "
            f"For OpenConfig, use RESTCONF/NETCONF directly."
        )
    return napalm.get_network_driver(driver_name)


# ===============================================================================
# Deploy result dataclass
# ===============================================================================

class DeployResult:
    """Holds the outcome of deploying to a single device."""

    STATUS_SUCCESS  = "SUCCESS"
    STATUS_NO_CHANGE = "NO CHANGE"
    STATUS_DRY_RUN  = "DRY RUN"
    STATUS_SKIPPED  = "SKIPPED"
    STATUS_FAILED   = "FAILED"

    def __init__(self, hostname, mgmt_ip, status, diff="", error=""):
        self.hostname  = hostname
        self.mgmt_ip   = mgmt_ip
        self.status    = status
        self.diff      = diff
        self.error     = error
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ===============================================================================
# Core deploy function
# ===============================================================================

def deploy_configs(
    generated_files: list,
    ipam:            dict,
    vendor:          str,
    creds:           dict,
    dry_run:         bool = False,
) -> list:
    """
    Push generated config files to their respective devices via NAPALM.

    Parameters
    ----------
    generated_files  List of file paths, e.g. ['output/my_network/R-SPINE-1.conf']
    ipam             {hostname: {loopback_ip, mgmt_ip}} from load_ipam()
    vendor           "cisco" or "junos"
    creds            {username, password, ssh_port} from load_credentials()
    dry_run          If True, show diffs but never commit

    Returns
    -------
    List of DeployResult objects, one per device.
    """

    if vendor == "openconfig":
        print(f"\n  {YELLOW}⚠   OpenConfig JSON cannot be pushed directly via NAPALM.{RESET}")
        print(f"  {GREY}Use NETCONF/RESTCONF to push OpenConfig configs.{RESET}")
        return []

    driver = _get_napalm_driver(vendor)
    results = []

    mode_label = "DRY RUN — no changes will be applied" if dry_run else "LIVE DEPLOY"
    print(f"\n  {BOLD}{CYAN}── Deploying {len(generated_files)} device(s)  [{mode_label}] {'─' * 20}{RESET}")

    for cfg_path in generated_files:

        # Derive hostname from filename: output/my_network/R-SPINE-1.conf → R-SPINE-1
        hostname = os.path.splitext(os.path.basename(cfg_path))[0]

        # Look up management IP from IPAM
        device_info = ipam.get(hostname, {})
        mgmt_ip     = device_info.get("mgmt_ip", "")

        if not mgmt_ip:
            msg = "no mgmt_ip in IPAM — cannot connect"
            print(f"  {YELLOW}⚠   {hostname:<20}{RESET}  {YELLOW}SKIPPED  {GREY}{msg}{RESET}")
            results.append(DeployResult(hostname, "", DeployResult.STATUS_SKIPPED, error=msg))
            continue

        print(f"  {GREY}→   {hostname:<20}  {mgmt_ip}{RESET}", end="", flush=True)

        # Open connection
        device = driver(
            hostname = mgmt_ip,
            username = creds["username"],
            password = creds["password"],
            optional_args = {"port": creds.get("ssh_port", 22)},
        )

        try:
            device.open()

            # Load the generated config (merge mode — adds/changes, does not wipe device)
            device.load_merge_candidate(filename=cfg_path)

            # Diff: what would change on the device
            diff = device.compare_config()

            if not diff:
                device.discard_config()
                print(f"  {GREEN}NO CHANGE{RESET}")
                results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_NO_CHANGE))

            elif dry_run:
                device.discard_config()
                print(f"  {CYAN}DRY RUN{RESET}")
                _print_diff(diff)
                results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_DRY_RUN, diff=diff))

            else:
                device.commit_config()
                print(f"  {GREEN}SUCCESS{RESET}")
                _print_diff(diff)
                results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_SUCCESS, diff=diff))

        except Exception as e:
            try:
                device.discard_config()
            except Exception:
                pass
            print(f"  {RED}FAILED{RESET}")
            print(f"    {RED}{e}{RESET}")
            results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_FAILED, error=str(e)))

        finally:
            try:
                device.close()
            except Exception:
                pass

    return results


def _print_diff(diff: str):
    """Print a config diff with green/red colouring for added/removed lines."""
    for line in diff.splitlines():
        if line.startswith("+"):
            print(f"    {GREEN}{line}{RESET}")
        elif line.startswith("-"):
            print(f"    {RED}{line}{RESET}")
        else:
            print(f"    {GREY}{line}{RESET}")


# ===============================================================================
# Deploy summary printer
# ===============================================================================

def print_deploy_summary(results: list):
    """Print a summary table of all deploy results."""
    if not results:
        return

    print(f"\n  {BOLD}{WHITE}── Deploy Summary {'─' * 40}{RESET}")

    counts = {
        DeployResult.STATUS_SUCCESS:   0,
        DeployResult.STATUS_NO_CHANGE: 0,
        DeployResult.STATUS_DRY_RUN:   0,
        DeployResult.STATUS_SKIPPED:   0,
        DeployResult.STATUS_FAILED:    0,
    }

    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
        if r.status == DeployResult.STATUS_SUCCESS:
            colour = GREEN
        elif r.status == DeployResult.STATUS_NO_CHANGE:
            colour = GREEN
        elif r.status == DeployResult.STATUS_DRY_RUN:
            colour = CYAN
        elif r.status == DeployResult.STATUS_SKIPPED:
            colour = YELLOW
        else:
            colour = RED

        ip_str = f"  {r.mgmt_ip}" if r.mgmt_ip else ""
        print(f"  {BOLD}{r.hostname:<22}{RESET}  {colour}{r.status:<12}{RESET}{GREY}{ip_str}{RESET}")
        if r.error:
            print(f"    {RED}└─ {r.error}{RESET}")

    print()
    print(f"  {GREEN}Success : {counts[DeployResult.STATUS_SUCCESS]}{RESET}  "
          f"{GREEN}No change: {counts[DeployResult.STATUS_NO_CHANGE]}{RESET}  "
          f"{CYAN}Dry run : {counts[DeployResult.STATUS_DRY_RUN]}{RESET}  "
          f"{YELLOW}Skipped : {counts[DeployResult.STATUS_SKIPPED]}{RESET}  "
          f"{RED}Failed  : {counts[DeployResult.STATUS_FAILED]}{RESET}")


# ===============================================================================
# Deploy log writer
# ===============================================================================

def write_deploy_log(results: list, log_dir: str = "logs") -> str:
    """
    Write a timestamped deploy log to logs/<timestamp>.log
    Returns the path of the written log file.
    """
    os.makedirs(log_dir, exist_ok=True)
    ts       = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir, f"deploy_{ts}.log")

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"RouterLang Deploy Log — {ts}\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"Device    : {r.hostname}\n")
            f.write(f"Mgmt IP   : {r.mgmt_ip}\n")
            f.write(f"Status    : {r.status}\n")
            f.write(f"Timestamp : {r.timestamp}\n")
            if r.diff:
                f.write("Diff:\n")
                for line in r.diff.splitlines():
                    f.write(f"  {line}\n")
            if r.error:
                f.write(f"Error     : {r.error}\n")
            f.write("\n")

    return log_path