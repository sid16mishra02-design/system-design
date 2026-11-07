[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

A payment times out. Should another click create another charge?
<!-- END INQUIRY -->

<!-- BEGIN ORIGINAL TOPIC -->
# What is system design?

Before we start this course, let's talk about what even is system design.

System design is the process of defining the architecture, interfaces, and data
for a system that satisfies specific requirements. System design meets the needs
of your business or organization through coherent and efficient systems. It requires
a systematic approach to building and engineering systems. A good system design requires
us to think about everything, from infrastructure all the way down to the data and how it's stored.

## Why is System Design so important?

System design helps us define a solution that meets the business requirements. It is
one of the earliest decisions we can make when building a system. Often it is essential
to think from a high level as these decisions are very difficult to correct later. It
also makes it easier to reason about and manage architectural changes as the system evolves.
<!-- END ORIGINAL TOPIC -->

## Make it concrete

Trace order → payment → restaurant. Specify correctness, response time, and failure behavior before choosing components. If payment times out, recover the same operation safely; faster servers alone cannot prevent duplicate charges.

### Reason from the user's promise

Imagine the restaurant accepts the order, but the payment response disappears. The customer sees a spinner. Starting with “we need three microservices” does not tell you whether to retry the charge or cancel dinner. Start with the promise instead: one confirmed order must correspond to the intended payment, and an uncertain result must be recoverable.

Write the sequence of events, the data each step needs, and what the user sees after a failure. This exposes responsibilities before you name products. A single application and database may meet the first version's needs. Introduce a queue, cache, or service boundary only when a requirement explains the additional moving part.

**Try again:** the restaurant is closed after payment succeeds. What state must you record, who performs recovery, and what should the customer see while a refund is pending?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
