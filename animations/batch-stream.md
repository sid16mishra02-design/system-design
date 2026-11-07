# Batch and stream: choose freshness and recovery rules

[← Animation index](README.md)

**Problem:** Process event arrivals with the latency, cost, and recovery behavior the product actually needs.

**Scenario:** Payments feed a periodic sales report and a live threshold alert.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Batch and stream: choose freshness and recovery rules](../assets/animations/batch-stream.gif)

## Read the same sequence without motion

1. **Preserve the incoming events.** Events are retained so consumers can process and recover from the same input. Batch and stream describe processing choices, not whether input data must be durable.
   Each event has an identity/position.; Consumers need explicit output rules..
2. **Process an early arrival.** The stream path processes event 1 without waiting for the full report window. Streaming can produce useful results while later events are still arriving.
   This is an incremental result.; Output delay depends on actual work..
3. **Continue with the next input.** Event 2 updates the live result while the batch job still waits. Timely decisions and periodic reports can legitimately observe different processing progress.
   Separate consumers track positions.; Streaming is not zero latency..
4. **A live threshold is reached.** Event 3 makes the running amount 60 and can trigger a configured live decision. A live threshold use case values response time differently from a nightly report.
   Define threshold and window semantics.; Do not equate arrival with event time..
5. **Close a bounded batch.** The batch job reads the three retained events for its selected report interval. Batching waits so it can amortize work across a bounded collection.
   Specify which records belong.; Periodic timing adds waiting delay..
6. **Publish the report.** The batch publishes total 60 and records its own successful progress. A report result is a product contract, not proof that the stream path used identical timing.
   Publication needs recovery behavior.; A checkpoint is not the output itself..
7. **Recover after a crash.** The stream resumes from a checkpoint that can cause event 3 to be seen again. Output-before-checkpoint failures can repeat processing after recovery.
   Input repetition is possible.; A naive increment would double count..
8. **Protect repeated processing.** The consumer recognizes an already applied event or uses an appropriate coordinated output rule. Deduplication or transactional coordination must protect the actual output effect.
   Do not promise exactly-once by label.; Define durable recovery semantics..
9. **Choose the right path.** Compare result delay, batch efficiency, recovery, and late-arriving event behavior. The same system may use both paths for different requirements.
   Late events need an explicit policy.; Measure useful end-to-end results..

**Design tradeoff:** Frequent streaming results reduce delay; batching amortizes work but waits, and both need safe recovery and late-data rules.

[View all states as still images](../assets/animations/batch-stream-steps.png)

## Related lessons

- [Batch vs stream processing](../practice/TRADEOFFS.md)
