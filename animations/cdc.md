# CDC: capture commits, update views, and replay safely

[← Animation index](README.md)

**Problem:** Keep a search view updated without independently double-writing every application request.

**Scenario:** A price commit reaches search after lag, then appears again during connector recovery.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![CDC: capture commits, update views, and replay safely](../assets/animations/cdc.gif)

## Read the same sequence without motion

1. **Change the source.** The writer updates product 42; the transaction has not yet been acknowledged.
   - **Why it matters:** The source database, not search, decides whether the original write commits.
   - **Notice:** Identify the authoritative store; Derived views are separate.
2. **Commit durably.** The transaction log records the commit before successful acknowledgement.
   - **Why it matters:** A source commit does not imply immediate downstream visibility.
   - **Notice:** Search can still show 500; Durability follows the DB contract.
3. **Read the committed change.** The connector reads position 100 after its checkpoint.
   - **Why it matters:** A restart position is part of the data pipelineâ€™s correctness, not just performance.
   - **Notice:** Initial snapshot needs coordination; Only committed changes are exposed.
4. **Publish downstream.** E10 reaches the change stream while search still has version nine.
   - **Why it matters:** Each stage can introduce lag even while all processes are healthy.
   - **Notice:** Carry stable product identity; Handle deletes and schema changes.
5. **A consumer stalls.** The consumer pauses; source writes continue but search freshness degrades.
   - **Why it matters:** Watch retained-log growth as well as destination lag.
   - **Notice:** Retention cannot be ignored; Bound downstream pressure.
6. **Apply and checkpoint.** The consumer updates product 42 and records recoverable progress.
   - **Why it matters:** Coordinate the index effect and replay behavior; do not assume transport delivery is exactly once.
   - **Notice:** Upsert by product ID; Use a suitable version rule.
7. **Return the updated view.** A search reader now sees price 550.
   - **Why it matters:** Measure commit-to-visible delay, not just connector request latency.
   - **Notice:** Source and view have different roles; Authoritative checkout may read source.
8. **Restart from an older point.** Recovery resumes before E10 and emits it again.
   - **Why it matters:** Replaying a durable log is expected recovery behavior.
   - **Notice:** Checkpoint may precede last effect; A lost log segment needs a plan.
9. **Keep the result correct.** The version rule makes repeated E10 harmless; search remains at 550.
   - **Why it matters:** Batching can reduce overhead, but its waiting time still counts toward freshness.
   - **Notice:** Ignore stale version regressions; Test replay and connector downtime.

**Design tradeoff:** CDC reduces repeated scans but adds lag, schema coupling, log retention, and replay responsibilities.

[View all states as still images](../assets/animations/cdc-steps.png)

## Related lessons

- [Change Data Capture (CDC)](../curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md)
