# Cache-through policies: load reads and persist writes

[← Animation index](README.md)

**Problem:** Assign cache-loading and write-persistence responsibilities without assuming automatic freshness or atomicity.

**Scenario:** A product price is read, updated, then read after a partial cache failure.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Cache-through policies: load reads and persist writes](../assets/animations/read-write-through.gif)

## Read the same sequence without motion

1. **Request data through a layer.** The API asks the cache layer for a product instead of loading misses itself.
   - **Why it matters:** Read-through assigns missing-value loading to the cache layer.
   - **Notice:** Application and cache-aside differ here; A cache layer has an explicit contract.
2. **The layer loads the miss.** The cache layer fetches version 1 from the database.
   - **Why it matters:** A missing cached value still requires backing-store work.
   - **Notice:** Preserve the right cache key inputs; Loading can fail or be concurrent.
3. **Serve a reusable read.** The cache returns the value and the API responds to the reader.
   - **Why it matters:** Read-through changes responsibility for loading, not the operation's freshness guarantee by itself.
   - **Notice:** Reuse follows the expiry policy; Cached data can become stale.
4. **Submit a write-through edit.** The authorized editor sends 550 through the same cache layer.
   - **Why it matters:** Write-through puts backing persistence on the synchronous write path.
   - **Notice:** A pending write is not a success; The layer must handle partial failure.
5. **Persist before success.** After persistence succeeds, the layer can publish its new cached value under its policy.
   - **Why it matters:** Define what successful acknowledgement means across the layer and backing store.
   - **Notice:** Read and write policies can combine; This is not write-behind buffering.
6. **Handle a partial failure.** A later backing write can commit even if the cache update or its response fails.
   - **Why it matters:** Synchronous calls do not magically create a transaction across every component.
   - **Notice:** A timeout can hide a committed write; Do not return an invented result.
7. **Recover under a clear rule.** The API may use an authorized backing read when the layer's fallback policy permits it.
   - **Why it matters:** Fallback must preserve access and freshness requirements while respecting database capacity.
   - **Notice:** Bypassing cache increases store load; Fail closed where contract requires.
8. **Verify both operations.** Reload a missing value and measure writes, stale reads, and outage behavior together.
   - **Why it matters:** Choose the policy from reuse, durability, and consistency needs rather than treating names as opposites.
   - **Notice:** Read-through: who loads misses; Write-through: who persists writes.

**Design tradeoff:** Read-through and write-through can coexist; synchronous persistence adds write latency and still needs partial-failure rules.

[View all states as still images](../assets/animations/read-write-through-steps.png)

## Related lessons

- [Read-through vs write-through cache](../practice/TRADEOFFS.md)
