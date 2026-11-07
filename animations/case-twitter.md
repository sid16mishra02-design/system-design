# Design example: fanout makes feeds fast, at a cost

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Design example: fanout makes feeds fast, at a cost](../assets/animations/case-twitter.gif)

</details>

## Read the same sequence without motion

1. Persist a new post with its author and stable identifier.
2. Schedule recoverable fanout work rather than blocking on every follower.
3. Fanout updates follower timelines, which can temporarily lag.
4. A reader asks the feed service for a bounded page.
5. Read prepared timeline references, then retrieve authorized post content.
6. Very large authors may need another fanout policy; a hybrid trades write work for read work.

[View all states as still images](../assets/animations/case-twitter-steps.png)

## Related lessons

- [Twitter](../practice/twitter.md)
