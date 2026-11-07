# Idempotency: retries, durable state, and recovery

[← Animation index](README.md)

**Problem:** Prevent repeated requests from creating repeated effects while recovering uncertain outcomes.

**Scenario:** An illustrative 500-unit payment succeeds, its response disappears, and the caller retries.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Idempotency: retries, durable state, and recovery](../assets/animations/idempotency.gif)

## Read the same sequence without motion

1. **Start with the uncertainty.** A payment response can disappear after the money moves. What should a retry mean?
   - **Why it matters:** The operation's identity must survive a lost response and simultaneous retries.
   - **Notice:** Should K create another payment; Which state must survive a crash.
2. **Validate and claim K.** The API scopes K to its caller and operation, validates the body, then atomically claims a durable record.
   - **Why it matters:** A check followed by an unprotected insert can race; use a suitable atomic uniqueness rule.
   - **Notice:** Key scope: caller plus operation; Record a request fingerprint.
3. **A duplicate arrives early.** A simultaneous same-body request finds K already pending rather than becoming a second owner.
   - **Why it matters:** Define in-progress behavior; not every duplicate already has a completed result.
   - **Notice:** Only one claim can win; Do not report an unperformed charge.
4. **Perform the external step.** The winning operation uses a stable provider identifier; its charge result is durably associated with K.
   - **Why it matters:** Local records and external effects require one coherent retry and reconciliation design.
   - **Notice:** This provider supports stable IDs; Store enough state for crash recovery.
5. **Lose the final response.** The API sends success, but the client never receives it.
   - **Why it matters:** A transport timeout does not prove that the business operation failed.
   - **Notice:** The payment already completed; The caller still needs a safe answer.
6. **Return the existing result.** Retrying K with the same body reads its stored result instead of creating a new charge.
   - **Why it matters:** Idempotent handling ties repeated requests to the same logical operation.
   - **Notice:** No new provider operation is needed; Retention must cover supported retries.
7. **Reject a changed request.** Reusing K with a different amount fails the fingerprint rule instead of silently reusing or changing the payment.
   - **Why it matters:** A deduplication key needs an explicit meaning, not merely string equality.
   - **Notice:** Scope and payload validation matter; Never silently create a second effect.
8. **Rewind to a crash boundary.** Compare another crash point: K is pending and the provider outcome is not recorded locally.
   - **Why it matters:** Skipping every pending key can lose real work; blindly repeating the effect can duplicate it.
   - **Notice:** Rewind to a different crash boundary; A pending claim is not proof of success.
9. **Reconcile the pending work.** Recovery resumes K and resolves the provider's existing outcome using its safe retry or status contract.
   - **Why it matters:** A key-only table does not close the crash gap around an external side effect.
   - **Notice:** Do not invent a new payment identity; Preserve uncertain state until resolved.
10. **Return a truthful outcome.** The API returns the resolved result or a documented pending state while recovery continues.
   - **Why it matters:** Test duplicate arrivals and every crash boundary, not only a repeated successful response.
   - **Notice:** Track duplicate and pending operations; Do not expire keys too early.

**Design tradeoff:** Durable deduplication adds state and coordination; safe recovery must cover the external side effect, not merely store a key.

[View all states as still images](../assets/animations/idempotency-steps.png)

## Related lessons

- [Idempotency](../curriculum/06-api-fundamentals/04-idempotency.md)
- [Webhooks](../curriculum/06-api-fundamentals/07-webhooks.md)
- [Reliability](../curriculum/01-core-concepts/05-reliability.md)
