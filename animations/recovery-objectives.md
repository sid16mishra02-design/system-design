# Recovery time and data-loss targets differ

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Recovery time and data-loss targets differ](../assets/animations/recovery-objectives.gif)

</details>

## Read the same sequence without motion

1. A recoverable backup exists at 10:00.
2. The service fails at 10:20; newer data may need another recoverable log.
3. Without newer recoverable data, this scenario loses up to 20 minutes.
4. Restore and validation take until 11:00.
5. Observed recovery took 40 minutes. RPO/RTO are targets, not these observations.

[View all states as still images](../assets/animations/recovery-objectives-steps.png)

## Related lessons

- [Disaster recovery](../curriculum/09-reliability-and-microservices/05-disaster-recovery.md)
