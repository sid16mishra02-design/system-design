# ACID and BASE consistency models

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [ACID and BASE consistency models](../../sources/karan/README.md#acid-and-base-consistency-models) in the unchanged source course.

## Companion example

ACID consistency means a transaction preserves declared invariants. Distributed consistency describes what different readers observe across replicas. These are different uses of “consistency.” A replicated SQL database can use ACID locally while replicas lag.

Self-check: can an order commit correctly while a replica still shows the old order list?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
