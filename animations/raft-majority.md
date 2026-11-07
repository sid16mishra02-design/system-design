# Raft: minority isolation stops safe progress

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Raft: minority isolation stops safe progress](../assets/animations/raft-majority.gif)

</details>

## Read the same sequence without motion

1. A is leader in this illustrative three-voter crash-fault group.
2. Raft replicates and commits entries using its log, term, and majority rules.
3. A becomes isolated. A alone cannot commit conflicting new decisions.
4. B and C can elect a leader when protocol and timing conditions permit.
5. Only the communicating majority can progress under the protocol rules.

[View all states as still images](../assets/animations/raft-majority-steps.png)

## Related lessons

- [Consensus Algorithms](../curriculum/09-reliability-and-microservices/06-consensus-algorithms.md)
