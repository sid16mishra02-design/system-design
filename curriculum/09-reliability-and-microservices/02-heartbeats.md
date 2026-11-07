# HeartBeats

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A signal that a participant was recently reachable

A heartbeat is a periodic “I am here” signal. Another component tracks the last signal and suspects trouble if no new signal arrives within a chosen timeout.

Suppose workers report every five seconds. A monitor marks a worker suspect after fifteen seconds without a report. This is a design choice, not proof that every failure will be detected within exactly fifteen seconds.

A missed heartbeat can mean a crashed process, a slow network, a paused runtime, or an overloaded receiver. A heartbeat's arrival also does not prove the worker's database access or business operations are healthy.

Shorter timeouts can detect trouble sooner but produce more false alarms. Longer timeouts reduce false alarms while delaying reaction. Real designs often combine multiple signals and use separate readiness checks.

**Check:** a service-discovery system should not blindly send traffic forever just because a process is still sending a small heartbeat message.

## Optional further reading

- [Additional explanation](https://blog.algomaster.io/p/heartbeats-in-distributed-systems)

The lesson above is complete enough for this curriculum; external links are for deeper study.
