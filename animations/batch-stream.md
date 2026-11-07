# Batch and stream: choose freshness and recovery rules

[← Animation index](README.md)

**Problem:** Process event arrivals with the latency, cost, and recovery behavior the product actually needs.

**Scenario:** Payments feed a periodic sales report and a live threshold alert.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Batch and stream: choose freshness and recovery rules](../assets/animations/batch-stream.gif)

## Read the same sequence without motion

1. **Preserve the incoming events.** Events are retained so consumers can process and recover from the same input.
   - **Why it matters:** Batch and stream describe processing choices, not whether input data must be durable.
   - **Notice:** Each event has an identity/position; Consumers need explicit output rules.
2. **Process an early arrival.** The stream path processes event 1 without waiting for the full report window.
   - **Why it matters:** Streaming can produce useful results while later events are still arriving.
   - **Notice:** This is an incremental result; Output delay depends on actual work.
3. **Continue with the next input.** Event 2 updates the live result while the batch job still waits.
   - **Why it matters:** Timely decisions and periodic reports can legitimately observe different processing progress.
   - **Notice:** Separate consumers track positions; Streaming is not zero latency.
4. **A live threshold is reached.** Event 3 makes the running amount 60 and can trigger a configured live decision.
   - **Why it matters:** A live threshold use case values response time differently from a nightly report.
   - **Notice:** Define threshold and window semantics; Do not equate arrival with event time.
5. **Close a bounded batch.** The batch job reads the three retained events for its selected report interval.
   - **Why it matters:** Batching waits so it can amortize work across a bounded collection.
   - **Notice:** Specify which records belong; Periodic timing adds waiting delay.
6. **Publish the report.** The batch publishes total 60 and records its own successful progress.
   - **Why it matters:** A report result is a product contract, not proof that the stream path used identical timing.
   - **Notice:** Publication needs recovery behavior; A checkpoint is not the output itself.
7. **Recover after a crash.** The stream resumes from a checkpoint that can cause event 3 to be seen again.
   - **Why it matters:** Output-before-checkpoint failures can repeat processing after recovery.
   - **Notice:** Input repetition is possible; A naive increment would double count.
8. **Protect repeated processing.** The consumer recognizes an already applied event or uses an appropriate coordinated output rule.
   - **Why it matters:** Deduplication or transactional coordination must protect the actual output effect.
   - **Notice:** Do not promise exactly-once by label; Define durable recovery semantics.
9. **Choose the right path.** Compare result delay, batch efficiency, recovery, and late-arriving event behavior.
   - **Why it matters:** The same system may use both paths for different requirements.
   - **Notice:** Late events need an explicit policy; Measure useful end-to-end results.

**Design tradeoff:** Frequent streaming results reduce delay; batching amortizes work but waits, and both need safe recovery and late-data rules.

[View all states as still images](../assets/animations/batch-stream-steps.png)

## Related lessons

- [Batch vs stream processing](../practice/TRADEOFFS.md)
