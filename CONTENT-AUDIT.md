# Content preservation audit

[← Start here](README.md) · [Credits and licenses](ATTRIBUTION.md)

All 57 course and case-study topics are readable in full on their own lesson pages. Their marked original excerpts preserve the course wording, code, and examples. Course cross-reference destinations are relocated to the matching local lessons; platform line endings may differ. Original source snapshot files also remain byte-identical to the pinned snapshot hashes.

The 82 course images referenced by those excerpts are cached unchanged inside this repository. Only their Markdown destinations move from the original remote image host to `assets/source-diagrams/`. The source URLs and byte hashes are recorded in `metadata/localized-source-images.json`.

Copied topic wording has 0% changes. The table counts independent teaching additions, including opening scenarios, thinking questions, applied explanations, and checkpoints. Practice pages count their instructions. Newly written comparison-table rows are also assigned to their corresponding topic. Navigation and attribution labels are outside the teaching count.

The owner approved going beyond the initial 30% guideline where understanding needs more space, and removing or improving weak independent text. Added percentages below report the actual edition; they are not capped or presented as compliance with the old limit. Source excerpts remain intact. The metadata explicitly flags additions above the original guideline.

Word definition: sequences of word characters, optionally joined by apostrophes or hyphens. The same rule applies to original topics and additions.

