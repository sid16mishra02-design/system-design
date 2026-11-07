# Gossip spreads knowledge gradually

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Gossip spreads knowledge gradually](../assets/animations/gossip-spread.gif)

</details>

## Read the same sequence without motion

1. A learns a new membership observation, version V2.
2. A exchanges information with B.
3. B later exchanges with C; D may still have old information.
4. A reachable peer exchange eventually reaches D under convergence assumptions.
5. Spreading observations is not consensus on one committed transaction history.

[View all states as still images](../assets/animations/gossip-spread-steps.png)

## Related lessons

- [Gossip Protocol](../curriculum/09-reliability-and-microservices/08-gossip-protocol.md)
