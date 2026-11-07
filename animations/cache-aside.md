# Cache-aside: hit, miss, and update

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Cache-aside: hit, miss, and update](../assets/animations/cache-aside.gif)

</details>

## Read the same sequence without motion

1. The application checks the cache for product 42.
2. On a miss, the application reads the authoritative database.
3. The application fills the cache for later reads.
4. A write changes the database to 550; the cached copy is now old.
5. Invalidate the old entry, then reload on a later miss. Races still need a policy.

[View all states as still images](../assets/animations/cache-aside-steps.png)

## Related lessons

- [Caching](../curriculum/05-caching/01-caching.md)
- [Caching Strategies](../curriculum/05-caching/02-caching-strategies.md)
- [Distributed Caching](../curriculum/05-caching/04-distributed-caching.md)
