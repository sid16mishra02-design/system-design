# HeartBeats

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A signal that a participant was recently reachable

A heartbeat is a periodic “I am here” signal. Another component tracks the last signal and suspects trouble if no new signal arrives within a chosen timeout.

Suppose workers report every five seconds. A monitor marks a worker suspect after fifteen seconds without a report. This is a design choice, not proof that every failure will be detected within exactly fifteen seconds.

A missed heartbeat can mean a crashed process, a slow network, a paused runtime, or an overloaded receiver. A heartbeat's arrival also does not prove the worker's database access or business operations are healthy.

Shorter timeouts can detect trouble sooner but produce more false alarms. Longer timeouts reduce false alarms while delaying reaction. Real designs often combine multiple signals and use separate readiness checks.

**Check:** a service-discovery system should not blindly send traffic forever just because a process is still sending a small heartbeat message.

## Where this comes into play

Heartbeats support failure suspicion in worker pools, cluster membership, leases, and leader monitoring. They answer whether a signal recently arrived, which is narrower than proving an entire service is healthy.

## Work through a timeout

Assume a worker reports every five seconds and a monitor marks it suspect after fifteen seconds without an arrival. If the worker pauses for twenty seconds, a replacement may begin work while the old worker later resumes. That can create overlapping execution unless the work is fenced, idempotent, or otherwise coordinated.

A failure immediately after a heartbeat and a failure just before the next one may be noticed at different times. Network delay and monitor scheduling also affect detection. Do not promise an exact recovery bound from the interval alone.

## How to tune it

Choose the interval and suspicion threshold using observed delay, pause behavior, and acceptable detection time. Tolerating several missed reports can reduce false alarms at the cost of slower detection. Randomizing report timing can reduce synchronized bursts from thousands of workers.

Separate liveness from readiness. Liveness asks whether a process is operating; readiness asks whether it should receive the relevant traffic. A process can emit heartbeats while every order request fails because its database connection is broken.

## How to verify improvement

Test a real crash, packet delay, a network partition, a long process pause, and an overloaded monitor. Record detection delay and false suspicions, then verify that any replacement action cannot violate the business invariant.

## Optional further reading

- [Additional explanation](https://blog.algomaster.io/p/heartbeats-in-distributed-systems)

Optional references provide more detail; they are not required to follow this lesson.
