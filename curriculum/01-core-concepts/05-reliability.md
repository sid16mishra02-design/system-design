# Reliability

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## What it means

A reliable service keeps doing its intended job correctly over time, including when expected problems happen. Being reachable is only part of that: an available checkout that charges the wrong amount is not behaving reliably.

Imagine a food-ordering app. One payment request is retried because a response was lost. A reliable design avoids charging twice, preserves the order, and makes its actual status recoverable.

**Fault tolerance** means continuing useful operation despite some faults. **Failover** means switching work to a replacement, such as promoting a replica after a primary fails. A replacement must have usable data, and clients must be redirected to it; simply having another server is insufficient.

Draw payment request → recorded payment → order update. Mark what happens if the process stops between each pair of steps. This is a better reliability exercise than adding extra boxes without describing their behavior.

**Check:** a backup exists, but restoring it takes a day. It improves recovery options; it does not prove the service can remain available during a failure.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/reliability)

The lesson above is complete enough for this curriculum; external links are for deeper study.
