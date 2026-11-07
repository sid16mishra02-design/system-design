# Feeds: publish, fan out, read, and enforce visibility

[← Animation index](README.md)

**Problem:** Serve follower feeds while balancing publication fanout, reading work, freshness, and visibility.

**Scenario:** Ordinary posts and a celebrity post compete with delayed timeline workers.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Feeds: publish, fan out, read, and enforce visibility](../assets/animations/case-twitter.gif)

## Read the same sequence without motion

1. **Store the original post.** The post API records authoritative content, access rules, and recoverable fanout intent.
   - **Why it matters:** Publication acceptance does not prove every follower timeline is updated.
   - **Notice:** Keep a durable source of content; Define the required freshness.
2. **Distribute references later.** A queue decouples publication from follower timeline work.
   - **Why it matters:** Asynchronous precomputation adds a measurable post-to-feed delay.
   - **Notice:** Backlog age measures waiting; Retries need safe reference insertion.
3. **Precompute ordinary feeds.** The worker adds P references to the followers' timelines.
   - **Why it matters:** References avoid copying full post content into every timeline.
   - **Notice:** Content lookup still costs work; Visibility must still be enforced.
4. **Read a bounded page.** A follower asks the feed API for a page of timeline references.
   - **Why it matters:** Pagination bounds work instead of fetching an entire lifetime feed.
   - **Notice:** A reference is not the content; Feed ordering is an explicit choice.
5. **Fetch currently allowed posts.** The API resolves content and current access before returning the page.
   - **Why it matters:** An old timeline reference must not bypass current deletion or privacy rules.
   - **Notice:** Cache with the right user context; Check access at the content boundary.
6. **A celebrity changes the cost.** A huge follower count turns one publication into a large distribution burst.
   - **Why it matters:** Average followers per post can hide the worst write bursts.
   - **Notice:** 1k posts/s x 300 followers: 300k writes; A celebrity workload is different.
7. **Choose a mixed strategy.** Ordinary authors remain precomputed; large-author content is merged during reads.
   - **Why it matters:** A mixed design reduces massive write bursts while increasing read-path work.
   - **Notice:** Use measured fanout and read frequency; Do not copy an arbitrary threshold.
8. **A deleted post lingers.** The author disables P while a timeline reference still exists.
   - **Why it matters:** Reference cleanup and access enforcement are different tasks.
   - **Notice:** Synchronous global cleanup is costly; Never expose a forbidden cached copy.
9. **Return and measure the choice.** The feed excludes forbidden content and measures read latency and publication lag.
   - **Why it matters:** Assess feed-read latency, timeline writes, and post-to-feed delay together.
   - **Notice:** Cheaper reads can mean more writes; Fresher feeds may need extra work.

**Design tradeoff:** Precomputing feeds reduces read work but amplifies writes; merging large authors at read time shifts cost back to reads.

[View all states as still images](../assets/animations/case-twitter-steps.png)

## Related lessons

- [Twitter](../practice/twitter.md)
