# Concurrency: overlap work; parallelism: execute together

[← Animation index](README.md)

**Problem:** Distinguish managing overlapping tasks from executing independent work simultaneously.

**Scenario:** Two independent CPU tasks each require two equal work slots.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Concurrency: overlap work; parallelism: execute together](../assets/animations/concurrency-parallelism.gif)

## Read the same sequence without motion

1. **Use the same task workload.** A and B each need two equal CPU work slots in this illustration. Keep the workload fixed before comparing execution strategies.
   Assume tasks are independent.; These slots are not a benchmark..
2. **Single core starts A.** One core executes A's first slot while B remains pending. Both tasks can be in progress over time without running simultaneously.
   One core executes one CPU slot here.; The scheduler manages both tasks..
3. **Switch to B.** The next single-core slot serves B instead of finishing all of A first. Interleaving is concurrency, not evidence of simultaneous execution.
   A has unfinished work.; B now also has unfinished work..
4. **Return to A.** A receives its second slot and can complete. Concurrency describes overlap in task lifetimes, including switching and waiting.
   Task A has used two slots.; B still needs its second slot..
5. **Single-core trial finishes.** B completes in slot four; the collector returns both results. Finishing more tasks does not imply each task had shorter latency.
   Total CPU work remains four slots.; Measure per-task completion too..
6. **Repeat on two cores.** The same independent tasks are assigned to separate available cores. Parallelism needs actual simultaneous execution capacity, not merely more queued tasks.
   Reset the trial, not the workload.; Do not assume every task is independent..
7. **Work at the same time.** Core 1 serves A while core 2 serves B in the first parallel slot. This simultaneous execution is parallelism.
   Two CPU slots happen at once.; Synchronization can reduce real gains..
8. **Compare completion and limits.** Both tasks finish after two parallel slots under these simplified assumptions. I/O waits can overlap with concurrency; CPU parallelism depends on resources and independent work.
   Same total work, different elapsed time.; Shared bottlenecks can limit speedup..

**Design tradeoff:** Concurrency can overlap waiting without extra cores; parallel speedup requires independent work and available execution resources.

[View all states as still images](../assets/animations/concurrency-parallelism-steps.png)

## Related lessons

- [Concurrency vs parallelism](../practice/TRADEOFFS.md)
- [Latency vs throughput](../practice/TRADEOFFS.md)
