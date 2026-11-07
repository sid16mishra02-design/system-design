# Circuit breaker

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Circuit breaker](../../sources/karan/README.md#circuit-breaker) in the unchanged source course.

## Companion example

Closed: calls flow. Repeated failures open the breaker: calls fail fast. After a delay, half-open permits limited probes. A timeout bounds one call; a breaker reacts to a pattern of failures.

Self-check: what safe fallback exists when the payment breaker is open?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
