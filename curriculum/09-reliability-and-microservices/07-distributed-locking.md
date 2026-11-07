# Distributed Locking

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Coordinate work across processes carefully

A distributed lock tries to give one participant temporary ownership of work shared across machines. A local language mutex only coordinates within its own process or runtime.

Imagine two workers generating a monthly report. A shared lock can reduce simultaneous execution. But worker A may pause so long that its lease expires. Worker B acquires a new lease, then A resumes and continues writing. Both now believe they have work to do.

A **lease** is ownership valid until a deadline. A **fencing token** is a number that increases each time ownership is granted; the protected resource checks it. If B has a newer token, the resource can reject A's stale write. This works only if the resource actually enforces the check.

The design must specify ownership, expiry, renewal, safe release, and what happens during network partitions. A lock alone does not guarantee exactly-once execution. A uniqueness constraint, conditional write, or idempotent operation can sometimes express the invariant more directly.

**Check:** “the lease expired” does not mean the former holder has physically stopped running.

## Optional further reading


- [Distributed locks and fencing](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)

The lesson above is complete enough for this curriculum; external links are for deeper study.
