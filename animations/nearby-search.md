# Nearby search: index candidates, then verify real proximity

[← Animation index](README.md)

**Problem:** Find nearby eligible drivers without missing neighbors across a spatial cell boundary.

**Scenario:** A rider in (2,1) needs a nearby driver across the boundary in (3,1).

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Nearby search: index candidates, then verify real proximity](../assets/animations/nearby-search.gif)

## Read the same sequence without motion

1. **Place the search correctly.** The rider is near the right edge of cell (2,1). A cell identifier is a candidate-search aid, not a physical distance measurement.
   Radius can cross cell edges; Coordinates matter beyond prefix.
2. **Notice the adjacent driver.** The closest driver lies just across the boundary in cell (3,1). Nearby coordinates can have different cell labels.
   Different cell does not mean far; A quadtree has region boundaries too.
3. **Try an incomplete query.** Searching only the rider cell misses that driver. The missing result comes from incomplete candidate coverage.
   Do not filter on prefix alone; A missed ID cannot pass later filtering.
4. **Cover the search area.** Query the relevant neighboring regions that intersect the search area. Choose region coverage for the actual radius instead of one matching prefix.
   Expand when too few candidates; Cell precision affects work.
5. **Load candidate positions.** The index returns driver IDs; retrieve positions and timestamps. Index membership alone does not prove distance or current availability.
   Location records can be stale; Driver status also matters.
6. **Check distance and policy.** Calculate actual distances and remove stale, unavailable, or out-of-range drivers. Use geometry and business eligibility after narrowing candidates.
   Validate actual requested radius; Choose a location freshness policy.
7. **Return an eligible match.** Ranked results include the close driver across the cell boundary. The end-to-end result combines indexing, current records, and exact filtering.
   A candidate is not a reservation; Availability can change again.
8. **Tune the actual workload.** Measure candidate counts and location-update costs before changing precision. Geohash precision or quadtree splits trade query work against maintenance and neighboring-region work.
   Coarse regions return more candidates; Fine regions need more lookups.

**Design tradeoff:** Finer cells reduce candidates but increase lookups and update work; exact distance and freshness still need checks.

[View all states as still images](../assets/animations/nearby-search-steps.png)

## Related lessons

- [Geohashing and Quadtrees](../curriculum/10-security-and-location/04-geohashing-and-quadtrees.md)