| Topic | Original words | Source edits | Added teaching words | Added % |
| --- | ---: | ---: | ---: | ---: |
| [What is system design?](curriculum/01-core-concepts/01-what-is-system-design.md) | 151 | 0% | 227 | 150.33% |
| [Scalability](curriculum/01-core-concepts/02-scalability.md) | 167 | 0% | 267 | 159.88% |
| [Availability](curriculum/01-core-concepts/03-availability.md) | 446 | 0% | 280 | 62.78% |
| [IP](curriculum/02-networking/01-ip.md) | 451 | 0% | 274 | 60.75% |
| [OSI Model](curriculum/02-networking/02-osi-model.md) | 667 | 0% | 220 | 32.98% |
| [TCP and UDP](curriculum/02-networking/03-tcp-and-udp.md) | 347 | 0% | 263 | 75.79% |
| [Domain Name System (DNS)](curriculum/02-networking/04-domain-name-system-dns.md) | 1682 | 0% | 272 | 16.17% |
| [Proxy](curriculum/02-networking/05-proxy.md) | 471 | 0% | 276 | 58.6% |
| [Load Balancing](curriculum/02-networking/08-load-balancing.md) | 1131 | 0% | 293 | 25.91% |
| [Clustering](curriculum/02-networking/09-clustering.md) | 688 | 0% | 211 | 30.67% |
| [Storage](curriculum/03-databases/01-storage.md) | 834 | 0% | 216 | 25.9% |
| [Databases and DBMS](curriculum/03-databases/02-databases-and-dbms.md) | 563 | 0% | 183 | 32.5% |
| [SQL databases](curriculum/03-databases/03-sql-databases.md) | 401 | 0% | 271 | 67.58% |
| [NoSQL databases](curriculum/03-databases/04-nosql-databases.md) | 530 | 0% | 286 | 53.96% |
| [SQL vs NoSQL databases](curriculum/03-databases/05-sql-vs-nosql-databases.md) | 417 | 0% | 266 | 63.79% |
| [Indexes](curriculum/03-databases/06-indexes.md) | 472 | 0% | 282 | 59.75% |
| [Normalization and Denormalization](curriculum/03-databases/07-normalization-and-denormalization.md) | 1012 | 0% | 321 | 31.72% |
| [Transactions](curriculum/03-databases/08-transactions.md) | 316 | 0% | 241 | 76.27% |
| [ACID and BASE consistency models](curriculum/03-databases/09-acid-and-base-consistency-models.md) | 451 | 0% | 271 | 60.09% |
| [Database Replication](curriculum/03-databases/10-database-replication.md) | 374 | 0% | 261 | 69.79% |
| [Sharding](curriculum/03-databases/11-sharding.md) | 742 | 0% | 252 | 33.96% |
| [Consistent Hashing](curriculum/03-databases/12-consistent-hashing.md) | 932 | 0% | 261 | 28.0% |
| [Database Federation](curriculum/03-databases/13-database-federation.md) | 303 | 0% | 248 | 81.85% |
| [CAP Theorem](curriculum/04-distributed-data/01-cap-theorem.md) | 386 | 0% | 313 | 81.09% |
| [PACELC Theorem](curriculum/04-distributed-data/02-pacelc-theorem.md) | 171 | 0% | 224 | 130.99% |
| [Distributed Transactions](curriculum/04-distributed-data/03-distributed-transactions.md) | 656 | 0% | 317 | 48.32% |
| [Caching](curriculum/05-caching/01-caching.md) | 1267 | 0% | 243 | 19.18% |
| [Content Delivery Network (CDN)](curriculum/05-caching/05-content-delivery-network-cdn.md) | 628 | 0% | 299 | 47.61% |
| [REST, GraphQL, gRPC](curriculum/06-api-fundamentals/02-rest-graphql-grpc.md) | 1473 | 0% | 268 | 18.19% |
| [API Gateway](curriculum/06-api-fundamentals/03-api-gateway.md) | 546 | 0% | 400 | 73.26% |
| [Idempotency](curriculum/06-api-fundamentals/04-idempotency.md) | 693 | 0% | 318 | 45.89% |
| [Rate Limiting](curriculum/06-api-fundamentals/05-rate-limiting.md) | 799 | 0% | 192 | 24.03% |
| [Long polling, WebSockets, Server-Sent Events (SSE)](curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md) | 781 | 0% | 225 | 28.81% |
| [Message Brokers](curriculum/07-asynchronous-communication/01-message-brokers.md) | 467 | 0% | 275 | 58.89% |
| [Message Queues](curriculum/07-asynchronous-communication/02-message-queues.md) | 753 | 0% | 361 | 47.94% |
| [Publish-Subscribe](curriculum/07-asynchronous-communication/03-publish-subscribe.md) | 605 | 0% | 295 | 48.76% |
| [N-tier architecture](curriculum/08-architectural-patterns/01-n-tier-architecture.md) | 406 | 0% | 223 | 54.93% |
| [Monoliths and Microservices](curriculum/08-architectural-patterns/02-monoliths-and-microservices.md) | 1298 | 0% | 228 | 17.57% |
| [Event-Driven Architecture (EDA)](curriculum/08-architectural-patterns/03-event-driven-architecture-eda.md) | 360 | 0% | 228 | 63.33% |
| [Event Sourcing](curriculum/08-architectural-patterns/04-event-sourcing.md) | 280 | 0% | 231 | 82.5% |
| [Command and Query Responsibility Segregation (CQRS)](curriculum/08-architectural-patterns/05-command-and-query-responsibility-segregation-cqrs.md) | 377 | 0% | 230 | 61.01% |
| [Enterprise Service Bus (ESB)](curriculum/08-architectural-patterns/06-enterprise-service-bus-esb.md) | 307 | 0% | 227 | 73.94% |
| [Virtual Machines (VMs) and Containers](curriculum/08-architectural-patterns/07-virtual-machines-vms-and-containers.md) | 585 | 0% | 216 | 36.92% |
| [Service Discovery](curriculum/09-reliability-and-microservices/01-service-discovery.md) | 443 | 0% | 222 | 50.11% |
| [Circuit breaker](curriculum/09-reliability-and-microservices/03-circuit-breaker.md) | 344 | 0% | 221 | 64.24% |
| [SLA, SLO, SLI](curriculum/09-reliability-and-microservices/04-sla-slo-sli.md) | 267 | 0% | 232 | 86.89% |
| [Disaster recovery](curriculum/09-reliability-and-microservices/05-disaster-recovery.md) | 339 | 0% | 235 | 69.32% |
| [SSL, TLS, mTLS](curriculum/10-security-and-location/01-ssl-tls-mtls.md) | 408 | 0% | 224 | 54.9% |
| [OAuth 2.0 and OpenID Connect (OIDC)](curriculum/10-security-and-location/02-oauth-20-and-openid-connect-oidc.md) | 601 | 0% | 217 | 36.11% |
| [Single Sign-On (SSO)](curriculum/10-security-and-location/03-single-sign-on-sso.md) | 789 | 0% | 222 | 28.14% |
| [Geohashing and Quadtrees](curriculum/10-security-and-location/04-geohashing-and-quadtrees.md) | 723 | 0% | 228 | 31.54% |
| [System Design Interviews](practice/INTERVIEW-APPROACH.md) | 877 | 0% | 261 | 29.76% |
| [URL Shortener](practice/url-shortener.md) | 2581 | 0% | 629 | 24.37% |
| [WhatsApp](practice/whatsapp.md) | 2922 | 0% | 643 | 22.01% |
| [Twitter](practice/twitter.md) | 2995 | 0% | 646 | 21.57% |
| [Netflix](practice/netflix.md) | 3116 | 0% | 651 | 20.89% |
| [Uber](practice/uber.md) | 3058 | 0% | 643 | 21.03% |

