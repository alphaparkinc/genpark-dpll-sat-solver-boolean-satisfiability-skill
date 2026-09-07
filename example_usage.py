"""
Demonstration of DPLL SAT Solver Boolean Satisfiability Skill
"""

from client import DPLLSolver

def main():
    print("=== Testing DPLL Boolean Satisfiability (SAT) Solver ===")
    solver = DPLLSolver()

    # Problem 1: Satisfiable CNF
    # (x1 OR x2) AND (NOT x1 OR x3) AND (NOT x2 OR NOT x3)
    cnf_sat = [
        [1, 2],
        [-1, 3],
        [-2, -3]
    ]
    print("Evaluating Problem 1 (Satisfiable CNF):", cnf_sat)
    is_sat, model = solver.solve(cnf_sat)
    print(f"Result: is_satisfiable={is_sat}, Model={model}")
    assert is_sat is True

    # Problem 2: Unsatisfiable CNF
    # (x1) AND (NOT x1)
    cnf_unsat = [
        [1],
        [-1]
    ]
    print("\nEvaluating Problem 2 (Unsatisfiable CNF):", cnf_unsat)
    is_sat_2, model_2 = solver.solve(cnf_unsat)
    print(f"Result: is_satisfiable={is_sat_2}, Model={model_2}")
    assert is_sat_2 is False

    print("\nDPLL SAT Solver Verification PASS!")

if __name__ == "__main__":
    main()
