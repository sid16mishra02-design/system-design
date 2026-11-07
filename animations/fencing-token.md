# Fencing: make the protected resource reject stale owners

[← Animation index](README.md)

**Problem:** Prevent an expired lease holder from corrupting data after a newer owner takes over.

**Scenario:** Worker A pauses; B takes over; A later resumes with an older token.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Fencing: make the protected resource reject stale owners](../assets/animations/fencing-token.gif)

## Read the same sequence without motion

1. **Acquire an ownership lease.** A receives token 10 from an authority that issues increasing tokens.
   - **Why it matters:** A lease is a time-bounded ownership promise, not a mechanism that kills paused processes.
   - **Notice:** Tokens increase across ownership; Do not use client-local counters.
2. **Write under the first token.** The store accepts Aâ€™s token-ten write and records its fence.
   - **Why it matters:** The protected store participates in safety by validating tokens, not merely trusting a worker.
   - **Notice:** Compare token atomically with write; Persist the highest accepted fence.
3. **Pause beyond the lease.** A pauses long enough that its lease expires.
   - **Why it matters:** Expiry changes the authorityâ€™s ownership state; it does not stop Aâ€™s future instructions.
   - **Notice:** A can resume with old state; Clock and pause assumptions matter.
4. **Let another worker take over.** The coordinator retries the same logical job on B.
   - **Why it matters:** A newer lease carries a higher fencing token than the old ownerâ€™s token.
   - **Notice:** Report identity remains stable; Token issuance needs a safety contract.
5. **Advance the enforced fence.** B writes with token 11; the store durably advances its fence.
   - **Why it matters:** After observing eleven, the resource must refuse writes carrying older ownership.
   - **Notice:** The resource performs the check; Issuing tokens alone is insufficient.
6. **The old worker resumes.** A wakes and sends a stale write carrying token 10.
   - **Why it matters:** Both processes can be running even though only one holds the current lease.
   - **Notice:** No process was magically terminated; Stale requests can reach storage.
7. **Reject the stale effect.** The store rejects token 10 because it is older than its stored fence 11.
   - **Why it matters:** The protected data remains safe because the resource enforces the ordering.
   - **Notice:** 10 is less than 11; Rejection is not just advisory.
8. **Keep recovery explicit.** The workflow records the rejected stale attempt without overwriting Bâ€™s result.
   - **Why it matters:** Fencing protects this resource; external side effects need their own idempotency and authorization rules.
   - **Notice:** Every protected write needs a check; No resource check means no fencing.

**Design tradeoff:** Leases coordinate ownership, but fencing works only when the protected resource durably enforces monotonic tokens.

[View all states as still images](../assets/animations/fencing-token-steps.png)

## Related lessons

- [Distributed Locking](../curriculum/09-reliability-and-microservices/07-distributed-locking.md)
