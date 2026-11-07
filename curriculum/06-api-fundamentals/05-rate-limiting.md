# Rate Limiting

[← Category](README.md) · [Learning path](../../README.md)

## Read first

Read [Rate Limiting](../../sources/karan/README.md#rate-limiting) in the unchanged source course.

## Companion example

Limit: 100 requests per minute. A fixed window may allow 100 just before a boundary and 100 just after. A token bucket controls refill and permits a configured burst. Two independent server-local counters can exceed a global limit.

Self-check: is your rule per user, per IP, per instance, or global?

## Continue

Return to the [category sequence](README.md) and mark your [daily schedule](../../SCHEDULE.md).
