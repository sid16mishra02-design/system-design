# CQRS: a read view can lag behind a write

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![CQRS: a read view can lag behind a write](../assets/animations/cqrs.gif)

</details>

## Read the same sequence without motion

1. A command creates order 42 in the write model.
2. An update event waits for processing.
3. A list read can temporarily show the old view.
4. The projector applies the update to the read view.
5. CQRS separates read and write responsibilities; event sourcing is optional.

[View all states as still images](../assets/animations/cqrs-steps.png)

## Related lessons

- [Command and Query Responsibility Segregation (CQRS)](../curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md)
