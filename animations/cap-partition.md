# CAP: compare two partition policies

[← Animation index](README.md)

**Problem:** Reason about strong consistency and availability when replicas cannot communicate.

**Scenario:** Two ticket replicas lose communication while clients still reach their own regional copy.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![CAP: compare two partition policies](../assets/animations/cap-partition.gif)

## Read the same sequence without motion

1. **Two sides cannot talk.** Two reachable ticket replicas cannot communicate. Can both answer every request and still promise one latest shared state?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Can B know A's newest write; What must a confirmed sale mean.
2. **Break communication.** A and B can no longer coordinate even though both processes continue running.
   - **Why it matters:** A network partition is not the same as a crashed database process.
   - **Notice:** No instant failure certainty; Local nodes cannot know remote updates.
3. **Availability-first branch.** In this branch, A accepts and acknowledges a sale without waiting for B.
   - **Why it matters:** Acknowledging a write in isolation requires confronting what another reachable copy can safely answer.
   - **Notice:** This branch permits isolated progress; B has not learned the new value.
4. **B must answer somehow.** Client B asks after A's acknowledged sale; B cannot confirm A's current state.
   - **Why it matters:** The request reaches a non-failing node; missing coordination is the problem.
   - **Notice:** Strong freshness spans both sides; Local health does not supply new facts.
5. **Answer with old information.** Returning B's available value serves the request but can violate the chosen strong-consistency guarantee.
   - **Why it matters:** Availability-first behavior needs an explicit tolerance for stale or conflicting outcomes.
   - **Notice:** Do not treat this as safe ticket sale; A recommendation read may differ.
6. **Rewind: require agreement.** Compare an alternative protocol: require both toy replicas to agree before confirming the same sale.
   - **Why it matters:** These are alternative policies, not a safe mid-operation switch of guarantees.
   - **Notice:** Toy commit rule needs both replicas; Rewind to before the sale.
7. **Coordination-first waits.** A cannot confirm the sale; B refuses a fresh result while the agreement path is broken.
   - **Why it matters:** Refusing or waiting protects the coordination rule but sacrifices CAP availability for these requests.
   - **Notice:** No acknowledged conflicting sale here; CAP availability is not monthly uptime.
8. **Heal and finish safely.** After communication returns, the coordinated sale can be agreed and acknowledged.
   - **Why it matters:** Recovery enables coordination; the operation's protocol defines when completion is safe.
   - **Notice:** Apply the chosen agreement rules; Do not invent an unsafe local commit.
9. **Choose per requirement.** Define which operations tolerate stale answers and which must refuse when required coordination is unavailable.
   - **Why it matters:** A category label is less useful than a precise operation and failure response.
   - **Notice:** Normal-operation latency is separate; Partition repair needs explicit policy.

**Design tradeoff:** During a partition, answering at every non-failing node conflicts with one latest global state; refusal protects coordination at availability cost.

[View all states as still images](../assets/animations/cap-partition-steps.png)

## Related lessons

- [CAP Theorem](../curriculum/04-distributed-data/01-cap-theorem.md)
- [Strong vs eventual consistency](../practice/TRADEOFFS.md)
