# Cache Eviction Policies

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## What leaves when the cache is full?

**Eviction** removes entries to make room. **Expiration** removes entries after an age limit, often a TTL, or time to live. Neither alone guarantees that a cached value is still correct after the original changes.

Suppose a cache fits three products: A, B, and C. A is read again, then D needs space.

- **LRU**, least recently used, removes the item unused for the longest time. If B was last read before C, B goes.
- **LFU**, least frequently used, uses access frequency to prefer keeping popular items. Implementations may age old counts.
- **FIFO**, first in, first out, removes the item inserted earliest, regardless of a later read.

LRU works well when recent access predicts future access. A scan across thousands of one-time keys can still push out useful entries. LFU can favor historically popular items even after interest changes unless counts decay.

**Check:** changing the database price requires an update or invalidation policy. Waiting for memory pressure to evict an old price is not a freshness policy.

## Optional further reading

- [Additional explanation](https://blog.algomaster.io/p/7-cache-eviction-strategies)

The lesson above is complete enough for this curriculum; external links are for deeper study.
