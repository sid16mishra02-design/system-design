# Distributed Transactions

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Distributed Transactions](../../sources/karan/README.md#distributed-transactions) in the unchanged source course.

## Companion example

An order and payment span services. Two-phase commit coordinates a commit decision; a saga uses local commits and compensating actions. Refunding a payment compensates for an order failure; it does not erase every external effect, such as an email.

Self-check: what should a customer see while compensation is still running?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
