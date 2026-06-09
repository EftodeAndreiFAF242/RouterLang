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
    simulate   — no SSH at all; reads the config files and shows what would happen

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
    pip install napalm   (only needed for real deployment, not for simulate mode)
"""

import os
import sys
import time
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
# Simulation mode toggle
# ===============================================================================
# Set to True to simulate deployment without real SSH connections.
# The compiler will read each generated config file, compute a realistic diff,
# and report SUCCESS for every reachable device — no NAPALM or SSH required.
#
# Set to False for real deployment via NAPALM to actual network devices.

SIMULATE_DEPLOY = True


# ===============================================================================
# Per-device SSH port overrides (for lab / simulated environments)
# ===============================================================================

DEVICE_PORTS = {
    "R-SPINE-1": 6001,
    "R-SPINE-2": 6002,
    "R-LEAF-1":  6003,
    "R-LEAF-2":  6004,
    "R-LEAF-3":  6005,
    "R-LEAF-4":  6006,
    "R-EDGE-1":  6007,
    "R-EDGE-2":  6008,
}

# To switch to production mode:
# SIMULATE_DEPLOY = False
# DEVICE_PORTS = {}


# ===============================================================================
# Credentials loader
# ===============================================================================

def load_credentials(creds_path: str = "credentials.ini") -> dict:
    creds = {"username": "", "password": "", "ssh_port": 22}

    if creds_path and os.path.isfile(creds_path):
        cfg = configparser.ConfigParser()
        cfg.read(creds_path)
        section = "defaults" if cfg.has_section("defaults") else cfg.sections()[0] if cfg.sections() else None
        if section:
            creds["username"] = cfg.get(section, "username", fallback="")
            creds["password"] = cfg.get(section, "password", fallback="")
            creds["ssh_port"] = cfg.getint(section, "ssh_port", fallback=22)

    if not creds["username"]:
        creds["username"] = input("  SSH username: ").strip()
    if not creds["password"]:
        import getpass
        creds["password"] = getpass.getpass("  SSH password: ")

    return creds


# ===============================================================================
# NAPALM driver map
# ===============================================================================

_NAPALM_DRIVERS = {
    "cisco": "ios",
    "junos": "junos",
}


def _get_napalm_driver(vendor: str):
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
# Simulated deploy (no SSH, no NAPALM)
# ===============================================================================

def _simulate_deploy(
    generated_files: list,
    ipam:            dict,
    dry_run:         bool = False,
) -> list:
    results = []
    mode_label = "DRY RUN — simulated" if dry_run else "SIMULATED DEPLOY"
    print(f"\n  {BOLD}{CYAN}── Deploying {len(generated_files)} device(s)  [{mode_label}] {'─' * 20}{RESET}")

    for cfg_path in generated_files:
        hostname = os.path.splitext(os.path.basename(cfg_path))[0]
        device_info = ipam.get(hostname, {})
        mgmt_ip     = device_info.get("mgmt_ip", "")
        ssh_port    = DEVICE_PORTS.get(hostname, 22)

        if not mgmt_ip:
            msg = "no mgmt_ip in IPAM — cannot connect"
            print(f"  {YELLOW}⚠   {hostname:<20}{RESET}  {YELLOW}SKIPPED  {GREY}{msg}{RESET}")
            results.append(DeployResult(hostname, "", DeployResult.STATUS_SKIPPED, error=msg))
            continue

        print(f"  {GREY}→   {hostname:<20}  {mgmt_ip}:{ssh_port}{RESET}", end="", flush=True)

        # Simulate a brief connection delay
        time.sleep(0.3)

        # Read the generated config to build a realistic diff
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                config_lines = f.readlines()
        except Exception as e:
            print(f"  {RED}FAILED{RESET}")
            print(f"    {RED}Cannot read config file: {e}{RESET}")
            results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_FAILED, error=str(e)))
            continue

        # Build diff: every config line shown as added (simulating fresh device)
        diff_lines = []
        for line in config_lines:
            stripped = line.rstrip()
            if stripped and not stripped.startswith("!"):
                diff_lines.append(f"+{stripped}")

        diff = "\n".join(diff_lines)

        if dry_run:
            print(f"  {CYAN}DRY RUN{RESET}")
            _print_diff(diff)
            results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_DRY_RUN, diff=diff))
        else:
            print(f"  {GREEN}SUCCESS{RESET}")
            _print_diff(diff)
            results.append(DeployResult(hostname, mgmt_ip, DeployResult.STATUS_SUCCESS, diff=diff))

    return results


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
    if vendor == "openconfig":
        print(f"\n  {YELLOW}⚠   OpenConfig JSON cannot be pushed directly via NAPALM.{RESET}")
        print(f"  {GREY}Use NETCONF/RESTCONF to push OpenConfig configs.{RESET}")
        return []

    # ── Simulation mode: skip NAPALM entirely ──
    if SIMULATE_DEPLOY:
        return _simulate_deploy(generated_files, ipam, dry_run)

    # ── Real deployment via NAPALM ──
    driver = _get_napalm_driver(vendor)
    results = []

    mode_label = "DRY RUN — no changes will be applied" if dry_run else "LIVE DEPLOY"
    print(f"\n  {BOLD}{CYAN}── Deploying {len(generated_files)} device(s)  [{mode_label}] {'─' * 20}{RESET}")

    for cfg_path in generated_files:

        hostname = os.path.splitext(os.path.basename(cfg_path))[0]
        device_info = ipam.get(hostname, {})
        mgmt_ip     = device_info.get("mgmt_ip", "")

        if not mgmt_ip:
            msg = "no mgmt_ip in IPAM — cannot connect"
            print(f"  {YELLOW}⚠   {hostname:<20}{RESET}  {YELLOW}SKIPPED  {GREY}{msg}{RESET}")
            results.append(DeployResult(hostname, "", DeployResult.STATUS_SKIPPED, error=msg))
            continue

        ssh_port = DEVICE_PORTS.get(hostname, creds.get("ssh_port", 22))

        print(f"  {GREY}→   {hostname:<20}  {mgmt_ip}:{ssh_port}{RESET}", end="", flush=True)

        device = driver(
            hostname = mgmt_ip,
            username = creds["username"],
            password = creds["password"],
            optional_args = {"port": ssh_port},
        )

        try:
            device.open()
            device.load_merge_candidate(filename=cfg_path)
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