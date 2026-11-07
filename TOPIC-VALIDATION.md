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

## At-a-glance matrix

| Category / topic | Technical fundamental | Problem and design application | Animation decision |
| --- | --- | --- | --- |
| 01-core-concepts: [What is system design?](curriculum/01-core-concepts/01-what-is-system-design.md) | [Evidence](curriculum/01-core-concepts/01-what-is-system-design.md#make-it-concrete) | Choosing components before knowing the behavior and failure guarantees the system must provide. [Applied evidence](curriculum/01-core-concepts/01-what-is-system-design.md#make-it-concrete) | Static explanation sufficient |
| 01-core-concepts: [Scalability](curriculum/01-core-concepts/02-scalability.md) | [Evidence](curriculum/01-core-concepts/02-scalability.md#make-it-concrete) | A rising request rate exceeds the capacity of a particular stage. [Applied evidence](curriculum/01-core-concepts/02-scalability.md#make-it-concrete) | [load-balancer](animations/load-balancer.md) |
| 01-core-concepts: [Availability](curriculum/01-core-concepts/03-availability.md) | [Evidence](curriculum/01-core-concepts/03-availability.md#make-it-concrete) | Users lose access when a server or shared dependency fails. [Applied evidence](curriculum/01-core-concepts/03-availability.md#apply-and-improve) | [availability-failover](animations/availability-failover.md) |
| 01-core-concepts: [Latency vs Throughput vs Bandwidth](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) | [Evidence](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md#throughput-concurrency-and-waiting) | Optimizing the wrong performance quantity or interpreting averages and network capacity as interchangeable. [Applied evidence](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md#how-to-optimize-the-right-thing) | [request-latency](animations/request-latency.md) |
| 01-core-concepts: [Reliability](curriculum/01-core-concepts/05-reliability.md) | [Evidence](curriculum/01-core-concepts/05-reliability.md#what-it-means) | A partially completed operation can leave users with duplicate charges, lost state, or a permanently unresolved order. [Applied evidence](curriculum/01-core-concepts/05-reliability.md#worked-failure-and-recovery) | [saga](animations/saga.md), [idempotency](animations/idempotency.md) |
| 01-core-concepts: [SPOF](curriculum/01-core-concepts/06-spof.md) | [Evidence](curriculum/01-core-concepts/06-spof.md#one-failure-that-stops-the-whole-path) | Redundant application instances still depend on one component or common failure domain. [Applied evidence](curriculum/01-core-concepts/06-spof.md#worked-example-two-applications-one-database) | Static explanation sufficient |
| 02-networking: [IP](curriculum/02-networking/01-ip.md) | [Evidence](curriculum/02-networking/01-ip.md#make-it-concrete) | Services need reachable addresses without exposing every dependency to the internet. [Applied evidence](curriculum/02-networking/01-ip.md#apply-and-troubleshoot) | Static explanation sufficient |
| 02-networking: [OSI Model](curriculum/02-networking/02-osi-model.md) | [Evidence](curriculum/02-networking/02-osi-model.md#make-it-concrete) | A vague network failure leads to changing unrelated parts of the system. [Applied evidence](curriculum/02-networking/02-osi-model.md#apply-and-improve) | Static explanation sufficient |
| 02-networking: [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md) | [Evidence](curriculum/02-networking/03-tcp-and-udp.md#make-it-concrete) | Applications differ in whether ordered delivery, loss recovery, and timely delivery are most important. [Applied evidence](curriculum/02-networking/03-tcp-and-udp.md#apply-and-improve) | [tcp-udp](animations/tcp-udp.md) |
| 02-networking: [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md) | [Evidence](curriculum/02-networking/04-domain-name-system-dns.md#make-it-concrete) | Clients need to resolve service names, while cached answers can temporarily outlive a destination change. [Applied evidence](curriculum/02-networking/04-domain-name-system-dns.md#apply-and-improve) | [dns-lookup](animations/dns-lookup.md) |
| 02-networking: [Proxy](curriculum/02-networking/05-proxy.md) | [Evidence](curriculum/02-networking/05-proxy.md#make-it-concrete) | A system needs a controlled entry or exit point for routing and common request handling. [Applied evidence](curriculum/02-networking/05-proxy.md#apply-and-improve) | Static explanation sufficient |
| 02-networking: [HTTP/HTTPS](curriculum/02-networking/06-httphttps.md) | [Evidence](curriculum/02-networking/06-httphttps.md#a-request-and-its-response) | Clients and servers need a request/response contract and protected transport without confusing a network result with a business outcome. [Applied evidence](curriculum/02-networking/06-httphttps.md#how-to-optimize-responsibly) | [tls-mtls](animations/tls-mtls.md) |
| 02-networking: [Checksums](curriculum/02-networking/07-checksums.md) | [Evidence](curriculum/02-networking/07-checksums.md#detecting-that-data-changed) | A transferred, stored, or assembled file may differ from its expected bytes. [Applied evidence](curriculum/02-networking/07-checksums.md#how-to-improve-efficiency-without-losing-the-guarantee) | Static explanation sufficient |
| 02-networking: [Load Balancing](curriculum/02-networking/08-load-balancing.md) | [Evidence](curriculum/02-networking/08-load-balancing.md#make-it-concrete) | Requests must be distributed across healthy instances without losing state or overwhelming shared dependencies. [Applied evidence](curriculum/02-networking/08-load-balancing.md#apply-and-improve) | [load-balancer](animations/load-balancer.md) |
| 02-networking: [Clustering](curriculum/02-networking/09-clustering.md) | [Evidence](curriculum/02-networking/09-clustering.md#make-it-concrete) | Several machines must divide work or coordinate state and safely recover unfinished work. [Applied evidence](curriculum/02-networking/09-clustering.md#apply-and-improve) | [load-balancer](animations/load-balancer.md) |
| 03-databases: [Storage](curriculum/03-databases/01-storage.md) | [Evidence](curriculum/03-databases/01-storage.md#make-it-concrete) | Large file bytes and searchable application metadata need suitable interfaces and coordinated lifecycle handling. [Applied evidence](curriculum/03-databases/01-storage.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [Databases and DBMS](curriculum/03-databases/02-databases-and-dbms.md) | [Evidence](curriculum/03-databases/02-databases-and-dbms.md#make-it-concrete) | An application needs correct, persistent, concurrent access to related facts rather than ad hoc storage and unrestricted scans. [Applied evidence](curriculum/03-databases/02-databases-and-dbms.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [SQL databases](curriculum/03-databases/03-sql-databases.md) | [Evidence](curriculum/03-databases/03-sql-databases.md#make-it-concrete) | Related orders, customers, and items need explicit identities, integrity constraints, and coordinated changes. [Applied evidence](curriculum/03-databases/03-sql-databases.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [NoSQL databases](curriculum/03-databases/04-nosql-databases.md) | [Evidence](curriculum/03-databases/04-nosql-databases.md#make-it-concrete) | Different access patterns may fit document, key-value, graph, or other models better than one assumed universal schema. [Applied evidence](curriculum/03-databases/04-nosql-databases.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md) | [Evidence](curriculum/03-databases/05-sql-vs-nosql-databases.md#make-it-concrete) | Choosing by database category alone ignores required operations and operational cost. [Applied evidence](curriculum/03-databases/05-sql-vs-nosql-databases.md#apply-and-improve) | Static explanation sufficient |
| 03-databases: [Indexes](curriculum/03-databases/06-indexes.md) | [Evidence](curriculum/03-databases/06-indexes.md#make-it-concrete) | Finding a small relevant subset should not require scanning every unrelated database row. [Applied evidence](curriculum/03-databases/06-indexes.md#apply-and-improve) | [index-lookup](animations/index-lookup.md) |
| 03-databases: [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md) | [Evidence](curriculum/03-databases/07-normalization-and-denormalization.md#clarify-the-key-definitions) | Duplicated values can become inconsistent, while meaningful historical snapshots must not be overwritten as if they were current facts. [Applied evidence](curriculum/03-databases/07-normalization-and-denormalization.md#apply-and-improve) | [normalization](animations/normalization.md) |
| 03-databases: [Transactions](curriculum/03-databases/08-transactions.md) | [Evidence](curriculum/03-databases/08-transactions.md#make-it-concrete) | Concurrent buyers may both believe they reserved the same final unit. [Applied evidence](curriculum/03-databases/08-transactions.md#make-it-concrete) | [atomic-stock](animations/atomic-stock.md) |
| 03-databases: [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md) | [Evidence](curriculum/03-databases/09-acid-and-base-consistency-models.md#make-it-concrete) | The word consistency can incorrectly conflate local invariant preservation with visibility across replicas. [Applied evidence](curriculum/03-databases/09-acid-and-base-consistency-models.md#apply-and-improve) | [atomic-stock](animations/atomic-stock.md) |
| 03-databases: [Database Replication](curriculum/03-databases/10-database-replication.md) | [Evidence](curriculum/03-databases/10-database-replication.md#make-it-concrete) | Copies support read capacity or recovery but can lag, and copying the same mistake does not preserve historical recovery points. [Applied evidence](curriculum/03-databases/10-database-replication.md#make-it-concrete) | [replication](animations/replication.md) |
| 03-databases: [Sharding](curriculum/03-databases/11-sharding.md) | [Evidence](curriculum/03-databases/11-sharding.md#make-it-concrete) | A growing dataset or workload needs distribution without confusing copied data with divided ownership. [Applied evidence](curriculum/03-databases/11-sharding.md#apply-and-improve) | [sharding](animations/sharding.md) |
| 03-databases: [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md) | [Evidence](curriculum/03-databases/12-consistent-hashing.md#make-it-concrete) | Naive modulo-based key placement can move many keys when the number of nodes changes. [Applied evidence](curriculum/03-databases/12-consistent-hashing.md#apply-and-improve) | [consistent-hash](animations/consistent-hash.md) |
| 03-databases: [Database Federation](curriculum/03-databases/13-database-federation.md) | [Evidence](curriculum/03-databases/13-database-federation.md#make-it-concrete) | Business domains may need separate ownership or scaling without mistaking functional boundaries for key ranges. [Applied evidence](curriculum/03-databases/13-database-federation.md#make-it-concrete) | [sharding](animations/sharding.md) |
| 03-databases: [Bloom Filters](curriculum/03-databases/14-bloom-filters.md) | [Evidence](curriculum/03-databases/14-bloom-filters.md#a-small-filter-before-an-expensive-lookup) | Many absent-key queries waste expensive authoritative lookups. [Applied evidence](curriculum/03-databases/14-bloom-filters.md#how-to-tune-it) | [bloom-filter](animations/bloom-filter.md) |
| 04-distributed-data: [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md) | [Evidence](curriculum/04-distributed-data/01-cap-theorem.md#make-it-concrete) | A network partition prevents replicas coordinating while a client still expects a valid result. [Applied evidence](curriculum/04-distributed-data/01-cap-theorem.md#make-it-concrete) | [cap-partition](animations/cap-partition.md) |
| 04-distributed-data: [PACELC Theorem](curriculum/04-distributed-data/02-pacelc-theorem.md) | [Evidence](curriculum/04-distributed-data/02-pacelc-theorem.md#make-it-concrete) | CAP alone does not describe the latency-versus-consistency decision during normal network operation. [Applied evidence](curriculum/04-distributed-data/02-pacelc-theorem.md#make-it-concrete) | [pacelc](animations/pacelc.md) |
| 04-distributed-data: [Distributed Transactions](curriculum/04-distributed-data/03-distributed-transactions.md) | [Evidence](curriculum/04-distributed-data/03-distributed-transactions.md#distributed-transactions) | An order and an external payment can reach different committed states after a partial failure. [Applied evidence](curriculum/04-distributed-data/03-distributed-transactions.md#apply-and-improve) | [saga](animations/saga.md) |
| 05-caching: [Caching](curriculum/05-caching/01-caching.md) | [Evidence](curriculum/05-caching/01-caching.md#caching) | Repeated product reads unnecessarily hit slower authoritative storage, but cached copies can become stale. [Applied evidence](curriculum/05-caching/01-caching.md#apply-and-improve) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Caching Strategies](curriculum/05-caching/02-caching-strategies.md) | [Evidence](curriculum/05-caching/02-caching-strategies.md#decide-who-reads-and-who-updates-the-copy) | The design must assign ownership of cache loading and writes without silently losing freshness or durability guarantees. [Applied evidence](curriculum/05-caching/02-caching-strategies.md#work-through-a-price-update) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Cache Eviction Policies](curriculum/05-caching/03-cache-eviction-policies.md) | [Evidence](curriculum/05-caching/03-cache-eviction-policies.md#what-leaves-when-the-cache-is-full) | When the working set exceeds cache capacity, the system must choose which reusable values to remove. [Applied evidence](curriculum/05-caching/03-cache-eviction-policies.md#walk-through-a-small-cache) | [cache-eviction](animations/cache-eviction.md) |
| 05-caching: [Distributed Caching](curriculum/05-caching/04-distributed-caching.md) | [Evidence](curriculum/05-caching/04-distributed-caching.md#sharing-a-fast-copy-across-servers) | Many application instances duplicate expensive reads and can stampede the origin when a shared hot key expires. [Applied evidence](curriculum/05-caching/04-distributed-caching.md#work-through-a-hot-key-failure) | [cache-aside](animations/cache-aside.md) |
| 05-caching: [Content Delivery Network (CDN)](curriculum/05-caching/05-content-delivery-network-cdn.md) | [Evidence](curriculum/05-caching/05-content-delivery-network-cdn.md#content-delivery-network-cdn) | Serving every static asset from one origin creates repeated long-distance transfers and origin load. [Applied evidence](curriculum/05-caching/05-content-delivery-network-cdn.md#apply-and-improve) | [cdn-edge](animations/cdn-edge.md) |
| 06-api-fundamentals: [APIs](curriculum/06-api-fundamentals/01-apis.md) | [Evidence](curriculum/06-api-fundamentals/01-apis.md#a-contract-between-two-parts-of-a-system) | Independent clients need stable, unambiguous behavior without depending on internal implementation details. [Applied evidence](curriculum/06-api-fundamentals/01-apis.md#work-through-an-order-request) | Static explanation sufficient |
| 06-api-fundamentals: [REST, GraphQL, gRPC](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) | [Evidence](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md#use-a-concrete-client-requirement) | The interface must fit the clients, data shapes, and communication pattern without hiding inefficient backend work. [Applied evidence](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md#apply-and-improve-it) | Static explanation sufficient |
| 06-api-fundamentals: [API Gateway](curriculum/06-api-fundamentals/03-api-gateway.md) | [Evidence](curriculum/06-api-fundamentals/03-api-gateway.md#api-gateway) | Clients otherwise must discover and coordinate multiple backend services and shared entry-point concerns themselves. [Applied evidence](curriculum/06-api-fundamentals/03-api-gateway.md#apply-it-carefully) | Static explanation sufficient |
| 06-api-fundamentals: [Idempotency](curriculum/06-api-fundamentals/04-idempotency.md) | [Evidence](curriculum/06-api-fundamentals/04-idempotency.md#idempotency) | A retried payment after a lost response must not create an extra charge or skip a charge that never happened. [Applied evidence](curriculum/06-api-fundamentals/04-idempotency.md#apply-it-safely) | [idempotency](animations/idempotency.md) |
| 06-api-fundamentals: [Rate Limiting](curriculum/06-api-fundamentals/05-rate-limiting.md) | [Evidence](curriculum/06-api-fundamentals/05-rate-limiting.md#rate-limiting) | One customer or an aggregate traffic burst can overload shared search capacity or unfairly consume it. [Applied evidence](curriculum/06-api-fundamentals/05-rate-limiting.md#choose-what-you-are-protecting) | [token-bucket](animations/token-bucket.md) |
| 06-api-fundamentals: [Long polling, WebSockets, Server-Sent Events (SSE)](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) | [Evidence](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md#match-the-direction-of-communication) | Clients need timely updates, sometimes bidirectional, without losing all progress when a connection drops. [Applied evidence](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md#apply-and-improve-it) | [realtime-protocols](animations/realtime-protocols.md) |
| 06-api-fundamentals: [Webhooks](curriculum/06-api-fundamentals/07-webhooks.md) | [Evidence](curriculum/06-api-fundamentals/07-webhooks.md#let-another-system-call-you-when-something-happens) | A service needs provider events without constant polling, while tolerating duplicate, delayed, or reordered delivery. [Applied evidence](curriculum/06-api-fundamentals/07-webhooks.md#work-through-a-duplicate-delivery) | [idempotency](animations/idempotency.md) |
| 06-api-fundamentals: [API Design](curriculum/06-api-fundamentals/08-api-design.md) | [Evidence](curriculum/06-api-fundamentals/08-api-design.md#make-the-contract-predictable) | Unbounded lists, ambiguous results, incompatible changes, and unsafe retries prevent clients completing tasks predictably. [Applied evidence](curriculum/06-api-fundamentals/08-api-design.md#work-through-a-list-endpoint) | Static explanation sufficient |
| 07-asynchronous-communication: [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md) | [Evidence](curriculum/07-asynchronous-communication/01-message-brokers.md#a-real-integration-boundary) | Producers and consumers should exchange work/events without requiring each receiver to be synchronously active or directly addressed. [Applied evidence](curriculum/07-asynchronous-communication/01-message-brokers.md#apply-it) | [work-queue](animations/work-queue.md) |
| 07-asynchronous-communication: [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md) | [Evidence](curriculum/07-asynchronous-communication/02-message-queues.md#message-queues) | Bursts of thumbnail work should not hold upload requests open or overwhelm downstream processing; redeliveries must be safe. [Applied evidence](curriculum/07-asynchronous-communication/02-message-queues.md#apply-and-improve-it) | [work-queue](animations/work-queue.md) |
| 07-asynchronous-communication: [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md) | [Evidence](curriculum/07-asynchronous-communication/03-publish-subscribe.md#one-event-several-independent-reactions) | Several independent business reactions must each receive an event without being treated as competing workers for one job. [Applied evidence](curriculum/07-asynchronous-communication/03-publish-subscribe.md#apply-it) | [pub-sub](animations/pub-sub.md) |
| 07-asynchronous-communication: [Change Data Capture (CDC)](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md) | [Evidence](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md#turn-database-changes-into-downstream-updates) | A derived search index needs committed database changes without repeatedly scanning the entire source or independently double-writing each request. [Applied evidence](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md#follow-one-changed-price) | [cdc](animations/cdc.md) |
| 08-architectural-patterns: [N-tier architecture](curriculum/08-architectural-patterns/01-n-tier-architecture.md) | [Evidence](curriculum/08-architectural-patterns/01-n-tier-architecture.md#separate-responsibilities-and-deployment) | Separates presentation, business rules, and persistence so each responsibility has an explicit deployment and scaling boundary. [Applied evidence](curriculum/08-architectural-patterns/01-n-tier-architecture.md#apply-it) | Static explanation sufficient |
| 08-architectural-patterns: [Monoliths and Microservices](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md) | [Evidence](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md#start-with-a-boundary-that-solves-a-problem) | Defines capability and data-ownership boundaries without treating distributed deployment as an automatic performance improvement. [Applied evidence](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md#improve-the-system-you-have) | Static explanation sufficient |
| 08-architectural-patterns: [Event-Driven Architecture (EDA)](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md) | [Evidence](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md#an-action-can-finish-before-its-reactions) | Decouples an initiating business action from downstream reactions that can complete later. [Applied evidence](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md#apply-it) | [pub-sub](animations/pub-sub.md) |
| 08-architectural-patterns: [Event Sourcing](curriculum/08-architectural-patterns/04-event-sourcing.md) | [Evidence](curriculum/08-architectural-patterns/04-event-sourcing.md#rebuild-state-from-business-history) | Preserves authoritative business history so current state and derived views can be reconstructed. [Applied evidence](curriculum/08-architectural-patterns/04-event-sourcing.md#rebuild-state-from-business-history) | [event-sourcing](animations/event-sourcing.md) |
| 08-architectural-patterns: [Command and Query Responsibility Segregation (CQRS)](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md) | [Evidence](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md#different-models-for-changing-and-reading) | Allows write rules and read queries to use models shaped for their different responsibilities. [Applied evidence](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md#apply-it) | [cqrs](animations/cqrs.md) |
| 08-architectural-patterns: [Enterprise Service Bus (ESB)](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md) | [Evidence](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md#integrate-unlike-systems) | Integrates systems with incompatible message formats and routing requirements. [Applied evidence](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md#integrate-unlike-systems) | Static explanation sufficient |
| 08-architectural-patterns: [Virtual Machines (VMs) and Containers](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md) | [Evidence](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md#choose-the-boundary-you-need) | Chooses packaging, resource control, and operating-system isolation boundaries for workloads. [Applied evidence](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md#apply-and-improve-it) | Static explanation sufficient |
| 08-architectural-patterns: [Serverless Architecture](curriculum/08-architectural-patterns/08-serverless-architecture.md) | [Evidence](curriculum/08-architectural-patterns/08-serverless-architecture.md#let-a-platform-manage-more-of-the-runtime) | Offloads parts of runtime provisioning and operation for suitable request- or event-triggered work. [Applied evidence](curriculum/08-architectural-patterns/08-serverless-architecture.md#work-through-thumbnail-generation) | Static explanation sufficient |
| 08-architectural-patterns: [Peer-to-Peer (P2P) Architecture](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md) | [Evidence](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md#participants-can-provide-as-well-as-consume) | Distributes content-serving work among participants instead of making one origin serve every byte. [Applied evidence](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md#work-through-file-distribution) | [p2p-pieces](animations/p2p-pieces.md) |
| 09-reliability-and-microservices: [Service Discovery](curriculum/09-reliability-and-microservices/01-service-discovery.md) | [Evidence](curriculum/09-reliability-and-microservices/01-service-discovery.md#find-changing-service-instances) | Finds service instance addresses that change during deployment or failure. [Applied evidence](curriculum/09-reliability-and-microservices/01-service-discovery.md#apply-it) | [discovery-heartbeat](animations/discovery-heartbeat.md) |
| 09-reliability-and-microservices: [HeartBeats](curriculum/09-reliability-and-microservices/02-heartbeats.md) | [Evidence](curriculum/09-reliability-and-microservices/02-heartbeats.md#a-signal-that-a-participant-was-recently-reachable) | Provides recent reachability evidence to support failure suspicion, not proof of end-to-end health. [Applied evidence](curriculum/09-reliability-and-microservices/02-heartbeats.md#work-through-a-timeout) | [discovery-heartbeat](animations/discovery-heartbeat.md) |
| 09-reliability-and-microservices: [Circuit breaker](curriculum/09-reliability-and-microservices/03-circuit-breaker.md) | [Evidence](curriculum/09-reliability-and-microservices/03-circuit-breaker.md#stop-repeating-a-failing-dependency-call) | Stops repeated calls to a failing dependency from consuming resources and spreading failure. [Applied evidence](curriculum/09-reliability-and-microservices/03-circuit-breaker.md#stop-repeating-a-failing-dependency-call) | [circuit-breaker](animations/circuit-breaker.md) |
| 09-reliability-and-microservices: [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md) | [Evidence](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#turn-a-promise-into-a-measurement) | Connects a user-facing service promise to a measurable target and observed performance. [Applied evidence](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md#turn-a-promise-into-a-measurement) | Static explanation sufficient |
| 09-reliability-and-microservices: [Disaster recovery](curriculum/09-reliability-and-microservices/05-disaster-recovery.md) | [Evidence](curriculum/09-reliability-and-microservices/05-disaster-recovery.md#test-recovery-not-just-backup-creation) | Defines tolerable data loss and time to recover usable service after a serious disruption. [Applied evidence](curriculum/09-reliability-and-microservices/05-disaster-recovery.md#test-recovery-not-just-backup-creation) | [recovery-objectives](animations/recovery-objectives.md) |
| 09-reliability-and-microservices: [Consensus Algorithms](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md) | [Evidence](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md#agreeing-on-decisions-despite-some-failures) | Maintains an agreed ordered decision history among replicas under a specified failure model. [Applied evidence](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md#follow-a-simple-replicated-log-write) | [raft-majority](animations/raft-majority.md) |
| 09-reliability-and-microservices: [Distributed Locking](curriculum/09-reliability-and-microservices/07-distributed-locking.md) | [Evidence](curriculum/09-reliability-and-microservices/07-distributed-locking.md#coordinate-work-across-processes-carefully) | Coordinates exclusive work across processes while accounting for expiry and stale owners. [Applied evidence](curriculum/09-reliability-and-microservices/07-distributed-locking.md#work-through-a-stale-owner) | [fencing-token](animations/fencing-token.md) |
| 09-reliability-and-microservices: [Gossip Protocol](curriculum/09-reliability-and-microservices/08-gossip-protocol.md) | [Evidence](curriculum/09-reliability-and-microservices/08-gossip-protocol.md#spread-information-through-repeated-peer-exchanges) | Spreads membership or health observations without every update requiring one sender to contact all nodes directly. [Applied evidence](curriculum/09-reliability-and-microservices/08-gossip-protocol.md#follow-an-update) | [gossip-spread](animations/gossip-spread.md) |
| 09-reliability-and-microservices: [Distributed Tracing](curriculum/09-reliability-and-microservices/09-distributed-tracing.md) | [Evidence](curriculum/09-reliability-and-microservices/09-distributed-tracing.md#follow-one-request-across-several-services) | Connects request work across service boundaries to locate slow or failing dependencies. [Applied evidence](curriculum/09-reliability-and-microservices/09-distributed-tracing.md#work-through-a-slow-order-page) | [request-latency](animations/request-latency.md) |
| 10-security-and-location: [SSL, TLS, mTLS](curriculum/10-security-and-location/01-ssl-tls-mtls.md) | [Evidence](curriculum/10-security-and-location/01-ssl-tls-mtls.md#protect-a-connection-and-verify-identities) | Protects connection data and establishes endpoint identity while keeping authorization separate. [Applied evidence](curriculum/10-security-and-location/01-ssl-tls-mtls.md#protect-a-connection-and-verify-identities) | [tls-mtls](animations/tls-mtls.md) |
| 10-security-and-location: [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md) | [Evidence](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#separate-delegated-permission-from-login-identity) | Separates delegated access to protected resources from a client receiving authenticated login identity. [Applied evidence](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md#apply-it) | [oauth-oidc](animations/oauth-oidc.md) |
| 10-security-and-location: [Single Sign-On (SSO)](curriculum/10-security-and-location/03-single-sign-on-sso.md) | [Evidence](curriculum/10-security-and-location/03-single-sign-on-sso.md#one-sign-in-several-application-sessions) | Lets multiple applications share an identity-provider sign-in while retaining application-specific permissions and session policies. [Applied evidence](curriculum/10-security-and-location/03-single-sign-on-sso.md#apply-it-across-an-organization) | [single-sign-on](animations/single-sign-on.md) |
| 10-security-and-location: [Geohashing and Quadtrees](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md) | [Evidence](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md#find-nearby-candidates-before-calculating-exact-distance) | Narrows spatial search candidates so nearby-driver queries avoid a distance calculation against every driver. [Applied evidence](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md#apply-and-improve-it) | [nearby-search](animations/nearby-search.md) |

## Topic-by-topic findings

### What is system design?

- **Fundamental:** “First specify correct charging, acceptable response time, and failure behavior.”
- **Problem solved:** Choosing components before knowing the behavior and failure guarantees the system must provide.
- **System-design scenario:** A food-ordering app connecting customer orders, payment, and restaurant acceptance.
- **How it is applied:** Trace order → payment → restaurant. → Specify charging correctness, response time, and failure behavior. → Choose components for those requirements and handle an uncertain payment without duplicating a charge.
- **Decision / tradeoff:** Prioritize the required correctness behavior before adding faster servers.
- **Application evidence:** “Design a food-ordering app by tracing order → payment → restaurant.”
- **Visual decision:** Requirements-to-component mapping is clear in the short scenario; a static request flow is sufficient.

### Scalability

- **Fundamental:** “Checkout handles 100 requests/second. Scale up with a larger server; scale out with extra servers.”
- **Problem solved:** A rising request rate exceeds the capacity of a particular stage.
- **System-design scenario:** A checkout serving 100 requests per second grows beyond its current capacity.
- **How it is applied:** Measure CPU, database work, and waiting time. → Locate the actual saturated stage. → Scale that stage vertically or horizontally and reassess the shared database.
- **Decision / tradeoff:** Extra application instances cannot solve an overloaded shared database; vertical and horizontal capacity have different limits.
- **Application evidence:** “Measure CPU, database load, and waiting. Expand the bottleneck. Scaling alone does not determine data consistency.”
- **Visual decision:** The vertical-versus-horizontal distinction and bottleneck warning are explicit; a static before/after capacity sketch suffices.

### Availability

- **Fundamental:** “Two checkout servers can help if traffic automatically switches away from a failed one.”
- **Problem solved:** Users lose access when a server or shared dependency fails.
- **System-design scenario:** Two checkout instances must continue serving after one fails, while a payment outage may still prevent checkout.
- **How it is applied:** Trace the whole request and identify shared dependencies. → Provide health checks, replacement capacity, and tested failover where they remove a real failure point. → Measure successful requests and their latency, and test what can remain available during dependency failure.
- **Decision / tradeoff:** Redundancy costs capacity and only protects the failure domains it actually separates; degraded browsing is different from successful checkout.
- **Application evidence:** “Add health checks, replacement capacity, and tested failover where they remove a real failure point.”
- **Visual decision:** Failover has a temporal sequence: failure, detection, routing change, and surviving-instance load. Playback prevents equating two boxes with instant availability.

### Latency vs Throughput vs Bandwidth

- **Fundamental:** “Concurrency is how many operations are in progress. It is not the same as completed operations per second.”
- **Problem solved:** Optimizing the wrong performance quantity or interpreting averages and network capacity as interchangeable.
- **System-design scenario:** A 200 ms request contains 30 ms network, 70 ms application, and 100 ms database work; an index cuts the query to 25 ms.
- **How it is applied:** State the operation, measurement boundary, and units. → Measure the critical path and identify the dominant stage. → Compare an optimization under equivalent load using latency percentiles, throughput, queueing, and errors.
- **Decision / tradeoff:** More concurrency can increase queueing rather than completions; larger bandwidth may not reduce query-dominated response time.
- **Application evidence:** “Begin with a trace or timing breakdown, form one hypothesis, and compare before and after at a similar workload.”
- **Visual decision:** Show arrivals, queue length, active requests, completions, and transfer capacity over time to separate latency, throughput, concurrency, and bandwidth.

### Reliability

- **Fundamental:** “A reliable service keeps doing its intended job correctly over time, including when expected problems happen.”
- **Problem solved:** A partially completed operation can leave users with duplicate charges, lost state, or a permanently unresolved order.
- **System-design scenario:** Payment succeeds but an order worker crashes before recording the result.
- **How it is applied:** Define the invariant and durable acceptance boundary. → Reuse stable identifiers for retries and resume from durable state. → Reconcile unresolved orders/payments and inject failures after each durable step.
- **Decision / tradeoff:** Retries, replicas, and recovery mechanisms add complexity; use them to protect a defined invariant rather than treating successful HTTP responses as proof.
- **Application evidence:** “A more deliberate flow records a stable operation identifier, makes payment retries reuse it, and resumes the order update from durable state.”
- **Visual decision:** The crash-after-payment/lost-response/retry/reconciliation sequence is stateful; showing state transitions makes the unknown outcome understandable.

### SPOF

- **Fundamental:** “a component whose failure can stop the service you care about.”
- **Problem solved:** Redundant application instances still depend on one component or common failure domain.
- **System-design scenario:** Two app instances share a load balancer and database D; the database fails.
- **How it is applied:** Trace each dependency in the real request path. → Provide a tested replacement, promotion decision, client reconnection, and a rule for which database may accept writes. → Fail dependencies and measure detection, switchover, rejected work, and data loss.
- **Decision / tradeoff:** A fallback can suffice for optional recommendations, but not for a required payment confirmation; automatic promotion must avoid conflicting writers.
- **Application evidence:** “A failover plan needs data replication, a promotion decision, a stable address or discovery change, and client reconnection.”
- **Visual decision:** The existing dependency diagram and explicit failover walkthrough establish the concept; the Availability animation can cover the shared temporal behavior.

### IP

- **Fundamental:** “In an application, a public-facing gateway can receive internet requests while the database stays on a private network.”
- **Problem solved:** Services need reachable addresses without exposing every dependency to the internet.
- **System-design scenario:** A public shop gateway reaches a privately addressed database; home devices illustrate shared public IPv4 NAT.
- **How it is applied:** Determine which component must be internet-reachable. → Check destination address, route, firewall, and listening port when a connection fails. → Use DNS or discovery for changing instance addresses and restrict permitted connections.
- **Decision / tradeoff:** Private addressing is not access control; a correct address and a permitted/reachable connection are different requirements.
- **Application evidence:** “Use DNS or service discovery instead of hard-coding an instance address that may change.”
- **Visual decision:** A labeled public/private network diagram adequately explains placement and NAT; the lesson does not require a packet-timing simulation.

### OSI Model

- **Fundamental:** “The OSI model gives names to these different responsibilities; real implementations do not always fit perfectly into seven separate boxes.”
- **Problem solved:** A vague network failure leads to changing unrelated parts of the system.
- **System-design scenario:** A browser cannot load a product page because routing, TCP, TLS, or the application may fail independently.
- **How it is applied:** Separate reaching the IP, opening transport, securing the connection, and sending the application request. → Inspect the layer-specific evidence: routing, listeners/filtering, certificate verification, or HTTP errors. → Optimize the stage actually measured rather than treating all delay as one network problem.
- **Decision / tradeoff:** The model is a troubleshooting vocabulary, not a requirement that every implementation contain seven isolated boxes.
- **Application evidence:** “If a TCP connection cannot open, inspect ports, listeners, and filtering.”
- **Visual decision:** A static layer-to-symptom mapping is clearer than decorative packet movement for this troubleshooting purpose.

### TCP and UDP

- **Fundamental:** “TCP supplies an ordered byte stream with loss recovery; UDP leaves delivery and ordering to higher layers.”
- **Problem solved:** Applications differ in whether ordered delivery, loss recovery, and timely delivery are most important.
- **System-design scenario:** Live speech may prefer a small gap to a recovered sound packet that arrives too late.
- **How it is applied:** Specify acceptable loss, delay, and ordering. → Measure those properties and reuse connections where appropriate. → For UDP, explicitly design congestion handling, loss tolerance, and message sizing; keep business confirmation at the application level.
- **Decision / tradeoff:** UDP is not automatically faster for the application, and TCP delivery does not establish that a payment committed.
- **Application evidence:** “With UDP, explicitly design congestion handling, loss tolerance, and message sizing; “no retransmission” is not automatically faster for the application.”
- **Visual decision:** Packet loss, reordering, retransmission, and a live-playout deadline are temporal distinctions that static protocol labels can obscure.

### Domain Name System (DNS)

- **Fundamental:** “DNS finds an address; it does not carry the web page.”
- **Problem solved:** Clients need to resolve service names, while cached answers can temporarily outlive a destination change.
- **System-design scenario:** A shop moves from server A to B while different resolvers retain answers with different remaining TTLs.
- **How it is applied:** Trace browser, resolver, cached/authoritative answer, and subsequent server connection. → Lower TTL ahead of a planned move and allow the old TTL to expire before relying on shorter caching. → Keep the old destination available during transition where possible and inspect actual answers/TTLs when debugging.
- **Decision / tradeoff:** Shorter TTLs can reduce cache persistence but increase lookup traffic and do not move existing open connections instantly.
- **Application evidence:** “For a planned move, lower the TTL ahead of time and allow the previous TTL to elapse before relying on shorter caching.”
- **Visual decision:** Two clients retaining different cached answers through a TTL countdown makes propagation and the separation from connection lifetime concrete.

### Proxy

- **Fundamental:** “A school proxy acts for students making outgoing requests. A shop's reverse proxy acts for its servers receiving requests.”
- **Problem solved:** A system needs a controlled entry or exit point for routing and common request handling.
- **System-design scenario:** A shop reverse proxy routes /orders to order servers, terminates TLS, and enforces request limits.
- **How it is applied:** Identify whether the intermediary represents clients or servers. → Measure proxy queueing, connection counts, and request duration. → Set size/time limits, reuse connections where appropriate, and trust forwarded identity information only through a controlled chain.
- **Decision / tradeoff:** An intermediary centralizes useful behavior but can become a bottleneck or failure point; business authorization remains with the service.
- **Application evidence:** “Measure request duration, connection count, and queueing at the proxy before adding application servers.”
- **Visual decision:** The forward/reverse distinction is directional and well served by a static diagram labeling whose requests each proxy represents.

### HTTP/HTTPS

- **Fundamental:** “A request includes a method, path, headers, and sometimes a body.”
- **Problem solved:** Clients and servers need a request/response contract and protected transport without confusing a network result with a business outcome.
- **System-design scenario:** A first product-page visit resolves a name, establishes a connection and TLS, and downloads a response; an order write may commit before its response is lost.
- **How it is applied:** Separate resolution, connection setup, TLS, response start, and body transfer. → Reuse connections, reduce unnecessary redirects/round trips, and safely cache or compress suitable content. → Compare connection and body timing, errors, and percentiles under equivalent load while preserving authorization and retry safety.
- **Decision / tradeoff:** Batching reduces round trips but may enlarge payloads; HTTPS protects transport, not database storage or per-order ownership.
- **Application evidence:** “Reuse connections where supported instead of paying setup costs for every call.”
- **Visual decision:** Showing the first-connection lifecycle versus connection reuse and a lost response reveals timing and business-outcome distinctions.

### Checksums

- **Fundamental:** “A checksum is a value calculated from data. The receiver can calculate it again and compare the result with the expected value.”
- **Problem solved:** A transferred, stored, or assembled file may differ from its expected bytes.
- **System-design scenario:** A 1 GB archive arrives in ten chunks; per-chunk digests detect damaged pieces and a full-file digest checks final assembly.
- **How it is applied:** Choose integrity checks for accidental corruption versus deliberate replacement. → Verify chunks and the assembled file using trustworthy expected metadata. → Calculate incrementally while streaming, tune chunk sizes, and test byte changes, missing/reordered chunks, and untrusted expected values.
- **Decision / tradeoff:** Verification detects disagreement but does not repair data or establish authenticity when the expected digest is also untrusted.
- **Application evidence:** “Calculate a digest incrementally while streaming bytes rather than loading the whole file into memory.”
- **Visual decision:** A static chunk/digest/assembly example exposes the relevant distinction without requiring temporal animation.

### Load Balancing

- **Fundamental:** “Adding B spreads application work but does not double database capacity.”
- **Problem solved:** Requests must be distributed across healthy instances without losing state or overwhelming shared dependencies.
- **System-design scenario:** Checkout requests move between app A and B behind a load balancer while both share a database.
- **How it is applied:** Choose a routing policy for actual request/connection behavior and use readiness checks. → Stop new traffic and drain active work when removing instances, with spare capacity for failure. → Choose shared or suitable stateless session handling and measure per-instance latency, errors, and distribution.
- **Decision / tradeoff:** Sticky routing can reduce session movement but does not make instance memory durable; more app capacity may only shift the bottleneck.
- **Application evidence:** “When removing an instance, stop new requests and allow active work to finish.”
- **Visual decision:** Instance failure, readiness changes, active-request draining, and a session moving to another instance are state transitions that benefit from playback.

### Clustering

- **Fundamental:** “Putting machines behind a load balancer does not itself define coordination, replication, or recovery.”
- **Problem solved:** Several machines must divide work or coordinate state and safely recover unfinished work.
- **System-design scenario:** Three workers resize photos while sharing a queue and storage; a database cluster instead coordinates data changes.
- **How it is applied:** Specify assignment, failure detection, and recovery of unfinished tasks. → Make retried work safe and leave capacity for failures. → Measure completed work, coordination overhead, shared bottlenecks, and recovery time before adding nodes.
- **Decision / tradeoff:** More nodes can improve throughput but add communication and coordination; independent jobs and shared-data decisions have different requirements.
- **Application evidence:** “State how work is assigned, how failed members are detected, and whether unfinished work can be reassigned safely.”
- **Visual decision:** The distinction between independent workers and coordinated data is explicit; queue redelivery/failover animations elsewhere can illustrate the shared temporal mechanics.

### Storage

- **Fundamental:** “Block storage exposes blocks for an operating system or database to manage. File storage exposes files and directories.”
- **Problem solved:** Large file bytes and searchable application metadata need suitable interfaces and coordinated lifecycle handling.
- **System-design scenario:** A photo's bytes live in object storage while a database stores its key, owner, size, and upload status.
- **How it is applied:** Specify object size, read/write patterns, durability, and retrieval delay. → Choose block, file, or object interfaces for those operations and use authorized direct/CDN delivery when appropriate. → Define visibility, cleanup/reconciliation, and backups for failures between object and metadata writes.
- **Decision / tradeoff:** Direct object delivery can reduce application load; separate stores add partial-write and recovery coordination.
- **Application evidence:** “If writing the object succeeds but recording its database row fails, cleanup or reconciliation must handle the orphaned object.”
- **Visual decision:** A static byte-storage versus metadata flow and explicit partial-failure walkthrough cover the concept without additional animation.

### Databases and DBMS

- **Fundamental:** “The database stores the facts; the DBMS manages querying, concurrency, persistence, and the rules it supports.”
- **Problem solved:** An application needs correct, persistent, concurrent access to related facts rather than ad hoc storage and unrestricted scans.
- **System-design scenario:** A shop finds orders by customer, updates statuses, and prevents invalid customer/order relationships.
- **How it is applied:** List lookups, lists, updates, and reports before selecting a database. → Specify required freshness for each operation. → Inspect query/access patterns and determine whether disk, locks, CPU, or connections are the actual bottleneck.
- **Decision / tradeoff:** Indexes and bounded reads can avoid unnecessary scale-out, but different access and consistency needs require different choices.
- **Application evidence:** “Appropriate indexes, bounded result sets, and fewer unnecessary round trips can help before adding machines.”
- **Visual decision:** The database/DBMS roles and workload checklist are conceptual and adequately expressed with the existing text.

### SQL databases

- **Fundamental:** “Keys identify rows; constraints can reject invalid relationships or duplicate identifiers. Transactions can group changes that must succeed together.”
- **Problem solved:** Related orders, customers, and items need explicit identities, integrity constraints, and coordinated changes.
- **System-design scenario:** A shop retrieves a customer's newest orders from related relational tables.
- **How it is applied:** Model relationships with keys and the necessary constraints. → Write important queries and inspect candidate filter/sort indexes using a query plan. → Retrieve bounded results, keep transactions short, and use parameterized inputs.
- **Decision / tradeoff:** Relational structure helps express integrity but does not automatically make every query efficient; indexes add maintenance work.
- **Application evidence:** “For “this customer's newest orders,” consider an index matching the filter and sort, then inspect the query plan.”
- **Visual decision:** Tables, keys, and the example query are understandable with static relationships; transaction concurrency is handled by its dedicated animation.

### NoSQL databases

- **Fundamental:** “A graph database might explore relationships. These are different models within the broad NoSQL label.”
- **Problem solved:** Different access patterns may fit document, key-value, graph, or other models better than one assumed universal schema.
- **System-design scenario:** Flexible product attributes use documents; sessions use identifier-based key lookup; relationship exploration uses a graph model.
- **How it is applied:** Sketch actual reads and writes before choosing a model. → Check query/index support and the cost of relationship-heavy queries. → Choose traffic-aware partition keys and verify the specific product’s transaction scope, consistency, and limits.
- **Decision / tradeoff:** A convenient representation can make other queries expensive; NoSQL does not imply no schema, no transactions, or unlimited scale.
- **Application evidence:** “Choose partition keys that spread real traffic, not merely record counts.”
- **Visual decision:** A model/access-pattern comparison is a static decision; animated objects would not clarify a necessary time-dependent distinction.

### SQL vs NoSQL databases

- **Fundamental:** “SQL columns can be nullable; NoSQL includes structured graph and key-value models, not only document collections.”
- **Problem solved:** Choosing by database category alone ignores required operations and operational cost.
- **System-design scenario:** Compare creating orders, listing recent orders, updating stock, and representing flexible catalog attributes.
- **How it is applied:** Express the workload and invariants. → Compare representations, guarantees, and measured reads/writes for candidate products. → Account for backups, monitoring, and cross-store coordination before adding a second database type.
- **Decision / tradeoff:** Combining stores can fit different workloads but increases consistency and operational work.
- **Application evidence:** “Write a small workload: create an order, list recent orders, and update stock.”
- **Visual decision:** The comparison is best represented as a requirements/workload decision table, not a temporal animation.

### Indexes

- **Fundamental:** “A book index narrows where you look; it does not replace the pages.”
- **Problem solved:** Finding a small relevant subset should not require scanning every unrelated database row.
- **System-design scenario:** Find one customer’s recent orders using a filter on customer_id and a descending created_at sort.
- **How it is applied:** Match a candidate index to the filter and sort. → Inspect rows examined versus returned and compare query plans/timings on representative data. → Account for storage and write maintenance; check real use before removing an index.
- **Decision / tradeoff:** Indexes can speed reads while consuming space and making writes more expensive; one index does not optimize every query.
- **Application evidence:** “Compare its plan and timing before and after adding the candidate index using representative data.”
- **Visual decision:** A stepwise scan versus index lookup, followed by index maintenance on an insert, makes avoided work and write cost visible.

### Normalization and Denormalization

- **Fundamental:** “A candidate key is a minimal superkey; an alternate key is a candidate not chosen as primary.”
- **Problem solved:** Duplicated values can become inconsistent, while meaningful historical snapshots must not be overwritten as if they were current facts.
- **System-design scenario:** A customer changes a profile address after an order was shipped to an address captured at purchase.
- **How it is applied:** Identify minimal candidate keys and whether a non-key attribute depends on only part of a composite key. → Assign ownership and meaning to each fact. → Inspect query/index costs before introducing duplicated fields or a read model. → Define how current-value copies update and when historical snapshots are captured or corrected.
- **Decision / tradeoff:** Denormalized reads can be cheaper but create propagation work; an intentional historical snapshot is a separate business fact.
- **Application evidence:** “For every duplicated current value, decide who updates each copy and what readers may see while updates propagate.”
- **Visual decision:** Updating the current profile while retaining the order’s historical delivery address reveals why two similar fields have different update behavior.

### Transactions

- **Fundamental:** “A transaction boundary alone does not prevent overselling; isolation and the actual statements matter.”
- **Problem solved:** Concurrent buyers may both believe they reserved the same final unit.
- **System-design scenario:** Two buyers read stock = 1 and try to buy the last ticket.
- **How it is applied:** Use an atomic conditional update scoped to product_id and positive quantity. → Check whether a row changed before confirming success, and group related database changes. → Keep transactions short, choose suitable locking/isolation, retry conflicts safely, and handle external payment separately.
- **Decision / tradeoff:** Atomicity boundaries alone do not determine concurrency behavior; stronger isolation or locking can add waiting and retries.
- **Application evidence:** “lets the application check whether a row was changed before confirming success.”
- **Visual decision:** Interleaving two buyers’ reads and writes, then contrasting the conditional-update outcome, directly exposes the race and its prevention.

### ACID and BASE consistency models

- **Fundamental:** “ACID consistency means a transaction preserves declared invariants. Distributed consistency describes what readers observe across copies.”
- **Problem solved:** The word consistency can incorrectly conflate local invariant preservation with visibility across replicas.
- **System-design scenario:** An order commits correctly while a read replica still shows an older list; recommendations and checkout have different freshness requirements.
- **How it is applied:** State the business invariant and acceptable staleness for each operation. → Select coordination and failure behavior required for correctness. → Measure latency/availability cost and verify that update/conflict mechanisms support eventual convergence.
- **Decision / tradeoff:** Use stronger coordination where correctness requires it, while accepting stale data only where the operation allows it.
- **Application evidence:** “Use stronger coordination where correctness requires it, and measure the latency or availability cost.”
- **Visual decision:** A local commit followed by delayed replica visibility distinguishes the two meanings of consistency more clearly than labels alone.

### Database Replication

- **Fundamental:** “Replication copies data; sharding divides its ownership. Neither replaces backups.”
- **Problem solved:** Copies support read capacity or recovery but can lag, and copying the same mistake does not preserve historical recovery points.
- **System-design scenario:** A new address reaches the primary before a replica, so an immediate replica read returns the old value.
- **How it is applied:** Route freshness-sensitive reads to an appropriate authoritative path. → Use replicas for reads that tolerate their lag and monitor that lag. → Test failover and account for selected synchronous acknowledgements, write latency, and separate backups.
- **Decision / tradeoff:** Waiting for replicas can increase write latency; synchronous acknowledgement is not a blanket guarantee that every reader sees identical data.
- **Application evidence:** “Use replicas for reads that tolerate their lag; monitor that lag and test failover.”
- **Visual decision:** Write propagation, read timing, and promotion are temporal; two visible replica states prevent treating replication as instant synchronization.

### Sharding

- **Fundamental:** “A replica of A keeps another copy of A's range; B owns a different range.”
- **Problem solved:** A growing dataset or workload needs distribution without confusing copied data with divided ownership.
- **System-design scenario:** Customers 1–1000 belong to shard A and 1001–2000 to B, with one popular customer producing disproportionate traffic.
- **How it is applied:** Choose a shard key from frequent queries and traffic locality. → Measure request distribution and data sizes, including hot customers. → Plan cross-shard queries, key movement, and growth; check whether query/index improvements solve the immediate problem more simply.
- **Decision / tradeoff:** One-key routing can be efficient while cross-customer queries require fan-out and merging; equal row counts need not balance traffic.
- **Application evidence:** “Choose a shard key from frequent queries and traffic. A customer identifier can keep one customer's orders together.”
- **Visual decision:** Routing requests, showing a hot shard, and moving ownership during growth make partitioning, skew, and replica-versus-shard distinctions tangible.

### Consistent Hashing

- **Fundamental:** “On a consistent-hash ring, adding a node typically changes ownership of only part of the key space.”
- **Problem solved:** Naive modulo-based key placement can move many keys when the number of nodes changes.
- **System-design scenario:** A cache gains or loses a node, and key ownership must change without an unnecessary full remapping.
- **How it is applied:** Use compatible membership and key-to-owner rules across participants. → Plan data availability and client disagreement during membership changes. → Measure movement, misses, and load; use virtual nodes appropriately and limit origin pressure while warming reassigned keys.
- **Decision / tradeoff:** Virtual nodes improve ownership balance but do not remove hot-key traffic; replication and recovery still need separate decisions.
- **Application evidence:** “Warm caches gradually or limit database pressure when reassignment creates misses.”
- **Visual decision:** Animating a ring before/after node addition shows exactly which keys move and contrasts it with modulo remapping.

### Database Federation

- **Fundamental:** “Federation separates by function; sharding divides a dataset by a key.”
- **Problem solved:** Business domains may need separate ownership or scaling without mistaking functional boundaries for key ranges.
- **System-design scenario:** Billing and catalog each own their own database, while cross-domain pages still need combined information.
- **How it is applied:** Assign each fact a domain owner. → Define cross-domain reads and updates. → Avoid repeated latency-sensitive remote joins where a read model fits, and coordinate separate backup/recovery procedures.
- **Decision / tradeoff:** A read model can reduce cross-database read cost but introduces freshness rules; independent stores require operational coordination.
- **Application evidence:** “assign each fact an owner, then define how cross-domain reads and updates work.”
- **Visual decision:** A static billing/catalog ownership diagram and a contrast with customer-ID ranges make this distinction clear.

### Bloom Filters

- **Fundamental:** “A Bloom filter answers a membership question with two possible meanings: **definitely absent**, or **possibly present**.”
- **Problem solved:** Many absent-key queries waste expensive authoritative lookups.
- **System-design scenario:** Of 10,000 lookups, 9,000 keys are absent; a current 1% false-positive filter leaves about 1,090 authoritative lookups.
- **How it is applied:** Use the filter only as a preliminary gate, keeping the real store authoritative. → Choose expected capacity and false-positive tolerance, then size and maintain the filter. → Verify inserts/rebuilds and measure avoided reads, false positives, memory, and update lag.
- **Decision / tradeoff:** More memory and hashing can reduce wasted lookups at a cost; stale filters or clearing shared bits can violate the no-false-negative expectation.
- **Application evidence:** “Choose the expected item count and acceptable false-positive rate before sizing the filter.”
- **Visual decision:** Setting shared bit positions and then querying a different key exposes a false positive; showing a missing insert also clarifies the maintenance condition.

### CAP Theorem

- **Fundamental:** “CAP consistency requires one-copy, real-time behavior, not instantaneous forwarding everywhere.”
- **Problem solved:** A network partition prevents replicas coordinating while a client still expects a valid result.
- **System-design scenario:** Ticket reservations: replica A has confirmed sold while isolated replica B still has available.
- **How it is applied:** State the invariant: do not confirm the same ticket sale twice. → Require an authoritative reservation decision before confirming a sale. → Reject a sale when the partition prevents obtaining that decision; decide separately whether browsing may use older data.
- **Decision / tradeoff:** Preserve the reservation invariant by sacrificing availability for uncoordinated reservation requests during the partition.
- **Application evidence:** “ticket reservations need an authoritative decision preventing duplicate sales.”
- **Visual decision:** Show the link failing, the last successful write, and two different responses to B’s later request; static choose-two labels hide the timing.

### PACELC Theorem

- **Fundamental:** “During a partition, consider availability versus consistency. Else, waiting for distant replicas can trade latency for consistency.”
- **Problem solved:** CAP alone does not describe the latency-versus-consistency decision during normal network operation.
- **System-design scenario:** A global profile service can serve stale regional profiles, while a balance check may require a fresh result.
- **How it is applied:** Define acceptable freshness per operation. → Compare regional stale reads with waiting for cross-region coordination during normal operation. → Measure normal-operation delay and separately specify behavior during a partition.
- **Decision / tradeoff:** Regional reads can reduce waiting but accept staleness; coordinated fresh reads can cost cross-region latency.
- **Application evidence:** “a global profile service may permit stale regional reads; a fresh balance check may wait.”
- **Visual decision:** Contrast the same read with a working slow link and a broken link so the E/L/C branch is not confused with CAP’s partition branch.

### Distributed Transactions

- **Fundamental:** “A distributed transaction is a set of operations on data that is performed across two or more databases.”
- **Problem solved:** An order and an external payment can reach different committed states after a partial failure.
- **System-design scenario:** The payment service charges a customer but the order workflow fails or loses the payment response.
- **How it is applied:** List order and payment steps and their durable state. → Choose coordinated commit or local commits with compensation according to the invariant. → Give repeated commands stable identifiers and define compensation for each partial outcome. → Expose payment pending for uncertain results and reconcile stuck work instead of charging again blindly.
- **Decision / tradeoff:** Coordinated commit increases coupling and waiting; sagas permit intermediate states and require compensating actions rather than erasing every external effect.
- **Application evidence:** “Write the steps, retry behavior, and compensation for each partial outcome before choosing a mechanism.”
- **Visual decision:** The key confusion is temporal: charge succeeds, acknowledgement is lost, then recovery must distinguish failure from an unknown result.

### Caching

- **Fundamental:** “A cache's primary purpose is to increase data retrieval performance by reducing the need to access the underlying slower storage layer.”
- **Problem solved:** Repeated product reads unnecessarily hit slower authoritative storage, but cached copies can become stale.
- **System-design scenario:** A product page cache says ₹450 while the authoritative database price is ₹500.
- **How it is applied:** Choose reusable product data and a key including all result-affecting inputs. → On a miss, read authoritative storage and populate the cache. → Invalidate or refresh cached data after writes and define a TTL/freshness policy. → Recheck the payable price authoritatively for checkout and test cache outage behavior.
- **Decision / tradeoff:** Faster repeated reads and less origin load require extra memory, invalidation logic, and an explicit stale-data policy.
- **Application evidence:** “For checkout, confirm the actual payable price rather than trusting a potentially stale product-page copy.”
- **Visual decision:** Show miss → load → hit → database update → stale hit or invalidation so speed is not mistaken for correctness.

### Caching Strategies

- **Fundamental:** “Read-through and write-through are not opposites: they describe different sides of access and can be combined.”
- **Problem solved:** The design must assign ownership of cache loading and writes without silently losing freshness or durability guarantees.
- **System-design scenario:** A price changes from ₹500 to ₹550 while an older reader is still loading the old value.
- **How it is applied:** Choose who owns miss loading: application for cache-aside or a cache layer for read-through. → Choose synchronous persistence or explicitly bounded write-behind risk. → Trace the slow old reader filling the cache after invalidation. → Use a coordinated/version-aware policy or authoritative read where the required freshness demands it.
- **Decision / tradeoff:** Coordination can improve freshness while consuming latency and complexity; write-behind can shorten acceptance time while introducing unpersisted-write risk.
- **Application evidence:** “A writer commits ₹550 to the database and invalidates the cached entry.”
- **Visual decision:** The invalidation race depends on interleaving an old read, a newer write, invalidation, and the late old fill.

### Cache Eviction Policies

- **Fundamental:** “**Eviction** removes entries to make room. **Expiration** removes entries after an age limit, often a TTL, or time to live.”
- **Problem solved:** When the working set exceeds cache capacity, the system must choose which reusable values to remove.
- **System-design scenario:** Capacity is three equal-sized entries: insert A/B/C, read A, then insert D.
- **How it is applied:** Replay actual accesses against the cache capacity. → For the stated trace, observe LRU removes B while FIFO removes A. → For LFU, define frequency history and tie-breaking before predicting the victim. → Test scans and changing popularity; compare origin requests, latency, and policy bookkeeping cost.
- **Decision / tradeoff:** Recency/frequency tracking can improve useful retention but adds overhead and can predict the wrong reuse pattern; TTL is a separate freshness decision.
- **Application evidence:** “With LRU, B is removed because it was used least recently.”
- **Visual decision:** An animated access trace makes the different victims under LRU and FIFO immediately testable.

### Distributed Caching

- **Fundamental:** “A distributed cache is reached over the network and can be shared across application servers; its data may also be spread across several cache nodes.”
- **Problem solved:** Many application instances duplicate expensive reads and can stampede the origin when a shared hot key expires.
- **System-design scenario:** Two hundred app instances all miss the same popular product entry at once.
- **How it is applied:** Use a shared product key whose tenant and representation inputs are correct. → Coalesce concurrent reloads per key, with a defined failure/lease policy. → Bound cache timeouts and database fallback concurrency. → Measure hot-key traffic and test node loss plus a full cache outage.
- **Decision / tradeoff:** A shared cache increases reuse and pooled capacity but adds a network dependency; adding shards does not spread one hot key’s reload workload automatically.
- **Application evidence:** “A per-key load-coalescing mechanism can let one worker reload while others wait”
- **Visual decision:** Show many simultaneous misses collapsing into one origin load, then contrast the unbounded fallback during an outage.

### Content Delivery Network (CDN)

- **Fundamental:** “A content delivery network (CDN) is a geographically distributed group of servers that work together to provide fast delivery of internet content.”
- **Problem solved:** Serving every static asset from one origin creates repeated long-distance transfers and origin load.
- **System-design scenario:** Many viewers in different regions request the same public product image.
- **How it is applied:** Cache safely shareable static content at edges with explicit keys and cache-control. → Serve a hit at the edge; fetch the origin for a miss. → Publish changed bytes through versioned names or a deliberate invalidation/expiry policy. → Measure edge hits, origin requests, regional latency, and behavior when the origin is down.
- **Decision / tradeoff:** Edge reuse reduces transfer and origin work while introducing distributed stale-copy and access-control decisions.
- **Application evidence:** “Versioned names, such as `logo-v2.png`, let new pages request new content without depending entirely on purging an old cached name.”
- **Visual decision:** The first origin fetch, later edge hit, and content update arriving at different edges are timing-dependent.

### APIs

- **Fundamental:** “An API, or application programming interface, specifies how one program asks another to do something.”
- **Problem solved:** Independent clients need stable, unambiguous behavior without depending on internal implementation details.
- **System-design scenario:** A checkout client submits an order and loses the response after the order is recorded.
- **How it is applied:** Specify required inputs, authentication, validation, and business rejection rules. → Return a stable order identifier and distinguish accepted-for-later from completed. → Define how a retried request identifies the same operation. → Bound results and measure the calls/bytes/retries needed to complete checkout.
- **Decision / tradeoff:** An aggregate endpoint can reduce client round trips but combine larger payloads and different freshness needs.
- **Application evidence:** “If processing continues later, say “accepted” rather than claiming delivery or payment has already completed.”
- **Visual decision:** The contract’s inputs, outputs, errors, and retry rule can be explained with a static request/response example.

### REST, GraphQL, gRPC

- **Fundamental:** “These are different interface models, not a ranking from slowest to fastest.”
- **Problem solved:** The interface must fit the clients, data shapes, and communication pattern without hiding inefficient backend work.
- **System-design scenario:** A shop page displays 30 products with prices and inventory.
- **How it is applied:** Choose a resource, schema-selection, or typed-operation interface based on the client and operation. → Trace the inventory lookups for the 30 products. → Batch product IDs to avoid one backend query per item; bound query complexity and preserve data authorization. → Measure database calls, bytes, round trips, and end-to-end latency before choosing an optimization.
- **Decision / tradeoff:** Client field flexibility, HTTP resource behavior, and typed service calls solve different needs; a smaller response may still trigger more database work.
- **Application evidence:** “For a REST endpoint, a bounded batch endpoint or an appropriate cached product view can address the same workload.”
- **Visual decision:** A side-by-side static request and backend-query comparison is sufficient; the lesson’s main issue is interface choice rather than timing.

### API Gateway

- **Fundamental:** “The API Gateway is an API management tool that sits between a client and a collection of backend services.”
- **Problem solved:** Clients otherwise must discover and coordinate multiple backend services and shared entry-point concerns themselves.
- **System-design scenario:** A mobile product screen needs catalog and stock through one supported entry path.
- **How it is applied:** Route product and order requests to their service owners. → Aggregate catalog and stock only with a defined deadline and partial-response rule. → Enforce order ownership in the responsible service even after gateway authentication. → Deploy redundant gateways and measure gateway delay separately from downstream delay.
- **Decision / tradeoff:** A simpler client entry point concentrates routing and operational dependency; aggregation saves round trips but inherits downstream partial failure.
- **Application evidence:** “Suppose a product page needs catalog and stock data. A gateway can combine those responses, reducing client round trips.”
- **Visual decision:** A static gateway → catalog/stock fan-out diagram plus deadline labels explains this boundary adequately.

### Idempotency

- **Fundamental:** “An operation is idempotent if performing it multiple times has the same effect as performing it once.”
- **Problem solved:** A retried payment after a lost response must not create an extra charge or skip a charge that never happened.
- **System-design scenario:** The same ₹500 payment reaches two workers concurrently under key K.
- **How it is applied:** Scope K to caller and operation and record a payload fingerprint. → Use an atomic uniqueness rule to choose one owner; define the duplicate’s result or in-progress response. → Coordinate the durable key state with the actual side effect and recovery. → Use the external provider’s idempotency contract and reconcile uncertain outcomes before retrying a charge.
- **Decision / tradeoff:** Retry safety costs durable deduplication state and coordination; expiring keys before the supported retry period can re-enable duplicate work.
- **Application evidence:** “A unique constraint can ensure two concurrent requests cannot both claim K.”
- **Visual decision:** Simultaneous requests and a lost acknowledgement make the difference between atomic claim, in-progress work, and saved result confusing.

### Rate Limiting

- **Fundamental:** “Rate limiting refers to preventing the frequency of an operation from exceeding a defined limit.”
- **Problem solved:** One customer or an aggregate traffic burst can overload shared search capacity or unfairly consume it.
- **System-design scenario:** A nominal 100-request/second customer limit is enforced separately by ten app instances.
- **How it is applied:** Define the identity key, interval, sustained rate, and burst allowance. → Coordinate a global allowance or partition the budget intentionally across instances. → Choose token bucket refill/burst behavior or account for fixed-window boundary bursts. → Return a clear throttling response, require client backoff, and specify the unavailable-store policy.
- **Decision / tradeoff:** Coordinated global accounting improves rule accuracy but adds a dependency; failing open preserves access while risking overload, whereas failing closed rejects legitimate traffic.
- **Application evidence:** “A global rule needs coordinated accounting or a deliberately partitioned budget.”
- **Visual decision:** Token refill, burst depletion, and two adjacent fixed windows are easier to understand as a moving timeline.

### Long polling, WebSockets, Server-Sent Events (SSE)

- **Fundamental:** “These mechanisms carry updates; they do not automatically provide a durable message history.”
- **Problem solved:** Clients need timely updates, sometimes bidirectional, without losing all progress when a connection drops.
- **System-design scenario:** A scoreboard streams state changes; a collaborative editor exchanges changes both ways.
- **How it is applied:** Select SSE for suitable server-to-client updates, WebSockets for suitable bidirectional work, or long polling when appropriate. → Assign event positions or provide snapshots to recover missed updates. → Reconnect with backoff and bound per-client buffering. → Coalesce scoreboard state changes where safe, but retain chat messages when the product requires history.
- **Decision / tradeoff:** Long-lived communication reduces repeated polling but consumes connection/buffer resources and requires explicit reconnection/history behavior.
- **Application evidence:** “After reconnecting, a client can request events after its last confirmed position, or reload a current snapshot when history is unavailable.”
- **Visual decision:** Comparing held requests, repeated long-poll responses, and one persistent duplex connection is inherently temporal.

### Webhooks

- **Fundamental:** “A webhook is an event notification delivered to an endpoint you provide, commonly using an HTTP request.”
- **Problem solved:** A service needs provider events without constant polling, while tolerating duplicate, delayed, or reordered delivery.
- **System-design scenario:** A payment provider resends event E after the receiver durably accepted it but its acknowledgement was lost.
- **How it is applied:** Verify the provider’s signature against the specified representation and validate the event. → Durably accept E and acknowledge according to the delivery contract. → Process E with a uniqueness rule plus recoverable business-state changes. → Reject stale state regressions or consult the authoritative provider status when appropriate.
- **Decision / tradeoff:** A short accept-and-enqueue path reduces acknowledgement delays but separates acceptance from business completion and requires a durable worker/recovery path.
- **Application evidence:** “The provider sends event E. Your receiver verifies it and durably records E for processing.”
- **Visual decision:** The lost acknowledgement and duplicate delivery must be distinguished from a genuinely new payment event.

### API Design

- **Fundamental:** “Start with what clients need to do and the data they exchange.”
- **Problem solved:** Unbounded lists, ambiguous results, incompatible changes, and unsafe retries prevent clients completing tasks predictably.
- **System-design scenario:** An account with one million orders pages through a changing order list.
- **How it is applied:** Set a maximum page size and stable sort with a unique tie-breaker. → Return a continuation cursor and document snapshot versus live-list semantics. → Check authorization for every page and prevent cursors from granting someone else’s data access. → Test equal timestamps, concurrent inserts/deletes, invalid cursors, and repeated writes against the contract.
- **Decision / tradeoff:** Bounded pages reduce per-request work but require explicit ordering and continuation semantics; a cursor alone does not guarantee a stable snapshot.
- **Application evidence:** “Instead, enforce a maximum page size and return a continuation cursor.”
- **Visual decision:** A static pair of pages with equal timestamps and a documented cursor boundary can explain the contract; animation is optional.

### Message Brokers

- **Fundamental:** “The broker stores or routes messages according to its configured guarantees; a queue or topic describes the delivery pattern offered.”
- **Problem solved:** Producers and consumers should exchange work/events without requiring each receiver to be synchronously active or directly addressed.
- **System-design scenario:** An order service hands off billing and shipping work through messaging infrastructure.
- **How it is applied:** Decide whether one worker must do each job or independent subscribers each need the event. → Specify persistence, acknowledgement, ordering, and replay/retry guarantees before selecting a product. → Bound consumer in-flight work and batch only within acceptable delay. → Monitor backlog age and verify the crash-after-side-effect acknowledgement case.
- **Decision / tradeoff:** Buffering and decoupling introduce delayed processing, retained state, and duplicate/recovery responsibilities; product labels do not determine delivery semantics.
- **Application evidence:** “Limit consumers' in-flight work so a fast broker cannot overwhelm a slow database.”
- **Visual decision:** The broker’s role and queue/topic pattern choice can be established with a static producer–broker–consumer diagram; queue-specific timing is animated separately.

### Message Queues

- **Fundamental:** “A message queue is a form of service-to-service communication that facilitates asynchronous communication.”
- **Problem solved:** Bursts of thumbnail work should not hold upload requests open or overwhelm downstream processing; redeliveries must be safe.
- **System-design scenario:** One thousand uploads create queued thumbnail jobs, and a worker crashes after writing output but before acknowledgement.
- **How it is applied:** Durably enqueue stable job identifiers and use deterministic output keys. → Acknowledge after durable completion with realistic visibility/processing leases. → Handle a redelivered job without conflicting duplicate output. → Scale workers only while storage/database capacity permits and isolate repeatedly failing jobs.
- **Decision / tradeoff:** A queue absorbs temporary bursts but adds waiting time and cannot fix a sustained arrival rate above processing capacity.
- **Application evidence:** “Give each job a stable identifier and deterministic output key.”
- **Visual decision:** A worker crash before acknowledgement followed by redelivery visually disproves the misleading idea that a job is executed exactly once.

### Publish-Subscribe

- **Fundamental:** “An OrderPlaced event must reach both billing and shipping. Each needs its own subscription.”
- **Problem solved:** Several independent business reactions must each receive an event without being treated as competing workers for one job.
- **System-design scenario:** Billing and shipping both react to OrderPlaced; multiple billing workers share only billing work.
- **How it is applied:** Create separate billing and shipping subscriptions. → Specify event identifiers, versioned meaning, and safe repeated processing. → Choose durable subscriptions/history if offline consumers must catch up. → Scale each subscription independently and partition related events consistently when their ordering matters.
- **Decision / tradeoff:** Independent fan-out avoids direct producer coupling but increases delivery/state coordination; global ordering is not automatically available across partitions.
- **Application evidence:** “Use durable subscriptions or retained history when a temporarily offline consumer must catch up;”
- **Visual decision:** Show one copy per subscription and one worker per delivery within a subscription; learners often conflate these two distribution levels.

### Change Data Capture (CDC)

- **Fundamental:** “CDC observes changes in a database and makes them available to other systems.”
- **Problem solved:** A derived search index needs committed database changes without repeatedly scanning the entire source or independently double-writing each request.
- **System-design scenario:** A committed price update travels through a connector to the search index, whose consumer restarts from an older position.
- **How it is applied:** Take an initial snapshot and track a recoverable change-log position. → Apply records using stable product identifiers and a version rule that makes replay safe. → Handle deletes/schema changes and monitor time/log-position lag. → Bound retained-log growth and define resnapshot recovery if required history disappears.
- **Decision / tradeoff:** Streaming changes reduces repeated full reads but introduces lag, source retention overhead, schema coupling, and replay/recovery duties.
- **Application evidence:** “Updating the search record by stable product identifier and an appropriate version rule can make replay safe.”
- **Visual decision:** Animate commit → log → connector → index and then replay after restart so database commit is not mistaken for immediate search visibility.

### N-tier architecture

- **Fundamental:** “Browser → application server → database server is a three-tier deployment.”
- **Problem solved:** Separates presentation, business rules, and persistence so each responsibility has an explicit deployment and scaling boundary.
- **System-design scenario:** An online shop separates its browser presentation, order-validation service, and database.
- **How it is applied:** Place order validation in the application layer and authoritative records in the database. → Identify which boundary becomes a network call and can time out. → Measure the saturated tier, and use a bounded set-based request rather than one network round trip per order line.
- **Decision / tradeoff:** Independent tier scaling and ownership add network latency, deployment cost, and partial failures; folders alone do not create deployment tiers.
- **Application evidence:** “Keep order validation in the application layer and authoritative data in the database.”
- **Visual decision:** The local example already distinguishes logical layers from deployed tiers; the source diagram plus request trace is sufficient.

### Monoliths and Microservices

- **Fundamental:** “Clear module boundaries let developers reason about responsibilities even though deployment and many calls remain local.”
- **Problem solved:** Defines capability and data-ownership boundaries without treating distributed deployment as an automatic performance improvement.
- **System-design scenario:** A shop considers extracting catalog or billing after measuring different scaling, compliance, or release needs.
- **How it is applied:** Measure query cost, synchronous work, and resource contention before splitting services. → Choose a capability with clear data ownership and minimize chatty cross-boundary calls. → Trace an order with failed inventory reservation or delayed payment, then define intermediate states, retries, and compensation.
- **Decision / tradeoff:** A service split may improve independent scaling or release ownership, while introducing network failures and cross-service coordination; a better module or query can be sufficient.
- **Application evidence:** “If splitting helps, extract a capability with clear data ownership and minimize chatty calls across its boundary.”
- **Visual decision:** The source comparison and explicit order-failure walkthrough already explain the boundary; animation would add presentation rather than resolve a remaining gap.

### Event-Driven Architecture (EDA)

- **Fundamental:** “The order service records an order; shipping reacts to OrderPlaced later.”
- **Problem solved:** Decouples an initiating business action from downstream reactions that can complete later.
- **System-design scenario:** An order is accepted while shipping remains pending.
- **How it is applied:** Record the order and coordinate publication of its event, such as through a transactional outbox. → Give events identifiers and consumers safe retry behavior; tolerate delayed or reordered processing. → Show pending downstream state, and scale consumers using backlog age and downstream capacity.
- **Decision / tradeoff:** Asynchronous reactions reduce synchronous coupling but require explicit delay, duplicate, and publish-after-write failure handling.
- **Application evidence:** “Coordinate recording the order and publishing its event, for example with a transactional outbox, so a crash does not leave an order with no event.”
- **Visual decision:** A sequence should show order committed, shipping still pending, and a crash/retry around publication; otherwise learners can confuse asynchronous acceptance with downstream completion.

### Event Sourcing

- **Fundamental:** “Deposited(100), then Withdrawn(30), produces balance 70.”
- **Problem solved:** Preserves authoritative business history so current state and derived views can be reconstructed.
- **System-design scenario:** A balance is reconstructed from deposits and withdrawals rather than treated as only a mutable final number.
- **How it is applied:** Append business events as the system of record. → Rebuild balance from the ordered history; use a verified snapshot and later events to shorten replay. → Version event schemas and prevent replay from repeating external charges or receipt emails.
- **Decision / tradeoff:** Replay and audit history introduce schema evolution and recovery complexity; merely publishing notifications is not event sourcing.
- **Application evidence:** “To shorten replay, load a verified snapshot and apply later events.”
- **Visual decision:** Animate replay changing balance 0→100→70 while external side effects stay disabled, then contrast that with notification-only EDA.

### Command and Query Responsibility Segregation (CQRS)

- **Fundamental:** “CQRS separates those responsibilities; it does not require event sourcing.”
- **Problem solved:** Allows write rules and read queries to use models shaped for their different responsibilities.
- **System-design scenario:** Creating an order updates a write model while a separate customer-order-list projection updates afterward.
- **How it is applied:** Accept the create-order command through the write model. → Update an idempotent customer-order projection and monitor its lag. → Return the confirmed order identifier with a pending-view state, and define how to rebuild a lost projection.
- **Decision / tradeoff:** A query-optimized read view can reduce expensive joins but adds synchronization and recovery work; simple CRUD may not benefit.
- **Application evidence:** “Optimize the read view for actual queries, such as recent orders by customer, instead of making every screen join the write model.”
- **Visual decision:** Show the write succeeding before the read projection catches up, including duplicate projection delivery; this makes the lag and model separation visible.

### Enterprise Service Bus (ESB)

- **Fundamental:** “An ESB can transform fields and route messages between them.”
- **Problem solved:** Integrates systems with incompatible message formats and routing requirements.
- **System-design scenario:** Billing messages need transformation before legacy shipping can consume them.
- **How it is applied:** Define an integration boundary and the required field transformation. → Route the transformed message to the intended endpoint and bound retries. → Measure transformation cost and queue delay, and verify routing state during failover.
- **Decision / tradeoff:** Central integration can simplify connections while concentrating operational dependency and accumulating business-rule coupling.
- **Application evidence:** “Apply transformations at clear integration boundaries.”
- **Visual decision:** The billing-to-shipping transformation is a static contract and routing example; the existing source diagram and concrete fields/routing explanation are sufficient.

### Virtual Machines (VMs) and Containers

- **Fundamental:** “Containers normally share the host kernel while isolating processes and resource usage.”
- **Problem solved:** Chooses packaging, resource control, and operating-system isolation boundaries for workloads.
- **System-design scenario:** A shop deploys replaceable application workers while deciding whether a different guest kernel or stronger boundary requires VMs.
- **How it is applied:** Choose a VM or container boundary from kernel and isolation requirements. → Set CPU and memory budgets using measured workload and store durable state outside disposable instances. → Check readiness and in-progress job recovery before replacing a worker.
- **Decision / tradeoff:** Small images can shorten distribution, but actual readiness also includes initialization, connections, and warm-up; VMs and containers can be combined.
- **Application evidence:** “Set CPU and memory budgets based on measured workload.”
- **Visual decision:** A static kernel/process boundary diagram is enough; the lesson explicitly rejects equating a small image with a separate guest OS.

### Serverless Architecture

- **Fundamental:** “Serverless does not mean no servers exist.”
- **Problem solved:** Offloads parts of runtime provisioning and operation for suitable request- or event-triggered work.
- **System-design scenario:** A stored photo triggers thumbnail generation that can run again after a repeated event.
- **How it is applied:** Store photo P and use a deterministic output key such as P/version/thumbnail. → Make duplicate events safe without relying on invocation-local memory. → Measure cold versus warm execution, tune concurrency against downstream limits, and compare cost per successful job.
- **Decision / tradeoff:** Reduced infrastructure management and burst scaling come with lifecycle limits, cold starts, provider coupling, and downstream saturation risk.
- **Application evidence:** “A function reads P, creates a thumbnail, and stores the output under a deterministic key such as `P/version/thumbnail`.”
- **Visual decision:** The local upload→function→deterministic-output walkthrough already exposes lifecycle and duplicate behavior; no unresolved temporal ambiguity requires animation.

### Peer-to-Peer (P2P) Architecture

- **Fundamental:** “In a peer-to-peer design, participants can exchange data or provide services to one another.”
- **Problem solved:** Distributes content-serving work among participants instead of making one origin serve every byte.
- **System-design scenario:** Peers A and B exchange different verified pieces of the same large file.
- **How it is applied:** Split content into verifiable pieces and obtain trustworthy piece metadata. → Discover reachable peers with useful pieces and resume from alternative sources when peers depart. → Bound connections and upload usage; measure completion time and origin bandwidth savings under churn.
- **Decision / tradeoff:** Distributed upload capacity reduces origin load but complicates reachability, trust, abuse prevention, discovery dependencies, and availability of scarce pieces.
- **Application evidence:** “They exchange useful pieces rather than downloading every byte from the origin.”
- **Visual decision:** A piece-exchange animation with one peer leaving should show why partial progress, scarce pieces, and alternative sources matter.

### Service Discovery

- **Fundamental:** “Discovery supplies usable destinations; load balancing chooses among them.”
- **Problem solved:** Finds service instance addresses that change during deployment or failure.
- **System-design scenario:** A long-lived orders client must notice that one of three service instances was replaced.
- **How it is applied:** Publish instances whose readiness checks show they can accept work. → Drain bounded in-flight work while removing a retiring instance from new routing. → Refresh cached discovery state and use deadlines and safe retries when an address becomes stale.
- **Decision / tradeoff:** Cached discovery reduces lookup traffic while delaying awareness of changes; discovery does not eliminate request-time failures.
- **Application evidence:** “Use readiness checks that reflect whether an instance can accept work, not merely whether its process exists.”
- **Visual decision:** The source already distinguishes client/server discovery paths, and the replacement-instance example gives the necessary application steps without another animated sequence.

### HeartBeats

- **Fundamental:** “A heartbeat is a periodic “I am here” signal.”
- **Problem solved:** Provides recent reachability evidence to support failure suspicion, not proof of end-to-end health.
- **System-design scenario:** A worker reporting every five seconds pauses long enough to cross a fifteen-second suspicion threshold.
- **How it is applied:** Choose report interval and suspicion threshold from observed delay, pauses, and detection needs. → Separate liveness from readiness so a heartbeat does not hide a broken business dependency. → Test pause-and-resume after replacement and coordinate work with fencing, idempotency, or another safe invariant.
- **Decision / tradeoff:** Short thresholds detect trouble sooner but increase false suspicions; longer thresholds delay failover and do not prove exact recovery time.
- **Application evidence:** “If the worker pauses for twenty seconds, a replacement may begin work while the old worker later resumes.”
- **Visual decision:** Animate a live but paused worker missing heartbeats, a replacement starting, and the old worker resuming; it demonstrates why timeout is suspicion and can cause overlapping work.

### Circuit breaker

- **Fundamental:** “A timeout bounds one call, while the breaker reacts to a failure pattern.”
- **Problem solved:** Stops repeated calls to a failing dependency from consuming resources and spreading failure.
- **System-design scenario:** Checkout payment calls repeatedly time out, then limited probes test whether payment service recovered.
- **How it is applied:** Measure failures and configure a breaker independently for the payment dependency. → Open to reject new calls temporarily, then admit limited half-open probes. → Use bounded retries and backoff, and show payment pending or unavailable rather than fabricate a successful charge.
- **Decision / tradeoff:** Fail-fast protection gives up some attempted calls during trouble; thresholds and recovery probes must avoid preventing useful recovery or creating another retry flood.
- **Application evidence:** “A checkout can show payment pending or unavailable; inventing a successful charge is not a safe fallback.”
- **Visual decision:** The closed→open→half-open→closed/open state loop is a common confusion; animate allowed and blocked requests separately from each call timeout.

### SLA, SLO, SLI

- **Fundamental:** “SLI: measured successful-request percentage. SLO: your target, such as 99.9%. SLA: an agreement that may specify consequences.”
- **Problem solved:** Connects a user-facing service promise to a measurable target and observed performance.
- **System-design scenario:** Checkout needs a success definition and latency threshold before requests are counted.
- **How it is applied:** Define a successful checkout and which slow responses count as failures. → Choose a target and measurement window, then calculate the measured indicator. → Use user-visible failures, latency, and remaining error allowance to prioritize reliability work.
- **Decision / tradeoff:** An internal objective and a contractual agreement have different roles; optimizing a fast component does not help the service if another cause dominates failures.
- **Application evidence:** “For checkout, define success and a latency threshold before counting requests.”
- **Visual decision:** The measurement/target/agreement distinction and concrete checkout classification are clearer as a small table or worked count than an animation.

### Disaster recovery

- **Fundamental:** “Restoring service within two hours concerns RTO.”
- **Problem solved:** Defines tolerable data loss and time to recover usable service after a serious disruption.
- **System-design scenario:** Hourly backups with no newer recoverable log are restored in a rehearsed shop recovery exercise.
- **How it is applied:** Set RPO and RTO from business tolerance. → Restore data, configuration, credentials, and traffic routing in an isolated exercise. → Measure time until users can work, and protect backups from the same deletion or compromise as production.
- **Decision / tradeoff:** More frequent recoverable data capture improves RPO; faster restore automation improves RTO, and backup existence alone proves neither.
- **Application evidence:** “Rehearse restoring data, application configuration, credentials, and traffic routing in an isolated recovery exercise.”
- **Visual decision:** The hourly-backup and two-hour-restore example already separates the two dimensions; a labeled static timeline suffices.

### Consensus Algorithms

- **Fundamental:** “Consensus protocols help cooperating nodes agree on decisions, such as the order of entries in a **replicated log**, the same ordered history kept on multiple nodes.”
- **Problem solved:** Maintains an agreed ordered decision history among replicas under a specified failure model.
- **System-design scenario:** A three-voter Raft group must handle an isolated former leader without conflicting committed decisions.
- **How it is applied:** Use a well-understood protocol implementation and specify voters and failure assumptions. → Replicate log entries through leader, term, history, persistence, and quorum rules. → Test leader loss and partitions; batch or pipeline only while retaining required correctness rules.
- **Decision / tradeoff:** Distant voters can improve regional failure tolerance while adding commit latency; losing the communicating majority may stop progress to preserve safety.
- **Application evidence:** “In a three-voter Raft group, a client sends a command to the leader.”
- **Visual decision:** Show leader A isolated, B/C forming a communicating majority, and A unable to commit conflicting decisions; simple moving majority votes alone would teach the wrong protocol.

### Distributed Locking

- **Fundamental:** “A distributed lock tries to give one participant temporary ownership of work shared across machines.”
- **Problem solved:** Coordinates exclusive work across processes while accounting for expiry and stale owners.
- **System-design scenario:** Report worker A pauses past lease expiry, B gets token 11, then A resumes with token 10.
- **How it is applied:** Decide whether duplicates are a cost problem or a correctness violation. → Acquire ownership with a lease and have the protected store enforce fencing or another direct invariant. → Make release ownership-safe, shorten the critical section, and test old owners resuming after takeover.
- **Decision / tradeoff:** A longer lease delays takeover while a shorter lease can expire during legitimate work; idempotent or conditional writes may express the invariant more directly than a lock.
- **Application evidence:** “If the protected store checks ownership tokens, it can reject token 10 after observing token 11.”
- **Visual decision:** Animate the lease timeline with tokens 10/11 and the protected store rejecting A after B writes; lease expiry alone does not stop A from executing.

### Gossip Protocol

- **Fundamental:** “In a gossip protocol, nodes periodically exchange information with selected peers.”
- **Problem solved:** Spreads membership or health observations without every update requiring one sender to contact all nodes directly.
- **System-design scenario:** A learns member D joined, tells B, and C learns later after another peer exchange.
- **How it is applied:** Select peers and exchange membership observations using the chosen protocol version rules. → Allow temporary view disagreement and reconnect or resynchronize after separation. → Tune exchange frequency, fanout, and message size against convergence time and bandwidth.
- **Decision / tradeoff:** Faster or wider exchanges consume more network and processing; gradual dissemination is not consensus on a single committed write order.
- **Application evidence:** “A tells B during a periodic exchange; B later tells C.”
- **Visual decision:** Animate update D reaching A, B, then C across exchanges, with visibly different views before convergence and a partition delaying spread.

### Distributed Tracing

- **Fundamental:** “A trace connects the work caused by one request.”
- **Problem solved:** Connects request work across service boundaries to locate slow or failing dependencies.
- **System-design scenario:** An order-page trace separates gateway work, orders-service work, and a slow sequential database call, then contrasts overlapping dependency calls.
- **How it is applied:** Propagate trace context through HTTP and message metadata and create meaningful spans. → Find the critical path rather than summing overlapping spans or inclusive parent times. → Connect traces to metrics and logs, test broken context propagation, and choose sampling against overhead and rare-event visibility.
- **Decision / tradeoff:** Sampling reduces volume but may miss rare slow failures; recording more data raises overhead and privacy cost without automatically explaining the root cause.
- **Application evidence:** “Inspect the query and its execution behavior before adding application instances.”
- **Visual decision:** A span timeline should contrast sequential and concurrent calls; animation can demonstrate why overlapping spans must not simply be added.

### SSL, TLS, mTLS

- **Fundamental:** “With mTLS, the server also verifies a client certificate, useful for identifying calling services.”
- **Problem solved:** Protects connection data and establishes endpoint identity while keeping authorization separate.
- **System-design scenario:** A gateway accepts HTTPS and creates a separately protected internal service connection.
- **How it is applied:** Identify where TLS terminates and which endpoint identities are verified on each hop. → Use supported configurations, certificate renewal, and expiry monitoring. → Reuse suitable connections for efficiency without bypassing verification, and authorize the identified caller separately.
- **Decision / tradeoff:** Connection reuse can save handshake work, but a gateway termination does not automatically protect the next hop or grant the caller permission.
- **Application evidence:** “A gateway that terminates TLS creates a new internal connection whose protection must be designed separately.”
- **Visual decision:** Endpoint identity and termination boundaries are explicit in the local example and can be shown with a static two-hop diagram.

### OAuth 2.0 and OpenID Connect (OIDC)

- **Fundamental:** “Access tokens belong at their intended API; ID tokens identify the user to their intended client.”
- **Problem solved:** Separates delegated access to protected resources from a client receiving authenticated login identity.
- **System-design scenario:** A photo-printing client requests limited photo access and uses authorization-code exchange rather than receiving the user password.
- **How it is applied:** Redirect to the provider, receive an authorization code, and exchange it for tokens with PKCE for public clients. → Validate each token according to its contract and request only required permissions. → Send the access token to its intended photo API, check photo ownership there, and refresh signing keys with rotation-aware behavior.
- **Decision / tradeoff:** Shorter lifetimes and refresh policy affect revocation behavior and renewal cost; a valid identity or token never grants access to all photos.
- **Application evidence:** “With an authorization-code flow, redirect the user to the provider, receive a code, and exchange it for tokens.”
- **Visual decision:** Animate user/client/provider/API roles and separately label code, ID token, and access token so token audience and password handling cannot be confused.

### Single Sign-On (SSO)

- **Fundamental:** “Each application trusts identity information through an agreed protocol, but still owns its permissions and often maintains its own session.”
- **Problem solved:** Lets multiple applications share an identity-provider sign-in while retaining application-specific permissions and session policies.
- **System-design scenario:** An employee signs in once and opens payroll and email, then the organization disables their account.
- **How it is applied:** Map provider identities using stable identifiers and assign local application roles explicitly. → Define provider outage, provisioning, group-change, and employment-ending behavior. → Choose application session lifetimes and logout/revocation behavior that satisfy the required access-removal delay.
- **Decision / tradeoff:** Reusing sessions improves convenience and reduces provider interactions but can delay revocation; single sign-on does not imply universal logout.
- **Application evidence:** “Map identity-provider accounts to local accounts using stable identifiers. Decide which roles grant payroll access rather than treating every authenticated employee as an administrator.”
- **Visual decision:** The separate payroll/provider/email sessions and disable-account check explicitly resolve the key confusion; a session-state table is sufficient.

### Geohashing and Quadtrees

- **Fundamental:** “Both help narrow candidates rather than calculating every driver's distance.”
- **Problem solved:** Narrows spatial search candidates so nearby-driver queries avoid a distance calculation against every driver.
- **System-design scenario:** A ride app searches for eligible drivers near a customer whose nearest driver may lie across a grid-cell boundary.
- **How it is applied:** Retrieve candidates from the relevant and neighboring cells or suitable quadtree regions. → Calculate actual distances and reject or explicitly account for stale location records. → Tune precision, radius, occupancy/depth, and outward expansion using candidate counts and index-update cost.
- **Decision / tradeoff:** Coarse cells return excess candidates; overly fine cells require more lookups, and frequent movement increases maintenance work.
- **Application evidence:** “Search the relevant cell and neighboring cells, then calculate actual distances for the candidates.”
- **Visual decision:** Animate two close points on opposite cell sides and a search expanding into neighbors; it exposes the false assumption that same-cell search finds every nearest driver.
