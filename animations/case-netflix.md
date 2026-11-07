# Video: prepare renditions, then serve media nearby

[← Animation index](README.md)

**Problem:** Prepare video safely and serve repeated media segments without making playback wait for encoding.

**Scenario:** A new title launches while regional CDN caches are still cold.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Video: prepare renditions, then serve media nearby](../assets/animations/case-netflix.gif)

## Read the same sequence without motion

1. **Persist before preparation.** The upload API stores the original before starting background preparation. Upload and playback are different workloads with different readiness guarantees.
   Do not encode on the playback request.; Preparation must be retryable..
2. **Create separate renditions.** Workers read the source and build versions for different device/network needs. A rendition is one resolution and bitrate choice, not an extra user request.
   Encoding consumes compute.; More versions consume more storage..
3. **A worker stops midway.** Partial output must not be advertised as playable content. A successful file write alone does not prove a complete rendition is usable.
   Keep incomplete outputs unexposed.; Resume or retry with safe output keys..
4. **Retry and publish readiness.** A successful retry finishes the required outputs and verifies readiness. Expose a manifest only when its required media outputs can be served.
   Coordinate publication of readiness.; Duplicate jobs must not corrupt media..
5. **Fetch the playback plan.** The player obtains the manifest and available rendition choices. The application describes playback; media bytes use the delivery path.
   Login API capacity is not media capacity.; Authorization applies to media too..
6. **Cold edge reaches origin.** The first regional request fetches a segment from media origin. A cold CDN request still consumes origin capacity and network distance.
   Different regions warm independently.; Cache keys affect safe reuse..
7. **Warm viewers reuse bytes.** Later requests for reusable segments are served near viewers. 2,000 viewers at 4 Mb/s imply roughly 8 Gb/s before overhead.
   Media bandwidth is a major constraint.; Do not count only application requests..
8. **Adapt to the connection.** The player chooses an available lower bitrate when needed to reduce buffering. Lower transfer demand can improve continuity at the cost of visual quality.
   More renditions add preparation cost.; Observe startup and buffering too..
9. **Test a regional launch.** Cold-miss bursts and origin pressure need bounds, not assumptions of a warm cache. Measure quality, buffering, origin load, and cache geography together.
   Protect origin from synchronized misses.; Higher hit ratio alone is not success..

**Design tradeoff:** More renditions improve adaptation but increase encoding and storage; regional caching introduces cold-miss and access-policy costs.

[View all states as still images](../assets/animations/case-netflix-steps.png)

## Related lessons

- [Netflix](../practice/netflix.md)
