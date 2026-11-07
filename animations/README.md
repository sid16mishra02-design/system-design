# Animated system-design walkthroughs

[← Learning path](../README.md) · [Topic validation](../TOPIC-VALIDATION.md)

Animations are visible by default, play automatically, and repeat with four seconds per step. Motion shows the active path, then the finished state pauses for reading. Each frame focuses on what happened, why it matters, and what comes next. Follow the numbered explanation or open the full-resolution still sequence to study at your own pace. These are illustrative architectures, not performance benchmarks or complete protocol simulations.

| Walkthrough | Lessons using it |
| --- | --- |
| [Latency: trace the complete request](request-latency.md) | Latency vs Throughput vs Bandwidth, Distributed Tracing, Latency vs throughput |
| [DNS: lookup, cache, and a server move](dns-lookup.md) | Domain Name System (DNS) |
| [TCP and UDP: what a loss changes](tcp-udp.md) | TCP and UDP |
| [Load balancing: healthy routing and shared state](load-balancer.md) | Scalability, Load Balancing, Clustering, Stateful vs stateless design |
| [Cache-aside: speed, stale copies, and recovery](cache-aside.md) | Caching, Caching Strategies, Distributed Caching |
| [Replication: write, lag, read, and restore](replication.md) | Database Replication, Strong vs eventual consistency |
| [Transactions: two buyers and the final ticket](atomic-stock.md) | Transactions, ACID and BASE consistency models |
| [Normalize current facts; preserve historical snapshots](normalization.md) | Normalization and Denormalization |
| [Sharding: route by ownership, then handle growth](sharding.md) | Sharding, Database Federation |
| [Consistent hashing: placement and membership changes](consistent-hash.md) | Consistent Hashing |
| [Bloom filters: a cheap gate, not the authority](bloom-filter.md) | Bloom Filters |
| [CAP: compare two partition policies](cap-partition.md) | CAP Theorem, Strong vs eventual consistency |
| [PACELC: healthy-path latency and partition policy](pacelc.md) | PACELC Theorem |
| [Saga: local commits and compensating recovery](saga.md) | Distributed Transactions, Reliability |
| [Cache eviction: replay LRU and FIFO](cache-eviction.md) | Cache Eviction Policies |
| [Idempotency: retries, durable state, and recovery](idempotency.md) | Idempotency, Webhooks, Reliability |
| [Token bucket: protect shared search capacity](token-bucket.md) | Rate Limiting |
| [Live updates: compare complete connection lifecycles](realtime-protocols.md) | Long polling, WebSockets, Server-Sent Events (SSE), Long polling vs WebSockets |
| [Work queues: absorb bursts and survive worker crashes](work-queue.md) | Message Brokers, Message Queues |
| [Pub/sub: one event, independent business reactions](pub-sub.md) | Publish-Subscribe, Event-Driven Architecture (EDA) |
| [CDC: capture commits, update views, and replay safely](cdc.md) | Change Data Capture (CDC) |
| [Event sourcing: history is authoritative, views are rebuildable](event-sourcing.md) | Event Sourcing |
| [CQRS: separate writes from query-shaped read views](cqrs.md) | Command and Query Responsibility Segregation (CQRS) |
| [Circuit breaker: stop cascading calls, then test recovery](circuit-breaker.md) | Circuit breaker |
| [Discovery: find instances, detect suspicion, and route safely](discovery-heartbeat.md) | Service Discovery, HeartBeats |
| [Disaster recovery: recover data and restore useful service](recovery-objectives.md) | Disaster recovery |
| [OAuth and OIDC: delegated access without sharing passwords](oauth-oidc.md) | OAuth 2.0 and OpenID Connect (OIDC) |
| [SSO: reuse provider login, keep application sessions explicit](single-sign-on.md) | Single Sign-On (SSO) |
| [TLS and mTLS: protect connections, then authorize the operation](tls-mtls.md) | SSL, TLS, mTLS, HTTP/HTTPS |
| [Nearby search: index candidates, then verify real proximity](nearby-search.md) | Geohashing and Quadtrees |
| [Raft: commit one replicated history despite a minority partition](raft-majority.md) | Consensus Algorithms |
| [Fencing: make the protected resource reject stale owners](fencing-token.md) | Distributed Locking |
| [Gossip: membership spreads without instant agreement](gossip-spread.md) | Gossip Protocol |
| [Availability: replace, reroute, and inspect dependencies](availability-failover.md) | Availability |
| [Indexes: narrow a query without forgetting write cost](index-lookup.md) | Indexes |
| [CDN: origin content, nearby reuse, and freshness](cdn-edge.md) | Content Delivery Network (CDN) |
| [P2P: exchange verified pieces and survive departures](p2p-pieces.md) | Peer-to-Peer (P2P) Architecture |
| [URL shortener: create, resolve, cache, and disable](case-url-shortener.md) | URL Shortener |
| [Messaging: durable acceptance, routing, and reconnect](case-whatsapp.md) | WhatsApp |
| [Feeds: publish, fan out, read, and enforce visibility](case-twitter.md) | Twitter |
| [Video: prepare renditions, then serve media nearby](case-netflix.md) | Netflix |
| [Ride matching: fresh candidates are not reservations](case-uber.md) | Uber |
| [Concurrency: overlap work; parallelism: execute together](concurrency-parallelism.md) | Concurrency vs parallelism, Latency vs throughput |
| [Batch and stream: choose freshness and recovery rules](batch-stream.md) | Batch vs stream processing |
| [Cache-through policies: load reads and persist writes](read-write-through.md) | Read-through vs write-through cache |
| [Push and pull: who initiates learning about a change?](push-pull.md) | Push vs pull |
| [Sync and async: complete the order, then process email](sync-async.md) | Synchronous vs asynchronous communication |
| [API gateway: derive the boundary from the screen](api-gateway.md) | API Gateway |
