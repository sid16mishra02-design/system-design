# Bloom filters: a cheap gate, not the authority

[← Animation index](README.md)

**Problem:** Avoid expensive absent-key reads without mistaking possible membership for actual membership.

**Scenario:** Illustrative 12-bit filter: A and missing X share positions 1, 4, and 8.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Bloom filters: a cheap gate, not the authority](../assets/animations/bloom-filter.gif)

## Read the same sequence without motion

1. **Skip unnecessary reads?.** Most requested keys do not exist. Can a small precheck avoid disk reads without inventing membership?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Which result can safely skip storage; What if two keys share positions.
2. **Insert a real item.** The writer stores A, then its hash positions 1, 4, and 8 are represented in the filter.
   - **Why it matters:** Insertion sets shared bits; it does not store a unique full record in each bit.
   - **Notice:** Use the same hashes when querying; Keep insertions and filter state aligned.
3. **Probe a missing position.** Query Y needs positions 2, 6, and 10; a required zero proves absence from the represented set.
   - **Why it matters:** A negative can avoid disk work only when the filter covers the relevant current data.
   - **Notice:** One required zero is enough; This conclusion is about represented data.
4. **Skip the costly lookup.** With a current filter, Y is definitely absent, so this query does not reach the store.
   - **Why it matters:** Cheap negative results are where the saved authoritative reads come from.
   - **Notice:** Most-existing workloads save less; Every request still pays filter cost.
5. **Probe a colliding key.** Different key X also maps to 1, 4, and 8, all already set by A.
   - **Why it matters:** Shared positions allow false positives; all set bits do not prove the key exists.
   - **Notice:** X was never inserted in this example; Bit positions do not identify the key.
6. **Verify maybe in storage.** The client queries the authoritative store, which confirms that X does not exist.
   - **Why it matters:** A Bloom positive is permission to check, not a reason to reject a username as taken.
   - **Notice:** This one false positive costs a lookup; The store settles actual membership.
7. **Tune memory and work.** Choose capacity and acceptable false positives; overfilling a fixed filter increases wasted lookups.
   - **Why it matters:** More bits reduce collision pressure, but hashing and memory both have costs.
   - **Notice:** No arbitrary bit clearing for deletes; Shared bits may belong to other items.
8. **Expose a maintenance gap.** A new item reaches storage but its filter update is delayed; trusting a negative can miss real data.
   - **Why it matters:** The no-false-negative property assumes the queried set has actually been inserted.
   - **Notice:** Stale filter differs from false positive; Update lag can become a correctness bug.
9. **Bypass until repaired.** When coverage is uncertain, consult the store and restore the filter's maintenance guarantees.
   - **Why it matters:** Use the optimization only when it preserves the operation's correctness.
   - **Notice:** Measure filter update lag; Track memory, false positives, and reads.

**Design tradeoff:** Space-efficient negatives save reads, but positives need verification and filter maintenance must cover the actual queried data.

[View all states as still images](../assets/animations/bloom-filter-steps.png)

## Related lessons

- [Bloom Filters](../curriculum/03-databases/14-bloom-filters.md)
