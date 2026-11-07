# Animated system-design walkthroughs

[← Learning path](../README.md) · [Topic validation](../TOPIC-VALIDATION.md)

Open an animation only when you want motion. Every walkthrough has numbered text steps and a still-image sequence, so you can study without autoplay or at your own pace. Each state is held for seven seconds, with a short movement between states. Loops replay the same illustrative scenario; they are not performance benchmarks or complete protocol simulations.

| Walkthrough | Lessons using it |
| --- | --- |
| [Find the slow part of a request](request-latency.md) | Latency vs Throughput vs Bandwidth, Distributed Tracing, Latency vs throughput |
| [DNS: a name becomes an address](dns-lookup.md) | Domain Name System (DNS) |
| [Lost data: transport choices](tcp-udp.md) | TCP and UDP |
| [Scale a service without losing sessions](load-balancer.md) | Scalability, Load Balancing, Clustering, Stateful vs stateless design |
| [Cache-aside: hit, miss, and update](cache-aside.md) | Caching, Caching Strategies, Distributed Caching |
| [Replication is copying, not partitioning](replication.md) | Database Replication, Strong vs eventual consistency |
| [Two buyers, one remaining ticket](atomic-stock.md) | Transactions, ACID and BASE consistency models |
| [An address update and duplicated data](normalization.md) | Normalization and Denormalization |
| [Sharding divides ownership of data](sharding.md) | Sharding, Database Federation |
| [Consistent hashing: a node joins](consistent-hash.md) | Consistent Hashing |
| [Bloom filter: no, or maybe](bloom-filter.md) | Bloom Filters |
| [CAP: a choice during a partition](cap-partition.md) | CAP Theorem, Strong vs eventual consistency |
| [PACELC: normal operation also matters](pacelc.md) | PACELC Theorem |
| [A saga compensates a completed step](saga.md) | Distributed Transactions, Reliability |
| [LRU and FIFO make different choices](cache-eviction.md) | Cache Eviction Policies |
| [A lost response must not mean two charges](idempotency.md) | Idempotency, Webhooks, Reliability |
| [Token bucket: bursts have a limit](token-bucket.md) | Rate Limiting |
| [Which way do live updates travel?](realtime-protocols.md) | Long polling, WebSockets, Server-Sent Events (SSE), Long polling vs WebSockets |
| [A work queue can redeliver a job](work-queue.md) | Message Brokers, Message Queues |
| [Independent subscribers need their own copy](pub-sub.md) | Publish-Subscribe, Event-Driven Architecture (EDA) |
| [CDC: a committed change reaches a read view](cdc.md) | Change Data Capture (CDC) |
| [Event sourcing: replay builds state](event-sourcing.md) | Event Sourcing |
| [CQRS: a read view can lag behind a write](cqrs.md) | Command and Query Responsibility Segregation (CQRS) |
| [Circuit breaker: closed, open, half-open](circuit-breaker.md) | Circuit breaker |
| [Discovery data can become stale](discovery-heartbeat.md) | Service Discovery, HeartBeats |
| [Recovery time and data-loss targets differ](recovery-objectives.md) | Disaster recovery |
| [OAuth / OIDC: code, tokens, and audiences](oauth-oidc.md) | OAuth 2.0 and OpenID Connect (OIDC) |
| [SSO does not mean one universal app session](single-sign-on.md) | Single Sign-On (SSO) |
| [TLS identity is separate from authorization](tls-mtls.md) | SSL, TLS, mTLS, HTTP/HTTPS |
| [Nearby search must cross cell boundaries](nearby-search.md) | Geohashing and Quadtrees |
| [Raft: minority isolation stops safe progress](raft-majority.md) | Consensus Algorithms |
| [Lease expiry does not stop the old worker](fencing-token.md) | Distributed Locking |
| [Gossip spreads knowledge gradually](gossip-spread.md) | Gossip Protocol |
| [A replacement helps only if traffic reaches it](availability-failover.md) | Availability |
| [An index narrows the records to examine](index-lookup.md) | Indexes |
| [CDN: origin miss, then nearby reuse](cdn-edge.md) | Content Delivery Network (CDN) |
| [Peers share verified pieces and may leave](p2p-pieces.md) | Peer-to-Peer (P2P) Architecture |
| [Design example: create and resolve a short URL](case-url-shortener.md) | URL Shortener |
| [Design example: accepted is not yet delivered](case-whatsapp.md) | WhatsApp |
| [Design example: fanout makes feeds fast, at a cost](case-twitter.md) | Twitter |
| [Design example: prepare video, then serve nearby](case-netflix.md) | Netflix |
| [Design example: near a rider does not mean available](case-uber.md) | Uber |
| [Interleaving is different from simultaneous execution](concurrency-parallelism.md) | Concurrency vs parallelism, Latency vs throughput |
| [Batch and streaming organize the same arrivals differently](batch-stream.md) | Batch vs stream processing |
| [Read-through and write-through can be combined](read-write-through.md) | Read-through vs write-through cache |
| [Who initiates the update: sender or receiver?](push-pull.md) | Push vs pull |
| [An order response can precede email completion](sync-async.md) | Synchronous vs asynchronous communication |
