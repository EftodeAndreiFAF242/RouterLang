class SemanticError(Exception):
    pass

class SemanticChecker:
    def __init__(self):
        self.roles = {}        # role name -> count range
        self.links = []        # list of (r1, r2) pairs
        self.policies = {}     # policy name -> list of ranks

    def check_role_decl(self, name, low, high=None):
        # E-1: Duplicate role name
        if name in self.roles:
            raise SemanticError(f"E-1: Duplicate role name '{name}'")
        # E-2: count = 0
        if low == 0:
            raise SemanticError(f"E-2: Role '{name}' has count 0 — meaningless")
        # E-3: lower bound > upper bound
        if high is not None and low > high:
            raise SemanticError(f"E-3: Role '{name}' range {low}..{high} is invalid — lower > upper")
        self.roles[name] = (low, high)
        print(f"  ✅ Role '{name}' declared OK")

    def check_link_decl(self, r1, r2):
        # E-4: Role not declared
        if r1 not in self.roles:
            raise SemanticError(f"E-4: Link references undeclared role '{r1}'")
        if r2 not in self.roles:
            raise SemanticError(f"E-4: Link references undeclared role '{r2}'")
        # E-6: Reflexive edge
        if r1 == r2:
            raise SemanticError(f"E-6: Reflexive link '{r1} -- {r2}' is not allowed")
        # E-5: Duplicate edge (warning only)
        if (r1, r2) in self.links or (r2, r1) in self.links:
            print(f"  ⚠️  WARNING E-5: Duplicate link '{r1} -- {r2}' — merged")
        else:
            self.links.append((r1, r2))
            print(f"  ✅ Link '{r1} -- {r2}' declared OK")

    def check_policy_rank(self, policy_name, rank):
        # E-7: Duplicate rank within same policy
        if policy_name not in self.policies:
            self.policies[policy_name] = []
        if rank in self.policies[policy_name]:
            raise SemanticError(f"E-7: Duplicate rank {rank} in policy '{policy_name}'")
        self.policies[policy_name].append(rank)
        print(f"  ✅ Policy '{policy_name}' rank {rank} OK")

    def check_path_expr(self, roles_in_path):
        # E-10: Role in path not declared
        for r in roles_in_path:
            if r not in self.roles:
                raise SemanticError(f"E-10: Path references undeclared role '{r}'")
        # E-11: No link between consecutive roles
        for i in range(len(roles_in_path) - 1):
            r1 = roles_in_path[i]
            r2 = roles_in_path[i + 1]
            if (r1, r2) not in self.links and (r2, r1) not in self.links:
                raise SemanticError(f"E-11: No link between '{r1}' and '{r2}' in topology")
        print(f"  ✅ Path {' >> '.join(roles_in_path)} is valid")


# ========== RUN SEMANTIC TESTS ==========

print("\n--- Test 1: Valid topology ---")
try:
    checker = SemanticChecker()
    checker.check_role_decl("r1", 1)
    checker.check_role_decl("r2", 1)
    checker.check_link_decl("r1", "r2")
    checker.check_path_expr(["r1", "r2"])
    print("✅ PASSED\n")
except SemanticError as e:
    print(f"❌ FAILED: {e}\n")

print("--- Test 2: Duplicate role name ---")
try:
    checker = SemanticChecker()
    checker.check_role_decl("r1", 1)
    checker.check_role_decl("r1", 2)
    print("❌ FAILED — should have been rejected\n")
except SemanticError as e:
    print(f"✅ CORRECTLY REJECTED: {e}\n")

print("--- Test 3: Invalid range lower > upper ---")
try:
    checker = SemanticChecker()
    checker.check_role_decl("r1", 5, 2)
    print("❌ FAILED — should have been rejected\n")
except SemanticError as e:
    print(f"✅ CORRECTLY REJECTED: {e}\n")

print("--- Test 4: Reflexive link ---")
try:
    checker = SemanticChecker()
    checker.check_role_decl("r1", 1)
    checker.check_link_decl("r1", "r1")
    print("❌ FAILED — should have been rejected\n")
except SemanticError as e:
    print(f"✅ CORRECTLY REJECTED: {e}\n")

print("--- Test 5: Path with undeclared role ---")
try:
    checker = SemanticChecker()
    checker.check_role_decl("r1", 1)
    checker.check_role_decl("r2", 1)
    checker.check_link_decl("r1", "r2")
    checker.check_path_expr(["r1", "r2", "r3"])
    print("❌ FAILED — should have been rejected\n")
except SemanticError as e:
    print(f"✅ CORRECTLY REJECTED: {e}\n")

print("--- Test 6: Duplicate rank in policy ---")
try:
    checker = SemanticChecker()
    checker.check_policy_rank("P", 10)
    checker.check_policy_rank("P", 10)
    print("❌ FAILED — should have been rejected\n")
except SemanticError as e:
    print(f"✅ CORRECTLY REJECTED: {e}\n")