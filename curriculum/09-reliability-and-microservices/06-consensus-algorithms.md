# Consensus Algorithms

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Agreeing on decisions despite some failures

Consensus protocols help cooperating nodes agree on decisions, such as the order of entries in a **replicated log**, the same ordered history kept on multiple nodes. Raft and Paxos address this under stated assumptions about faults and communication.

Assume nodes may stop, without deliberately sending false information: a **crash-fault** model. For a simple Raft example, imagine three voting servers: A, B, and C. A leader coordinates log replication. A majority can support progress under the protocol's rules. If A is isolated, B and C may elect a leader; A alone must not keep committing conflicting new decisions.

The point is not simply taking any majority vote. Election rules, log history, terms, and commit rules protect agreement. A split that leaves no communicating majority can stop progress even while every process is still running.

Consensus does not mean every reader automatically gets the latest value, or that the system tolerates malicious participants. Those properties require additional choices and fault assumptions.

**Check:** distinguish **safety**, avoiding conflicting committed decisions, from **liveness**, eventually making progress. A protocol may preserve safety while waiting for communication to recover.

## Where this comes into play

Use consensus-backed coordination when several nodes must maintain one agreed sequence of important decisions under a specified fault model: for example, cluster configuration or a replicated state machine. Do not introduce a consensus group merely because there are multiple application instances.

## Follow a simple replicated-log write

In a three-voter Raft group, a client sends a command to the leader. The leader replicates log entries and uses Raft's term, log, and majority rules to determine commitment. Once committed, entries are applied in the agreed order. “Two machines replied” is not a complete independent substitute for those rules.

With one voter unavailable, a communicating majority may still make progress. With no communicating majority, progress can stop while safety remains intact. Safety means avoiding conflicting committed decisions; liveness concerns eventually making progress when the necessary conditions hold.

## How to optimize without weakening correctness

Batch or pipeline suitable proposals to amortize network and storage overhead, accepting possible extra wait for a batch to fill. Reduce slow durable-write or network stages rather than skipping required persistence or quorum rules.

Place voting members according to the failure tolerance and latency requirements. Geographically distant voters can improve resilience to a local disaster while increasing communication delay. Adding voters is not the same as adding independent read servers and may increase coordination cost.

Use a well-understood implementation rather than improvising election and commit behavior from a majority-vote analogy.

## How to verify improvement

Measure commit latency and throughput, then test leader loss, partitions, delayed messages, and recovery. Verify that committed history remains consistent across failover; a fast benchmark with no failures does not establish protocol safety.

## Optional further reading

- [Additional explanation](https://medium.com/@sourabhatta1819/consensus-in-distributed-system-ac79f8ba2b8c)
- [Raft: paper and illustrated introduction](https://raft.github.io/)

Optional references provide more detail; they are not required to follow this lesson.
