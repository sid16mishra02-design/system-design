# P2P: exchange verified pieces and survive departures

[← Animation index](README.md)

**Problem:** Distribute content-serving work while verifying pieces and tolerating peers leaving.

**Scenario:** A new downloader exchanges file pieces with peers, then loses one source.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![P2P: exchange verified pieces and survive departures](../assets/animations/p2p-pieces.gif)

## Read the same sequence without motion

1. **Find potential sources.** C obtains candidate peers instead of asking the origin for every byte.
   - **Why it matters:** Discovery helps locate peers but does not prove they are reachable or trustworthy.
   - **Notice:** Addresses are candidates, not guarantees; Discovery may remain centralized.
2. **Know what to verify.** C retrieves trusted metadata identifying the expected file pieces.
   - **Why it matters:** A matching untrusted file and untrusted checksum do not establish authenticity.
   - **Notice:** Use trustworthy expected hashes; Check each received piece.
3. **Receive useful pieces.** A sends pieces 1 and 2, which C verifies before keeping.
   - **Why it matters:** A peer can serve data it already has without holding the entire file.
   - **Notice:** Verification precedes useful reuse; Transfers can be resumed by piece.
4. **Obtain another piece.** B provides piece 3 while C still lacks piece 4.
   - **Why it matters:** Different peers contribute different parts of the same logical content.
   - **Notice:** Track which pieces are still missing; Choose useful reachable sources.
5. **Become a source too.** C uploads verified piece 3 to A rather than only consuming bandwidth.
   - **Why it matters:** Participants can provide as well as consume, spreading origin-serving work.
   - **Notice:** Upload limits protect participants; Sharing does not imply no servers.
6. **A source disappears.** B leaves before C receives its remaining piece.
   - **Why it matters:** Churn and scarce pieces can delay completion even after most bytes arrive.
   - **Notice:** Peers can leave without warning; More peers need not hold every piece.
7. **Recover missing content.** C finds piece 4 at the origin and verifies the fallback transfer.
   - **Why it matters:** Alternative sources and resumable progress keep one departure from discarding all work.
   - **Notice:** Origin fallback still consumes capacity; Trust checks apply to every source.
8. **Measure the real exchange.** C assembles the file while the system measures origin traffic and completion time.
   - **Why it matters:** Optimize useful pieces, reachability, and upload cost rather than counting peers alone.
   - **Notice:** Test low-upload and malicious peers; Bound connections and per-peer work.

**Design tradeoff:** Peer upload capacity reduces origin load but introduces discovery, integrity, reachability, and scarce-piece challenges.

[View all states as still images](../assets/animations/p2p-pieces-steps.png)

## Related lessons

- [Peer-to-Peer (P2P) Architecture](../curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md)
