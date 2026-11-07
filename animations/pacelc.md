# PACELC: normal operation also matters

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![PACELC: normal operation also matters](../assets/animations/pacelc.gif)

</details>

## Read the same sequence without motion

1. Normal operation: waiting for distant coordination can cost latency.
2. Coordinated completion can provide the chosen stronger guarantee.
3. An asynchronous path can respond sooner while the remote copy lags.
4. During a partition, availability versus consistency becomes a separate choice.

[View all states as still images](../assets/animations/pacelc-steps.png)

## Related lessons

- [PACELC Theorem](../curriculum/04-distributed-data/02-pacelc-theorem.md)
