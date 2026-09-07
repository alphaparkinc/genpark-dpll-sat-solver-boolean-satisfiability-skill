# GenPark DPLL SAT Solver Boolean Satisfiability Skill

Davis-Putnam-Logemann-Loveland (DPLL) Boolean CNF satisfiability solver with unit propagation and pure literal elimination.

Explore more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    A[CNF Formula Clauses] --> B[Unit Propagation]
    B --> C[Pure Literal Elimination]
    C --> D{Base Case Check}
    D -->|Empty Clause Found| E[Backtrack: UNSAT branch]
    D -->|All Clauses Satisfied| F[Return SAT with Model Assignment]
    D -->|Undetermined| G[Branch Variable x = True / False]
    G --> B
```

## Features
- Complete pure Python DPLL CNF solver.
- Fast unit clause reduction and pure literal simplification.
- Zero external dependencies.
