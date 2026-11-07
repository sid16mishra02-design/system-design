# Transactions

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Transactions](../../sources/karan/README.md#transactions) in the unchanged source course.

## Companion example

Two buyers see one ticket. A transaction boundary alone does not prevent overselling: use an appropriate isolation level, locking, or an atomic conditional update. “Read stock; subtract one” can race.

Self-check: how would UPDATE stock SET quantity = quantity - 1 WHERE quantity > 0 help?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
