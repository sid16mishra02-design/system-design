# Independent subscribers need their own copy

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Independent subscribers need their own copy](../assets/animations/pub-sub.gif)

</details>

## Read the same sequence without motion

1. Publish OrderPlaced once to a topic.
2. The billing subscription receives its own logical delivery.
3. The shipping subscription receives its own logical delivery.
4. Workers within one subscription may compete; independent subscriptions do not.
5. Timing and delivery guarantees depend on the broker and configuration.

[View all states as still images](../assets/animations/pub-sub-steps.png)

## Related lessons

- [Publish-Subscribe](../curriculum/07-asynchronous-communication/03-publish-subscribe.md)
- [Event-Driven Architecture (EDA)](../curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md)
