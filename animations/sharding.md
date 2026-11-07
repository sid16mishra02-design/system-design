# Sharding divides ownership of data

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Sharding divides ownership of data](../assets/animations/sharding.gif)

</details>

## Read the same sequence without motion

1. Choose a shard from the customer identifier.
2. Customer 42 is routed to A.
3. Customer 1500 is routed to B, not to a duplicate of A.
4. A replica of A copies A data, not B data.
5. A query across both customer ranges needs deliberate coordination.

[View all states as still images](../assets/animations/sharding-steps.png)

## Related lessons

- [Sharding](../curriculum/03-databases/11-sharding.md)
- [Database Federation](../curriculum/03-databases/13-database-federation.md)
