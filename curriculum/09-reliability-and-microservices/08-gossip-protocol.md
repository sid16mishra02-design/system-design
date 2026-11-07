# Gossip Protocol

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Spread information through repeated peer exchanges

In a gossip protocol, nodes periodically exchange information with selected peers. Those peers spread what they know further. Repeated exchanges let knowledge travel through a cluster without every node contacting every other node each time.

Imagine A learns that a new member joined. A tells B; B later tells C. For a while, C may have an older membership view than A. The system must tolerate that temporary disagreement.

Gossip can help distribute membership and health observations. The exact protocol determines how versions, conflicting observations, failed nodes, and convergence are handled. A delay in receiving news is not proof that the sender is dead.

Gossip is not the same as consensus: spreading information does not by itself establish one agreed order of committed writes. Its usefulness depends on which information may safely propagate gradually.

**Check:** a cluster can use gossip for membership and a separate mechanism for deciding writes. One protocol need not solve both problems.

## Optional further reading

- [Additional explanation](http://highscalability.com/blog/2023/7/16/gossip-protocol-explained.html)

The lesson above is complete enough for this curriculum; external links are for deeper study.
