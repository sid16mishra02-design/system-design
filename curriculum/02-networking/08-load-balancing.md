# Load Balancing

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Load Balancing](../../sources/karan/README.md#load-balancing) in the unchanged source course.

## Companion example

Draw client → load balancer → servers A/B → shared database. Adding B spreads application work but does not double database capacity. If A holds sessions in memory, a later request routed to B may lose its session.

Self-check: where could session state live so either server can handle the next request?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
