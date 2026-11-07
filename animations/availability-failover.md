# Availability: replace, reroute, and inspect dependencies

[← Animation index](README.md)

**Problem:** Keep a required operation reachable when individual components fail.

**Scenario:** Checkout has two application instances but shares one database.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Availability: replace, reroute, and inspect dependencies](../assets/animations/availability-failover.gif)

## Read the same sequence without motion

1. **Trace a working checkout.** The customer reaches A, which commits the order in the shared database.
   - **Why it matters:** Measure the whole operation, not just whether an instance responds.
   - **Notice:** Router and database are dependencies; A successful process ping is narrower.
2. **Instance A fails.** A stops serving; the monitor observes failed readiness checks.
   - **Why it matters:** Having B does not help until callers stop routing new work to A.
   - **Notice:** Detection takes time; In-flight work may fail.
3. **Remove A from routing.** The router learns that B is the usable destination.
   - **Why it matters:** Readiness information must actually affect the traffic path.
   - **Notice:** Cached routes can be stale; Retries must be safe for the write.
4. **The survivor needs room.** B handles A's replacement load and still depends on database capacity.
   - **Why it matters:** Failover can overload a survivor that lacks spare capacity.
   - **Notice:** Two instances do not double DB capacity; Tail latency can rise under overload.
5. **The shared database fails.** B loses the shared database; restoring A would not repair checkout.
   - **Why it matters:** Application redundancy does not remove a shared database failure point.
   - **Notice:** Independent failure assumptions matter; A fast error is not checkout success.
6. **Degrade by operation.** B can serve cached public products while checkout reports temporary failure.
   - **Why it matters:** State which product function still works instead of claiming universal availability.
   - **Notice:** Browsing tolerates its cache policy; Do not invent a successful payment.
7. **Recover and verify.** After database recovery, readiness and real checkout behavior are checked again.
   - **Why it matters:** Recovery is complete when the required operation works safely again.
   - **Notice:** Verify usable data and routing; Avoid sending all traffic at once.
8. **Measure the promise.** The customer receives a real checkout result through the healthy path.
   - **Why it matters:** Track successful operations and latency under failures, not server counts alone.
   - **Notice:** Test failover under representative load; Protect every critical dependency.

**Design tradeoff:** Redundancy needs spare capacity and working failover; shared dependencies can still stop both instances.

[View all states as still images](../assets/animations/availability-failover-steps.png)

## Related lessons

- [Availability](../curriculum/01-core-concepts/03-availability.md)
