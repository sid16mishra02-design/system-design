# Bloom filter: no, or maybe

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Bloom filter: no, or maybe](../assets/animations/bloom-filter.gif)

</details>

## Read the same sequence without motion

1. Insert A with illustrative hash positions 1, 4, and 8.
2. A query needing bit 2 finds zero: definitely absent from the represented set.
3. A different key X can map to bits 1, 4, and 8 too.
4. Verify a positive result in real storage; a collision can mean X is absent.
5. The filter saves absent-key reads, but is not the final membership authority.

[View all states as still images](../assets/animations/bloom-filter-steps.png)

## Related lessons

- [Bloom Filters](../curriculum/03-databases/14-bloom-filters.md)
