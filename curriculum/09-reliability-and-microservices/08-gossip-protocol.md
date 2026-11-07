# Gossip Protocol

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Spread information through repeated peer exchanges

In a gossip protocol, nodes periodically exchange information with selected peers. Those peers spread what they know further. Repeated exchanges let knowledge travel through a cluster without every node contacting every other node each time.

Imagine A learns that a new member joined. A tells B; B later tells C. For a while, C may have an older membership view than A. The system must tolerate that temporary disagreement.

Gossip can help distribute membership and health observations. The exact protocol determines how versions, conflicting observations, failed nodes, and convergence are handled. A delay in receiving news is not proof that the sender is dead.

Gossip is not the same as consensus: spreading information does not by itself establish one agreed order of committed writes. Its usefulness depends on which information may safely propagate gradually.

**Check:** a cluster can use gossip for membership and a separate mechanism for deciding writes. One protocol need not solve both problems.

## Where this comes into play

Gossip is useful for disseminating membership and health observations in large groups without requiring one node to send every update directly to everyone. Its suitability depends on whether temporary disagreement about that information is acceptable.

## Follow an update

A learns that member D joined. A tells B during a periodic exchange; B later tells C. A and C can therefore have different views for some time. Version information helps a receiver distinguish a newer observation from an older one. The exact conflict-resolution rule belongs to the chosen protocol; simply receiving a message last is not always proof that it describes the newest state.

Gossip is often combined with other mechanisms. A node may learn a peer address through gossip but use another protocol to agree on writes. Gradual information spread does not establish a single safe order for financial transactions.

## How to tune it

Change exchange frequency, number of peers contacted, and message size based on convergence goals and bandwidth. More frequent or wider exchanges can spread updates faster while consuming more network and processing capacity. Sending small differences instead of complete state may help when the protocol supports it.

Use peer selection and resynchronization behavior that eventually reconnect temporarily separated groups. Do not turn a delayed health observation into an unsafe irreversible action without appropriate safeguards.

## How to verify improvement

Measure how long an update takes to reach most or all reachable nodes, plus message volume. Test lost messages, network partitions, joining members, and old state returning after recovery. State convergence assumptions explicitly rather than promising instant agreement.

## Optional further reading

- [Additional explanation](http://highscalability.com/blog/2023/7/16/gossip-protocol-explained.html)

Optional references provide more detail; they are not required to follow this lesson.
