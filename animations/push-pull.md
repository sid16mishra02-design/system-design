# Who initiates the update: sender or receiver?

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Who initiates the update: sender or receiver?](../assets/animations/push-pull.gif)

</details>

## Read the same sequence without motion

1. Both alternatives begin with the receiver knowing version V1.
2. The provider records V2 and initiates a push notification.
3. The polling receiver can remain on V1 until its next check.
4. The polling receiver initiates a request asking for updates.
5. The pull response now supplies V2. Poll interval and retry behavior affect delay.

[View all states as still images](../assets/animations/push-pull-steps.png)

## Related lessons

- [Push vs pull](../practice/TRADEOFFS.md)
