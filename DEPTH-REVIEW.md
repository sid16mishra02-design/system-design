# Applied-depth review

[← Learning path](README.md) · [Content preservation audit](CONTENT-AUDIT.md)

This edition reviews all **71 foundational lessons, five worked designs, and the interview-method lesson**. It expands teaching guidance without altering the marked original course wording. The goal is to connect an idea to a situation, a design decision, its cost, and evidence that a change helped.

The twenty originally written lessons include application scenarios, worked behavior or calculations, optimization choices, and verification. Course lessons now begin with a problem to reason through before the explanation. With the owner's permission, terse independent notes are expanded beyond the initial 30% guideline where the reasoning needs room. A larger word count alone is not evidence of a better explanation.

Numbers in the new examples are stated assumptions for learning, not production benchmarks or claims about the named services' actual implementations. Optimization guidance is conditional: identify a bottleneck, protect correctness, measure the change, and account for its cost.

## Read the additions

Start with **Try solving this first**, and record an answer or sketch before scrolling. On course pages, compare your answer with the original explanation and **Make it concrete**. On standalone lessons, follow the practical-use, worked-example, improvement, and verification sections. Case-study questions come before the worked guidance and complete solution.

If a deeper lesson takes more than one session, use the existing carry-forward rule in the [schedule](SCHEDULE.md). No catch-up sprint is required.

## Coverage and teaching-word counts

Counts below measure independent teaching guidance, including the opening questions, not the preserved original topic. Comparison-table allocations are included in the separate content audit. Initial numeric allowances are retained in metadata for history; the current edition uses approved clarity expansion.

