# Token bucket: protect shared search capacity

[← Animation index](README.md)

**Problem:** Protect a service from sustained overload while allowing a controlled burst.

**Scenario:** A customer sends four search requests in one burst.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Token bucket: protect shared search capacity](../assets/animations/token-bucket.gif)

## Read the same sequence without motion

1. **Define the budget.** One shared bucket limits this customer across all gateway instances. A local bucket per instance can multiply a supposedly global allowance.
   Key: customer + operation; Capacity and refill are different.
2. **Spend one token.** Request one atomically changes the bucket from three tokens to two. Checking and decrementing must be one coordinated decision.
   Same logical burst; Only admitted work reaches search.
3. **Do useful work.** Search reads its index and returns the first result. The limiter protects downstream capacity rather than speeding up individual queries.
   Admission precedes expensive work; Measure search saturation separately.
4. **Use the burst allowance.** Two more immediate requests spend the remaining tokens. Capacity permits a bounded burst; refill sets the sustained allowance.
   No model time passes in this burst; Requests still share one bucket.
5. **Reject excess work.** The fourth immediate request finds no token. Reject before the expensive stage becomes overloaded.
   No negative token balance; This policy rejects rather than queues.
6. **Tell the caller clearly.** The gateway returns 429; the client backs off instead of hammering. Fast immediate retries would amplify the original overload.
   Document retry behavior; Track rejected customer requests.
7. **Advance the model clock.** One logical second later, one token is available again. Displayed step timing is illustrative; a real limiter uses actual elapsed time.
   Refill cannot exceed capacity; Use a consistent accounting clock.
8. **Admit a later retry.** A later request spends the new token and reaches search. Choose a shared-store failure policy explicitly; fail-open and fail-closed have different costs.
   Do not exceed downstream capacity; Monitor limiter-store availability.

**Design tradeoff:** Burst capacity helps normal clients, but shared accounting adds a dependency and an outage policy.

[View all states as still images](../assets/animations/token-bucket-steps.png)

## Related lessons

- [Rate Limiting](../curriculum/06-api-fundamentals/05-rate-limiting.md)
