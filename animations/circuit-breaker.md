# Circuit breaker: stop cascading calls, then test recovery

[← Animation index](README.md)

**Problem:** Limit repeated calls to a failing dependency while preserving truthful business outcomes.

**Scenario:** A checkout calls a payment service that begins timing out.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Circuit breaker: stop cascading calls, then test recovery](../assets/animations/circuit-breaker.gif)

## Read the same sequence without motion

1. **Closed permits calls.** Checkout reaches payment through a closed breaker with a bounded deadline. A breaker observes a failure pattern; a timeout bounds an individual call.
   Thresholds depend on workload; Do not allow endless waiting.
2. **Timeout creates uncertainty.** A payment call times out; its business result may still be unknown. A timeout is not proof that the payment never happened.
   Keep payment request identity; Do not invent a successful charge.
3. **Open after the policy.** Repeated failures meet the configured opening rule. Opening is based on an explicit policy, not one universal failure count.
   Release caller resources; Isolate unrelated dependencies.
4. **Fail fast on the next call.** The open breaker refuses another call before it reaches payment. Stopping repeated calls can prevent cascading resource exhaustion.
   No probe yet; Bound retries above the breaker.
5. **Preserve business truth.** Checkout records pending or unavailable and returns a clear response. The fallback must preserve business correctness, not merely return HTTP success.
   A fallback is product-specific; Uncertain payments need reconciliation.
6. **Permit limited probes.** After cooldown, half-open allows only controlled recovery probes. Unbounded probes could immediately recreate the original overload.
   Backoff controls retry pressure; Probe choice must be safe.
7. **Close after recovery.** A successful probe satisfies the selected recovery policy. A failed probe would reopen the breaker under its policy.
   Keep measuring real traffic; Health is not permanent.
8. **Resolve earlier unknown work.** Checkout queries the durable payment outcome before settling order 42. Closing the breaker does not automatically resolve payments whose responses were lost.
   Reconcile using the same identity; Retries still need idempotency.

**Design tradeoff:** Fail-fast behavior preserves resources but rejects or delays useful work until the dependency recovers.

[View all states as still images](../assets/animations/circuit-breaker-steps.png)

## Related lessons

- [Circuit breaker](../curriculum/09-reliability-and-microservices/03-circuit-breaker.md)
