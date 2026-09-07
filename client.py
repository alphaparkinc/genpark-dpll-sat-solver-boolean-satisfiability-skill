"""
DPLL SAT Solver Boolean Satisfiability Skill Client
Pure Python Standard Library implementation of the DPLL Algorithm (Davis, Putnam, Logemann, Loveland).
Solves Conjunctive Normal Form (CNF) formulas with unit propagation, pure literal elimination,
and chronological backtracking search.
"""

from typing import List, Dict, Any, Tuple, Optional, Set
import copy


class DPLLSolver:
    def __init__(self):
        pass

    def solve(self, cnf_clauses: List[List[int]]) -> Tuple[bool, Dict[int, bool]]:
        """
        Solve CNF formula.
        Variables are represented by non-zero integers (e.g. 1, -1, 2, -2).
        Returns (is_satisfiable, model_assignment).
        """
        clauses = [set(c) for c in cnf_clauses]
        assignment: Dict[int, bool] = {}
        sat, model = self._dpll(clauses, assignment)
        return sat, model

    def _dpll(self, clauses: List[Set[int]], assignment: Dict[int, bool]) -> Tuple[bool, Dict[int, bool]]:
        clauses, assignment = self._unit_propagate(clauses, assignment)
        clauses, assignment = self._pure_literal_eliminate(clauses, assignment)

        # Base conditions
        if any(len(c) == 0 for c in clauses):
            return False, {}
        if len(clauses) == 0:
            return True, assignment

        # Choose branching variable
        chosen_var = abs(next(iter(clauses[0])))

        # Branch True
        clauses_true = copy.deepcopy(clauses)
        assign_true = copy.deepcopy(assignment)
        assign_true[chosen_var] = True
        clauses_true = self._simplify(clauses_true, chosen_var)
        sat, res = self._dpll(clauses_true, assign_true)
        if sat:
            return True, res

        # Branch False
        clauses_false = copy.deepcopy(clauses)
        assign_false = copy.deepcopy(assignment)
        assign_false[chosen_var] = False
        clauses_false = self._simplify(clauses_false, -chosen_var)
        sat, res = self._dpll(clauses_false, assign_false)
        if sat:
            return True, res

        return False, {}

    def _simplify(self, clauses: List[Set[int]], assigned_literal: int) -> List[Set[int]]:
        new_clauses = []
        for c in clauses:
            if assigned_literal in c:
                continue  # Clause satisfied
            if -assigned_literal in c:
                new_c = set(c)
                new_c.remove(-assigned_literal)
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)
        return new_clauses

    def _unit_propagate(self, clauses: List[Set[int]], assignment: Dict[int, bool]) -> Tuple[List[Set[int]], Dict[int, bool]]:
        changed = True
        while changed:
            changed = False
            for c in clauses:
                if len(c) == 1:
                    lit = next(iter(c))
                    var = abs(lit)
                    assignment[var] = (lit > 0)
                    clauses = self._simplify(clauses, lit)
                    changed = True
                    break
        return clauses, assignment

    def _pure_literal_eliminate(self, clauses: List[Set[int]], assignment: Dict[int, bool]) -> Tuple[List[Set[int]], Dict[int, bool]]:
        all_literals = set()
        for c in clauses:
            all_literals.update(c)

        pure = []
        for lit in all_literals:
            if -lit not in all_literals:
                pure.append(lit)

        for lit in pure:
            var = abs(lit)
            assignment[var] = (lit > 0)
            clauses = self._simplify(clauses, lit)

        return clauses, assignment