| Lesson | Previous teaching words | Current teaching words | Allowance for additions |
| --- | ---: | ---: | --- |
| [What is system design?](curriculum/01-core-concepts/01-what-is-system-design.md) | 43 | 227 | Clarity expansion approved |
| [Scalability](curriculum/01-core-concepts/02-scalability.md) | 32 | 221 | Clarity expansion approved |
| [Availability](curriculum/01-core-concepts/03-availability.md) | 41 | 280 | Clarity expansion approved |
| [Latency vs Throughput vs Bandwidth](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) | 165 | 1143 | Approved exception |
| [Reliability](curriculum/01-core-concepts/05-reliability.md) | 170 | 543 | Approved exception |
| [SPOF](curriculum/01-core-concepts/06-spof.md) | 153 | 464 | Approved exception |
| [IP](curriculum/02-networking/01-ip.md) | 45 | 274 | Clarity expansion approved |
| [OSI Model](curriculum/02-networking/02-osi-model.md) | 61 | 220 | Clarity expansion approved |
| [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md) | 49 | 263 | Clarity expansion approved |
| [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md) | 50 | 272 | Clarity expansion approved |
| [Proxy](curriculum/02-networking/05-proxy.md) | 34 | 276 | Clarity expansion approved |
| [HTTP/HTTPS](curriculum/02-networking/06-httphttps.md) | 181 | 538 | Approved exception |
| [Checksums](curriculum/02-networking/07-checksums.md) | 165 | 481 | Approved exception |
| [Load Balancing](curriculum/02-networking/08-load-balancing.md) | 50 | 293 | Clarity expansion approved |
| [Clustering](curriculum/02-networking/09-clustering.md) | 39 | 211 | Clarity expansion approved |
| [Storage](curriculum/03-databases/01-storage.md) | 43 | 216 | Clarity expansion approved |
| [Databases and DBMS](curriculum/03-databases/02-databases-and-dbms.md) | 57 | 183 | Clarity expansion approved |
| [SQL databases](curriculum/03-databases/03-sql-databases.md) | 52 | 271 | Clarity expansion approved |
| [NoSQL databases](curriculum/03-databases/04-nosql-databases.md) | 59 | 286 | Clarity expansion approved |
| [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md) | 43 | 266 | Clarity expansion approved |
| [Indexes](curriculum/03-databases/06-indexes.md) | 48 | 282 | Clarity expansion approved |
| [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md) | 51 | 321 | Clarity expansion approved |
| [Transactions](curriculum/03-databases/08-transactions.md) | 43 | 241 | Clarity expansion approved |
| [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md) | 49 | 271 | Clarity expansion approved |
| [Database Replication](curriculum/03-databases/10-database-replication.md) | 64 | 261 | Clarity expansion approved |
| [Sharding](curriculum/03-databases/11-sharding.md) | 81 | 252 | Clarity expansion approved |
| [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md) | 53 | 261 | Clarity expansion approved |
| [Database Federation](curriculum/03-databases/13-database-federation.md) | 37 | 248 | Clarity expansion approved |
| [Bloom Filters](curriculum/03-databases/14-bloom-filters.md) | 183 | 566 | Approved exception |
| [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md) | 77 | 257 | Clarity expansion approved |
| [PACELC Theorem](curriculum/04-distributed-data/02-pacelc-theorem.md) | 27 | 224 | Clarity expansion approved |
| [Distributed Transactions](curriculum/04-distributed-data/03-distributed-transactions.md) | 50 | 317 | Clarity expansion approved |
| [Caching](curriculum/05-caching/01-caching.md) | 74 | 243 | Clarity expansion approved |
| [Caching Strategies](curriculum/05-caching/02-caching-strategies.md) | 175 | 556 | Approved exception |
| [Cache Eviction Policies](curriculum/05-caching/03-cache-eviction-policies.md) | 172 | 528 | Approved exception |
| [Distributed Caching](curriculum/05-caching/04-distributed-caching.md) | 183 | 534 | Approved exception |
| [Content Delivery Network (CDN)](curriculum/05-caching/05-content-delivery-network-cdn.md) | 40 | 299 | Clarity expansion approved |
| [APIs](curriculum/06-api-fundamentals/01-apis.md) | 161 | 497 | Approved exception |
| [REST, GraphQL, gRPC](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) | 47 | 219 | Clarity expansion approved |
| [API Gateway](curriculum/06-api-fundamentals/03-api-gateway.md) | 45 | 400 | Clarity expansion approved |
| [Idempotency](curriculum/06-api-fundamentals/04-idempotency.md) | 84 | 318 | Clarity expansion approved |
| [Rate Limiting](curriculum/06-api-fundamentals/05-rate-limiting.md) | 50 | 192 | Clarity expansion approved |
| [Long polling, WebSockets, Server-Sent Events (SSE)](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) | 47 | 176 | Clarity expansion approved |
| [Webhooks](curriculum/06-api-fundamentals/07-webhooks.md) | 180 | 526 | Approved exception |
| [API Design](curriculum/06-api-fundamentals/08-api-design.md) | 176 | 491 | Approved exception |
| [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md) | 44 | 275 | Clarity expansion approved |
| [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md) | 73 | 309 | Clarity expansion approved |
| [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md) | 62 | 295 | Clarity expansion approved |
| [Change Data Capture (CDC)](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md) | 164 | 520 | Approved exception |
| [N-tier architecture](curriculum/08-architectural-patterns/01-n-tier-architecture.md) | 53 | 223 | Clarity expansion approved |
| [Monoliths and Microservices](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md) | 47 | 228 | Clarity expansion approved |
| [Event-Driven Architecture (EDA)](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md) | 38 | 228 | Clarity expansion approved |
| [Event Sourcing](curriculum/08-architectural-patterns/04-event-sourcing.md) | 40 | 231 | Clarity expansion approved |
| [Command and Query Responsibility Segregation (CQRS)](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md) | 66 | 230 | Clarity expansion approved |
| [Enterprise Service Bus (ESB)](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md) | 54 | 227 | Clarity expansion approved |
| [Virtual Machines (VMs) and Containers](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md) | 42 | 216 | Clarity expansion approved |
| [Serverless Architecture](curriculum/08-architectural-patterns/08-serverless-architecture.md) | 173 | 478 | Approved exception |
| [Peer-to-Peer (P2P) Architecture](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md) | 158 | 516 | Approved exception |
| [Service Discovery](curriculum/09-reliability-and-microservices/01-service-discovery.md) | 39 | 222 | Clarity expansion approved |
| [HeartBeats](curriculum/09-reliability-and-microservices/02-heartbeats.md) | 155 | 491 | Approved exception |
| [Circuit breaker](curriculum/09-reliability-and-microservices/03-circuit-breaker.md) | 42 | 221 | Clarity expansion approved |
| [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md) | 33 | 232 | Clarity expansion approved |
| [Disaster recovery](curriculum/09-reliability-and-microservices/05-disaster-recovery.md) | 45 | 235 | Clarity expansion approved |
| [Consensus Algorithms](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md) | 188 | 556 | Approved exception |
| [Distributed Locking](curriculum/09-reliability-and-microservices/07-distributed-locking.md) | 178 | 543 | Approved exception |
| [Gossip Protocol](curriculum/09-reliability-and-microservices/08-gossip-protocol.md) | 162 | 513 | Approved exception |
| [Distributed Tracing](curriculum/09-reliability-and-microservices/09-distributed-tracing.md) | 180 | 549 | Approved exception |
| [SSL, TLS, mTLS](curriculum/10-security-and-location/01-ssl-tls-mtls.md) | 43 | 224 | Clarity expansion approved |
| [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md) | 50 | 217 | Clarity expansion approved |
| [Single Sign-On (SSO)](curriculum/10-security-and-location/03-single-sign-on-sso.md) | 37 | 222 | Clarity expansion approved |
| [Geohashing and Quadtrees](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md) | 41 | 228 | Clarity expansion approved |
| [System Design Interviews](practice/INTERVIEW-APPROACH.md) | 118 | 261 | Clarity expansion approved |
| [Netflix](practice/netflix.md) | 152 | 651 | Clarity expansion approved |
| [Twitter](practice/twitter.md) | 152 | 646 | Clarity expansion approved |
| [Uber](practice/uber.md) | 152 | 643 | Clarity expansion approved |
| [URL Shortener](practice/url-shortener.md) | 153 | 629 | Clarity expansion approved |
| [WhatsApp](practice/whatsapp.md) | 152 | 643 | Clarity expansion approved |