## Twenty newly written lessons

These topics previously had only links, rather than reusable lesson text. The learner approved writing original explanations with an exception to the 30% addition limit for this group. These are not modified copies of the linked articles. Each keeps its external reference as optional further reading.

- [Latency vs Throughput vs Bandwidth](curriculum/01-core-concepts/04-latency-vs-throughput-vs-bandwidth.md): 1143 teaching words.
- [Reliability](curriculum/01-core-concepts/05-reliability.md): 543 teaching words.
- [SPOF](curriculum/01-core-concepts/06-spof.md): 464 teaching words.
- [HTTP/HTTPS](curriculum/02-networking/06-httphttps.md): 538 teaching words.
- [Checksums](curriculum/02-networking/07-checksums.md): 481 teaching words.
- [Bloom Filters](curriculum/03-databases/14-bloom-filters.md): 566 teaching words.
- [Caching Strategies](curriculum/05-caching/02-caching-strategies.md): 556 teaching words.
- [Cache Eviction Policies](curriculum/05-caching/03-cache-eviction-policies.md): 528 teaching words.
- [Distributed Caching](curriculum/05-caching/04-distributed-caching.md): 534 teaching words.
- [APIs](curriculum/06-api-fundamentals/01-apis.md): 497 teaching words.
- [Webhooks](curriculum/06-api-fundamentals/07-webhooks.md): 526 teaching words.
- [API Design](curriculum/06-api-fundamentals/08-api-design.md): 491 teaching words.
- [Change Data Capture (CDC)](curriculum/07-asynchronous-communication/04-change-data-capture-cdc.md): 520 teaching words.
- [Serverless Architecture](curriculum/08-architectural-patterns/08-serverless-architecture.md): 478 teaching words.
- [Peer-to-Peer (P2P) Architecture](curriculum/08-architectural-patterns/09-peer-to-peer-p2p-architecture.md): 516 teaching words.
- [HeartBeats](curriculum/09-reliability-and-microservices/02-heartbeats.md): 491 teaching words.
- [Consensus Algorithms](curriculum/09-reliability-and-microservices/06-consensus-algorithms.md): 556 teaching words.
- [Distributed Locking](curriculum/09-reliability-and-microservices/07-distributed-locking.md): 543 teaching words.
- [Gossip Protocol](curriculum/09-reliability-and-microservices/08-gossip-protocol.md): 513 teaching words.
- [Distributed Tracing](curriculum/09-reliability-and-microservices/09-distributed-tracing.md): 549 teaching words.

Run `python scripts/validate.py` to check excerpt preservation, actual teaching counts and expansion disclosures, all 71 local lessons, opening-scenario coverage, schedule coverage, and local links.

## Animation accounting

The requested visual layer is documented separately: 48 walkthroughs, captions, text transcripts, and still storyboards. Independent lesson notes and comparison rows are counted in the table above; animation narratives are additional teaching media and are not included in those prose percentages. See metadata/animations.json and ATTRIBUTION.md.
