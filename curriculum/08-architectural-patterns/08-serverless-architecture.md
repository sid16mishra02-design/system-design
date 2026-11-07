# Serverless Architecture

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

A campaign sends one million image jobs after weeks of silence. Functions scale quickly, then cold starts delay the first users, retries duplicate processing, and concurrent invocations overwhelm the database. Which work benefits from on-demand execution, what limits downstream pressure, and which long-running or stateful task should remain elsewhere?
<!-- END INQUIRY -->

## Let a platform manage more of the runtime

Serverless does not mean no servers exist. It means the provider manages much of provisioning and running the execution environment. Functions triggered by requests or events are one common form; managed services also play a role.

Example: a photo upload creates an event that invokes a function to generate a thumbnail. The function reads the photo, writes a thumbnail, and finishes. When no uploads arrive, there need not be a continuously running application worker allocated in the same way.

Benefits can include reduced infrastructure management and scaling with demand. Constraints can include cold-start delay, execution limits, concurrency limits, and dependence on provider-specific services. Pricing depends on actual usage and the platform's model.

Do not assume memory from one invocation will be available to the next. Store durable state externally. Event-triggered execution can repeat work, so use safe output keys or another duplicate-handling rule.

**Check:** a task requiring a long-lived connection or hours of uninterrupted processing needs a runtime whose lifecycle and limits actually support it.

## Where this comes into play

Event-driven, bursty work such as image processing, lightweight integration handlers, and scheduled maintenance can fit function execution. Suitability depends on the platform's actual lifecycle, resource limits, and required state—not the label “serverless.”

## Work through thumbnail generation

An upload stores photo P and emits an event. A function reads P, creates a thumbnail, and stores the output under a deterministic key such as `P/version/thumbnail`. If the event repeats, the function can detect or safely replace the same output according to the chosen policy. Do not rely on one invocation's in-memory flag to prevent duplication across other invocations.

## How to optimize

Measure startup delay separately from execution time. Reuse safe initialized clients when the environment permits it, keep dependencies proportionate, and avoid repeatedly downloading unchanged configuration. Treat environment reuse as a possible optimization, not a guarantee that durable state will survive.

Tune memory, CPU allocation, batch size, and concurrency against the provider's model and actual measurements. Raising concurrency may finish a burst sooner while overwhelming a database connection limit. A queue and a concurrency bound can protect that dependency at the cost of waiting.

Warm-capacity options, where available, may reduce startup variation but introduce ongoing cost. Long or stateful work may fit another managed execution model better.

## How to verify improvement

Test cold and warm execution, retries, large events, bursts, and downstream saturation. Compare end-to-end completion time and cost per successful job, including retries and auxiliary services, rather than function duration alone.

## Optional further reading

- [Additional explanation](https://blog.algomaster.io/p/2edeb23b-cfa5-4b24-845e-3f6f7a39d162)

Optional references provide more detail; they are not required to follow this lesson.
