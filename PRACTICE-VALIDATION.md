# Practice-category validation

[← Full category/topic audit](TOPIC-VALIDATION.md) · [Animations](animations/README.md)

Categories 11–13 are reviewed here: eleven tradeoff comparisons, the interview method, and five complete system designs. This complements the 71 fundamental topics, bringing coverage to **88 learning items across all 13 categories**.

| Category / item | Fundamental evidence | Problem / application evidence | Visual |
| --- | --- | --- | --- |
| 11-tradeoffs: [Vertical vs horizontal scaling](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A shop adds application servers while all requests still reach one saturated shared database. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | Static method/comparison sufficient |
| 11-tradeoffs: [Concurrency vs parallelism](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A product page makes independent remote calls; overlapping their waits differs from running CPU work on several cores. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [concurrency-parallelism](animations/concurrency-parallelism.md) |
| 11-tradeoffs: [Long polling vs WebSockets](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A frequently interactive editor exchanges updates both ways, while another client can use repeated held requests. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [realtime-protocols](animations/realtime-protocols.md) |
| 11-tradeoffs: [Batch vs stream processing](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A shop produces a nightly sales report and also evaluates time-sensitive fraud signals. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [batch-stream](animations/batch-stream.md) |
| 11-tradeoffs: [Stateful vs stateless design](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A load balancer routes consecutive shopping-session requests to different application servers. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [load-balancer](animations/load-balancer.md) |
| 11-tradeoffs: [Strong vs eventual consistency](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A profile display may show an older value, while reserving the last ticket must preserve the no-duplicate-sale invariant. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [replication](animations/replication.md), [cap-partition](animations/cap-partition.md) |
| 11-tradeoffs: [Read-through vs write-through cache](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A product cache loads a price after a read miss, while a write path persists a later price update synchronously. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [read-write-through](animations/read-write-through.md) |
| 11-tradeoffs: [Push vs pull](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A checkout needs payment status from an independent provider. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [push-pull](animations/push-pull.md) |
| 11-tradeoffs: [REST vs RPC](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A shop exposes product resources to clients and an inventory-reservation operation between cooperating services. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | Static method/comparison sufficient |
| 11-tradeoffs: [Synchronous vs asynchronous communication](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A shop confirms an order while an email worker sends its receipt later. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [sync-async](animations/sync-async.md) |
| 11-tradeoffs: [Latency vs throughput](practice/TRADEOFFS.md) | [Definition](practice/TRADEOFFS.md#compare-your-reasoning) | A checkout service adds workers and completes more requests per second, but each successful checkout still takes the same time. [Evidence](practice/TRADEOFFS.md#compare-your-reasoning) | [concurrency-parallelism](animations/concurrency-parallelism.md), [request-latency](animations/request-latency.md) |
| 12-interview-method: [System Design Interviews](practice/INTERVIEW-APPROACH.md) | [Definition](practice/INTERVIEW-APPROACH.md#requirements-clarifications) | A practice design contains a 200 ms read whose repeated database queries consume 150 ms, so the candidate must justify an optimization rather than add unrelated components. [Evidence](practice/INTERVIEW-APPROACH.md#turn-an-optimization-into-an-argument) | Static method/comparison sufficient |
| 13-system-designs: [URL Shortener](practice/url-shortener.md) | [Definition](practice/url-shortener.md#what-is-a-url-shortener) | A campaign makes one link viral while a 20,000-redirects/second workload has a 95% cache hit rate; the link owner may later disable that link. [Evidence](practice/url-shortener.md#optimize-the-bottleneck-you-measured) | [case-url-shortener](animations/case-url-shortener.md) |
| 13-system-designs: [WhatsApp](practice/whatsapp.md) | [Definition](practice/whatsapp.md#follow-one-message) | A recipient disconnects after message 41 but before acknowledgement, reconnects through another server, and must resume without duplicate visible messages. [Evidence](practice/whatsapp.md#test-ordering-and-failure) | [case-whatsapp](animations/case-whatsapp.md) |
| 13-system-designs: [Twitter](practice/twitter.md) | [Definition](practice/twitter.md#follow-one-post-and-one-feed-read) | A chronological feed receives 1,000 posts/second with 300 followers per post, while a celebrity post creates a much larger fanout burst and some distribution workers lag. [Evidence](practice/twitter.md#optimize-the-measured-bottleneck) | [case-twitter](animations/case-twitter.md) |
| 13-system-designs: [Netflix](practice/netflix.md) | [Definition](practice/netflix.md#follow-upload-and-playback-separately) | A new title launches into cold regional caches while 2,000 concurrent viewers request roughly 4 megabits/second each. [Evidence](practice/netflix.md#optimize-the-measured-bottleneck) | [case-netflix](animations/case-netflix.md) |
| 13-system-designs: [Uber](practice/uber.md) | [Definition](practice/uber.md#follow-location-and-assignment-separately) | Two passengers discover the same driver while location reports may be delayed, and a 100,000-driver fleet changes reporting frequency from five seconds to one second. [Evidence](practice/uber.md#protect-correctness-while-scaling) | [case-uber](animations/case-uber.md) |

## Vertical vs horizontal scaling

- **Fundamental:** “Larger machine vs more machines.”
- **Problem solved:** Choose a capacity change for an overloaded stage without assuming that every shared dependency scales with it.
- **Design scenario:** A shop adds application servers while all requests still reach one saturated shared database.
- **Application:** Locate the saturated component rather than treating the whole system as one box. → Compare more resources on that component with distributing its work across instances. → Trace the shared database path and verify whether it remains the limiting stage after application scaling.
- **Tradeoff:** A larger instance has practical capacity limits; more instances require suitable work distribution and do not automatically increase shared database capacity.
- **Evidence:** “Check the shared database bottleneck.”
- **Visual decision:** A static larger-machine versus multiple-machines diagram with the shared dependency highlighted is sufficient.

## Concurrency vs parallelism

- **Fundamental:** “Managing overlapping tasks vs executing tasks at the same time.”
- **Problem solved:** Distinguish overlapping in-progress tasks from simultaneous execution when trying to remove waiting or add compute capacity.
- **Design scenario:** A product page makes independent remote calls; overlapping their waits differs from running CPU work on several cores.
- **Application:** Identify which tasks are independent and which depend on earlier results. → Overlap independent remote waits where appropriate, while bounding in-flight work. → For CPU work, determine whether simultaneous execution and available cores actually provide extra capacity. → Measure the critical path and throughput instead of equating more in-progress requests with faster completion.
- **Tradeoff:** Concurrency can hide waiting without adding simultaneous CPU execution; excess in-flight work can overload dependencies.
- **Evidence:** “One cook can alternate tasks; several cooks can work simultaneously.”
- **Visual decision:** A single-worker interleaving timeline versus multiple workers executing simultaneously exposes the distinction clearly.

## Long polling vs WebSockets

- **Fundamental:** “Repeated waiting requests vs a persistent two-way connection.”
- **Problem solved:** Select an update transport based on interaction direction, frequency, and recovery requirements rather than a universal faster/slower label.
- **Design scenario:** A frequently interactive editor exchanges updates both ways, while another client can use repeated held requests.
- **Application:** State whether messages travel one way or both ways and how frequently they are expected. → Compare a held request that is renewed after each response with a persistent two-way connection. → Define what happens after disconnection, including backoff and recovering missed updates. → Measure active connections, delivery delay, and buffer use.
- **Tradeoff:** Persistent communication avoids repeated request cycles but adds connection lifecycle and buffering responsibilities; neither transport supplies durable history automatically.
- **Evidence:** “Use message direction, frequency, and reconnect behavior to choose.”
- **Visual decision:** Renewed long-poll requests and persistent bidirectional messages are behaviors over time; the existing real-time communication sequence can illustrate them.

## Batch vs stream processing

- **Fundamental:** “Process accumulated records together vs process a continuing flow.”
- **Problem solved:** Choose processing cadence according to the age of data the business can tolerate and the overhead of processing it.
- **Design scenario:** A shop produces a nightly sales report and also evaluates time-sensitive fraud signals.
- **Application:** Specify the maximum acceptable delay separately for the report and the fraud signal. → Accumulate suitable report records for a batch while processing time-sensitive changes continuously. → Define replay and progress tracking so restarts do not lose or double-apply changes. → Measure waiting introduced by batching together with downstream freshness and processing cost.
- **Tradeoff:** Larger batches can amortize processing overhead but delay results; continuous processing favors freshness while requiring ongoing progress and failure management.
- **Evidence:** “Nightly sales reports favor batches; live fraud signals need timely updates.”
- **Visual decision:** Show identical arriving records waiting for a batch boundary versus entering continuous processing; CDC/replay timing provides a related existing sequence.

## Stateful vs stateless design

- **Fundamental:** “Requests depend on server-local session state vs portable request context.”
- **Problem solved:** Avoid making a user's next request depend on the same application instance remaining available.
- **Design scenario:** A load balancer routes consecutive shopping-session requests to different application servers.
- **Application:** Identify session information that exists only in one application process. → Make required request context portable or place shared session data in a deliberately designed external store. → Route the next request to another instance and verify authorization and session behavior. → Account for availability, freshness, and access costs of the shared state dependency.
- **Tradeoff:** Stateless application instances simplify replacement and routing, but the system still has durable business state and may depend on shared session infrastructure.
- **Evidence:** “With an external session store, another app server can handle the next request.”
- **Visual decision:** Route the same session first to A and then B, contrasting missing local memory with a shared store; the failure occurs between requests.

## Strong vs eventual consistency

- **Fundamental:** “Reads reflect completed writes vs replicas converge after writes stop and communication recovers.”
- **Problem solved:** Choose observable data guarantees per operation while defining whether temporary stale reads are acceptable.
- **Design scenario:** A profile display may show an older value, while reserving the last ticket must preserve the no-duplicate-sale invariant.
- **Application:** State the operation's correctness invariant and acceptable staleness. → Allow profile reads to use lagging replicas only within the product's policy. → Require an authoritative reservation decision before confirming a sale; define failure behavior when coordination is unavailable. → For eventual behavior, state the convergence assumptions: writes stop, communication recovers, and the replication/reconciliation mechanism can complete.
- **Tradeoff:** Serving stale values can preserve useful access with less coordination; stronger read guarantees may require waiting or rejecting requests. Eventual consistency requires convergence under its assumptions, not permanent arbitrary staleness.
- **Evidence:** “Profile display may tolerate lag; stock reservation needs an explicit correctness rule.”
- **Visual decision:** Show a completed write, a lagging read, and later convergence; contrast with a partition that prevents an authoritative reservation decision.

## Read-through vs write-through cache

- **Fundamental:** “The cache loads missed reads vs the cache layer persists writes synchronously.”
- **Problem solved:** Assign cache loading and persistence responsibilities without mistaking complementary read and write policies for mutually exclusive designs.
- **Design scenario:** A product cache loads a price after a read miss, while a write path persists a later price update synchronously.
- **Application:** Trace who loads the backing store when a requested price is absent. → Separately trace when a write is considered persisted and acknowledged. → Combine read-through and write-through where the requirements warrant both. → Define concurrent update, failure, and stale-value behavior rather than assuming the combination guarantees perfect freshness.
- **Tradeoff:** Read-through moves miss-loading responsibility into a layer; write-through adds synchronous persistence work to writes. They solve different sides of access and may coexist.
- **Evidence:** “A product cache can load read misses and synchronously persist writes; these policies can be combined.”
- **Visual decision:** Separate read-miss arrows from write-and-persist arrows, then overlay both policies in one cache; the existing caching sequence can supply part of this explanation.

## Push vs pull

- **Fundamental:** “Sender initiates delivery vs receiver requests updates.”
- **Problem solved:** Decide who initiates update delivery and how to avoid unnecessary requests or unhandled delivery failures.
- **Design scenario:** A checkout needs payment status from an independent provider.
- **Application:** Compare receiving a provider webhook with periodically requesting status. → For push, verify the sender and durably accept events before acknowledgement according to the provider contract. → Handle duplicates and out-of-order events, or define polling frequency and acceptable status delay for pull. → Measure timely business completion rather than only endpoint response speed.
- **Tradeoff:** Push can avoid repeated empty polls but requires a reachable and recoverable receiver; pull gives the receiver control over requests while introducing polling load and delay.
- **Evidence:** “A webhook pushes payment news; polling repeatedly asks for it.”
- **Visual decision:** A provider-initiated webhook compared with repeated receiver-initiated checks makes request ownership and delay visible.

## REST vs RPC

- **Fundamental:** “Resource-oriented interfaces vs calling defined operations.”
- **Problem solved:** Choose an interface model without assuming it supplies the service's business correctness or storage consistency guarantees.
- **Design scenario:** A shop exposes product resources to clients and an inventory-reservation operation between cooperating services.
- **Application:** Identify whether clients primarily manipulate resources or invoke defined service operations. → Specify the product-read or reservation contract, including errors, authorization, and retries. → Keep inventory correctness independent of the interface label and enforce the invariant in the service/data design. → Measure end-to-end backend work rather than choosing solely from a REST-versus-RPC speed stereotype.
- **Tradeoff:** Resource semantics and typed operation contracts suit different client and service needs; neither automatically selects a consistency model.
- **Evidence:** “Use resource reads for products; typed service operations can reserve inventory.”
- **Visual decision:** A static pair of resource and operation requests, with identical invariant requirements, is sufficient.

## Synchronous vs asynchronous communication

- **Fundamental:** “Caller waits for completion vs completion is decoupled from the initiating call.”
- **Problem solved:** Decide which work must finish before responding and which can safely complete later without misrepresenting business state.
- **Design scenario:** A shop confirms an order while an email worker sends its receipt later.
- **Application:** Specify what order confirmation guarantees and which email work may remain pending. → Durably record or enqueue the deferred work with recovery for the handoff. → Acknowledge completion at the appropriate stage and make repeated email jobs safe. → Monitor queue age and failure recovery instead of treating a fast initial response as proof that email completed.
- **Tradeoff:** Deferring work can shorten the initiating request but adds lag, queue state, retry handling, and truthful pending-status requirements.
- **Evidence:** “Queued email can finish after the order confirmation.”
- **Visual decision:** Show the order response returning before the email worker completes; queue delivery and acknowledgement sequences make the distinction concrete.

## Latency vs throughput

- **Fundamental:** “Time for one operation vs operations completed per unit time.”
- **Problem solved:** Avoid confusing increased total capacity with a shorter wait or execution time for each request.
- **Design scenario:** A checkout service adds workers and completes more requests per second, but each successful checkout still takes the same time.
- **Application:** Measure per-operation durations and completed operations per interval separately. → Trace the slow request's critical path before optimizing latency. → Add capacity or reduce service work where saturation limits throughput. → Retest under representative load and inspect waiting, tail latency, errors, and the next shared bottleneck.
- **Tradeoff:** More workers can increase completed requests without shortening individual service time; excessive concurrency can instead increase queuing and tail latency.
- **Evidence:** “More counters can serve more customers without shortening each individual checkout.”
- **Visual decision:** A moving sequence can keep each customer's service duration constant while changing how many customers finish in the interval.

## System Design Interviews

- **Fundamental:** “Asking questions about the exact scope of the problem, and clarifying functional requirements early in the interview is essential.”
- **Problem solved:** Turns an ambiguous design prompt into explicit scope, measurable requirements, defensible architecture, and a reasoned discussion of bottlenecks and failures.
- **Design scenario:** A practice design contains a 200 ms read whose repeated database queries consume 150 ms, so the candidate must justify an optimization rather than add unrelated components.
- **Application:** Clarify scope, functional behavior, scale, latency, availability, and failure assumptions. → Estimate with units, define interfaces and data, then draw a complete request path. → Identify one observed bottleneck, propose a change, explain its new costs and failure modes, and compare the same workload before and after.
- **Tradeoff:** Optimize a demonstrated bottleneck with explicit freshness, write, or failure costs; a queue does not automatically shorten a synchronous database query.
- **Evidence:** “Suppose a read currently takes 200 ms, with 150 ms spent on repeated database queries. Say what you would measure, propose caching or a query improvement, then explain freshness or write costs.”
- **Visual decision:** The structured method, timing guide, worked bottleneck example, and worksheet are adequately expressed as static steps; there is no system-state race that requires animation.

## URL Shortener

- **Fundamental:** “A URL shortener service creates an alias or a short URL for a long URL.”
- **Problem solved:** Creates unique short aliases and serves high-volume redirects while preserving update, deletion, and abuse rules.
- **Design scenario:** A campaign makes one link viral while a 20,000-redirects/second workload has a 95% cache hit rate; the link owner may later disable that link.
- **Application:** Create a mapping while enforcing short-code uniqueness in authoritative storage; retry generation after collisions. → Trace redirect service, cached mapping, database miss, and destination response, keeping acceptable delayed analytics off the critical path. → Measure miss load and viral-key behavior, coalesce simultaneous reloads, and enforce expiry or invalidation needed for edits and disabled links.
- **Tradeoff:** Local and shared caches reduce redirect and database work but create stale copies; long cache lifetimes can conflict with disabling or editing a link.
- **Evidence:** “Under these simplified assumptions, database reads fall to about `20,000 × 0.05 = 1,000/second`.”
- **Visual decision:** Show cache hit and miss request paths, asynchronous analytics, and a disabled viral mapping remaining cached; this connects optimization to full request flow and invalidation correctness.

## WhatsApp

- **Fundamental:** “If the recipient is offline, retain the message for later retrieval.”
- **Problem solved:** Provides durable messaging across intermittent connections with explicit accepted, delivered, and read meanings, safe retries, and scalable recipient routing.
- **Design scenario:** A recipient disconnects after message 41 but before acknowledgement, reconnects through another server, and must resume without duplicate visible messages.
- **Application:** Record the message durably before acknowledging the chosen acceptance guarantee, and retain offline-recipient work. → Route to the server holding the current recipient connection, while handling stale connection-location information and reconnects. → Reuse stable message identifiers and enforce deduplication at the durable write, define ordering per conversation, and measure fanout attempts and backlog age.
- **Tradeoff:** Queueing absorbs bursts but does not add unlimited delivery capacity; conversation-scoped ordering permits parallel chats while global ordering adds coordination and a hot group can dominate work.
- **Evidence:** “Pause a worker after it records a message but before it acknowledges processing. On restart, verify that redelivery does not create a second visible message.”
- **Visual decision:** Animate accepted versus delivered states, offline storage, lost acknowledgement, repeated delivery, and reconnect to a new connection server so duplicate handling is part of the whole message flow.

## Twitter

- **Fundamental:** “On a write, store the post durably, then distribute references to the followers' timelines if using precomputed feeds.”
- **Problem solved:** Delivers follower feeds with an explicit balance between publication fanout cost, read latency, freshness, and visibility enforcement.
- **Design scenario:** A chronological feed receives 1,000 posts/second with 300 followers per post, while a celebrity post creates a much larger fanout burst and some distribution workers lag.
- **Application:** Store each post durably and decide whether follower timelines are precomputed references or assembled on reads. → Estimate timeline insertions per post and compare ordinary versus celebrity workloads before choosing a mixed fanout strategy. → Paginate and cache with correct visibility context, monitor post-to-feed lag, and enforce deletion or privacy rules even when old references remain.
- **Tradeoff:** Precomputed feeds make reads cheaper but amplify writes and lag; merging large authors at read time reduces massive write bursts while making reads perform additional work.
- **Evidence:** “One option is a mixed strategy: distribute ordinary authors' posts ahead of time, while merging very large authors' posts when a follower reads the feed.”
- **Visual decision:** Show publication, queued timeline fanout, delayed projection, and a follower read that merges a large-author path; then show why a deleted post reference must not expose content.

## Netflix

- **Fundamental:** “A rendition is one encoded version, such as a particular resolution and bitrate.”
- **Problem solved:** Prepares durable video variants and serves repeated media segments efficiently without placing encoding or large media transfers on the playback API path.
- **Design scenario:** A new title launches into cold regional caches while 2,000 concurrent viewers request roughly 4 megabits/second each.
- **Application:** Store an upload and generate renditions in retry-safe background jobs; publish usable manifests only when required outputs are ready. → Trace playback manifest and media-segment requests separately from login and application APIs. → Use regionally reusable segments and appropriate cache keys, choose renditions for device and network conditions, and measure startup delay, buffering, quality, and origin traffic under cold caches.
- **Tradeoff:** More renditions improve adaptation while increasing encoding and storage; lower bitrates can reduce buffering at a quality cost, and warm-cache success does not establish cold-launch origin capacity.
- **Evidence:** “Cache reusable segments near viewers through a CDN. A warm popular segment can serve many viewers without each request reaching origin storage.”
- **Visual decision:** Animate upload-to-rendition preparation independently of manifest/segment playback, with CDN hits and cold misses; show that adding login servers does not remove media bandwidth demand.

## Uber

- **Fundamental:** “Candidate discovery does not reserve a driver.”
- **Problem solved:** Finds suitably fresh nearby candidates and assigns a limited driver resource without letting simultaneous requests create conflicting assignments.
- **Design scenario:** Two passengers discover the same driver while location reports may be delayed, and a 100,000-driver fleet changes reporting frequency from five seconds to one second.
- **Application:** Index observed driver locations with timestamps and query neighboring spatial cells before checking exact distance and freshness. → Apply a conditional available-to-assigned transition to the selected candidate; if it fails, choose another candidate rather than trust the earlier search. → Tune update intervals and partitioning against observed movement, freshness needs, hotspot load, and matching latency; rehearse delayed updates and assignment timeouts.
- **Tradeoff:** Fresher updates increase bandwidth and write load; finer cells or partitions reduce some candidate work but add lookups and boundary coordination, and approximate discovery cannot replace authoritative assignment.
- **Evidence:** “Use an atomic conditional update or another explicit coordination mechanism to move a driver from available to assigned.”
- **Visual decision:** Animate location update, neighboring-cell discovery, two simultaneous passenger selections, and the atomic assignment where only one wins; include stale locations and retrying another candidate.
