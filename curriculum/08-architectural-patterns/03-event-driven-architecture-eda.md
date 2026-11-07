[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

An order is saved, but a crash prevents shipping from hearing about it. What information must survive? Should checkout success mean shipping already finished?
<!-- END INQUIRY -->

<!-- BEGIN ORIGINAL TOPIC -->
# Event-Driven Architecture (EDA)

Event-Driven Architecture (EDA) is about using events as a way to communicate within a system. Generally, leveraging a message broker to publish and consume events asynchronously. The publisher is unaware of who is consuming an event and the consumers are unaware of each other. Event-Driven Architecture is simply a way of achieving loose coupling between services within a system.

## What is an event?

An event is a data point that represents state changes in a system. It doesn't specify what should happen and how the change should modify the system, it only notifies the system of a particular state change. When a user makes an action, they trigger an event.

## Components

Event-driven architectures have three key components:

- **Event producers**: Publishes an event to the router.
- **Event routers**: Filters and pushes the events to consumers.
- **Event consumers**: Uses events to reflect changes in the system.

![event-driven-architecture](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-III/event-driven-architecture/event-driven-architecture.png)

_Note: Dots in the diagram represents different events in the system._

## Patterns

There are several ways to implement the event-driven architecture, and which method we use depends on the use case but here are some common examples:

- [Sagas](../04-distributed-data/03-distributed-transactions.md#sagas)
- [Publish-Subscribe](../07-asynchronous-communication/03-publish-subscribe.md)
- [Event Sourcing](04-event-sourcing.md)
- [Command and Query Responsibility Segregation (CQRS)](05-command-and-query-responsibility-segregation-cqrs.md)

_Note: Each of these methods is discussed separately._

## Advantages

Let's discuss some advantages:

- Decoupled producers and consumers.
- Highly scalable and distributed.
- Easy to add new consumers.
- Improves agility.

## Challenges

Here are some challenges of event-drive architecture:

- Guaranteed delivery.
- Error handling is difficult.
- Event-driven systems are complex in general.
- Exactly once, in-order processing of events.

## Use cases

Below are some common use cases where event-driven architectures are beneficial:

- Metadata and metrics.
- Server and security logs.
- Integrating heterogeneous systems.
- Fanout and parallel processing.

## Examples

Here are some widely used technologies for implementing event-driven architectures:

- [NATS](https://nats.io)
- [Apache Kafka](https://kafka.apache.org)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge)
- [Amazon SNS](https://aws.amazon.com/sns)
- [Google PubSub](https://cloud.google.com/pubsub)
<!-- END ORIGINAL TOPIC -->

<!-- BEGIN ANIMATION -->
## Watch the sequence

![Pub/sub: one event, independent business reactions](../../assets/animations/pub-sub.gif)

[Read the numbered steps](../../animations/pub-sub.md) · [View the still sequence](../../assets/animations/pub-sub-steps.png)
<!-- END ANIMATION -->

## Make it concrete

EDA lets consumers react after the initiating action commits. Save the order and an outbox event together; a relay publishes committed events. This closes the save-then-publish crash gap.

Give events identifiers and consumers duplicate-safe processing. Expect delay and reordering. Show shipping as pending until processed. Scale consumers using backlog age and downstream capacity; more workers cannot fix one overloaded database.

For example, storing OrderPlaced in an outbox row within the order transaction gives a relay something durable to find after a restart. Publication can repeat if the relay crashes after sending but before recording progress. The shipping consumer must therefore recognize repeated event identifiers where it writes its business result, not only in temporary memory.

An event states something that happened; it does not imply every reaction has completed. Record shipping progress separately and provide a way to retry or investigate failed processing. Queue depth alone is insufficient: observe the age of the oldest work and the useful processing rate. A continually growing delay means buffering is hiding a capacity or dependency problem.

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
