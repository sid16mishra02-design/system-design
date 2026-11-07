# Category × topic validation

[← Learning path](README.md) · [Animations](animations/README.md) · [Content audit](CONTENT-AUDIT.md)

Every one of the **71 foundational topics** was read for understandable technical fundamentals, the specific problem it solves, and its use inside a system-design scenario. The evidence links below point to actual lesson text, not a check based only on headings. The application steps and tradeoff explain why the component belongs in that design.

This is an editorial review, not proof that every reader will find every concept easy. Ambiguous inherited statements were clarified in independent teaching notes; original licensed passages remain unchanged. For those topics, read the applied clarification as well as the preserved excerpt.

Animations are selected for sequence, state, interleaving, or spatial-boundary confusion. A simple definition or comparison does not automatically need one. Shared walkthroughs show a particular application and do not claim that related concepts are identical. Every animation has text steps and still images.

## Clarifications made during validation

- [Scalability](curriculum/01-core-concepts/02-scalability.md#make-it-concrete): Scaling capacity does not determine consistency.
- [Availability](curriculum/01-core-concepts/03-availability.md#make-it-concrete): Redundancy formulas need failure-dependence assumptions.
- [OSI Model](curriculum/02-networking/02-osi-model.md#make-it-concrete): The layered model is conceptual rather than seven separate machines.
- [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md#make-it-concrete): Transport delivery and application-level behavior are distinct.
- [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md#make-it-concrete): Managed DNS can support health-aware routing; caching still affects changes.
- [Proxy](curriculum/02-networking/05-proxy.md#make-it-concrete): Reverse proxies and load balancers can overlap in responsibility.
- [Load Balancing](curriculum/02-networking/08-load-balancing.md#make-it-concrete): Balancing application traffic does not remove shared dependency limits.
- [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md#make-it-concrete): NULL behavior and access models are not universal SQL/NoSQL distinctions.
- [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md#make-it-concrete): Keys, partial dependencies, and historical snapshots require precise meanings.
- [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md#make-it-concrete): ACID consistency is distinct from replica consistency; isolation levels vary.
- [Sharding](curriculum/03-databases/11-sharding.md#make-it-concrete): Dividing ownership is different from copying data for resilience.
- [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md#make-it-concrete): Key movement, load balance, and hot-key traffic are separate concerns.
- [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md#make-it-concrete): One-copy real-time consistency and CAP availability need precise definitions.
- [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md#make-it-concrete): Streaming systems can track consumer progress and provide delivery guarantees.
- [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md#make-it-concrete): At-least-once delivery can repeat execution.
- [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md#make-it-concrete): Subscription delivery can be pull-based or retained rather than immediate push.
- [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#make-it-concrete): Code exchange, PKCE, token audience, format, and lifetime are separate choices.
- [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#make-it-concrete): Targets, observations, measurement windows, and error budgets are different concepts.

## Practice categories 11–13

The [practice-category audit](PRACTICE-VALIDATION.md) covers the eleven comparisons, interview method, and five designs. Together, the two audits cover all **88 items across 13 categories**. The five designs have their own animated request flows.

## Problem-first learning

All 71 foundational topics now open with a concrete situation and questions to attempt before the explanation. The five design exercises and interview method also start with a problem. The [inquiry review](metadata/inquiry-review.json) records every foundational opening. These prompts and the independent notes are counted together in the content audit. The owner approved expansion beyond the initial 30% guideline where understanding needs more space; the table reports actual additions. None of the preserved source explanations has been removed.

## At-a-glance matrix

| Category / topic | Try the problem | Technical fundamental | Problem and design application | Animation |
| --- | --- | --- | --- | --- |
| 01-core-concepts: [What is system design?](curriculum/01-core-concepts/01-what-is-system-design.md) | [Scenario](curriculum/01-core-concepts/01-what-is-system-design.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/01-what-is-system-design.md#make-it-concrete) | Choosing components before knowing the behavior and failure guarantees the system must provide. [Applied evidence](curriculum/01-core-concepts/01-what-is-system-design.md#make-it-concrete) | Static explanation sufficient |
| 01-core-concepts: [Scalability](curriculum/01-core-concepts/02-scalability.md) | [Scenario](curriculum/01-core-concepts/02-scalability.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/02-scalability.md#make-it-concrete) | A rising request rate exceeds the capacity of a particular stage. [Applied evidence](curriculum/01-core-concepts/02-scalability.md#make-it-concrete) | [load-balancer](animations/load-balancer.md) |
| 01-core-concepts: [Availability](curriculum/01-core-concepts/03-availability.md) | [Scenario](curriculum/01-core-concepts/03-availability.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/03-availability.md#make-it-concrete) | Users lose access when a server or shared dependency fails. [Applied evidence](curriculum/01-core-concepts/03-availability.md#make-it-concrete) | [availability-failover](animations/availability-failover.md) |
| 01-core-concepts: [Latency vs Throughput vs Bandwidth](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) | [Scenario](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md#throughput-concurrency-and-waiting) | Optimizing the wrong performance quantity or interpreting averages and network capacity as interchangeable. [Applied evidence](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md#how-to-optimize-the-right-thing) | [request-latency](animations/request-latency.md) |
| 01-core-concepts: [Reliability](curriculum/01-core-concepts/05-reliability.md) | [Scenario](curriculum/01-core-concepts/05-reliability.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/05-reliability.md#what-it-means) | A partially completed operation can leave users with duplicate charges, lost state, or a permanently unresolved order. [Applied evidence](curriculum/01-core-concepts/05-reliability.md#worked-failure-and-recovery) | [saga](animations/saga.md), [idempotency](animations/idempotency.md) |
| 01-core-concepts: [SPOF](curriculum/01-core-concepts/06-spof.md) | [Scenario](curriculum/01-core-concepts/06-spof.md#try-solving-this-first) | [Evidence](curriculum/01-core-concepts/06-spof.md#one-failure-that-stops-the-whole-path) | Redundant application instances still depend on one component or common failure domain. [Applied evidence](curriculum/01-core-concepts/06-spof.md#worked-example-two-applications-one-database) | Static explanation sufficient |
| 02-networking: [IP](curriculum/02-networking/01-ip.md) | [Scenario](curriculum/02-networking/01-ip.md#try-solving-this-first) | [Evidence](curriculum/02-networking/01-ip.md#make-it-concrete) | Services need reachable addresses without exposing every dependency to the internet. [Applied evidence](curriculum/02-networking/01-ip.md#make-it-concrete) | Static explanation sufficient |
| 02-networking: [OSI Model](curriculum/02-networking/02-osi-model.md) | [Scenario](curriculum/02-networking/02-osi-model.md#try-solving-this-first) | [Evidence](curriculum/02-networking/02-osi-model.md#make-it-concrete) | A vague network failure leads to changing unrelated parts of the system. [Applied evidence](curriculum/02-networking/02-osi-model.md#apply-and-improve) | Static explanation sufficient |
| 02-networking: [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md) | [Scenario](curriculum/02-networking/03-tcp-and-udp.md#try-solving-this-first) | [Evidence](curriculum/02-networking/03-tcp-and-udp.md#make-it-concrete) | Applications differ in whether ordered delivery, loss recovery, and timely delivery are most important. [Applied evidence](curriculum/02-networking/03-tcp-and-udp.md#make-it-concrete) | [tcp-udp](animations/tcp-udp.md) |
| 02-networking: [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md) | [Scenario](curriculum/02-networking/04-domain-name-system-dns.md#try-solving-this-first) | [Evidence](curriculum/02-networking/04-domain-name-system-dns.md#make-it-concrete) | Clients need to resolve service names, while cached answers can temporarily outlive a destination change. [Applied evidence](curriculum/02-networking/04-domain-name-system-dns.md#apply-and-improve) | [dns-lookup](animations/dns-lookup.md) |
| 02-networking: [Proxy](curriculum/02-networking/05-proxy.md) | [Scenario](curriculum/02-networking/05-proxy.md#try-solving-this-first) | [Evidence](curriculum/02-networking/05-proxy.md#make-it-concrete) | A system needs a controlled entry or exit point for routing and common request handling. [Applied evidence](curriculum/02-networking/05-proxy.md#make-it-concrete) | Static explanation sufficient |
| 02-networking: [HTTP/HTTPS](curriculum/02-networking/06-httphttps.md) | [Scenario](curriculum/02-networking/06-httphttps.md#try-solving-this-first) | [Evidence](curriculum/02-networking/06-httphttps.md#a-request-and-its-response) | Clients and servers need a request/response contract and protected transport without confusing a network result with a business outcome. [Applied evidence](curriculum/02-networking/06-httphttps.md#how-to-optimize-responsibly) | [tls-mtls](animations/tls-mtls.md) |
| 02-networking: [Checksums](curriculum/02-networking/07-checksums.md) | [Scenario](curriculum/02-networking/07-checksums.md#try-solving-this-first) | [Evidence](curriculum/02-networking/07-checksums.md#detecting-that-data-changed) | A transferred, stored, or assembled file may differ from its expected bytes. [Applied evidence](curriculum/02-networking/07-checksums.md#how-to-improve-efficiency-without-losing-the-guarantee) | Static explanation sufficient |
| 02-networking: [Load Balancing](curriculum/02-networking/08-load-balancing.md) | [Scenario](curriculum/02-networking/08-load-balancing.md#try-solving-this-first) | [Evidence](curriculum/02-networking/08-load-balancing.md#make-it-concrete) | Requests must be distributed across healthy instances without losing state or overwhelming shared dependencies. [Applied evidence](curriculum/02-networking/08-load-balancing.md#apply-and-improve) | [load-balancer](animations/load-balancer.md) |
| 02-networking: [Clustering](curriculum/02-networking/09-clustering.md) | [Scenario](curriculum/02-networking/09-clustering.md#try-solving-this-first) | [Evidence](curriculum/02-networking/09-clustering.md#make-it-concrete) | Several machines must divide work or coordinate state and safely recover unfinished work. [Applied evidence](curriculum/02-networking/09-clustering.md#apply-and-improve) | [load-balancer](animations/load-balancer.md) |
| 03-databases: [Storage](curriculum/03-databases/01-storage.md) | [Scenario](curriculum/03-databases/01-storage.md#try-solving-this-first) | [Evidence](curriculum/03-databases/01-storage.md#make-it-concrete) | Large file bytes and searchable application metadata need suitable interfaces and coordinated lifecycle handling. [Applied evidence](curriculum/03-databases/01-storage.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [Databases and DBMS](curriculum/03-databases/02-databases-and-dbms.md) | [Scenario](curriculum/03-databases/02-databases-and-dbms.md#try-solving-this-first) | [Evidence](curriculum/03-databases/02-databases-and-dbms.md#make-it-concrete) | An application needs correct, persistent, concurrent access to related facts rather than ad hoc storage and unrestricted scans. [Applied evidence](curriculum/03-databases/02-databases-and-dbms.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [SQL databases](curriculum/03-databases/03-sql-databases.md) | [Scenario](curriculum/03-databases/03-sql-databases.md#try-solving-this-first) | [Evidence](curriculum/03-databases/03-sql-databases.md#make-it-concrete) | Related orders, customers, and items need explicit identities, integrity constraints, and coordinated changes. [Applied evidence](curriculum/03-databases/03-sql-databases.md#make-it-concrete) | Static explanation sufficient |
| 03-databases: [NoSQL databases](curriculum/03-databases/04-nosql-databases.md) | [Scenario](curriculum/03-databases/04-nosql-databases.md#try-solving-this-first) | [Evidence](curriculum/03-databases/04-nosql-databases.md#make-it-concrete) | Different access patterns may fit document, key-value, graph, or other models better than one assumed universal schema. [Applied evidence](curriculum/03-databases/04-nosql-databases.md#make-it-concrete) | Static explanation sufficient |
| 03-databases: [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md) | [Scenario](curriculum/03-databases/05-sql-vs-nosql-databases.md#try-solving-this-first) | [Evidence](curriculum/03-databases/05-sql-vs-nosql-databases.md#make-it-concrete) | Choosing by database category alone ignores required operations and operational cost. [Applied evidence](curriculum/03-databases/05-sql-vs-nosql-databases.md#make-it-concrete) | Static explanation sufficient |
| 03-databases: [Indexes](curriculum/03-databases/06-indexes.md) | [Scenario](curriculum/03-databases/06-indexes.md#try-solving-this-first) | [Evidence](curriculum/03-databases/06-indexes.md#make-it-concrete) | Finding a small relevant subset should not require scanning every unrelated database row. [Applied evidence](curriculum/03-databases/06-indexes.md#make-it-concrete) | [index-lookup](animations/index-lookup.md) |
| 03-databases: [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md) | [Scenario](curriculum/03-databases/07-normalization-and-denormalization.md#try-solving-this-first) | [Evidence](curriculum/03-databases/07-normalization-and-denormalization.md#clarify-the-key-definitions) | Duplicated values can become inconsistent, while meaningful historical snapshots must not be overwritten as if they were current facts. [Applied evidence](curriculum/03-databases/07-normalization-and-denormalization.md#apply-and-improve) | [normalization](animations/normalization.md) |
| 03-databases: [Transactions](curriculum/03-databases/08-transactions.md) | [Scenario](curriculum/03-databases/08-transactions.md#try-solving-this-first) | [Evidence](curriculum/03-databases/08-transactions.md#make-it-concrete) | Concurrent buyers may both believe they reserved the same final unit. [Applied evidence](curriculum/03-databases/08-transactions.md#make-it-concrete) | [atomic-stock](animations/atomic-stock.md) |
| 03-databases: [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md) | [Scenario](curriculum/03-databases/09-acid-and-base-consistency-models.md#try-solving-this-first) | [Evidence](curriculum/03-databases/09-acid-and-base-consistency-models.md#make-it-concrete) | The word consistency can incorrectly conflate local invariant preservation with visibility across replicas. [Applied evidence](curriculum/03-databases/09-acid-and-base-consistency-models.md#make-it-concrete) | [atomic-stock](animations/atomic-stock.md) |
| 03-databases: [Database Replication](curriculum/03-databases/10-database-replication.md) | [Scenario](curriculum/03-databases/10-database-replication.md#try-solving-this-first) | [Evidence](curriculum/03-databases/10-database-replication.md#make-it-concrete) | Copies support read capacity or recovery but can lag, and copying the same mistake does not preserve historical recovery points. [Applied evidence](curriculum/03-databases/10-database-replication.md#make-it-concrete) | [replication](animations/replication.md) |
| 03-databases: [Sharding](curriculum/03-databases/11-sharding.md) | [Scenario](curriculum/03-databases/11-sharding.md#try-solving-this-first) | [Evidence](curriculum/03-databases/11-sharding.md#make-it-concrete) | A growing dataset or workload needs distribution without confusing copied data with divided ownership. [Applied evidence](curriculum/03-databases/11-sharding.md#apply-and-improve) | [sharding](animations/sharding.md) |
| 03-databases: [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md) | [Scenario](curriculum/03-databases/12-consistent-hashing.md#try-solving-this-first) | [Evidence](curriculum/03-databases/12-consistent-hashing.md#make-it-concrete) | Naive modulo-based key placement can move many keys when the number of nodes changes. [Applied evidence](curriculum/03-databases/12-consistent-hashing.md#apply-and-improve) | [consistent-hash](animations/consistent-hash.md) |
| 03-databases: [Database Federation](curriculum/03-databases/13-database-federation.md) | [Scenario](curriculum/03-databases/13-database-federation.md#try-solving-this-first) | [Evidence](curriculum/03-databases/13-database-federation.md#make-it-concrete) | Business domains may need separate ownership or scaling without mistaking functional boundaries for key ranges. [Applied evidence](curriculum/03-databases/13-database-federation.md#make-it-concrete) | [sharding](animations/sharding.md) |
| 03-databases: [Bloom Filters](curriculum/03-databases/14-bloom-filters.md) | [Scenario](curriculum/03-databases/14-bloom-filters.md#try-solving-this-first) | [Evidence](curriculum/03-databases/14-bloom-filters.md#a-small-filter-before-an-expensive-lookup) | Many absent-key queries waste expensive authoritative lookups. [Applied evidence](curriculum/03-databases/14-bloom-filters.md#how-to-tune-it) | [bloom-filter](animations/bloom-filter.md) |
| 04-distributed-data: [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md) | [Scenario](curriculum/04-distributed-data/01-cap-theorem.md#try-solving-this-first) | [Evidence](curriculum/04-distributed-data/01-cap-theorem.md#make-it-concrete) | A network partition prevents replicas coordinating while a client still expects a valid result. [Applied evidence](curriculum/04-distributed-data/01-cap-theorem.md#make-it-concrete) | [cap-partition](animations/cap-partition.md) |
| 04-distributed-data: [PACELC Theorem](curriculum/04-distributed-data/02-pacelc-theorem.md) | [Scenario](curriculum/04-distributed-data/02-pacelc-theorem.md#try-solving-this-first) | [Evidence](curriculum/04-distributed-data/02-pacelc-theorem.md#make-it-concrete) | CAP alone does not describe the latency-versus-consistency decision during normal network operation. [Applied evidence](curriculum/04-distributed-data/02-pacelc-theorem.md#make-it-concrete) | [pacelc](animations/pacelc.md) |
| 04-distributed-data: [Distributed Transactions](curriculum/04-distributed-data/03-distributed-transactions.md) | [Scenario](curriculum/04-distributed-data/03-distributed-transactions.md#try-solving-this-first) | [Evidence](curriculum/04-distributed-data/03-distributed-transactions.md#make-it-concrete) | An order and an external payment can reach different committed states after a partial failure. [Applied evidence](curriculum/04-distributed-data/03-distributed-transactions.md#make-it-concrete) | [saga](animations/saga.md) |
| 05-caching: [Caching](curriculum/05-caching/01-caching.md) | [Scenario](curriculum/05-caching/01-caching.md#try-solving-this-first) | [Evidence](curriculum/05-caching/01-caching.md#make-it-concrete) | Repeated product reads unnecessarily hit slower authoritative storage, but cached copies can become stale. [Applied evidence](curriculum/05-caching/01-caching.md#make-it-concrete) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Caching Strategies](curriculum/05-caching/02-caching-strategies.md) | [Scenario](curriculum/05-caching/02-caching-strategies.md#try-solving-this-first) | [Evidence](curriculum/05-caching/02-caching-strategies.md#decide-who-reads-and-who-updates-the-copy) | The design must assign ownership of cache loading and writes without silently losing freshness or durability guarantees. [Applied evidence](curriculum/05-caching/02-caching-strategies.md#work-through-a-price-update) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Cache Eviction Policies](curriculum/05-caching/03-cache-eviction-policies.md) | [Scenario](curriculum/05-caching/03-cache-eviction-policies.md#try-solving-this-first) | [Evidence](curriculum/05-caching/03-cache-eviction-policies.md#what-leaves-when-the-cache-is-full) | When the working set exceeds cache capacity, the system must choose which reusable values to remove. [Applied evidence](curriculum/05-caching/03-cache-eviction-policies.md#walk-through-a-small-cache) | [cache-eviction](animations/cache-eviction.md) |
| 05-caching: [Distributed Caching](curriculum/05-caching/04-distributed-caching.md) | [Scenario](curriculum/05-caching/04-distributed-caching.md#try-solving-this-first) | [Evidence](curriculum/05-caching/04-distributed-caching.md#sharing-a-fast-copy-across-servers) | Many application instances duplicate expensive reads and can stampede the origin when a shared hot key expires. [Applied evidence](curriculum/05-caching/04-distributed-caching.md#work-through-a-hot-key-failure) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Content Delivery Network (CDN)](curriculum/05-caching/05-content-delivery-network-cdn.md) | [Scenario](curriculum/05-caching/05-content-delivery-network-cdn.md#try-solving-this-first) | [Evidence](curriculum/05-caching/05-content-delivery-network-cdn.md#make-it-concrete) | Serving every static asset from one origin creates repeated long-distance transfers and origin load. [Applied evidence](curriculum/05-caching/05-content-delivery-network-cdn.md#make-it-concrete) | [cdn-edge](animations/cdn-edge.md) |
| 06-api-fundamentals: [APIs](curriculum/06-api-fundamentals/01-apis.md) | [Scenario](curriculum/06-api-fundamentals/01-apis.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/01-apis.md#a-contract-between-two-parts-of-a-system) | Independent clients need stable, unambiguous behavior without depending on internal implementation details. [Applied evidence](curriculum/06-api-fundamentals/01-apis.md#work-through-an-order-request) | Static explanation sufficient |
| 06-api-fundamentals: [REST, GraphQL, gRPC](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) | [Scenario](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md#make-it-concrete) | The interface must fit the clients, data shapes, and communication pattern without hiding inefficient backend work. [Applied evidence](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md#make-it-concrete) | Static explanation sufficient |
| 06-api-fundamentals: [API Gateway](curriculum/06-api-fundamentals/03-api-gateway.md) | [Scenario](curriculum/06-api-fundamentals/03-api-gateway.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/03-api-gateway.md#make-it-concrete) | Clients otherwise must discover and coordinate multiple backend services and shared entry-point concerns themselves. [Applied evidence](curriculum/06-api-fundamentals/03-api-gateway.md#make-it-concrete) | [api-gateway](animations/api-gateway.md) |
| 06-api-fundamentals: [Idempotency](curriculum/06-api-fundamentals/04-idempotency.md) | [Scenario](curriculum/06-api-fundamentals/04-idempotency.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/04-idempotency.md#make-it-concrete) | A retried payment after a lost response must not create an extra charge or skip a charge that never happened. [Applied evidence](curriculum/06-api-fundamentals/04-idempotency.md#make-it-concrete) | [idempotency](animations/idempotency.md) |
| 06-api-fundamentals: [Rate Limiting](curriculum/06-api-fundamentals/05-rate-limiting.md) | [Scenario](curriculum/06-api-fundamentals/05-rate-limiting.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/05-rate-limiting.md#make-it-concrete) | One customer or an aggregate traffic burst can overload shared search capacity or unfairly consume it. [Applied evidence](curriculum/06-api-fundamentals/05-rate-limiting.md#make-it-concrete) | [token-bucket](animations/token-bucket.md) |
| 06-api-fundamentals: [Long polling, WebSockets, Server-Sent Events (SSE)](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) | [Scenario](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md#make-it-concrete) | Clients need timely updates, sometimes bidirectional, without losing all progress when a connection drops. [Applied evidence](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md#make-it-concrete) | [realtime-protocols](animations/realtime-protocols.md) |
| 06-api-fundamentals: [Webhooks](curriculum/06-api-fundamentals/07-webhooks.md) | [Scenario](curriculum/06-api-fundamentals/07-webhooks.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/07-webhooks.md#let-another-system-call-you-when-something-happens) | A service needs provider events without constant polling, while tolerating duplicate, delayed, or reordered delivery. [Applied evidence](curriculum/06-api-fundamentals/07-webhooks.md#work-through-a-duplicate-delivery) | [idempotency](animations/idempotency.md) |
| 06-api-fundamentals: [API Design](curriculum/06-api-fundamentals/08-api-design.md) | [Scenario](curriculum/06-api-fundamentals/08-api-design.md#try-solving-this-first) | [Evidence](curriculum/06-api-fundamentals/08-api-design.md#make-the-contract-predictable) | Unbounded lists, ambiguous results, incompatible changes, and unsafe retries prevent clients completing tasks predictably. [Applied evidence](curriculum/06-api-fundamentals/08-api-design.md#work-through-a-list-endpoint) | Static explanation sufficient |
| 07-asynchronous-communication: [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md) | [Scenario](curriculum/07-asynchronous-communication/01-message-brokers.md#try-solving-this-first) | [Evidence](curriculum/07-asynchronous-communication/01-message-brokers.md#make-it-concrete) | Producers and consumers should exchange work/events without requiring each receiver to be synchronously active or directly addressed. [Applied evidence](curriculum/07-asynchronous-communication/01-message-brokers.md#make-it-concrete) | [work-queue](animations/work-queue.md) |
| 07-asynchronous-communication: [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md) | [Scenario](curriculum/07-asynchronous-communication/02-message-queues.md#try-solving-this-first) | [Evidence](curriculum/07-asynchronous-communication/02-message-queues.md#make-it-concrete) | Bursts of thumbnail work should not hold upload requests open or overwhelm downstream processing; redeliveries must be safe. [Applied evidence](curriculum/07-asynchronous-communication/02-message-queues.md#make-it-concrete) | [work-queue](animations/work-queue.md) |
| 07-asynchronous-communication: [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md) | [Scenario](curriculum/07-asynchronous-communication/03-publish-subscribe.md#try-solving-this-first) | [Evidence](curriculum/07-asynchronous-communication/03-publish-subscribe.md#make-it-concrete) | Several independent business reactions must each receive an event without being treated as competing workers for one job. [Applied evidence](curriculum/07-asynchronous-communication/03-publish-subscribe.md#make-it-concrete) | [pub-sub](animations/pub-sub.md) |
| 07-asynchronous-communication: [Change Data Capture (CDC)](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md) | [Scenario](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md#try-solving-this-first) | [Evidence](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md#turn-database-changes-into-downstream-updates) | A derived search index needs committed database changes without repeatedly scanning the entire source or independently double-writing each request. [Applied evidence](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md#follow-one-changed-price) | [cdc](animations/cdc.md) |
| 08-architectural-patterns: [N-tier architecture](curriculum/08-architectural-patterns/01-n-tier-architecture.md) | [Scenario](curriculum/08-architectural-patterns/01-n-tier-architecture.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/01-n-tier-architecture.md#make-it-concrete) | Separates presentation, business rules, and persistence so each responsibility has an explicit deployment and scaling boundary. [Applied evidence](curriculum/08-architectural-patterns/01-n-tier-architecture.md#make-it-concrete) | Static explanation sufficient |
| 08-architectural-patterns: [Monoliths and Microservices](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md) | [Scenario](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md#make-it-concrete) | Defines capability and data-ownership boundaries without treating distributed deployment as an automatic performance improvement. [Applied evidence](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md#make-it-concrete) | Static explanation sufficient |
| 08-architectural-patterns: [Event-Driven Architecture (EDA)](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md) | [Scenario](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md#make-it-concrete) | Decouples an initiating business action from downstream reactions that can complete later. [Applied evidence](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md#make-it-concrete) | [pub-sub](animations/pub-sub.md) |
| 08-architectural-patterns: [Event Sourcing](curriculum/08-architectural-patterns/04-event-sourcing.md) | [Scenario](curriculum/08-architectural-patterns/04-event-sourcing.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/04-event-sourcing.md#make-it-concrete) | Preserves authoritative business history so current state and derived views can be reconstructed. [Applied evidence](curriculum/08-architectural-patterns/04-event-sourcing.md#make-it-concrete) | [event-sourcing](animations/event-sourcing.md) |
| 08-architectural-patterns: [Command and Query Responsibility Segregation (CQRS)](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md) | [Scenario](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md#make-it-concrete) | Allows write rules and read queries to use models shaped for their different responsibilities. [Applied evidence](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md#make-it-concrete) | [cqrs](animations/cqrs.md) |
| 08-architectural-patterns: [Enterprise Service Bus (ESB)](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md) | [Scenario](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md#make-it-concrete) | Integrates systems with incompatible message formats and routing requirements. [Applied evidence](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md#make-it-concrete) | Static explanation sufficient |
| 08-architectural-patterns: [Virtual Machines (VMs) and Containers](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md) | [Scenario](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md#make-it-concrete) | Chooses packaging, resource control, and operating-system isolation boundaries for workloads. [Applied evidence](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md#make-it-concrete) | Static explanation sufficient |
| 08-architectural-patterns: [Serverless Architecture](curriculum/08-architectural-patterns/08-serverless-architecture.md) | [Scenario](curriculum/08-architectural-patterns/08-serverless-architecture.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/08-serverless-architecture.md#let-a-platform-manage-more-of-the-runtime) | Offloads parts of runtime provisioning and operation for suitable request- or event-triggered work. [Applied evidence](curriculum/08-architectural-patterns/08-serverless-architecture.md#work-through-thumbnail-generation) | Static explanation sufficient |
| 08-architectural-patterns: [Peer-to-Peer (P2P) Architecture](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md) | [Scenario](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md#try-solving-this-first) | [Evidence](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md#participants-can-provide-as-well-as-consume) | Distributes content-serving work among participants instead of making one origin serve every byte. [Applied evidence](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md#work-through-file-distribution) | [p2p-pieces](animations/p2p-pieces.md) |
| 09-reliability-and-microservices: [Service Discovery](curriculum/09-reliability-and-microservices/01-service-discovery.md) | [Scenario](curriculum/09-reliability-and-microservices/01-service-discovery.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/01-service-discovery.md#make-it-concrete) | Finds service instance addresses that change during deployment or failure. [Applied evidence](curriculum/09-reliability-and-microservices/01-service-discovery.md#make-it-concrete) | [discovery-heartbeat](animations/discovery-heartbeat.md) |
| 09-reliability-and-microservices: [HeartBeats](curriculum/09-reliability-and-microservices/02-heartbeats.md) | [Scenario](curriculum/09-reliability-and-microservices/02-heartbeats.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/02-heartbeats.md#a-signal-that-a-participant-was-recently-reachable) | Provides recent reachability evidence to support failure suspicion, not proof of end-to-end health. [Applied evidence](curriculum/09-reliability-and-microservices/02-heartbeats.md#work-through-a-timeout) | [discovery-heartbeat](animations/discovery-heartbeat.md) |
| 09-reliability-and-microservices: [Circuit breaker](curriculum/09-reliability-and-microservices/03-circuit-breaker.md) | [Scenario](curriculum/09-reliability-and-microservices/03-circuit-breaker.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/03-circuit-breaker.md#make-it-concrete) | Stops repeated calls to a failing dependency from consuming resources and spreading failure. [Applied evidence](curriculum/09-reliability-and-microservices/03-circuit-breaker.md#make-it-concrete) | [circuit-breaker](animations/circuit-breaker.md) |
| 09-reliability-and-microservices: [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md) | [Scenario](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#make-it-concrete) | Connects a user-facing service promise to a measurable target and observed performance. [Applied evidence](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#make-it-concrete) | Static explanation sufficient |
| 09-reliability-and-microservices: [Disaster recovery](curriculum/09-reliability-and-microservices/05-disaster-recovery.md) | [Scenario](curriculum/09-reliability-and-microservices/05-disaster-recovery.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/05-disaster-recovery.md#make-it-concrete) | Defines tolerable data loss and time to recover usable service after a serious disruption. [Applied evidence](curriculum/09-reliability-and-microservices/05-disaster-recovery.md#make-it-concrete) | [recovery-objectives](animations/recovery-objectives.md) |
| 09-reliability-and-microservices: [Consensus Algorithms](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md) | [Scenario](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md#agreeing-on-decisions-despite-some-failures) | Maintains an agreed ordered decision history among replicas under a specified failure model. [Applied evidence](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md#follow-a-simple-replicated-log-write) | [raft-majority](animations/raft-majority.md) |
| 09-reliability-and-microservices: [Distributed Locking](curriculum/09-reliability-and-microservices/07-distributed-locking.md) | [Scenario](curriculum/09-reliability-and-microservices/07-distributed-locking.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/07-distributed-locking.md#coordinate-work-across-processes-carefully) | Coordinates exclusive work across processes while accounting for expiry and stale owners. [Applied evidence](curriculum/09-reliability-and-microservices/07-distributed-locking.md#work-through-a-stale-owner) | [fencing-token](animations/fencing-token.md) |
| 09-reliability-and-microservices: [Gossip Protocol](curriculum/09-reliability-and-microservices/08-gossip-protocol.md) | [Scenario](curriculum/09-reliability-and-microservices/08-gossip-protocol.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/08-gossip-protocol.md#spread-information-through-repeated-peer-exchanges) | Spreads membership or health observations without every update requiring one sender to contact all nodes directly. [Applied evidence](curriculum/09-reliability-and-microservices/08-gossip-protocol.md#follow-an-update) | [gossip-spread](animations/gossip-spread.md) |
| 09-reliability-and-microservices: [Distributed Tracing](curriculum/09-reliability-and-microservices/09-distributed-tracing.md) | [Scenario](curriculum/09-reliability-and-microservices/09-distributed-tracing.md#try-solving-this-first) | [Evidence](curriculum/09-reliability-and-microservices/09-distributed-tracing.md#follow-one-request-across-several-services) | Connects request work across service boundaries to locate slow or failing dependencies. [Applied evidence](curriculum/09-reliability-and-microservices/09-distributed-tracing.md#work-through-a-slow-order-page) | [request-latency](animations/request-latency.md) |
| 10-security-and-location: [SSL, TLS, mTLS](curriculum/10-security-and-location/01-ssl-tls-mtls.md) | [Scenario](curriculum/10-security-and-location/01-ssl-tls-mtls.md#try-solving-this-first) | [Evidence](curriculum/10-security-and-location/01-ssl-tls-mtls.md#make-it-concrete) | Protects connection data and establishes endpoint identity while keeping authorization separate. [Applied evidence](curriculum/10-security-and-location/01-ssl-tls-mtls.md#make-it-concrete) | [tls-mtls](animations/tls-mtls.md) |
| 10-security-and-location: [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md) | [Scenario](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#try-solving-this-first) | [Evidence](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#make-it-concrete) | Separates delegated access to protected resources from a client receiving authenticated login identity. [Applied evidence](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#make-it-concrete) | [oauth-oidc](animations/oauth-oidc.md) |
| 10-security-and-location: [Single Sign-On (SSO)](curriculum/10-security-and-location/03-single-sign-on-sso.md) | [Scenario](curriculum/10-security-and-location/03-single-sign-on-sso.md#try-solving-this-first) | [Evidence](curriculum/10-security-and-location/03-single-sign-on-sso.md#make-it-concrete) | Lets multiple applications share an identity-provider sign-in while retaining application-specific permissions and session policies. [Applied evidence](curriculum/10-security-and-location/03-single-sign-on-sso.md#make-it-concrete) | [single-sign-on](animations/single-sign-on.md) |
| 10-security-and-location: [Geohashing and Quadtrees](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md) | [Scenario](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md#try-solving-this-first) | [Evidence](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md#make-it-concrete) | Narrows spatial search candidates so nearby-driver queries avoid a distance calculation against every driver. [Applied evidence](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md#make-it-concrete) | [nearby-search](animations/nearby-search.md) |

## What is system design?

- **Opening problem:** A payment times out. Should another click create another charge?
- **Fundamental:** “Specify correctness, response time, and failure behavior before choosing components.”
- **Problem solved:** Choosing components before knowing the behavior and failure guarantees the system must provide.
- **Applied evidence:** “If payment times out, recover the same operation safely; faster servers alone cannot prevent duplicate charges.”
- **Apply it:** Trace order → payment → restaurant. → Specify charging correctness, response time, and failure behavior. → Choose components for those requirements and handle an uncertain payment without duplicating a charge.
- **Decision or tradeoff:** Prioritize the required correctness behavior before adding faster servers.
- **Animation decision:** Requirements-to-component mapping is clear in the short scenario; a static request flow is sufficient.

## Scalability

- **Opening problem:** Demand doubles; the database is saturated. Where should capacity grow?
- **Fundamental:** “Scale up adds machine resources; scale out adds machines.”
- **Problem solved:** A rising request rate exceeds the capacity of a particular stage.
- **Applied evidence:** “Measure bottlenecks before expanding capacity.”
- **Apply it:** Measure CPU, database work, and waiting time. → Locate the actual saturated stage. → Scale that stage vertically or horizontally and reassess the shared database.
- **Decision or tradeoff:** Extra application instances cannot solve an overloaded shared database; vertical and horizontal capacity have different limits.
- **Animation decision:** The vertical-versus-horizontal distinction and bottleneck warning are explicit; a static before/after capacity sketch suffices.

## Availability

- **Opening problem:** One checkout server fails during a sale. What must happen before its spare can safely serve the waiting customers?
- **Fundamental:** “Two checkout servers help only if traffic switches to a usable survivor.”
- **Problem solved:** Users lose access when a server or shared dependency fails.
- **Applied evidence:** “Add readiness checks, replacement capacity, and tested failover where they remove a failure point.”
- **Apply it:** Trace the whole request and identify shared dependencies. → Provide health checks, replacement capacity, and tested failover where they remove a real failure point. → Measure successful requests and their latency, and test what can remain available during dependency failure.
- **Decision or tradeoff:** Redundancy costs capacity and only protects the failure domains it actually separates; degraded browsing is different from successful checkout.
- **Animation decision:** Failover has a temporal sequence: failure, detection, routing change, and surviving-instance load. Playback prevents equating two boxes with instant availability.

## Latency vs Throughput vs Bandwidth

- **Opening problem:** During a sale, checkout responds in 200 ms on average, yet some users wait over a second. An illustrative trace shows 30 ms of network travel, 70 ms of application work, and a 100 ms query. More users arrive each second. Would you buy bandwidth, add servers, change the query, or limit concurrency? Which measurement would tell you whether the change helped the customer's experience?
- **Fundamental:** “Concurrency is how many operations are in progress. It is not the same as completed operations per second.”
- **Problem solved:** Optimizing the wrong performance quantity or interpreting averages and network capacity as interchangeable.
- **Applied evidence:** “Begin with a trace or timing breakdown, form one hypothesis, and compare before and after at a similar workload.”
- **Apply it:** State the operation, measurement boundary, and units. → Measure the critical path and identify the dominant stage. → Compare an optimization under equivalent load using latency percentiles, throughput, queueing, and errors.
- **Decision or tradeoff:** More concurrency can increase queueing rather than completions; larger bandwidth may not reduce query-dominated response time.
- **Animation decision:** Show arrivals, queue length, active requests, completions, and transfer capacity over time to separate latency, throughput, concurrency, and bandwidth.

## Reliability

- **Opening problem:** A customer places an order. The payment provider charges successfully, but the order worker crashes before recording the result or replying. The customer sees an error and tries again. Which facts must survive the crash? How can the system decide whether to retry, resume, or refund without inventing a second purchase? What should the customer see while the outcome is still uncertain?
- **Fundamental:** “A reliable service keeps doing its intended job correctly over time, including when expected problems happen.”
- **Problem solved:** A partially completed operation can leave users with duplicate charges, lost state, or a permanently unresolved order.
- **Applied evidence:** “A more deliberate flow records a stable operation identifier, makes payment retries reuse it, and resumes the order update from durable state.”
- **Apply it:** Define the invariant and durable acceptance boundary. → Reuse stable identifiers for retries and resume from durable state. → Reconcile unresolved orders/payments and inject failures after each durable step.
- **Decision or tradeoff:** Retries, replicas, and recovery mechanisms add complexity; use them to protect a defined invariant rather than treating successful HTTP responses as proof.
- **Animation decision:** The crash-after-payment/lost-response/retry/reconciliation sequence is stateful; showing state transitions makes the unknown outcome understandable.

## SPOF

- **Opening problem:** A shop deploys two application servers and promises to survive a machine failure. Both servers use one load balancer, one database, and the same configuration service. During a sale, the shared database stops responding. Which requests can still work? Where would another copy actually help? Who would select the replacement, reconnect clients, and prevent two machines from accepting conflicting writes?
- **Fundamental:** “a component whose failure can stop the service you care about.”
- **Problem solved:** Redundant application instances still depend on one component or common failure domain.
- **Applied evidence:** “A failover plan needs data replication, a promotion decision, a stable address or discovery change, and client reconnection.”
- **Apply it:** Trace each dependency in the real request path. → Provide a tested replacement, promotion decision, client reconnection, and a rule for which database may accept writes. → Fail dependencies and measure detection, switchover, rejected work, and data loss.
- **Decision or tradeoff:** A fallback can suffice for optional recommendations, but not for a required payment confirmation; automatic promotion must avoid conflicting writers.
- **Animation decision:** The existing dependency diagram and explicit failover walkthrough establish the concept; the Availability animation can cover the shared temporal behavior.

## IP

- **Opening problem:** Your shop must accept internet traffic, but its database should not. Which machines need public addresses, and how will the others communicate?
- **Fundamental:** “Private addressing is not access control: restrict permitted connections.”
- **Problem solved:** Services need reachable addresses without exposing every dependency to the internet.
- **Applied evidence:** “Check the destination address, route, firewall, and listening port when debugging.”
- **Apply it:** Determine which component must be internet-reachable. → Check destination address, route, firewall, and listening port when a connection fails. → Use DNS or discovery for changing instance addresses and restrict permitted connections.
- **Decision or tradeoff:** Private addressing is not access control; a correct address and a permitted/reachable connection are different requirements.
- **Animation decision:** A labeled public/private network diagram adequately explains placement and NAT; the lesson does not require a packet-timing simulation.

## OSI Model

- **Opening problem:** Your browser cannot load the shop. Would you inspect a cable, a port, a certificate, or the database first—and what evidence changes that choice?
- **Fundamental:** “The OSI model gives names to these different responsibilities; real implementations do not always fit perfectly into seven separate boxes.”
- **Problem solved:** A vague network failure leads to changing unrelated parts of the system.
- **Applied evidence:** “If a TCP connection cannot open, inspect ports, listeners, and filtering.”
- **Apply it:** Separate reaching the IP, opening transport, securing the connection, and sending the application request. → Inspect the layer-specific evidence: routing, listeners/filtering, certificate verification, or HTTP errors. → Optimize the stage actually measured rather than treating all delay as one network problem.
- **Decision or tradeoff:** The model is a troubleshooting vocabulary, not a requirement that every implementation contain seven isolated boxes.
- **Animation decision:** A static layer-to-symptom mapping is clearer than decorative packet movement for this troubleshooting purpose.

## TCP and UDP

- **Opening problem:** A voice call loses a sound packet; a file download loses some bytes. Should both wait for recovery?
- **Fundamental:** “TCP supplies an ordered byte stream with loss recovery; a missing range can delay later bytes.”
- **Problem solved:** Applications differ in whether ordered delivery, loss recovery, and timely delivery are most important.
- **Applied evidence:** “Choose using measured loss, delay, and required ordering.”
- **Apply it:** Specify acceptable loss, delay, and ordering. → Measure those properties and reuse connections where appropriate. → For UDP, explicitly design congestion handling, loss tolerance, and message sizing; keep business confirmation at the application level.
- **Decision or tradeoff:** UDP is not automatically faster for the application, and TCP delivery does not establish that a payment committed.
- **Animation decision:** Packet loss, reordering, retransmission, and a live-playout deadline are temporal distinctions that static protocol labels can obscure.

## Domain Name System (DNS)

- **Opening problem:** You move shop.example from server A to B. Some users still reach A. What information could they be using, and when should it change?
- **Fundamental:** “DNS finds an address; it does not carry the web page.”
- **Problem solved:** Clients need to resolve service names, while cached answers can temporarily outlive a destination change.
- **Applied evidence:** “For a planned move, lower the TTL ahead of time and allow the previous TTL to elapse before relying on shorter caching.”
- **Apply it:** Trace browser, resolver, cached/authoritative answer, and subsequent server connection. → Lower TTL ahead of a planned move and allow the old TTL to expire before relying on shorter caching. → Keep the old destination available during transition where possible and inspect actual answers/TTLs when debugging.
- **Decision or tradeoff:** Shorter TTLs can reduce cache persistence but increase lookup traffic and do not move existing open connections instantly.
- **Animation decision:** Two clients retaining different cached answers through a TTL countdown makes propagation and the separation from connection lifetime concrete.

## Proxy

- **Opening problem:** A school controls students' outgoing browsing; a shop controls traffic entering its servers. What should each intermediary represent, inspect, and forward?
- **Fundamental:** “A forward proxy represents clients making outgoing requests; a reverse proxy represents servers receiving requests.”
- **Problem solved:** A system needs a controlled entry or exit point for routing and common request handling.
- **Applied evidence:** “Measure its queueing, connections, and latency before adding app servers.”
- **Apply it:** Identify whether the intermediary represents clients or servers. → Measure proxy queueing, connection counts, and request duration. → Set size/time limits, reuse connections where appropriate, and trust forwarded identity information only through a controlled chain.
- **Decision or tradeoff:** An intermediary centralizes useful behavior but can become a bottleneck or failure point; business authorization remains with the service.
- **Animation decision:** The forward/reverse distinction is directional and well served by a static diagram labeling whose requests each proxy represents.

## HTTP/HTTPS

- **Opening problem:** A mobile app's first product request is slow, while later requests are faster. The order endpoint uses HTTPS, yet one customer can still request someone else's order by changing an identifier. Then a checkout request times out after the server may have created the order. Which parts of these problems concern connection setup, protected transport, authorization, and business-level retry behavior?
- **Fundamental:** “A request includes a method, path, headers, and sometimes a body.”
- **Problem solved:** Clients and servers need a request/response contract and protected transport without confusing a network result with a business outcome.
- **Applied evidence:** “Reuse connections where supported instead of paying setup costs for every call.”
- **Apply it:** Separate resolution, connection setup, TLS, response start, and body transfer. → Reuse connections, reduce unnecessary redirects/round trips, and safely cache or compress suitable content. → Compare connection and body timing, errors, and percentiles under equivalent load while preserving authorization and retry safety.
- **Decision or tradeoff:** Batching reduces round trips but may enlarge payloads; HTTPS protects transport, not database storage or per-order ownership.
- **Animation decision:** Showing the first-connection lifecycle versus connection reuse and a lost response reveals timing and business-outcome distinctions.

## Checksums

- **Opening problem:** A user uploads a large archive in ten chunks. The network drops during one chunk, two pieces arrive in the wrong order, and the final assembled file will later be restored from backup. What would let you detect which bytes differ, retry only damaged work, and verify the completed object? If a supplied verification value is also replaced, what confidence should it give you?
- **Fundamental:** “A checksum is a value calculated from data. The receiver can calculate it again and compare the result with the expected value.”
- **Problem solved:** A transferred, stored, or assembled file may differ from its expected bytes.
- **Applied evidence:** “Calculate a digest incrementally while streaming bytes rather than loading the whole file into memory.”
- **Apply it:** Choose integrity checks for accidental corruption versus deliberate replacement. → Verify chunks and the assembled file using trustworthy expected metadata. → Calculate incrementally while streaming, tune chunk sizes, and test byte changes, missing/reordered chunks, and untrusted expected values.
- **Decision or tradeoff:** Verification detects disagreement but does not repair data or establish authenticity when the expected digest is also untrusted.
- **Animation decision:** A static chunk/digest/assembly example exposes the relevant distinction without requiring temporal animation.

## Load Balancing

- **Opening problem:** App A accepted your login, but the next request reaches App B. How can B identify the same session? What if A dies mid-purchase?
- **Fundamental:** “Adding B spreads application work but does not double database capacity.”
- **Problem solved:** Requests must be distributed across healthy instances without losing state or overwhelming shared dependencies.
- **Applied evidence:** “When removing an instance, stop new requests and allow active work to finish.”
- **Apply it:** Choose a routing policy for actual request/connection behavior and use readiness checks. → Stop new traffic and drain active work when removing instances, with spare capacity for failure. → Choose shared or suitable stateless session handling and measure per-instance latency, errors, and distribution.
- **Decision or tradeoff:** Sticky routing can reduce session movement but does not make instance memory durable; more app capacity may only shift the bottleneck.
- **Animation decision:** Instance failure, readiness changes, active-request draining, and a session moving to another instance are state transitions that benefit from playback.

## Clustering

- **Opening problem:** Three workers resize photos. One crashes after writing an image but before reporting success. Who should resume the job, and what could go wrong?
- **Fundamental:** “Putting machines behind a load balancer does not itself define coordination, replication, or recovery.”
- **Problem solved:** Several machines must divide work or coordinate state and safely recover unfinished work.
- **Applied evidence:** “State how work is assigned, how failed members are detected, and whether unfinished work can be reassigned safely.”
- **Apply it:** Specify assignment, failure detection, and recovery of unfinished tasks. → Make retried work safe and leave capacity for failures. → Measure completed work, coordination overhead, shared bottlenecks, and recovery time before adding nodes.
- **Decision or tradeoff:** More nodes can improve throughput but add communication and coordination; independent jobs and shared-data decisions have different requirements.
- **Animation decision:** The distinction between independent workers and coordinated data is explicit; queue redelivery/failover animations elsewhere can illustrate the shared temporal mechanics.

## Storage

- **Opening problem:** A photo upload stores the image, then crashes before recording its database row. Where should the bytes and metadata live, and how could you recover?
- **Fundamental:** “Block storage exposes blocks for an operating system or database to manage. File storage exposes files and directories.”
- **Problem solved:** Large file bytes and searchable application metadata need suitable interfaces and coordinated lifecycle handling.
- **Applied evidence:** “If writing the object succeeds but recording its database row fails, cleanup or reconciliation must handle the orphaned object.”
- **Apply it:** Specify object size, read/write patterns, durability, and retrieval delay. → Choose block, file, or object interfaces for those operations and use authorized direct/CDN delivery when appropriate. → Define visibility, cleanup/reconciliation, and backups for failures between object and metadata writes.
- **Decision or tradeoff:** Direct object delivery can reduce application load; separate stores add partial-write and recovery coordination.
- **Animation decision:** A static byte-storage versus metadata flow and explicit partial-failure walkthrough cover the concept without additional animation.

## Databases and DBMS

- **Opening problem:** A shop must find orders by customer, update statuses, and reject impossible relationships. Which guarantees should the data manager enforce, and which workload should guide its design?
- **Fundamental:** “The database stores the facts; the DBMS manages querying, concurrency, persistence, and the rules it supports.”
- **Problem solved:** An application needs correct, persistent, concurrent access to related facts rather than ad hoc storage and unrestricted scans.
- **Applied evidence:** “Appropriate indexes, bounded result sets, and fewer unnecessary round trips can help before adding machines.”
- **Apply it:** List lookups, lists, updates, and reports before selecting a database. → Specify required freshness for each operation. → Inspect query/access patterns and determine whether disk, locks, CPU, or connections are the actual bottleneck.
- **Decision or tradeoff:** Indexes and bounded reads can avoid unnecessary scale-out, but different access and consistency needs require different choices.
- **Animation decision:** The database/DBMS roles and workload checklist are conceptual and adequately expressed with the existing text.

## SQL databases

- **Opening problem:** A customer's order-history screen becomes slow as the shop grows. What would you inspect before adding servers, and which data relationships must remain valid?
- **Fundamental:** “Keys identify rows; constraints reject invalid relationships or duplicate identifiers.”
- **Problem solved:** Related orders, customers, and items need explicit identities, integrity constraints, and coordinated changes.
- **Applied evidence:** “For a customer's newest orders, inspect a query plan and an index matching the filter and sort.”
- **Apply it:** Model relationships with keys and the necessary constraints. → Write important queries and inspect candidate filter/sort indexes using a query plan. → Retrieve bounded results, keep transactions short, and use parameterized inputs.
- **Decision or tradeoff:** Relational structure helps express integrity but does not automatically make every query efficient; indexes add maintenance work.
- **Animation decision:** Tables, keys, and the example query are understandable with static relationships; transaction concurrency is handled by its dedicated animation.

## NoSQL databases

- **Opening problem:** Products have different attributes, sessions are fetched by identifier, and recommendations explore relationships. Would one representation suit all three? What would you measure before choosing?
- **Fundamental:** “NoSQL is a collection of models, not one universal design.”
- **Problem solved:** Different access patterns may fit document, key-value, graph, or other models better than one assumed universal schema.
- **Applied evidence:** “Choose partition keys that spread traffic, not merely records.”
- **Apply it:** Sketch actual reads and writes before choosing a model. → Check query/index support and the cost of relationship-heavy queries. → Choose traffic-aware partition keys and verify the specific product’s transaction scope, consistency, and limits.
- **Decision or tradeoff:** A convenient representation can make other queries expensive; NoSQL does not imply no schema, no transactions, or unlimited scale.
- **Animation decision:** A model/access-pattern comparison is a static decision; animated objects would not clarify a necessary time-dependent distinction.

## SQL vs NoSQL databases

- **Opening problem:** Checkout updates stock while a catalog stores varied product attributes. Which operations and guarantees should decide the databases—not their labels?
- **Fundamental:** “SQL columns can be nullable; NoSQL includes structured graph and key-value models, not only documents.”
- **Problem solved:** Choosing by database category alone ignores required operations and operational cost.
- **Applied evidence:** “Compare creating an order, listing recent orders, and updating stock in candidate products.”
- **Apply it:** Express the workload and invariants. → Compare representations, guarantees, and measured reads/writes for candidate products. → Account for backups, monitoring, and cross-store coordination before adding a second database type.
- **Decision or tradeoff:** Combining stores can fit different workloads but increases consistency and operational work.
- **Animation decision:** The comparison is best represented as a requirements/workload decision table, not a temporal animation.

## Indexes

- **Opening problem:** One customer's latest ten orders require examining a million rows. What information could narrow the search, and what extra work would writes inherit?
- **Fundamental:** “An index narrows the search instead of replacing the data.”
- **Problem solved:** Finding a small relevant subset should not require scanning every unrelated database row.
- **Applied evidence:** “Compare rows examined, rows returned, and timing before and after adding the candidate index using representative data.”
- **Apply it:** Match a candidate index to the filter and sort. → Inspect rows examined versus returned and compare query plans/timings on representative data. → Account for storage and write maintenance; check real use before removing an index.
- **Decision or tradeoff:** Indexes can speed reads while consuming space and making writes more expensive; one index does not optimize every query.
- **Animation decision:** A stepwise scan versus index lookup, followed by index maintenance on an insert, makes avoided work and write cost visible.

## Normalization and Denormalization

- **Opening problem:** A customer moves after an order ships. Should every address change? How would you distinguish today's profile from the delivery fact recorded when the order was placed?
- **Fundamental:** “A candidate key is a minimal superkey; an alternate key is a candidate not chosen as primary.”
- **Problem solved:** Duplicated values can become inconsistent, while meaningful historical snapshots must not be overwritten as if they were current facts.
- **Applied evidence:** “For every duplicated current value, decide who updates each copy and what readers may see while updates propagate.”
- **Apply it:** Identify minimal candidate keys and whether a non-key attribute depends on only part of a composite key. → Assign ownership and meaning to each fact. → Inspect query/index costs before introducing duplicated fields or a read model. → Define how current-value copies update and when historical snapshots are captured or corrected.
- **Decision or tradeoff:** Denormalized reads can be cheaper but create propagation work; an intentional historical snapshot is a separate business fact.
- **Animation decision:** Updating the current profile while retaining the order’s historical delivery address reveals why two similar fields have different update behavior.

## Transactions

- **Opening problem:** Two buyers see one ticket. Which single database action should determine who reserves it, and what result permits confirmation?
- **Fundamental:** “A transaction boundary alone does not prevent overselling; isolation and statements matter.”
- **Problem solved:** Concurrent buyers may both believe they reserved the same final unit.
- **Applied evidence:** “Check affected rows before confirming success; commit related reservation changes together.”
- **Apply it:** Use an atomic conditional update scoped to product_id and positive quantity. → Check whether a row changed before confirming success, and group related database changes. → Keep transactions short, choose suitable locking/isolation, retry conflicts safely, and handle external payment separately.
- **Decision or tradeoff:** Atomicity boundaries alone do not determine concurrency behavior; stronger isolation or locking can add waiting and retries.
- **Animation decision:** Interleaving two buyers’ reads and writes, then contrasting the conditional-update outcome, directly exposes the race and its prevention.

## ACID and BASE consistency models

- **Opening problem:** An order commits, but its replica still shows yesterday's list. Which correctness promise held, and which reader-visible guarantee did not?
- **Fundamental:** “ACID consistency preserves declared transaction invariants; distributed consistency describes what readers observe across copies.”
- **Problem solved:** The word consistency can incorrectly conflate local invariant preservation with visibility across replicas.
- **Applied evidence:** “Specify the invariant, acceptable staleness, and failure response before choosing coordination, then measure its latency and availability costs.”
- **Apply it:** State the business invariant and acceptable staleness for each operation. → Select coordination and failure behavior required for correctness. → Measure latency/availability cost and verify that update/conflict mechanisms support eventual convergence.
- **Decision or tradeoff:** Use stronger coordination where correctness requires it, while accepting stale data only where the operation allows it.
- **Animation decision:** A local commit followed by delayed replica visibility distinguishes the two meanings of consistency more clearly than labels alone.

## Database Replication

- **Opening problem:** You save an address and immediately read its old value elsewhere. Which copy answered? Would another live copy also protect you from accidental deletion?
- **Fundamental:** “Replication copies data; sharding divides ownership.”
- **Problem solved:** Copies support read capacity or recovery but can lag, and copying the same mistake does not preserve historical recovery points.
- **Applied evidence:** “Route freshness-sensitive reads through the appropriate authoritative protocol; use replicas where their lag is acceptable.”
- **Apply it:** Route freshness-sensitive reads to an appropriate authoritative path. → Use replicas for reads that tolerate their lag and monitor that lag. → Test failover and account for selected synchronous acknowledgements, write latency, and separate backups.
- **Decision or tradeoff:** Waiting for replicas can increase write latency; synchronous acknowledgement is not a blanket guarantee that every reader sees identical data.
- **Animation decision:** Write propagation, read timing, and promotion are temporal; two visible replica states prevent treating replication as instant synchronization.

## Sharding

- **Opening problem:** A shop outgrows one database. Which customer requests can stay together, how will callers find their owner, and which reports need multiple owners?
- **Fundamental:** “A replica of A keeps another copy of A's range; B owns a different range.”
- **Problem solved:** A growing dataset or workload needs distribution without confusing copied data with divided ownership.
- **Applied evidence:** “Choose a shard key from frequent queries and traffic. A customer identifier can keep one customer's orders together.”
- **Apply it:** Choose a shard key from frequent queries and traffic locality. → Measure request distribution and data sizes, including hot customers. → Plan cross-shard queries, key movement, and growth; check whether query/index improvements solve the immediate problem more simply.
- **Decision or tradeoff:** One-key routing can be efficient while cross-customer queries require fan-out and merging; equal row counts need not balance traffic.
- **Animation decision:** Routing requests, showing a hot shard, and moving ownership during growth make partitioning, skew, and replica-versus-shard distinctions tangible.

## Consistent Hashing

- **Opening problem:** A cache gains a node. How much data should move, how will clients agree on ownership, and when is the new owner ready?
- **Fundamental:** “On a consistent-hash ring, adding a node typically changes ownership of only part of the key space.”
- **Problem solved:** Naive modulo-based key placement can move many keys when the number of nodes changes.
- **Applied evidence:** “Warm caches gradually or limit database pressure when reassignment creates misses.”
- **Apply it:** Use compatible membership and key-to-owner rules across participants. → Plan data availability and client disagreement during membership changes. → Measure movement, misses, and load; use virtual nodes appropriately and limit origin pressure while warming reassigned keys.
- **Decision or tradeoff:** Virtual nodes improve ownership balance but do not remove hot-key traffic; replication and recovery still need separate decisions.
- **Animation decision:** Animating a ring before/after node addition shows exactly which keys move and contrasts it with modulo remapping.

## Database Federation

- **Opening problem:** Billing and catalog teams need independent databases. How will a checkout read both without assuming their writes and recovery happen together?
- **Fundamental:** “Functional partitioning separates databases by business domain; federation can also provide unified queries across autonomous stores.”
- **Problem solved:** Business domains may need separate ownership or scaling without mistaking functional boundaries for key ranges.
- **Applied evidence:** “Consider a read model instead of repeated remote joins, with explicit freshness rules.”
- **Apply it:** Assign each fact a domain owner. → Define cross-domain reads and updates. → Avoid repeated latency-sensitive remote joins where a read model fits, and coordinate separate backup/recovery procedures.
- **Decision or tradeoff:** A read model can reduce cross-database read cost but introduces freshness rules; independent stores require operational coordination.
- **Animation decision:** A static billing/catalog ownership diagram and a contrast with customer-ID ranges make this distinction clear.

## Bloom Filters

- **Opening problem:** A storage service receives many key lookups, but most requested keys do not exist. Disk reads are expensive. You can keep a small memory structure that sometimes says a missing key might exist. Which result could safely avoid a disk read? Which result must be verified? What could go wrong if the database accepts a new key before that memory structure learns about it?
- **Fundamental:** “A Bloom filter answers a membership question with two possible meanings: **definitely absent**, or **possibly present**.”
- **Problem solved:** Many absent-key queries waste expensive authoritative lookups.
- **Applied evidence:** “Choose the expected item count and acceptable false-positive rate before sizing the filter.”
- **Apply it:** Use the filter only as a preliminary gate, keeping the real store authoritative. → Choose expected capacity and false-positive tolerance, then size and maintain the filter. → Verify inserts/rebuilds and measure avoided reads, false positives, memory, and update lag.
- **Decision or tradeoff:** More memory and hashing can reduce wasted lookups at a cost; stale filters or clearing shared bits can violate the no-false-negative expectation.
- **Animation decision:** Setting shared bit positions and then querying a different key exposes a false positive; showing a missing insert also clarifies the maintenance condition.

## CAP Theorem

- **Opening problem:** Two ticket servers lose contact. A sells the last seat; B still shows it available. Should B confirm another sale? What if B cannot check?
- **Fundamental:** “CAP consistency means one-copy, real-time behavior, not instant forwarding everywhere.”
- **Problem solved:** A network partition prevents replicas coordinating while a client still expects a valid result.
- **Applied evidence:** “Require an authoritative reservation decision; reject an uncoordinated sale rather than sell twice.”
- **Apply it:** State the invariant: do not confirm the same ticket sale twice. → Require an authoritative reservation decision before confirming a sale. → Reject a sale when the partition prevents obtaining that decision; decide separately whether browsing may use older data.
- **Decision or tradeoff:** Preserve the reservation invariant by sacrificing availability for uncoordinated reservation requests during the partition.
- **Animation decision:** Show the link failing, the last successful write, and two different responses to B’s later request; static choose-two labels hide the timing.

## PACELC Theorem

- **Opening problem:** Your global profile app runs normally, but fresh reads wait for another region. Is the network partitioned? What delay/freshness choice still exists?
- **Fundamental:** “PACELC includes normal-operation latency versus consistency, not only partition behavior.”
- **Problem solved:** CAP alone does not describe the latency-versus-consistency decision during normal network operation.
- **Applied evidence:** “Permit stale regional profiles when acceptable; coordinate reads requiring freshness.”
- **Apply it:** Define acceptable freshness per operation. → Compare regional stale reads with waiting for cross-region coordination during normal operation. → Measure normal-operation delay and separately specify behavior during a partition.
- **Decision or tradeoff:** Regional reads can reduce waiting but accept staleness; coordinated fresh reads can cost cross-region latency.
- **Animation decision:** Contrast the same read with a working slow link and a broken link so the E/L/C branch is not confused with CAP’s partition branch.

## Distributed Transactions

- **Opening problem:** An order is recorded in one service and charged in another. Then the workflow fails, or the charge response disappears. Can one local database transaction settle everything? When should you retry, wait, or compensate?
- **Fundamental:** “A distributed transaction spans multiple databases.”
- **Problem solved:** An order and an external payment can reach different committed states after a partial failure.
- **Applied evidence:** “If a charge response is lost, reconcile the provider outcome before creating another charge.”
- **Apply it:** List order and payment steps and their durable state. → Choose coordinated commit or local commits with compensation according to the invariant. → Give repeated commands stable identifiers and define compensation for each partial outcome. → Expose payment pending for uncertain results and reconcile stuck work instead of charging again blindly.
- **Decision or tradeoff:** Coordinated commit increases coupling and waiting; sagas permit intermediate states and require compensating actions rather than erasing every external effect.
- **Animation decision:** The key confusion is temporal: charge succeeds, acknowledgement is lost, then recovery must distinguish failure from an unknown result.

## Caching

- **Opening problem:** A product page repeatedly reads a slow database. You add a fast copy of its price. Later the database says ₹550 while the copy still says ₹500. Which price should checkout trust? How should a missing or outdated copy be refreshed? What happens when hundreds of readers miss together?
- **Fundamental:** “A cache stores a reusable faster copy; the database remains authoritative in this example.”
- **Problem solved:** Repeated product reads unnecessarily hit slower authoritative storage, but cached copies can become stale.
- **Applied evidence:** “For checkout, confirm the actual payable price rather than trusting a stale product-page copy.”
- **Apply it:** Choose reusable product data and a key including all result-affecting inputs. → On a miss, read authoritative storage and populate the cache. → Invalidate or refresh cached data after writes and define a TTL/freshness policy. → Recheck the payable price authoritatively for checkout and test cache outage behavior.
- **Decision or tradeoff:** Faster repeated reads and less origin load require extra memory, invalidation logic, and an explicit stale-data policy.
- **Animation decision:** Show miss → load → hit → database update → stale hit or invalidation so speed is not mistaken for correctness.

## Caching Strategies

- **Opening problem:** Your product page uses a fast copy of database prices. A reader fetches ₹500, pauses, and later stores it after another request updates the database to ₹550 and removes the old copy. Which value might readers now see? Who should load missing values and update writes? When may a write be acknowledged if persistence happens later?
- **Fundamental:** “Read-through and write-through are not opposites: they describe different sides of access and can be combined.”
- **Problem solved:** The design must assign ownership of cache loading and writes without silently losing freshness or durability guarantees.
- **Applied evidence:** “A writer commits ₹550 to the database and invalidates the cached entry.”
- **Apply it:** Choose who owns miss loading: application for cache-aside or a cache layer for read-through. → Choose synchronous persistence or explicitly bounded write-behind risk. → Trace the slow old reader filling the cache after invalidation. → Use a coordinated/version-aware policy or authoritative read where the required freshness demands it.
- **Decision or tradeoff:** Coordination can improve freshness while consuming latency and complexity; write-behind can shorten acceptance time while introducing unpersisted-write risk.
- **Animation decision:** The invalidation race depends on interleaving an old read, a newer write, invalidation, and the late old fill.

## Cache Eviction Policies

- **Opening problem:** A cache holds only three products. You insert A, B, and C, read A again, then need room for D. Which item would you remove, and why? Would your answer change if B had been read hundreds of times earlier? Does removing an old item for space also guarantee that retained prices are fresh?
- **Fundamental:** “**Eviction** removes entries to make room. **Expiration** removes entries after an age limit, often a TTL, or time to live.”
- **Problem solved:** When the working set exceeds cache capacity, the system must choose which reusable values to remove.
- **Applied evidence:** “With LRU, B is removed because it was used least recently.”
- **Apply it:** Replay actual accesses against the cache capacity. → For the stated trace, observe LRU removes B while FIFO removes A. → For LFU, define frequency history and tie-breaking before predicting the victim. → Test scans and changing popularity; compare origin requests, latency, and policy bookkeeping cost.
- **Decision or tradeoff:** Recency/frequency tracking can improve useful retention but adds overhead and can predict the wrong reuse pattern; TTL is a separate freshness decision.
- **Animation decision:** An animated access trace makes the different victims under LRU and FIFO immediately testable.

## Distributed Caching

- **Opening problem:** Two hundred application instances reuse one popular product through a shared cache. Its entry expires, and every instance asks the database for it at once. Would adding more cache nodes solve this one-key burst? How could callers share the reload work? What should happen if the cache is entirely unavailable but the database cannot absorb unlimited fallback requests?
- **Fundamental:** “A distributed cache is reached over the network and can be shared across application servers; its data may also be spread across several cache nodes.”
- **Problem solved:** Many application instances duplicate expensive reads and can stampede the origin when a shared hot key expires.
- **Applied evidence:** “A per-key load-coalescing mechanism can let one worker reload while others wait”
- **Apply it:** Use a shared product key whose tenant and representation inputs are correct. → Coalesce concurrent reloads per key, with a defined failure/lease policy. → Bound cache timeouts and database fallback concurrency. → Measure hot-key traffic and test node loss plus a full cache outage.
- **Decision or tradeoff:** A shared cache increases reuse and pooled capacity but adds a network dependency; adding shards does not spread one hot key’s reload workload automatically.
- **Animation decision:** Show many simultaneous misses collapsing into one origin load, then contrast the unbounded fallback during an outage.

## Content Delivery Network (CDN)

- **Opening problem:** Viewers in several countries request the same product image from one distant server. Which work can happen closer to them? If you replace the image, why might some viewers still see its old version? Would the same sharing policy be safe for private invoices?
- **Fundamental:** “A CDN keeps reusable content at geographically distributed edge locations.”
- **Problem solved:** Serving every static asset from one origin creates repeated long-distance transfers and origin load.
- **Applied evidence:** “New origin bytes do not instantly replace every existing edge copy.”
- **Apply it:** Cache safely shareable static content at edges with explicit keys and cache-control. → Serve a hit at the edge; fetch the origin for a miss. → Publish changed bytes through versioned names or a deliberate invalidation/expiry policy. → Measure edge hits, origin requests, regional latency, and behavior when the origin is down.
- **Decision or tradeoff:** Edge reuse reduces transfer and origin work while introducing distributed stale-copy and access-control decisions.
- **Animation decision:** The first origin fetch, later edge hit, and content update arriving at different edges are timing-dependent.

## APIs

- **Opening problem:** A mobile developer needs to create an order without knowing your internal database structure. What information must their request contain, and what must your response guarantee? The service records the order but the response disappears. How should the developer retry without accidentally creating another order? Think about inputs, permissions, errors, and the difference between acceptance and completed work.
- **Fundamental:** “An API, or application programming interface, specifies how one program asks another to do something.”
- **Problem solved:** Independent clients need stable, unambiguous behavior without depending on internal implementation details.
- **Applied evidence:** “If processing continues later, say “accepted” rather than claiming delivery or payment has already completed.”
- **Apply it:** Specify required inputs, authentication, validation, and business rejection rules. → Return a stable order identifier and distinguish accepted-for-later from completed. → Define how a retried request identifies the same operation. → Bound results and measure the calls/bytes/retries needed to complete checkout.
- **Decision or tradeoff:** An aggregate endpoint can reduce client round trips but combine larger payloads and different freshness needs.
- **Animation decision:** The contract’s inputs, outputs, errors, and retry rule can be explained with a static request/response example.

## REST, GraphQL, gRPC

- **Opening problem:** Your product screen needs names, prices, and stock for thirty items. Should the client fetch resources, request selected fields, or call a typed inventory operation? If the response is small but triggers thirty database lookups, what actually needs improving?
- **Fundamental:** “These are interface models, not a universal speed ranking.”
- **Problem solved:** The interface must fit the clients, data shapes, and communication pattern without hiding inefficient backend work.
- **Applied evidence:** “Batch stock lookups by product IDs.”
- **Apply it:** Choose a resource, schema-selection, or typed-operation interface based on the client and operation. → Trace the inventory lookups for the 30 products. → Batch product IDs to avoid one backend query per item; bound query complexity and preserve data authorization. → Measure database calls, bytes, round trips, and end-to-end latency before choosing an optimization.
- **Decision or tradeoff:** Client field flexibility, HTTP resource behavior, and typed service calls solve different needs; a smaller response may still trigger more database work.
- **Animation decision:** A side-by-side static request and backend-query comparison is sufficient; the lesson’s main issue is interface choice rather than timing.

## API Gateway

- **Opening problem:** Your app has five microservices with ten APIs each. One screen needs three APIs from different services. Which calls should the client make? Where could you combine their responses? What should happen if one service is slow?
- **Fundamental:** “An API gateway provides a shared entry point for routing and cross-cutting policies.”
- **Problem solved:** Clients otherwise must discover and coordinate multiple backend services and shared entry-point concerns themselves.
- **Applied evidence:** “A BFF or aggregation endpoint can combine this screen’s three results; not every gateway must aggregate, and small systems may not need one.”
- **Apply it:** Route product and order requests to their service owners. → Aggregate catalog and stock only with a defined deadline and partial-response rule. → Enforce order ownership in the responsible service even after gateway authentication. → Deploy redundant gateways and measure gateway delay separately from downstream delay.
- **Decision or tradeoff:** A simpler client entry point concentrates routing and operational dependency; aggregation saves round trips but inherits downstream partial failure.
- **Animation decision:** Compare direct client calls with gateway routing and optional BFF composition, including deadlines and partial failures.

## Idempotency

- **Opening problem:** A ₹500 payment succeeds, but its response disappears. Two identical retries arrive together. How can both return a sensible result without charging twice? What if you record “already handled” and crash before performing the payment?
- **Fundamental:** “An idempotent operation has the same effect when repeated as when performed once.”
- **Problem solved:** A retried payment after a lost response must not create an extra charge or skip a charge that never happened.
- **Applied evidence:** “An atomic uniqueness rule chooses one owner when retries arrive concurrently.”
- **Apply it:** Scope K to caller and operation and record a payload fingerprint. → Use an atomic uniqueness rule to choose one owner; define the duplicate’s result or in-progress response. → Coordinate the durable key state with the actual side effect and recovery. → Use the external provider’s idempotency contract and reconcile uncertain outcomes before retrying a charge.
- **Decision or tradeoff:** Retry safety costs durable deduplication state and coordination; expiring keys before the supported retry period can re-enable duplicate work.
- **Animation decision:** Simultaneous requests and a lost acknowledgement make the difference between atomic claim, in-progress work, and saved result confusing.

## Rate Limiting

- **Opening problem:** A search customer should receive at most 100 requests per second, but ten app servers each enforce that allowance locally. What could the customer actually send? How much burst traffic is acceptable, and what should happen when allowance runs out?
- **Fundamental:** “Rate limiting bounds operation frequency to protect capacity or fairness.”
- **Problem solved:** One customer or an aggregate traffic burst can overload shared search capacity or unfairly consume it.
- **Applied evidence:** “Coordinate a global rule or deliberately partition its budget.”
- **Apply it:** Define the identity key, interval, sustained rate, and burst allowance. → Coordinate a global allowance or partition the budget intentionally across instances. → Choose token bucket refill/burst behavior or account for fixed-window boundary bursts. → Return a clear throttling response, require client backoff, and specify the unavailable-store policy.
- **Decision or tradeoff:** Coordinated global accounting improves rule accuracy but adds a dependency; failing open preserves access while risking overload, whereas failing closed rejects legitimate traffic.
- **Animation decision:** Token refill, burst depletion, and two adjacent fixed windows are easier to understand as a moving timeline.

## Long polling, WebSockets, Server-Sent Events (SSE)

- **Opening problem:** A scoreboard mainly sends scores to browsers; an editor exchanges changes both ways. Which connection pattern fits each? After a thirty-second disconnect, how will the client discover missed updates rather than silently continue with old state?
- **Fundamental:** “These transports do not automatically provide durable history.”
- **Problem solved:** Clients need timely updates, sometimes bidirectional, without losing all progress when a connection drops.
- **Applied evidence:** “Give updates sequence positions and recover after the last confirmed position, or reload a current snapshot when history is unavailable.”
- **Apply it:** Select SSE for suitable server-to-client updates, WebSockets for suitable bidirectional work, or long polling when appropriate. → Assign event positions or provide snapshots to recover missed updates. → Reconnect with backoff and bound per-client buffering. → Coalesce scoreboard state changes where safe, but retain chat messages when the product requires history.
- **Decision or tradeoff:** Long-lived communication reduces repeated polling but consumes connection/buffer resources and requires explicit reconnection/history behavior.
- **Animation decision:** Comparing held requests, repeated long-poll responses, and one persistent duplex connection is inherently temporal.

## Webhooks

- **Opening problem:** A payment provider tells your shop that a charge succeeded. Your shop records the event, but its acknowledgement disappears, so the provider sends the same event again. Should another shipment begin? How will you recognize the sender and distinguish a retry from a new event? What if a delayed pending event arrives after you already know payment completed?
- **Fundamental:** “A webhook is an event notification delivered to an endpoint you provide, commonly using an HTTP request.”
- **Problem solved:** A service needs provider events without constant polling, while tolerating duplicate, delayed, or reordered delivery.
- **Applied evidence:** “The provider sends event E. Your receiver verifies it and durably records E for processing.”
- **Apply it:** Verify the provider’s signature against the specified representation and validate the event. → Durably accept E and acknowledge according to the delivery contract. → Process E with a uniqueness rule plus recoverable business-state changes. → Reject stale state regressions or consult the authoritative provider status when appropriate.
- **Decision or tradeoff:** A short accept-and-enqueue path reduces acknowledgement delays but separates acceptance from business completion and requires a durable worker/recovery path.
- **Animation decision:** The lost acknowledgement and duplicate delivery must be distinguished from a genuinely new payment event.

## API Design

- **Opening problem:** One customer has a million orders, and a client asks to list them. Should one response contain everything? If you divide results into pages, how do equal creation times and concurrent inserts affect the next page? What must a continuation marker mean, and how do you stop a user changing it to read another customer’s orders?
- **Fundamental:** “Start with what clients need to do and the data they exchange.”
- **Problem solved:** Unbounded lists, ambiguous results, incompatible changes, and unsafe retries prevent clients completing tasks predictably.
- **Applied evidence:** “Instead, enforce a maximum page size and return a continuation cursor.”
- **Apply it:** Set a maximum page size and stable sort with a unique tie-breaker. → Return a continuation cursor and document snapshot versus live-list semantics. → Check authorization for every page and prevent cursors from granting someone else’s data access. → Test equal timestamps, concurrent inserts/deletes, invalid cursors, and repeated writes against the contract.
- **Decision or tradeoff:** Bounded pages reduce per-request work but require explicit ordering and continuation semantics; a cursor alone does not guarantee a stable snapshot.
- **Animation decision:** A static pair of pages with equal timestamps and a documented cursor boundary can explain the contract; animation is optional.

## Message Brokers

- **Opening problem:** An order must trigger billing and shipping, even when a receiver is temporarily offline. Should workers compete for one job or each receive the event? What must survive a crash?
- **Fundamental:** “A broker stores or routes messages between producers and consumers under configured guarantees.”
- **Problem solved:** Producers and consumers should exchange work/events without requiring each receiver to be synchronously active or directly addressed.
- **Applied evidence:** “Choose a queue when one worker should perform each job, and independent subscriptions when several business reactions each need the event.”
- **Apply it:** Decide whether one worker must do each job or independent subscribers each need the event. → Specify persistence, acknowledgement, ordering, and replay/retry guarantees before selecting a product. → Bound consumer in-flight work and batch only within acceptable delay. → Monitor backlog age and verify the crash-after-side-effect acknowledgement case.
- **Decision or tradeoff:** Buffering and decoupling introduce delayed processing, retained state, and duplicate/recovery responsibilities; product labels do not determine delivery semantics.
- **Animation decision:** The broker’s role and queue/topic pattern choice can be established with a static producer–broker–consumer diagram; queue-specific timing is animated separately.

## Message Queues

- **Opening problem:** A thousand uploads arrive together. Thumbnail generation is slower than upload acceptance. Where should unfinished jobs wait? A worker saves an image and crashes before reporting completion: should the replacement do the work again?
- **Fundamental:** “A work queue buffers jobs for competing consumers, letting uploads return while thumbnails remain pending.”
- **Problem solved:** Bursts of thumbnail work should not hold upload requests open or overwhelm downstream processing; redeliveries must be safe.
- **Applied evidence:** “A replacement can recognize complete output instead of creating conflicting duplicates.”
- **Apply it:** Durably enqueue stable job identifiers and use deterministic output keys. → Acknowledge after durable completion with realistic visibility/processing leases. → Handle a redelivered job without conflicting duplicate output. → Scale workers only while storage/database capacity permits and isolate repeatedly failing jobs.
- **Decision or tradeoff:** A queue absorbs temporary bursts but adds waiting time and cannot fix a sustained arrival rate above processing capacity.
- **Animation decision:** A worker crash before acknowledgement followed by redelivery visually disproves the misleading idea that a job is executed exactly once.

## Publish-Subscribe

- **Opening problem:** Every order needs billing and shipping. Both teams put workers on one shared work queue, but some orders get only one action. Why? How should deliveries and progress differ between teams and within one team?
- **Fundamental:** “Pub/sub gives independent subscriptions their own logical delivery.”
- **Problem solved:** Several independent business reactions must each receive an event without being treated as competing workers for one job.
- **Applied evidence:** “Billing and shipping each need a subscription; workers within billing may compete for its work.”
- **Apply it:** Create separate billing and shipping subscriptions. → Specify event identifiers, versioned meaning, and safe repeated processing. → Choose durable subscriptions/history if offline consumers must catch up. → Scale each subscription independently and partition related events consistently when their ordering matters.
- **Decision or tradeoff:** Independent fan-out avoids direct producer coupling but increases delivery/state coordination; global ordering is not automatically available across partitions.
- **Animation decision:** Show one copy per subscription and one worker per delivery within a subscription; learners often conflate these two distribution levels.

## Change Data Capture (CDC)

- **Opening problem:** The product database commits a new price, but updating the search index fails. Repeated full scans are expensive, and independently writing both stores creates awkward failure cases. How could search learn about committed changes? After a pipeline restart, what if the same change appears again? How would you detect a destination falling far behind while retained change history keeps growing?
- **Fundamental:** “CDC observes changes in a database and makes them available to other systems.”
- **Problem solved:** A derived search index needs committed database changes without repeatedly scanning the entire source or independently double-writing each request.
- **Applied evidence:** “Updating the search record by stable product identifier and an appropriate version rule can make replay safe.”
- **Apply it:** Take an initial snapshot and track a recoverable change-log position. → Apply records using stable product identifiers and a version rule that makes replay safe. → Handle deletes/schema changes and monitor time/log-position lag. → Bound retained-log growth and define resnapshot recovery if required history disappears.
- **Decision or tradeoff:** Streaming changes reduces repeated full reads but introduces lag, source retention overhead, schema coupling, and replay/recovery duties.
- **Animation decision:** Animate commit → log → connector → index and then replay after restart so database commit is not mistaken for immediate search visibility.

## N-tier architecture

- **Opening problem:** A shop's checkout slows while product pages remain responsive. Which responsibility needs extra capacity? What changes if the database runs on another machine?
- **Fundamental:** “Layers separate responsibilities; tiers separate deployed processes or machines.”
- **Problem solved:** Separates presentation, business rules, and persistence so each responsibility has an explicit deployment and scaling boundary.
- **Applied evidence:** “Fetch needed order lines in a bounded request instead of adding one network round trip per line.”
- **Apply it:** Identify presentation, order rules, and persistence. → Place deployment boundaries deliberately and trace network calls. → Measure the busy tier and reduce unnecessary round trips.
- **Decision or tradeoff:** Independent tier deployment adds network latency and partial failure; logical layers do not require separate machines.
- **Animation decision:** The local example already distinguishes logical layers from deployed tiers; the source diagram plus request trace is sufficient.

## Monoliths and Microservices

- **Opening problem:** A shop's catalog team cannot release a small search change without coordinating a billing deployment. Catalog traffic also grows faster than checkout. Would splitting services solve both problems? What new failures could one order encounter? Which data should each team own?
- **Fundamental:** “A monolith is one deployable application; microservices introduce independently deployed service boundaries.”
- **Problem solved:** Defines capability and data-ownership boundaries without treating distributed deployment as an automatic performance improvement.
- **Applied evidence:** “For an order crossing billing and inventory, define intermediate states if reservation fails or payment is delayed.”
- **Apply it:** Measure the bottleneck and release constraint. → Choose explicit capability and data ownership. → Trace cross-boundary reservation/payment failure and define recovery.
- **Decision or tradeoff:** Independent scaling or releases may justify a service split, but coordination and partial failures can outweigh that benefit.
- **Animation decision:** The source comparison and explicit order-failure walkthrough already explain the boundary; animation would add presentation rather than resolve a remaining gap.

## Event-Driven Architecture (EDA)

- **Opening problem:** An order is saved, but a crash prevents shipping from hearing about it. What information must survive? Should checkout success mean shipping already finished?
- **Fundamental:** “EDA lets consumers react after the initiating action commits.”
- **Problem solved:** Decouples an initiating business action from downstream reactions that can complete later.
- **Applied evidence:** “Save the order and an outbox event together; a relay publishes committed events.”
- **Apply it:** Coordinate the order and publication intent durably. → Publish committed events and handle repeated delivery safely. → Expose pending shipping and monitor processing delay.
- **Decision or tradeoff:** Decoupled reactions reduce synchronous waiting but require publication recovery, delayed state, and duplicate handling.
- **Animation decision:** A sequence should show order committed, shipping still pending, and a crash/retry around publication; otherwise learners can confuse asynchronous acceptance with downstream completion.

## Event Sourcing

- **Opening problem:** A balance changed several times, and an auditor asks how it reached 70. Can you reconstruct it? How would rebuilding avoid charging or emailing someone again?
- **Fundamental:** “Event sourcing makes stored events authoritative, not merely notifications.”
- **Problem solved:** Preserves authoritative business history so current state and derived views can be reconstructed.
- **Applied evidence:** “Deposited(100), then Withdrawn(30), rebuilds balance 70.”
- **Apply it:** Persist authoritative business event history. → Replay events or a verified snapshot and later events. → Keep rebuilding isolated from external side effects.
- **Decision or tradeoff:** Historical replay and auditability require event-version and recovery discipline; publishing notifications alone does not provide them.
- **Animation decision:** Animate replay changing balance 0→100→70 while external side effects stay disabled, then contrast that with notification-only EDA.

## Command and Query Responsibility Segregation (CQRS)

- **Opening problem:** Creating an order succeeds, but the customer's order-list screen does not show it yet. Which state is authoritative? What should the customer see while the list catches up?
- **Fundamental:** “CQRS separates write responsibilities from read views; it does not require event sourcing.”
- **Problem solved:** Allows write rules and read queries to use models shaped for their different responsibilities.
- **Applied evidence:** “Return the confirmed order identifier with a pending-view state.”
- **Apply it:** Commit create-order through the write model. → Project changes safely into a customer read model. → Expose lag and define projection recovery.
- **Decision or tradeoff:** Query-specific models can speed screens while adding lag, synchronization, and recovery work.
- **Animation decision:** Show the write succeeding before the read projection catches up, including duplicate projection delivery; this makes the lag and model separation visible.

## Enterprise Service Bus (ESB)

- **Opening problem:** Billing emits one address format; legacy shipping expects another. Where should conversion happen? What happens to orders if the converter fails?
- **Fundamental:** “An ESB transforms and routes messages between unlike systems.”
- **Problem solved:** Integrates systems with incompatible message formats and routing requirements.
- **Applied evidence:** “Put billing-to-shipping transformations at explicit integration boundaries.”
- **Apply it:** Define source and target message contracts. → Transform and route at a clear integration boundary. → Bound retries and verify bus state and failover.
- **Decision or tradeoff:** Central integration simplifies connections while concentrating operational dependency and potential business-rule coupling.
- **Animation decision:** The billing-to-shipping transformation is a static contract and routing example; the existing source diagram and concrete fields/routing explanation are sufficient.

## Virtual Machines (VMs) and Containers

- **Opening problem:** A shop replaces workers frequently. One needs a different operating-system kernel; another repeatedly runs out of memory. Which isolation boundary matters? What must remain after a worker disappears?
- **Fundamental:** “VMs can run separate guest kernels; containers normally share their host kernel while isolating processes and resources.”
- **Problem solved:** Chooses packaging, resource control, and operating-system isolation boundaries for workloads.
- **Applied evidence:** “Keep durable job state outside disposable instances and check readiness before routing work.”
- **Apply it:** Choose the required kernel and isolation boundary. → Allocate measured resources and externalize durable state. → Replace a worker and test readiness and job resumption.
- **Decision or tradeoff:** Lightweight packaging does not create a separate guest kernel or guarantee fast readiness; stronger boundaries may add overhead.
- **Animation decision:** A static kernel/process boundary diagram is enough; the lesson explicitly rejects equating a small image with a separate guest OS.

## Serverless Architecture

- **Opening problem:** Your photo service receives no uploads all night, then 5,000 photos in a minute. Thumbnail jobs sometimes run twice, and the database accepts only 100 connections. What must survive between executions? How would you control the burst without losing work? Which measurements would tell you whether paying for warm capacity is worthwhile?
- **Fundamental:** “Serverless does not mean no servers exist.”
- **Problem solved:** Offloads parts of runtime provisioning and operation for suitable request- or event-triggered work.
- **Applied evidence:** “A function reads P, creates a thumbnail, and stores the output under a deterministic key such as `P/version/thumbnail`.”
- **Apply it:** Store photo P and use a deterministic output key such as P/version/thumbnail. → Make duplicate events safe without relying on invocation-local memory. → Measure cold versus warm execution, tune concurrency against downstream limits, and compare cost per successful job.
- **Decision or tradeoff:** Reduced infrastructure management and burst scaling come with lifecycle limits, cold starts, provider coupling, and downstream saturation risk.
- **Animation decision:** The local upload→function→deterministic-output walkthrough already exposes lifecycle and duplicate behavior; no unresolved temporal ambiguity requires animation.

## Peer-to-Peer (P2P) Architecture

- **Opening problem:** A training app distributes one large video file to many learners. Some learners already have different pieces and can upload them; others sit behind restrictive routers. One helpful peer suddenly leaves before sharing its last piece. How would a newcomer find trustworthy content and finish downloading? Which dependencies remain even if peers exchange most bytes directly?
- **Fundamental:** “In a peer-to-peer design, participants can exchange data or provide services to one another.”
- **Problem solved:** Distributes content-serving work among participants instead of making one origin serve every byte.
- **Applied evidence:** “They exchange useful pieces rather than downloading every byte from the origin.”
- **Apply it:** Split content into verifiable pieces and obtain trustworthy piece metadata. → Discover reachable peers with useful pieces and resume from alternative sources when peers depart. → Bound connections and upload usage; measure completion time and origin bandwidth savings under churn.
- **Decision or tradeoff:** Distributed upload capacity reduces origin load but complicates reachability, trust, abuse prevention, discovery dependencies, and availability of scarce pieces.
- **Animation decision:** A piece-exchange animation with one peer leaving should show why partial progress, scarce pieces, and alternative sources matter.

## Service Discovery

- **Opening problem:** An orders instance is replaced, but a long-lived caller keeps using its old address. How should the caller learn the change? Can a recently discovered destination still fail?
- **Fundamental:** “Discovery supplies service destinations; load balancing chooses among them.”
- **Problem solved:** Finds service instance addresses that change during deployment or failure.
- **Applied evidence:** “For orders deployments, register instances using meaningful readiness checks.”
- **Apply it:** Register instances only when ready for relevant work. → Remove retiring routes and drain bounded existing work. → Refresh destinations and handle request-time failures safely.
- **Decision or tradeoff:** Caching discovery reduces lookup load but delays changes; request-time deadlines and retry policy remain necessary.
- **Animation decision:** The source already distinguishes client/server discovery paths, and the replacement-instance example gives the necessary application steps without another animated sequence.

## HeartBeats

- **Opening problem:** A worker reports every five seconds, then sends nothing for twenty seconds. A replacement begins the same job, but the original worker later resumes and still believes it owns the work. Was the original worker necessarily dead? What should the monitor infer from silence? How would you prevent both workers from applying the same irreversible business effect?
- **Fundamental:** “A heartbeat is a periodic “I am here” signal.”
- **Problem solved:** Provides recent reachability evidence to support failure suspicion, not proof of end-to-end health.
- **Applied evidence:** “If the worker pauses for twenty seconds, a replacement may begin work while the old worker later resumes.”
- **Apply it:** Choose report interval and suspicion threshold from observed delay, pauses, and detection needs. → Separate liveness from readiness so a heartbeat does not hide a broken business dependency. → Test pause-and-resume after replacement and coordinate work with fencing, idempotency, or another safe invariant.
- **Decision or tradeoff:** Short thresholds detect trouble sooner but increase false suspicions; longer thresholds delay failover and do not prove exact recovery time.
- **Animation decision:** Animate a live but paused worker missing heartbeats, a replacement starting, and the old worker resuming; it demonstrates why timeout is suspicion and can cause overlapping work.

## Circuit breaker

- **Opening problem:** Checkout repeatedly waits on a failing payment service until workers are exhausted. Should it keep trying every request? How can it notice recovery safely?
- **Fundamental:** “A breaker reacts to repeated dependency failures; a timeout bounds one call.”
- **Problem solved:** Stops repeated calls to a failing dependency from consuming resources and spreading failure.
- **Applied evidence:** “For payments, show pending or unavailable rather than inventing success.”
- **Apply it:** Measure payment failures and select thresholds. → Stop calls while open and admit limited recovery probes. → Preserve correct pending/unavailable outcomes with bounded retries.
- **Decision or tradeoff:** Fail-fast protection limits wasted capacity but temporarily rejects calls and needs careful recovery probing.
- **Animation decision:** The closed→open→half-open→closed/open state loop is a common confusion; animate allowed and blocked requests separately from each call timeout.

## SLA, SLO, SLI

- **Opening problem:** Checkout responds quickly but sometimes returns errors. What counts as success? Which measured percentage would show whether the service meets its promise?
- **Fundamental:** “SLI is the measurement; SLO the target; SLA an agreement that may specify consequences.”
- **Problem solved:** Connects a user-facing service promise to a measurable target and observed performance.
- **Applied evidence:** “For checkout, count correct purchases within a latency threshold over a defined window.”
- **Apply it:** Define successful purchase and latency threshold. → Measure a window and compare the target. → Use allowed failure budget to prioritize reliability work.
- **Decision or tradeoff:** A quick process response can still fail the business operation; measurement window and success definition determine the conclusion.
- **Animation decision:** The measurement/target/agreement distinction and concrete checkout classification are clearer as a small table or worked count than an animation.

## Disaster recovery

- **Opening problem:** A region fails when the latest usable order backup is an hour old. What can be lost? When will customers actually be able to purchase again?
- **Fundamental:** “RPO limits tolerable data loss; RTO limits recovery time.”
- **Problem solved:** Defines tolerable data loss and time to recover usable service after a serious disruption.
- **Applied evidence:** “Rehearse restoring order data, configuration, credentials, and traffic routing.”
- **Apply it:** Set data-loss and recovery targets from business tolerance. → Rehearse restoring data and operational dependencies. → Measure usable service and test backup isolation.
- **Decision or tradeoff:** Backup frequency and restore speed improve different targets; backup creation alone does not prove usable recovery.
- **Animation decision:** The hourly-backup and two-hour-restore example already separates the two dimensions; a labeled static timeline suffices.

## Consensus Algorithms

- **Opening problem:** Three servers maintain a shared configuration history. The current leader becomes isolated from the other two, but can still hear from one client. Both network groups want to accept changes. Which decisions may safely become committed? What should happen if no communicating group satisfies the protocol's rules? How would a returning leader learn what it missed?
- **Fundamental:** “Consensus protocols help cooperating nodes agree on decisions, such as the order of entries in a **replicated log**, the same ordered history kept on multiple nodes.”
- **Problem solved:** Maintains an agreed ordered decision history among replicas under a specified failure model.
- **Applied evidence:** “In a three-voter Raft group, a client sends a command to the leader.”
- **Apply it:** Use a well-understood protocol implementation and specify voters and failure assumptions. → Replicate log entries through leader, term, history, persistence, and quorum rules. → Test leader loss and partitions; batch or pipeline only while retaining required correctness rules.
- **Decision or tradeoff:** Distant voters can improve regional failure tolerance while adding commit latency; losing the communicating majority may stop progress to preserve safety.
- **Animation decision:** Show leader A isolated, B/C forming a communicating majority, and A unable to commit conflicting decisions; simple moving majority votes alone would teach the wrong protocol.

## Distributed Locking

- **Opening problem:** Worker A starts a monthly report, pauses for a long time, then resumes. Meanwhile its ownership deadline passed, so worker B took over and saved a newer report. A now tries to overwrite that result. Did deadline expiry physically stop A? What must the protected storage check? Could a conditional write avoid needing this lock at all?
- **Fundamental:** “A distributed lock tries to give one participant temporary ownership of work shared across machines.”
- **Problem solved:** Coordinates exclusive work across processes while accounting for expiry and stale owners.
- **Applied evidence:** “If the protected store checks ownership tokens, it can reject token 10 after observing token 11.”
- **Apply it:** Decide whether duplicates are a cost problem or a correctness violation. → Acquire ownership with a lease and have the protected store enforce fencing or another direct invariant. → Make release ownership-safe, shorten the critical section, and test old owners resuming after takeover.
- **Decision or tradeoff:** A longer lease delays takeover while a shorter lease can expire during legitimate work; idempotent or conditional writes may express the invariant more directly than a lock.
- **Animation decision:** Animate the lease timeline with tokens 10/11 and the protected store rejecting A after B writes; lease expiry alone does not stop A from executing.

## Gossip Protocol

- **Opening problem:** A new storage node announces itself to one peer. Some clients can discover it immediately, while other peers still list only the old members. A temporary network partition delays one part of the cluster. Must every view already match? How can peers decide whether returning observations are old or new? Would learning the same membership list also establish one safe order for payments?
- **Fundamental:** “In a gossip protocol, nodes periodically exchange information with selected peers.”
- **Problem solved:** Spreads membership or health observations without every update requiring one sender to contact all nodes directly.
- **Applied evidence:** “A tells B during a periodic exchange; B later tells C.”
- **Apply it:** Select peers and exchange membership observations using the chosen protocol version rules. → Allow temporary view disagreement and reconnect or resynchronize after separation. → Tune exchange frequency, fanout, and message size against convergence time and bandwidth.
- **Decision or tradeoff:** Faster or wider exchanges consume more network and processing; gradual dissemination is not consensus on a single committed write order.
- **Animation decision:** Animate update D reaching A, B, then C across exchanges, with visibly different views before convergence and a partition delaying spread.

## Distributed Tracing

- **Opening problem:** An order page calls inventory and delivery at the same time. Each call has a recorded duration, and the parent request records time that already includes those calls. A dashboard adds every span and reports more time than the customer waited. Which measurements overlap? Where is the actual critical path? How would you prove the trace follows the same request across all services?
- **Fundamental:** “A trace connects the work caused by one request.”
- **Problem solved:** Connects request work across service boundaries to locate slow or failing dependencies.
- **Applied evidence:** “Inspect the query and its execution behavior before adding application instances.”
- **Apply it:** Propagate trace context through HTTP and message metadata and create meaningful spans. → Find the critical path rather than summing overlapping spans or inclusive parent times. → Connect traces to metrics and logs, test broken context propagation, and choose sampling against overhead and rare-event visibility.
- **Decision or tradeoff:** Sampling reduces volume but may miss rare slow failures; recording more data raises overhead and privacy cost without automatically explaining the root cause.
- **Animation decision:** A span timeline should contrast sequential and concurrent calls; animation can demonstrate why overlapping spans must not simply be added.

## SSL, TLS, mTLS

- **Opening problem:** A browser connects securely to a gateway, which forwards the request internally. Where can the data be read? How does the next service know who called it?
- **Fundamental:** “TLS protects a connection; usually the client verifies the server certificate.”
- **Problem solved:** Protects connection data and establishes endpoint identity while keeping authorization separate.
- **Applied evidence:** “At a gateway, design protection for the new internal connection separately.”
- **Apply it:** Locate TLS termination and each subsequent connection. → Verify endpoint identities and authorize the operation separately. → Manage renewal and measure safe connection reuse.
- **Decision or tradeoff:** Connection reuse saves handshake work; one protected hop does not secure later hops or grant business permissions.
- **Animation decision:** Endpoint identity and termination boundaries are explicit in the local example and can be shown with a static two-hop diagram.

## OAuth 2.0 and OpenID Connect (OIDC)

- **Opening problem:** A printing app needs selected photos but must not receive the user's password. What permission should it request? Which returned information proves login, and what belongs at the photo API?
- **Fundamental:** “OAuth delegates resource access; OIDC adds authenticated login identity.”
- **Problem solved:** Separates delegated access to protected resources from a client receiving authenticated login identity.
- **Applied evidence:** “For the printing app, redirect to the provider, receive an authorization code, and exchange it for tokens.”
- **Apply it:** Obtain narrow delegated permission through a provider flow. → Exchange the code with appropriate PKCE and validate the token contract. → Present the access token at its API, enforce ownership, and plan refresh/revocation.
- **Decision or tradeoff:** Token lifetime, renewal cost, and revocation delay interact; valid identity is not universal permission.
- **Animation decision:** Animate user/client/provider/API roles and separately label code, ID token, and access token so token audience and password handling cannot be confused.

## Single Sign-On (SSO)

- **Opening problem:** An employee signs in once and opens payroll and email. Later, payroll logout leaves email open, and disabling the employee at the provider does not immediately close an existing payroll session. Which sessions and permissions must the organization control? How quickly must access removal take effect?
- **Fundamental:** “SSO lets applications trust one provider's authenticated identity, but each application still owns permissions and often a separate session.”
- **Problem solved:** Lets multiple applications share an identity-provider sign-in while retaining application-specific permissions and session policies.
- **Applied evidence:** “Test an already open payroll session after disabling the employee.”
- **Apply it:** Map stable provider identities to explicit application roles. → Define provider/application sessions and revocation requirements. → Disable an account and test established application access.
- **Decision or tradeoff:** Reusing sessions lowers provider work and improves convenience while potentially delaying access removal.
- **Animation decision:** The separate payroll/provider/email sessions and disable-account check explicitly resolve the key confusion; a session-state table is sufficient.

## Geohashing and Quadtrees

- **Opening problem:** A rider stands near a grid boundary. A closer driver is across the line, and a farther driver is inside the same cell. Which candidates should the search inspect? What if a candidate's last location is old?
- **Fundamental:** “Geohashes encode locations into grid cells; quadtrees repeatedly subdivide regions.”
- **Problem solved:** Narrows spatial search candidates so nearby-driver queries avoid a distance calculation against every driver.
- **Applied evidence:** “For ride matching, inspect relevant and neighboring cells, then calculate actual distances and check eligibility and freshness.”
- **Apply it:** Choose regions from radius, density, and current index shape. → Inspect neighbors and calculate exact distances. → Check location freshness and measure index-update costs.
- **Decision or tradeoff:** Finer regions reduce some candidate work but increase lookups and movement-maintenance cost.
- **Animation decision:** Animate two close points on opposite cell sides and a search expanding into neighbors; it exposes the false assumption that same-cell search finds every nearest driver.
