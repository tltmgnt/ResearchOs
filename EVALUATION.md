# Controlled evaluation protocol (proposed)

**Primary outcome:** false acceptance rate of invalid claims.

Compare: (A) human reviewers, (B) single model, (C) unstructured multi-agent, (D) matched multi-agent plus TECT. Use identical tasks, tools and comparable time/compute budgets where possible. Keep a held-out test set. Establish ground truth independently (formal proof checkers for suitable tasks, expert adjudication otherwise).

Report false acceptance, false rejection, uncertain rate, audit reconstruction time, verified claims per unit cost, and confidence intervals. Conduct ablations removing dependency tracking, transition guards, and adversarial evaluation. Pre-register scoring and clarify how UNCERTAIN outcomes are treated. Proposed targets are not measured results.
