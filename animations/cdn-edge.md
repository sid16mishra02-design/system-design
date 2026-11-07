# CDN: origin content, nearby reuse, and freshness

[← Animation index](README.md)

**Problem:** Serve safely reusable content near viewers while reducing origin transfers.

**Scenario:** Two viewers request a popular image that a publisher later replaces.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![CDN: origin content, nearby reuse, and freshness](../assets/animations/cdn-edge.gif)

## Read the same sequence without motion

1. **Publish the original.** The publisher stores logo v1 at the origin with a deliberate caching policy. A CDN serves origin content under a cache and access policy, not arbitrary private data.
   Cache keys identify reusable variants.; Response policy controls reuse..
2. **The first viewer misses.** A's nearby edge has no usable copy and asks the origin. Cold requests still reach origin storage and may include long-distance transfer.
   Each region can begin cold.; A CDN does not erase the origin..
3. **Fill and respond.** Origin bytes reach the edge, which stores an allowed copy and responds to A. The edge can reuse only the responses its keys and policy permit.
   Store expiry and variant information.; Honor access requirements..
4. **Reuse near the viewer.** B asks for the same safe cache key and receives the edge copy. A warm hit reduces origin traffic and repeated distance, not personalized query cost.
   Same reusable object; another request.; Measure hit ratio by region..
5. **The origin changes.** The publisher replaces bytes under the old name while the edge still holds v1. Updating origin bytes does not instantly replace existing cached copies.
   Freshness is a separate decision.; An old copy can outlive the update..
6. **Invalidate the old cache key.** The publisher invalidates the old key; the next request fetches v2 from the origin. Choose versioning, expiry, or invalidation for the product's freshness requirement.
   Versioned names change the cache key.; Invalidation has operational behavior..
7. **Keep private data private.** A private invoice must not reuse a public image-style cache key and policy. Authentication and private variants must be designed before permitting shared reuse.
   Tenant/user inputs may affect results.; A high hit rate cannot justify leakage..
8. **Verify the whole benefit.** Compare viewer response time and origin traffic for warm and cold requests. Test geography, updates, outages, and access behavior alongside cache hit rate.
   Cached public content may survive outage.; A slow database query needs other work..

**Design tradeoff:** Caching lowers repeated origin work but introduces freshness, access-control, and regional cold-miss decisions.

[View all states as still images](../assets/animations/cdn-edge-steps.png)

## Related lessons

- [Content Delivery Network (CDN)](../curriculum/05-caching/05-content-delivery-network-cdn.md)
