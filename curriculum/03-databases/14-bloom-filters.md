# Bloom Filters

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A small filter before an expensive lookup

A Bloom filter answers a membership question with two possible meanings: **definitely absent**, or **possibly present**. It saves space by accepting some false positives.

Suppose a storage service has millions of keys on disk. Before looking for `invoice-900`, it checks the filter. “Definitely absent” lets it skip the disk lookup. “Possibly present” means it must consult the real storage to know.

The filter hashes a key into several positions in a bit array. Inserting a key sets those bits. Other keys may set the same positions, so all required bits being set is not conclusive proof of membership. A zero in a required position proves absence from the represented set.

For a correctly maintained standard Bloom filter, previously inserted items have no false negatives. A stale filter that has not received a new insertion cannot make that guarantee about the current database. Ordinary Bloom filters also do not support arbitrary deletion by simply clearing bits.

**Check:** never reject a username as already taken solely because a Bloom filter says “possibly present.” Verify against the authoritative store.

## Where this comes into play

Use a Bloom filter as a cheap gate before an expensive authoritative lookup when many requested keys are absent. Storage engines and large membership checks are natural examples. It is less useful if nearly every requested item exists, because most requests still need the real lookup.

## Work through the benefit

Suppose 10,000 lookups contain 9,000 absent keys and 1,000 existing keys. Assume the filter is current, contains all existing keys, and has a 1% false-positive rate for absent keys. About 90 absent lookups are expected to pass the filter, alongside the 1,000 existing ones. Roughly 1,090 authoritative lookups remain instead of 10,000, plus the cost of every filter check. These are expected illustrative counts, not a guarantee for every batch.

The filter must never become the final authority for accepting a payment or rejecting a username. A positive result only says that an authoritative lookup may be needed.

## How to tune it

Choose the expected item count and acceptable false-positive rate before sizing the filter. More bits generally reduce false positives for a given set size, at a memory cost. Filling a fixed filter far beyond its intended capacity worsens its usefulness. More hash work also costs CPU; “use more hashes” is not an unlimited improvement.

Plan updates and rebuilds. A filter that misses a recent insert can incorrectly suppress a lookup for data that really exists. For ordinary Bloom filters, deleting by clearing shared bits can damage other entries' membership evidence.

## How to verify improvement

Measure actual absent-key frequency, authoritative reads avoided, false positives, filter memory, and update lag. A lower lookup count is beneficial only if correctness remains intact.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/bloom-filters)
- [Redis: Bloom filter concepts](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter/)

Optional references provide more detail; they are not required to follow this lesson.
