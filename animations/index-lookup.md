# Indexes: narrow a query without forgetting write cost

[← Animation index](README.md)

**Problem:** Reduce unnecessary record examination for a demonstrated access pattern.

**Scenario:** A customer requests ten recent orders from a large order table.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Indexes: narrow a query without forgetting write cost](../assets/animations/index-lookup.gif)

## Read the same sequence without motion

1. **State the access pattern.** The API asks for one customer's newest ten orders, not every order.
   - **Why it matters:** An index should serve an actual filter, ordering, and result size.
   - **Notice:** Inputs define the query; A bounded page limits returned work.
2. **Measure the starting plan.** Without a suitable access path, many unrelated records may be examined.
   - **Why it matters:** Separate rows examined from rows returned when locating expensive work.
   - **Notice:** Use representative data; A small test table can hide the cost.
3. **Consider a matching index.** An index beginning with customer and creation time offers a narrower path.
   - **Why it matters:** A matching index may avoid scanning unrelated customer records.
   - **Notice:** Column order matters to this query; Benefit depends on the database.
4. **Locate the needed records.** The selected range leads to the records needed for the page.
   - **Why it matters:** An index is an access structure, not a second independent source of truth.
   - **Notice:** Some plans still fetch table rows; Not every query uses this index.
5. **Return and compare.** The API returns the page and compares query timing with the original workload.
   - **Why it matters:** Verify the actual plan and latency rather than assuming index presence means improvement.
   - **Notice:** Keep workload and data comparable; Check result correctness too.
6. **Writes maintain the index.** A newly created order changes both stored records and the index structure.
   - **Why it matters:** Read acceleration creates extra write and storage work.
   - **Notice:** Updates may modify index entries; Too many indexes multiply maintenance.
7. **Another query may scan.** A broad filter may make scanning preferable to many individual lookups.
   - **Why it matters:** The planner can reasonably choose a different access path for a different query.
   - **Notice:** Low selectivity changes the work; Do not force one universal index.
8. **Keep evidence, not clutter.** Compare read gain, write latency, storage, and the workloads each index supports.
   - **Why it matters:** Remove only genuinely unused indexes after checking all relevant query workloads.
   - **Notice:** Inspect plans after workload changes; Optimize the bottleneck you measured.

**Design tradeoff:** Useful indexes can speed selected reads while consuming storage and adding maintenance work to writes.

[View all states as still images](../assets/animations/index-lookup-steps.png)

## Related lessons

- [Indexes](../curriculum/03-databases/06-indexes.md)
