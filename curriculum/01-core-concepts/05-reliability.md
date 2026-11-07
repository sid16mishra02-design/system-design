# Reliability

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## What it means

A reliable service keeps doing its intended job correctly over time, including when expected problems happen. Being reachable is only part of that: an available checkout that charges the wrong amount is not behaving reliably.

Imagine a food-ordering app. One payment request is retried because a response was lost. A reliable design avoids charging twice, preserves the order, and makes its actual status recoverable.

**Fault tolerance** means continuing useful operation despite some faults. **Failover** means switching work to a replacement, such as promoting a replica after a primary fails. A replacement must have usable data, and clients must be redirected to it; simply having another server is insufficient.

Draw payment request → recorded payment → order update. Mark what happens if the process stops between each pair of steps. This is a better reliability exercise than adding extra boxes without describing their behavior.

**Check:** a backup exists, but restoring it takes a day. It improves recovery options; it does not prove the service can remain available during a failure.

## Where this comes into play

Use reliability reasoning whenever a user action spans multiple steps: creating an order, charging a payment, reserving stock, or sending a notification. The question is what the user can safely rely on when a step fails or a result is uncertain.

## Worked failure and recovery

Suppose payment succeeds but the order worker stops before updating the order. A naive retry can charge again. A more deliberate flow records a stable operation identifier, makes payment retries reuse it, and resumes the order update from durable state. A reconciliation job periodically compares recorded orders and payments to find unresolved states. This handles uncertainty explicitly instead of assuming every timeout means failure.

## How to improve the design

- Define the invariant first: for example, one successful charge per order attempt.
- Put durable boundaries around accepted work. A successful response should mean exactly what the API contract promises.
- Use timeouts and bounded retries with backoff, which means waiting longer between repeated attempts. Retrying every failed call immediately can overload a recovering dependency.
- Test failover and restore procedures, including what data may be missing afterward.
- Separate optional work. A receipt email failure should not necessarily make a completed payment appear to have failed.

Extra replicas, logs, and recovery jobs add operational cost. More components are useful only when their failure behavior is understood.

## How to verify improvement

Deliberately interrupt the flow after each durable step in a test environment. Confirm that retrying preserves the invariant and eventually resolves the order's state. Count duplicate charges, permanently stuck orders, and recovery time—not just successful HTTP responses.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/reliability)

Optional references provide more detail; they are not required to follow this lesson.
