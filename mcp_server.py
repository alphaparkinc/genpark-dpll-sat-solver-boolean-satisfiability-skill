"""
MCP Server for DPLL SAT Solver Boolean Satisfiability Skill
"""

import json
import sys
from client import DPLLSolver

solver = DPLLSolver()

def handle_call(name: str, args: dict) -> dict:
    if name == "solve_cnf":
        clauses = args.get("clauses", [])
        is_sat, model = solver.solve(clauses)
        return {"satisfiable": is_sat, "model": model}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
