# Latency: trace the complete request

[← Animation index](README.md)

**Problem:** Find the stage limiting response time before choosing an optimization.

**Scenario:** Illustrative sequential request: 30 ms network, 70 ms application, 100 ms database.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Latency: trace the complete request](../assets/animations/request-latency.gif)

## Read the same sequence without motion

1. **The checkout is slow.** A checkout takes 200 ms. Which stage would you change, and what evidence would justify it?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** What does the timer include; Which stage dominates this path.
2. **Reach the application.** The gateway routes the request; connection and network costs belong in the full path.
   - **Why it matters:** A fast server-only timer can hide client-observed delay.
   - **Notice:** Gateway and app have different roles; Return travel also belongs in timing.
3. **Do application work.** The application performs 70 ms of its own work, then needs database data.
   - **Why it matters:** Optimize the critical path, not a conveniently visible component.
   - **Notice:** Query depends on preceding work; Dependent stages cannot overlap.
4. **Complete the first query.** The 100 ms query finishes; the application can build its response.
   - **Why it matters:** For this sequential example: 30 + 70 + 100 = 200 ms.
   - **Notice:** Network budget: 30 ms total; Own application work: 70 ms.
5. **Locate the dominant stage.** A trace links stages; investigate the database rather than guessing that bandwidth is slow.
   - **Why it matters:** Parent spans can include child time; avoid counting it twice.
   - **Notice:** Inspect the actual query plan; Do not sum overlapping spans.
6. **Apply a useful index.** A suitable index reduces the illustrative query from 100 ms to 25 ms.
   - **Why it matters:** Change the measured bottleneck, then check its costs.
   - **Notice:** Index avoids unnecessary row work; Index writes consume extra work.
7. **Measure the new result.** The same path now totals 125 ms, a 37.5% reduction in this example.
   - **Why it matters:** Lower request latency and higher throughput are separate measurements.
   - **Notice:** 30 + 70 + 25 = 125 ms; 75 / 200 = 37.5% saved.
8. **Watch overload separately.** More arrivals than capacity build a queue, even after the query improves.
   - **Why it matters:** Adding concurrency does not guarantee more completed requests.
   - **Notice:** Use stable averages for Little's Law; Tail latency reveals slow requests.

**Design tradeoff:** An index can shorten reads but adds storage and write maintenance; more concurrency can increase waiting.

[View all states as still images](../assets/animations/request-latency-steps.png)

## Related lessons

- [Latency vs Throughput vs Bandwidth](../curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md)
- [Distributed Tracing](../curriculum/09-reliability-and-microservices/09-distributed-tracing.md)
- [Latency vs throughput](../practice/TRADEOFFS.md)
