# Event sourcing: replay builds state

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Event sourcing: replay builds state](../assets/animations/event-sourcing.gif)

</details>

## Read the same sequence without motion

1. Append Deposited(100) to the durable event history.
2. Apply the event to the derived balance.
3. Append Withdrawn(30), then update the view.
4. The current balance is 70.
5. Replay rebuilds the view; avoid repeating external side effects such as email.

[View all states as still images](../assets/animations/event-sourcing-steps.png)

## Related lessons

- [Event Sourcing](../curriculum/08-architectural-patterns/04-event-sourcing.md)
