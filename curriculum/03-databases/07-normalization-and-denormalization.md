# Normalization and Denormalization

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Normalization and Denormalization](../../sources/karan/README.md#normalization-and-denormalization) in the unchanged source course.

## Companion example

Store a customer’s address once and orders reference the customer: less duplication. Copy an address onto each order: faster historical reads and a record of the delivery address at purchase time. That snapshot has different meaning from the customer’s current address.

Self-check: should changing a profile address alter an already-shipped order?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
