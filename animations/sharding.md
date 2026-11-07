# Sharding: route by ownership, then handle growth

[← Animation index](README.md)

**Problem:** Divide a dataset while accounting for routing, replication, hot shards, and cross-shard queries.

**Scenario:** Illustrative customer ranges 1-1000 and 1001-2000 live on different shards.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Sharding: route by ownership, then handle growth](../assets/animations/sharding.gif)

## Read the same sequence without motion

1. **Outgrow one database.** Customer traffic outgrows one database. How should a request find its owner without querying every machine?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Which key determines ownership; Does a copy own a different range.
2. **Use the customer's key.** Customer 42 reaches the router, which selects A from the range map.
   - **Why it matters:** A suitable shard key can keep one customer's related work local.
   - **Notice:** Route by an explicit ownership rule; A key is not merely a random label.
3. **Return the local result.** A returns the customer's data without asking B to scan its unrelated range.
   - **Why it matters:** Sharding helps targeted work when queries know the partition key.
   - **Notice:** Not every query benefits equally; Shared dependencies can remain.
4. **Route another owner.** Customer 1500 instead goes to B and receives B's result.
   - **Why it matters:** B is another owner, not an interchangeable replica of A.
   - **Notice:** Requests need the correct owner; Data model and routing must agree.
5. **Copy A independently.** A's changes propagate to its replica while B continues owning a different dataset.
   - **Why it matters:** Availability requires deliberate replicas and failover, not just more distinct shards.
   - **Notice:** Losing an unreplicated shard hurts; Replica lag still needs a policy.
6. **Run a cross-range query.** The reporting service needs both ranges, so the router fans out and merges the results.
   - **Why it matters:** A fast single-key read does not make global joins or totals free.
   - **Notice:** Fan-out adds work and waiting; Cross-shard writes need coordination.
7. **Notice a hot customer.** A celebrity customer overloads A even though both shards contain similar customer counts.
   - **Why it matters:** Balance actual traffic and data, not just the number of keys.
   - **Notice:** One hot key can dominate requests; More B capacity does not help A.
8. **Plan growth and movement.** Changing ownership needs a migration plan that keeps routing and data location compatible.
   - **Why it matters:** Rebalancing is an operational process, not a label on a diagram.
   - **Notice:** Control client map disagreement; Verify copies before switching owners.
9. **Compare the alternatives.** Improve queries first; split by domain only when billing and catalog need functional separation.
   - **Why it matters:** Customer-key sharding differs from a domain split or a federated query layer.
   - **Notice:** Domain split changes fact ownership; Federation can unify autonomous stores.

**Design tradeoff:** Targeted reads can scale, but skew, rebalancing, and cross-shard coordination add complexity; sharding alone is not redundancy.

[View all states as still images](../assets/animations/sharding-steps.png)

## Related lessons

- [Sharding](../curriculum/03-databases/11-sharding.md)
- [Database Federation](../curriculum/03-databases/13-database-federation.md)
