# Replication: write, lag, read, and restore

[← Animation index](README.md)

**Problem:** Use data copies for reads and recovery while recognizing lag and propagated mistakes.

**Scenario:** An address changes from V1 to V2; a later accidental deletion reaches both live copies.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Replication: write, lag, read, and restore](../assets/animations/replication.gif)

## Read the same sequence without motion

1. **One update, two views.** An address changes, but a reader sees its old value. Which copies and timing could explain that?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** When may the writer see success; Which copy served the reader.
2. **Commit without waiting.** The primary commits V2 and acknowledges under this example's asynchronous replication policy.
   - **Why it matters:** An acknowledged primary write need not already be applied on every replica.
   - **Notice:** This demo uses asynchronous copying; Acknowledgement policy is configurable.
3. **Read during lag.** A reader queries the replica before the change arrives and receives V1.
   - **Why it matters:** Route reads according to their required freshness, not merely lower load.
   - **Notice:** Old read is possible during lag; A healthy replica can still be stale.
4. **Apply the change.** The replication stream carries V2 to the replica, which applies it.
   - **Why it matters:** Asynchronous replication has a propagation stage that may take variable time.
   - **Notice:** Monitor lag, not only connectivity; Replicated order must be respected.
5. **Read after catch-up.** A later replica read sees V2 after the change has been applied.
   - **Why it matters:** Eventual visibility depends on successful propagation and application.
   - **Notice:** A particular read can still race updates; No promise of instant equal state.
6. **Choose a fresher path.** A freshness-sensitive read uses the appropriate authoritative path instead of an arbitrary lagging copy.
   - **Why it matters:** Read guarantees require a complete routing and consistency protocol.
   - **Notice:** Waiting for replicas can cost latency; Failover needs an explicit policy.
7. **Delete the wrong data.** An accidental deletion commits on the primary; live replication does not know it was a mistake.
   - **Why it matters:** More live copies do not automatically preserve older correct data.
   - **Notice:** Bad writes can be valid database work; Backup retention serves another purpose.
8. **Copy the mistake too.** The deletion propagates, so both primary and replica now lack the address.
   - **Why it matters:** Replication is not a substitute for historical recovery.
   - **Notice:** Replicas can copy logical errors; Restore points may lose newer changes.
9. **Test an isolated restore.** The backup restores V1 in a sandbox, proving which historical data that restore point can recover.
   - **Why it matters:** A usable backup requires a tested restore procedure and explicit recovery objectives.
   - **Notice:** Restore is isolated from live writes; V2 is newer than this snapshot.

**Design tradeoff:** Asynchronous copies can lag; waiting for acknowledgements costs latency, and historical backups still need restore testing.

[View all states as still images](../assets/animations/replication-steps.png)

## Related lessons

- [Database Replication](../curriculum/03-databases/10-database-replication.md)
- [Strong vs eventual consistency](../practice/TRADEOFFS.md)
