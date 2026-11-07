# Find the slow part of a request

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Find the slow part of a request](../assets/animations/request-latency.gif)

</details>

## Read the same sequence without motion

1. A request begins. Its response time includes each sequential stage.
2. Application work adds 70 ms before the database call.
3. Sequential total: 30 + 70 + 100 = 200 ms. This is one request latency.
4. A suitable index reduces only the query stage: 100 ms becomes 25 ms.
5. New total: 125 ms. More completed requests per second is a separate measure.

[View all states as still images](../assets/animations/request-latency-steps.png)

## Related lessons

- [Latency vs Throughput vs Bandwidth](../curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md)
- [Distributed Tracing](../curriculum/09-reliability-and-microservices/09-distributed-tracing.md)
- [Latency vs throughput](../practice/TRADEOFFS.md)
