# Raft: commit one replicated history despite a minority partition

[← Animation index](README.md)

**Problem:** Agree on a committed operation order under stated crash-fault and communication assumptions.

**Scenario:** Three voters replicate configuration changes; the old leader becomes isolated.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Raft: commit one replicated history despite a minority partition](../assets/animations/raft-majority.gif)

## Read the same sequence without motion

1. **Propose through the leader.** The client sends X: set limit to 20, to leader A in term one. An appended entry is not yet a committed or applied decision.
   Leader also stores its own entry; Replicas retain durable logs.
2. **Replicate to a majority.** B durably acknowledges X; A and B form two of three voters. Raft commits current-term entries using its majority and log rules, not arbitrary voting on values.
   A counts in the majority; Entry term matters for commit.
3. **Apply, then confirm.** A applies committed X and returns the committed result. Committed history drives deterministic state-machine application.
   Replication is not application; Do not confirm uncommitted writes.
4. **Isolate the old leader.** A appends Y: set limit to 30, but cannot contact a majority. A minority cannot safely commit new entries just because its process is still running.
   Old leader may not know immediately; Do not count missing acknowledgements.
5. **Elect with log rules.** B gets its own vote and Câ€™s eligible vote in a newer term. Election requires majority votes and an up-to-date-log check.
   B retains the committed X; Timing affects election start.
6. **Retry with the new leader.** The client retries the idempotent set; B appends Y in term two. The new leader may need to repair follower log prefixes before replication succeeds.
   Old term1 Y was not committed; Keep the client operation identity.
7. **Commit a current-term entry.** C acknowledges; B and C form a majority for term-two Y. Quorum contact alone is insufficient: Raftâ€™s term and log conditions still apply.
   Majority is two of three here; This is a crash-fault example.
8. **Apply and return success.** B applies Y and confirms the new limit of 30. Safety preserves one committed order while the isolated minority cannot progress.
   Read guarantees need separate choices; No Byzantine-fault tolerance claim.
9. **Repair the returning voter.** A learns the newer term and replaces its conflicting uncommitted suffix. Raft can discard conflicting uncommitted entries; committed history must not be overwritten.
   A steps down on newer term; Membership changes need special rules.

**Design tradeoff:** A communicating majority can progress; losing a majority sacrifices progress to protect committed-history safety.

[View all states as still images](../assets/animations/raft-majority-steps.png)

## Related lessons

- [Consensus Algorithms](../curriculum/09-reliability-and-microservices/06-consensus-algorithms.md)
