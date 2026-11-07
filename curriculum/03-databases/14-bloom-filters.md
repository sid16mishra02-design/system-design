# Bloom Filters

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A small filter before an expensive lookup

A Bloom filter answers a membership question with two possible meanings: **definitely absent**, or **possibly present**. It saves space by accepting some false positives.

Suppose a storage service has millions of keys on disk. Before looking for `invoice-900`, it checks the filter. “Definitely absent” lets it skip the disk lookup. “Possibly present” means it must consult the real storage to know.

The filter hashes a key into several positions in a bit array. Inserting a key sets those bits. Other keys may set the same positions, so all required bits being set is not conclusive proof of membership. A zero in a required position proves absence from the represented set.

For a correctly maintained standard Bloom filter, previously inserted items have no false negatives. A stale filter that has not received a new insertion cannot make that guarantee about the current database. Ordinary Bloom filters also do not support arbitrary deletion by simply clearing bits.

**Check:** never reject a username as already taken solely because a Bloom filter says “possibly present.” Verify against the authoritative store.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/bloom-filters)
- [Redis: Bloom filter concepts](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter/)

The lesson above is complete enough for this curriculum; external links are for deeper study.
