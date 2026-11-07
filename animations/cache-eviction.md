# Cache eviction: replay LRU and FIFO

[← Animation index](README.md)

**Problem:** Free limited cache memory using a deliberate reuse policy without confusing eviction with freshness.

**Scenario:** Compare two alternative caches holding three equally sized entries under the same access trace.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Cache eviction: replay LRU and FIFO](../assets/animations/cache-eviction.gif)

## Read the same sequence without motion

1. **Start with limited memory.** Two alternative three-entry caches receive the same workload; which old item should make room for D? The useful choice depends on how past accesses predict future reuse.
   This is a side-by-side comparison.; Entries are equally sized in this toy.; Which history should influence removal?.
2. **Fill both alternatives.** Insert A, B, and C in that order; both caches initially contain the same entries. Equal contents can conceal different internal policy state.
   LRU remembers recent access order.; FIFO remembers insertion order..
3. **Read A again.** Both caches hit A; LRU updates recency while FIFO retains its insertion order. A read changes the eviction decision only for policies that use that information.
   Both returned the same value.; Policy bookkeeping differs..
4. **Miss on the new D.** D is absent and must be loaded from the origin before insertion. A new value requires an admission and space decision.
   Cache miss still costs origin work.; D is not yet in either cache..
5. **LRU removes B.** LRU evicts B, now the least recently used entry, and admits D. Recently reread A survives in LRU under this exact trace.
   B was last used before C and A.; This is not a universal best policy..
6. **FIFO removes A.** FIFO evicts A, the earliest inserted entry, despite the recent successful read. FIFO's simplicity means recency does not influence its victim.
   Both caches still obey capacity 3.; Neither knows future access..
7. **Read A next.** LRU hits A; FIFO misses and needs an origin read for this next operation. Compare real traces, origin requests, and tracking overhead instead of policy names.
   Other traces can favor other policies.; Huge values also affect memory use..
8. **Separate memory from truth.** If A changes at the origin, its surviving cached copy can still hold an old value. Eviction frees memory; TTLs and update/invalidation rules address freshness.
   Recent does not mean current.; Popularity does not prove correctness..
9. **Tune for the real workload.** Measure hit rate, byte capacity, miss latency, origin work, and policy bookkeeping under representative accesses. Choose policy and admission separately from the application's acceptable staleness.
   Include scans and popularity changes.; Consider object size and frequency aging.; Test cost, not only hit percentage..

**Design tradeoff:** LRU tracks recency; FIFO is simpler. Reuse, object size, metadata cost, and freshness require separate evaluation.

[View all states as still images](../assets/animations/cache-eviction-steps.png)

## Related lessons

- [Cache Eviction Policies](../curriculum/05-caching/03-cache-eviction-policies.md)
