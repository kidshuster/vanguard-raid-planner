# Planner audit — 2026-10-07

## Implemented

- Compact session schema v7 exports one roster plus minimal generated member assignments. Fellowships and validation results are recalculated when restoring. Full template libraries, pending edits, and members removed since the last generation are preserved. Imports of versions 1–6 remain supported; earlier planner versions cannot import v7 exports.
- Template JSON exports omit indentation. Keys remain descriptive and files remain standard JSON.
- Candidate scores are reused within each team improvement search. Fellowship cache hits avoid constructing unused initial groups; identical class/spec/role swaps are skipped.
- When individual replacements stall, search considers coordinated character/spec changes for two selected players. Cheap staffing/variety scoring selects at most 16 pairs for full constraint evaluation per pass. Changes are accepted only if the existing total objective improves.

## Measured example

Using the supplied Default raid session in the Node VM harness: original formatted JSON 41,752 bytes; compact v7 snapshot 11,004 bytes, about 74% smaller. One raid assignment took approximately 331 ms before and 366 ms after. These are single measurements, not a broad benchmark or a speedup claim. Better search has a small cost in this case. The existing regression suite and added compact round-trip / coordinated-change tests pass.

## Remaining limitations and priorities

1. Generation and recommendation searches are synchronous. A Web Worker with progress/cancellation is the next performance priority for larger rosters and parallel schedules.
2. Schedule selection is sequential; later runs cannot generally repair early character choices. Parallel teams have an exchange pass, but there is no full-schedule optimum guarantee. Bounded multi-start scheduling plus cross-run repair is the next search-quality improvement.
3. Fellowship allocation is bounded local search. Hard and soft rules use weighted penalties rather than a formally lexicographic objective; sufficiently conflicting goals can trade off. A structured objective (hard violations, coverage/fairness, preferred goals) would make priorities more predictable.
4. Cooldown selection uses a fast capacity estimate during selection and a greedy simulation for final validation. A failed greedy rotation does not prove no valid rotation exists. Bounded alternate rotations or a solver should precede any claim of infeasibility.
5. Export schema remains verbose in configuration libraries to preserve readability and compatibility. Compression and library deduplication are optional future work; avoid eliminating user templates from session backups.

No changes were pushed to the public GitHub repository. The review site carries these changes.

## Follow-up implemented

Generation now runs in a cancellable Web Worker with a spinner and stage messages. Schedule-wide repair and a bounded alternate-start final pass address early sequential choices and local minima. Required deficits and coverage have explicit priority in this pass. Cooldown validation remains a greedy simulation; no exact solver or global optimality guarantee was introduced. Worker/controller tests cover DOM-free execution, progress, cancellation, stale responses, failures and atomic commit. Search regressions cover parallel swaps, early-only availability and escape through a worse intermediate layout. The supplied one-raid sample remains valid; complete generation including recommendations took about 1.35 seconds in the Node harness.
