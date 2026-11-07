# Serverless Architecture

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Let a platform manage more of the runtime

Serverless does not mean no servers exist. It means the provider manages much of provisioning and running the execution environment. Functions triggered by requests or events are one common form; managed services also play a role.

Example: a photo upload creates an event that invokes a function to generate a thumbnail. The function reads the photo, writes a thumbnail, and finishes. When no uploads arrive, there need not be a continuously running application worker allocated in the same way.

Benefits can include reduced infrastructure management and scaling with demand. Constraints can include cold-start delay, execution limits, concurrency limits, and dependence on provider-specific services. Pricing depends on actual usage and the platform's model.

Do not assume memory from one invocation will be available to the next. Store durable state externally. Event-triggered execution can repeat work, so use safe output keys or another duplicate-handling rule.

**Check:** a task requiring a long-lived connection or hours of uninterrupted processing needs a runtime whose lifecycle and limits actually support it.

## Optional further reading

- [Additional explanation](https://blog.algomaster.io/p/2edeb23b-cfa5-4b24-845e-3f6f7a39d162)

The lesson above is complete enough for this curriculum; external links are for deeper study.
