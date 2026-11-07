# Load balancing: healthy routing and shared state

[← Animation index](README.md)

**Problem:** Spread requests while preserving sessions and handling instance failure.

**Scenario:** Two application instances share user 7's session and one database.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Load balancing: healthy routing and shared state](../assets/animations/load-balancer.gif)

## Read the same sequence without motion

1. **A request changes servers.** A customer's next request reaches another server. Where must session state live?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Which instances are actually ready; What if the selected app crashes.
2. **Route the first request.** The client reaches the balancer, which selects ready instance A.
   - **Why it matters:** A routing rule should match the workload and health information.
   - **Notice:** Round robin is one possible policy; Readiness can differ from liveness.
3. **Read the session.** App A obtains user 7's shared session and checks permissions before doing business work.
   - **Why it matters:** Shared lookup lets another instance continue later without relying on A's memory.
   - **Notice:** Session ID is not blanket permission; Store access adds network dependency.
4. **Finish business work.** A queries the database and sends its response back through the balancer.
   - **Why it matters:** A complete topology includes data access and the response path.
   - **Notice:** Adding apps does not double DB capacity; Watch per-instance latency and errors.
5. **An instance fails.** A stops responding; readiness checks remove it from new routing.
   - **Why it matters:** Detection and rerouting take time; in-flight work can have uncertain outcomes.
   - **Notice:** A failed request may need safe retry; Use spare surviving capacity.
6. **Route the next request.** A later request reaches B rather than the failed instance.
   - **Why it matters:** Multiple instances help only when routing actually avoids unusable ones.
   - **Notice:** Plan draining for planned removal; Failures need separate recovery handling.
7. **Recover the same session.** B loads user 7's existing shared state instead of inventing a new session.
   - **Why it matters:** External session state supports movement between application instances.
   - **Notice:** Sticky routing is a different choice; Memory on failed A is not durable.
8. **Return through B.** B performs the query and returns a response through the same service entry point.
   - **Why it matters:** Measure successful end-to-end work, not merely balanced request counts.
   - **Notice:** Shared DB can become the bottleneck; Healthy B still needs its dependencies.
9. **A shared dependency fails.** The session store becomes unavailable, so adding app instances cannot repair session access.
   - **Why it matters:** Shared state can remove instance affinity while introducing a shared failure point.
   - **Notice:** Do not bypass authorization on failure; Use bounded dependency timeouts.
10. **Recover safely.** Once session access recovers, B can resume authorized requests; monitor the whole dependency path.
   - **Why it matters:** Capacity, state placement, and failure handling must be designed together.
   - **Notice:** Test complete store outages; Replication adds cost and coordination.

**Design tradeoff:** Shared state permits flexible routing but remains a dependency; extra app instances do not scale the database.

[View all states as still images](../assets/animations/load-balancer-steps.png)

## Related lessons

- [Scalability](../curriculum/01-core-concepts/02-scalability.md)
- [Load Balancing](../curriculum/02-networking/08-load-balancing.md)
- [Clustering](../curriculum/02-networking/09-clustering.md)
- [Stateful vs stateless design](../practice/TRADEOFFS.md)
