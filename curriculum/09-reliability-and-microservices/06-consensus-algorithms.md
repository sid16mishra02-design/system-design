# Consensus Algorithms

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Agreeing on decisions despite some failures

Consensus protocols help cooperating nodes agree on decisions, such as the order of entries in a **replicated log**, the same ordered history kept on multiple nodes. Raft and Paxos address this under stated assumptions about faults and communication.

Assume nodes may stop, without deliberately sending false information: a **crash-fault** model. For a simple Raft example, imagine three voting servers: A, B, and C. A leader coordinates log replication. A majority can support progress under the protocol's rules. If A is isolated, B and C may elect a leader; A alone must not keep committing conflicting new decisions.

The point is not simply taking any majority vote. Election rules, log history, terms, and commit rules protect agreement. A split that leaves no communicating majority can stop progress even while every process is still running.

Consensus does not mean every reader automatically gets the latest value, or that the system tolerates malicious participants. Those properties require additional choices and fault assumptions.

**Check:** distinguish **safety**, avoiding conflicting committed decisions, from **liveness**, eventually making progress. A protocol may preserve safety while waiting for communication to recover.

## Optional further reading

- [Additional explanation](https://medium.com/@sourabhatta1819/consensus-in-distributed-system-ac79f8ba2b8c)
- [Raft: paper and illustrated introduction](https://raft.github.io/)

The lesson above is complete enough for this curriculum; external links are for deeper study.
