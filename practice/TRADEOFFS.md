# System design tradeoffs

[← Start here](../README.md) · [Schedule](../SCHEDULE.md)

Use these comparisons after the fundamentals. For each choice, state the requirement, what each option costs, and what changed requirement would make you reconsider. These summaries are study aids; the local lessons provide the detail.

| Comparison | What differs | Concrete consequence | Local explanation |
| --- | --- | --- | --- |
| Vertical vs horizontal scaling | Larger machine vs more machines. | Check the shared database bottleneck. | [Revisit lesson](../curriculum/01-core-concepts/02-scalability.md) |
| Concurrency vs parallelism | Managing overlapping tasks vs executing tasks at the same time. | One cook can alternate tasks; several cooks can work simultaneously. | [Revisit lesson](../curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) |
| Long polling vs WebSockets | Repeated waiting requests vs a persistent two-way connection. | Use message direction, frequency, and reconnect behavior to choose. | [Revisit lesson](../curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) |
| Batch vs stream processing | Process accumulated records together vs process a continuing flow. | Nightly sales reports favor batches; live fraud signals need timely updates. | [Revisit lesson](../curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md) |
| Stateful vs stateless design | Requests depend on server-local session state vs portable request context. | With an external session store, another app server can handle the next request. | [Revisit lesson](../curriculum/06-api-fundamentals/01-apis.md) |
| Strong vs eventual consistency | Reads reflect completed writes vs replicas converge after writes stop and communication recovers. | Profile display may tolerate lag; stock reservation needs an explicit correctness rule. | [Revisit lesson](../curriculum/04-distributed-data/01-cap-theorem.md) |
| Read-through vs write-through cache | The cache loads missed reads vs the cache layer persists writes synchronously. | A product cache can load read misses and synchronously persist writes; these policies can be combined. | [Revisit lesson](../curriculum/05-caching/02-caching-strategies.md) |
| Push vs pull | Sender initiates delivery vs receiver requests updates. | A webhook pushes payment news; polling repeatedly asks for it. | [Revisit lesson](../curriculum/06-api-fundamentals/07-webhooks.md) |
| REST vs RPC | Resource-oriented interfaces vs calling defined operations. | Use resource reads for products; typed service operations can reserve inventory. | [Revisit lesson](../curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) |
| Synchronous vs asynchronous communication | Caller waits for completion vs completion is decoupled from the initiating call. | Queued email can finish after the order confirmation. | [Revisit lesson](../curriculum/07-asynchronous-communication/02-message-queues.md) |
| Latency vs throughput | Time for one operation vs operations completed per unit time. | More counters can serve more customers without shortening each individual checkout. | [Revisit lesson](../curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) |

## Work through a decision

A public profile may tolerate briefly stale reads. Reserving the last ticket needs an explicit overselling policy. Write down the operation and acceptable failure behavior before picking a consistency model; avoid assigning one universal choice to the whole application.

## Visual comparisons

- Concurrency vs parallelism: [Walkthrough](../animations/concurrency-parallelism.md)
- Long polling vs WebSockets: [Walkthrough](../animations/realtime-protocols.md)
- Batch vs stream processing: [Walkthrough](../animations/batch-stream.md)
- Stateful vs stateless design: [Walkthrough](../animations/load-balancer.md)
- Strong vs eventual consistency: [Walkthrough](../animations/replication.md), [Walkthrough](../animations/cap-partition.md)
- Read-through vs write-through cache: [Walkthrough](../animations/read-write-through.md)
- Push vs pull: [Walkthrough](../animations/push-pull.md)
- Synchronous vs asynchronous communication: [Walkthrough](../animations/sync-async.md)
- Latency vs throughput: [Walkthrough](../animations/concurrency-parallelism.md), [Walkthrough](../animations/request-latency.md)

## Optional articles

The guide above covers the scheduled comparisons. These direct article links are for deeper reading, not prerequisites:

- [Top 15 Tradeoffs](https://blog.algomaster.io/p/system-design-top-15-trade-offs)
- [Vertical vs Horizontal Scaling](https://algomaster.io/learn/system-design/vertical-vs-horizontal-scaling)
- [Concurrency vs Parallelism](https://blog.algomaster.io/p/concurrency-vs-parallelism)
- [Long Polling vs WebSockets](https://blog.algomaster.io/p/long-polling-vs-websockets)
- [Batch vs Stream Processing](https://blog.algomaster.io/p/batch-processing-vs-stream-processing)
- [Stateful vs Stateless Design](https://blog.algomaster.io/p/stateful-vs-stateless-architecture)
- [Strong vs Eventual Consistency](https://blog.algomaster.io/p/strong-vs-eventual-consistency)
- [Read-Through vs Write-Through Cache](https://blog.algomaster.io/p/59cae60d-9717-4e20-a59e-759e370db4e5)
- [Push vs Pull Architecture](https://blog.algomaster.io/p/af5fe2fe-9a4f-4708-af43-184945a243af)
- [REST vs RPC](https://blog.algomaster.io/p/106604fb-b746-41de-88fb-60e932b2ff68)
- [Synchronous vs. asynchronous communications](https://blog.algomaster.io/p/aec1cebf-6060-45a7-8e00-47364ca70761)
- [Latency vs Throughput](https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/)
