# Discovery: find instances, detect suspicion, and route safely

[← Animation index](README.md)

**Problem:** Find changing service instances without assuming that discovered health remains current.

**Scenario:** A caller discovers orders A and B; A fails before the next request.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Discovery: find instances, detect suspicion, and route safely](../assets/animations/discovery-heartbeat.gif)

## Read the same sequence without motion

1. **Publish available instances.** A and B register addresses and report health information. A heartbeat proves recent reachability, not every business dependencyâ€™s health.
   Readiness should reflect useful work; Registration is not permanent health.
2. **Discover candidates.** The resolver returns its candidate endpoint set to the caller. Discovery finds destinations; load-balancing policy chooses among them.
   A lookup can be cached; Freshness has a cost.
3. **Call a selected instance.** The caller reads order 42 from A successfully. A successful past request cannot guarantee the next request will succeed.
   Set realistic deadlines; Observe actual call outcomes.
4. **An endpoint becomes stale.** A fails after discovery, but the caller still has its old address. A registry response is a point-in-time observation.
   Failure can happen after lookup; Cached lists can outlive instances.
5. **Bound the failed call.** The next call to A times out rather than waiting forever. A timeout can indicate failure or delay; it is not infallible proof of a crash.
   Do not retry indefinitely; A write may have an unknown outcome.
6. **Mark A suspect.** Health policy times out A and stops advertising it as eligible. Detection thresholds trade response speed against false alarms.
   Heartbeat loss is suspicion; Readiness and liveness differ.
7. **Refresh the candidate set.** A bounded refresh replaces the callerâ€™s stale candidates with B. A long-lived client must have a way to learn membership changes.
   Honor configured refresh behavior; Avoid synchronized lookup storms.
8. **Use a safe retry.** The caller sends the safe order read to B and receives a result. A payment write needs an idempotency or reconciliation policy before retrying another instance.
   Discovery is not exactly-once delivery; Routing does not prove business safety.

**Design tradeoff:** Cached discovery reduces lookups but delays changes; fast failure detection increases false-suspicion risk.

[View all states as still images](../assets/animations/discovery-heartbeat-steps.png)

## Related lessons

- [Service Discovery](../curriculum/09-reliability-and-microservices/01-service-discovery.md)
- [HeartBeats](../curriculum/09-reliability-and-microservices/02-heartbeats.md)
