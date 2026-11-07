# Applied-depth review

[← Learning path](README.md) · [Content preservation audit](CONTENT-AUDIT.md)

This edition reviews all **71 foundational lessons, five worked designs, and the interview-method lesson**. It expands teaching guidance without altering the marked original course wording. The goal is to connect an idea to a situation, a design decision, its cost, and evidence that a change helped.

The twenty originally written lessons now include fuller application scenarios, worked behavior or calculations, optimization choices, and verification. Existing course lessons and case studies gain relevant independent guidance within their individual 30% addition allowance. Short topics use compact examples because the allowance is based on that topic, not the whole course. A larger word count alone is not evidence of a better explanation.

Numbers in the new examples are stated assumptions for learning, not production benchmarks or claims about the named services' actual implementations. Optimization guidance is conditional: identify a bottleneck, protect correctness, measure the change, and account for its cost.

## Read the additions

On course pages, read **Make it concrete** after the original explanation. On standalone lessons, follow the practical-use, worked-example, improvement, and verification sections. The case-study guidance comes before the complete original solution so you can attempt the design first.

If a deeper lesson takes more than one session, use the existing carry-forward rule in the [schedule](SCHEDULE.md). No catch-up sprint is required.

## Coverage and teaching-word counts

Counts below measure independent teaching guidance, not the preserved original topic. The preserved source text is additional reading on course pages. Comparison-table allocations also count toward a course topic's allowance in the separate content audit.

