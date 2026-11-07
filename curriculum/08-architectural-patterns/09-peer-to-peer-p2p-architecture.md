# Peer-to-Peer (P2P) Architecture

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Participants can provide as well as consume

In a client-server design, clients ask a service for work or data. In a peer-to-peer design, participants can exchange data or provide services to one another.

Imagine sharing a large file. Instead of every downloader fetching every byte from one server, peers can exchange pieces they already have. The design still needs a way to discover peers, locate pieces, check integrity, and handle peers leaving.

P2P can distribute bandwidth and reduce dependence on one content-serving machine. It also makes availability, trust, abuse prevention, and reachability harder. A device behind a router may not be directly reachable from another peer.

A P2P system may still use centralized discovery, identity, or coordination. “Peer-to-peer” does not imply every component is decentralized, and it does not imply blockchain.

**Check:** if the only discovery service fails, existing peers may still exchange data while new participants struggle to join. State exactly which function depends on that service.

## Optional further reading

- [Additional explanation](https://www.spiceworks.com/tech/networking/articles/what-is-peer-to-peer/)

The lesson above is complete enough for this curriculum; external links are for deeper study.
