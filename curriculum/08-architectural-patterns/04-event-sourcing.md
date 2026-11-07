[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN ORIGINAL TOPIC -->
# Event Sourcing

Instead of storing just the current state of the data in a domain, use an append-only store to record the full series of actions taken on that data. The store acts as the system of record and can be used to materialize the domain objects.

![event-sourcing](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-III/event-sourcing/event-sourcing.png)

This can simplify tasks in complex domains, by avoiding the need to synchronize the data model and the business domain, while improving performance, scalability, and responsiveness. It can also provide consistency for transactional data, and maintain full audit trails and history that can enable compensating actions.

## Event sourcing vs Event-Driven Architecture (EDA)

Event sourcing is seemingly constantly being confused with [Event-driven Architecture (EDA)](03-event-driven-architecture-eda.md). Event-driven architecture is about using events to communicate between service boundaries. Generally, leveraging a message broker to publish and consume events asynchronously within other boundaries.

Whereas, event sourcing is about using events as a state, which is a different approach to storing data. Rather than storing the current state, we're instead going to be storing events. Also, event sourcing is one of the several patterns to implement an event-driven architecture.

## Advantages

Let's discuss some advantages of using event sourcing:

- Excellent for real-time data reporting.
- Great for fail-safety, data can be reconstituted from the event store.
- Extremely flexible, any type of message can be stored.
- Preferred way of achieving audit logs functionality for high compliance systems.

## Disadvantages

Following are the disadvantages of event sourcing:

- Requires an extremely efficient network infrastructure.
- Requires a reliable way to control message formats, such as a schema registry.
- Different events will contain different payloads.
<!-- END ORIGINAL TOPIC -->

<!-- BEGIN ANIMATION -->
## Watch the sequence

<details>
<summary>Open the looping animation</summary>

![Event sourcing: replay builds state](../../assets/animations/event-sourcing.gif)

</details>

[Read the numbered steps](../../animations/event-sourcing.md) · [View the still sequence](../../assets/animations/event-sourcing-steps.png)
<!-- END ANIMATION -->

## Make it concrete

### Rebuild state from business history

Deposited(100), then Withdrawn(30), produces balance 70. Stored events are authoritative; publishing notifications alone is not event sourcing.

Use it when historical decisions and replay matter. To shorten replay, load a verified snapshot and apply later events. Snapshots do not replace the event history. Version event schemas deliberately, and separate replay from external actions so rebuilding a view does not resend receipts.

**Check:** can you rebuild the balance without charging or emailing anyone again?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