| Lesson | Previous teaching words | Current teaching words | Allowance for additions |
| --- | ---: | ---: | --- |
| [What is system design?](curriculum/01-core-concepts/01-what-is-system-design.md) | 43 | 43 | 45 |
| [Scalability](curriculum/01-core-concepts/02-scalability.md) | 32 | 32 | 50 |
| [Availability](curriculum/01-core-concepts/03-availability.md) | 41 | 132 | 133 |
| [Latency vs Throughput vs Bandwidth](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md) | 165 | 1088 | Approved exception |
| [Reliability](curriculum/01-core-concepts/05-reliability.md) | 170 | 487 | Approved exception |
| [SPOF](curriculum/01-core-concepts/06-spof.md) | 153 | 405 | Approved exception |
| [IP](curriculum/02-networking/01-ip.md) | 45 | 124 | 135 |
| [OSI Model](curriculum/02-networking/02-osi-model.md) | 61 | 174 | 200 |
| [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md) | 49 | 100 | 104 |
| [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md) | 50 | 211 | 504 |
| [Proxy](curriculum/02-networking/05-proxy.md) | 34 | 138 | 141 |
| [HTTP/HTTPS](curriculum/02-networking/06-httphttps.md) | 181 | 481 | Approved exception |
| [Checksums](curriculum/02-networking/07-checksums.md) | 165 | 416 | Approved exception |
| [Load Balancing](curriculum/02-networking/08-load-balancing.md) | 50 | 236 | 339 |
| [Clustering](curriculum/02-networking/09-clustering.md) | 39 | 160 | 206 |
| [Storage](curriculum/03-databases/01-storage.md) | 43 | 168 | 250 |
| [Databases and DBMS](curriculum/03-databases/02-databases-and-dbms.md) | 57 | 131 | 168 |
| [SQL databases](curriculum/03-databases/03-sql-databases.md) | 52 | 108 | 120 |
| [NoSQL databases](curriculum/03-databases/04-nosql-databases.md) | 59 | 140 | 159 |
| [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md) | 43 | 119 | 125 |
| [Indexes](curriculum/03-databases/06-indexes.md) | 48 | 124 | 141 |
| [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md) | 51 | 270 | 303 |
| [Transactions](curriculum/03-databases/08-transactions.md) | 43 | 91 | 94 |
| [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md) | 49 | 134 | 135 |
| [Database Replication](curriculum/03-databases/10-database-replication.md) | 64 | 98 | 112 |
| [Sharding](curriculum/03-databases/11-sharding.md) | 81 | 196 | 222 |
| [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md) | 53 | 209 | 279 |
| [Database Federation](curriculum/03-databases/13-database-federation.md) | 37 | 80 | 90 |
| [Bloom Filters](curriculum/03-databases/14-bloom-filters.md) | 183 | 504 | Approved exception |
| [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md) | 77 | 81 | 115 |
| [PACELC Theorem](curriculum/04-distributed-data/02-pacelc-theorem.md) | 27 | 47 | 51 |
| [Distributed Transactions](curriculum/04-distributed-data/03-distributed-transactions.md) | 50 | 181 | 196 |
| [Caching](curriculum/05-caching/01-caching.md) | 74 | 217 | 380 |
| [Caching Strategies](curriculum/05-caching/02-caching-strategies.md) | 175 | 504 | Approved exception |
| [Cache Eviction Policies](curriculum/05-caching/03-cache-eviction-policies.md) | 172 | 478 | Approved exception |
| [Distributed Caching](curriculum/05-caching/04-distributed-caching.md) | 183 | 483 | Approved exception |
| [Content Delivery Network (CDN)](curriculum/05-caching/05-content-delivery-network-cdn.md) | 40 | 165 | 188 |
| [APIs](curriculum/06-api-fundamentals/01-apis.md) | 161 | 437 | Approved exception |
| [REST, GraphQL, gRPC](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) | 47 | 255 | 441 |
| [API Gateway](curriculum/06-api-fundamentals/03-api-gateway.md) | 45 | 148 | 163 |
| [Idempotency](curriculum/06-api-fundamentals/04-idempotency.md) | 84 | 187 | 207 |
| [Rate Limiting](curriculum/06-api-fundamentals/05-rate-limiting.md) | 50 | 195 | 239 |
| [Long polling, WebSockets, Server-Sent Events (SSE)](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) | 47 | 194 | 234 |
| [Webhooks](curriculum/06-api-fundamentals/07-webhooks.md) | 180 | 476 | Approved exception |
| [API Design](curriculum/06-api-fundamentals/08-api-design.md) | 176 | 430 | Approved exception |
| [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md) | 44 | 137 | 140 |
| [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md) | 73 | 196 | 225 |
| [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md) | 62 | 175 | 181 |
| [Change Data Capture (CDC)](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md) | 164 | 467 | Approved exception |
| [N-tier architecture](curriculum/08-architectural-patterns/01-n-tier-architecture.md) | 53 | 115 | 121 |
| [Monoliths and Microservices](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md) | 47 | 228 | 389 |
| [Event-Driven Architecture (EDA)](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md) | 38 | 104 | 108 |
| [Event Sourcing](curriculum/08-architectural-patterns/04-event-sourcing.md) | 40 | 80 | 84 |
| [Command and Query Responsibility Segregation (CQRS)](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md) | 66 | 105 | 113 |
| [Enterprise Service Bus (ESB)](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md) | 54 | 85 | 92 |
| [Virtual Machines (VMs) and Containers](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md) | 42 | 157 | 175 |
| [Serverless Architecture](curriculum/08-architectural-patterns/08-serverless-architecture.md) | 173 | 421 | Approved exception |
| [Peer-to-Peer (P2P) Architecture](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md) | 158 | 461 | Approved exception |
| [Service Discovery](curriculum/09-reliability-and-microservices/01-service-discovery.md) | 39 | 111 | 132 |
| [HeartBeats](curriculum/09-reliability-and-microservices/02-heartbeats.md) | 155 | 441 | Approved exception |
| [Circuit breaker](curriculum/09-reliability-and-microservices/03-circuit-breaker.md) | 42 | 89 | 103 |
| [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md) | 33 | 78 | 80 |
| [Disaster recovery](curriculum/09-reliability-and-microservices/05-disaster-recovery.md) | 45 | 93 | 101 |
| [Consensus Algorithms](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md) | 188 | 500 | Approved exception |
| [Distributed Locking](curriculum/09-reliability-and-microservices/07-distributed-locking.md) | 178 | 494 | Approved exception |
| [Gossip Protocol](curriculum/09-reliability-and-microservices/08-gossip-protocol.md) | 162 | 464 | Approved exception |
| [Distributed Tracing](curriculum/09-reliability-and-microservices/09-distributed-tracing.md) | 180 | 499 | Approved exception |
| [SSL, TLS, mTLS](curriculum/10-security-and-location/01-ssl-tls-mtls.md) | 43 | 106 | 122 |
| [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md) | 50 | 176 | 180 |
| [Single Sign-On (SSO)](curriculum/10-security-and-location/03-single-sign-on-sso.md) | 37 | 194 | 236 |
| [Geohashing and Quadtrees](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md) | 41 | 181 | 216 |
| [System Design Interviews](practice/INTERVIEW-APPROACH.md) | 118 | 236 | 263 |
| [Netflix](practice/netflix.md) | 152 | 597 | 934 |
| [Twitter](practice/twitter.md) | 152 | 599 | 898 |
| [Uber](practice/uber.md) | 152 | 596 | 917 |
| [URL Shortener](practice/url-shortener.md) | 153 | 577 | 774 |
| [WhatsApp](practice/whatsapp.md) | 152 | 593 | 876 |
