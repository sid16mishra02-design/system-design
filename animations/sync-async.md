# An order response can precede email completion

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![An order response can precede email completion](../assets/animations/sync-async.gif)

</details>

## Read the same sequence without motion

1. A client submits an order request.
2. Persist the order and recoverable email work record under the required atomic rule.
3. Asynchronous choice: acknowledge order creation, not email completion.
4. A recoverable handoff queues email work.
5. The worker can finish the email later and must tolerate retries.
6. Separate synchronous choice: the caller waits for required downstream work.
7. That response is delayed by the downstream result and its failure behavior.

[View all states as still images](../assets/animations/sync-async-steps.png)

## Related lessons

- [Synchronous vs asynchronous communication](../practice/TRADEOFFS.md)
