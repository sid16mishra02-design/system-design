# A saga compensates a completed step

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![A saga compensates a completed step](../assets/animations/saga.gif)

</details>

## Read the same sequence without motion

1. Record a pending order and a recoverable step identifier.
2. A local payment operation commits successfully.
3. Stock reservation fails. Earlier committed work did not vanish.
4. The saga issues a compensating refund with safe retry behavior.
5. Record completion after confirmation; compensation can take time or fail too.

[View all states as still images](../assets/animations/saga-steps.png)

## Related lessons

- [Distributed Transactions](../curriculum/04-distributed-data/03-distributed-transactions.md)
- [Reliability](../curriculum/01-core-concepts/05-reliability.md)
