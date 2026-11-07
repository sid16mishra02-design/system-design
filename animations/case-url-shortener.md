# Design example: create and resolve a short URL

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Design example: create and resolve a short URL](../assets/animations/case-url-shortener.gif)

</details>

## Read the same sequence without motion

1. Creation: validate the destination and allocate a short key with a collision policy.
2. Persist K -> destination under a uniqueness rule before confirming creation.
3. Resolution: a later request for K checks the fast lookup cache.
4. On a miss, retrieve the mapping and fill the cache using a freshness policy.
5. The service returns an HTTP redirect; the client requests the destination.
6. Later cache hits reduce mapping reads; expiry, deletion, and abuse still need policies.

[View all states as still images](../assets/animations/case-url-shortener-steps.png)

## Related lessons

- [URL Shortener](../practice/url-shortener.md)
