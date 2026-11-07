# Caching Strategies

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Decide who reads and who updates the copy

A cache holds a faster copy of data whose authoritative version lives elsewhere.

| Strategy | Request flow | Main concern |
| --- | --- | --- |
| Cache-aside | Application checks cache; on a miss it reads the database and fills the cache. | Stale entries and simultaneous misses. |
| Read-through | Application reads through a cache layer that loads missing data. | The cache layer owns loading behavior. |
| Write-through | A write goes through a layer that synchronously updates backing storage and cache. | More work on the write path; failures still need handling. |
| Write-behind | A layer accepts the cached write, then persists it later. | Unpersisted writes may be lost if the buffering layer fails. |

Example: a product page uses cache-aside. The first visitor fetches the database value; later visitors use the cached value. A price update must account for the old copy.

Read-through and write-through are not opposites: they describe different sides of access and can be combined.

**Check:** choose a strategy by acceptable staleness, write durability, and who should own loading. “Use a cache” alone does not answer those questions.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/caching-strategies)

The lesson above is complete enough for this curriculum; external links are for deeper study.
