# Consistent hashing: placement and membership changes

[← Animation index](README.md)

**Problem:** Limit key remapping when storage or cache membership changes.

**Scenario:** Illustrative K at 170 moves from C to new node D at 200.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Consistent hashing: placement and membership changes](../assets/animations/consistent-hash.gif)

## Read the same sequence without motion

1. **A member joins.** A cache node joins. Which keys must move, and how will clients find the new owners?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Which range changes ownership; Does a new map move actual data.
2. **Find the old owner.** Key K at 170 reaches C at 260 first; the router sends K's request there.
   - **Why it matters:** Ownership follows the ring rule even when another server looks physically nearer.
   - **Notice:** Clockwise successor owns the key; K is after B and before C.
3. **See a key that differs.** Key Q at 80 reaches B at 140 and is served independently.
   - **Why it matters:** Different key positions can have different owners on the same ring.
   - **Notice:** The router does not contact all nodes; Placement does not imply replication.
4. **Add a new member.** D joins at 200, splitting part of C's previous ownership range.
   - **Why it matters:** A new member changes only its affected successor range under this scheme.
   - **Notice:** Changed interval: greater than 140; Up to and including 200 maps to D.
5. **Move the affected data.** K at 170 moves from C to D; migration must make its data available at the new owner.
   - **Why it matters:** A new mapping alone does not transfer the stored value.
   - **Notice:** Copy data before relying on new owner; Coordinate writes during migration.
6. **Route using the new view.** The updated router now selects D for K, while Q still belongs to B.
   - **Why it matters:** The benefit is limited key movement, not a guarantee of perfectly even load.
   - **Notice:** Q at 80 still maps to B; K at 170 now meets D first.
7. **Handle a stale map.** A client using old membership may still contact C, so migration needs a compatibility policy.
   - **Why it matters:** Membership convergence and data migration are separate operational concerns.
   - **Notice:** Use versioning or deliberate forwarding; Do not assume instant map agreement.
8. **Account for hot keys.** Virtual nodes can balance ranges, but one extremely popular key can still overload its owner.
   - **Why it matters:** Consistent hashing reduces remapping; it does not remove skew or provide recovery automatically.
   - **Notice:** K/N is a balanced-case estimate; Replicas and hot-key handling are extra.

**Design tradeoff:** Limited movement reduces disruption, but membership agreement, data transfer, skew, replication, and recovery remain separate responsibilities.

[View all states as still images](../assets/animations/consistent-hash-steps.png)

## Related lessons

- [Consistent Hashing](../curriculum/03-databases/12-consistent-hashing.md)
