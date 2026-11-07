# System design tradeoffs

[← Start here](../README.md) · [Schedule](../SCHEDULE.md)

Use these after foundations. For each decision, write the requirement, both choices, the cost of each, and a condition that would reverse your choice.

The following source link list is preserved from Ashish Pratap Singh’s repository.

## ⚖️ System Design Tradeoffs
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

Example decision: a public profile may tolerate briefly stale reads; a limited-stock checkout needs an explicit overselling policy. Choose guarantees for an operation and a failure scenario, rather than labeling an entire database “always consistent.”
