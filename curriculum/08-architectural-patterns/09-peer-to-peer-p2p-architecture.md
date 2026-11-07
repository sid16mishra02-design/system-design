# Peer-to-Peer (P2P) Architecture

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Participants can provide as well as consume

In a client-server design, clients ask a service for work or data. In a peer-to-peer design, participants can exchange data or provide services to one another.

Imagine sharing a large file. Instead of every downloader fetching every byte from one server, peers can exchange pieces they already have. The design still needs a way to discover peers, locate pieces, check integrity, and handle peers leaving.

P2P can distribute bandwidth and reduce dependence on one content-serving machine. It also makes availability, trust, abuse prevention, and reachability harder. A device behind a router may not be directly reachable from another peer.

A P2P system may still use centralized discovery, identity, or coordination. “Peer-to-peer” does not imply every component is decentralized, and it does not imply blockchain.

**Check:** if the only discovery service fails, existing peers may still exchange data while new participants struggle to join. State exactly which function depends on that service.

## Where this comes into play

P2P can distribute content-serving work among participants, for example when many peers want the same large file. It can also support direct communication where reachability and trust requirements permit it. A client-server design is often simpler when centralized control and predictable availability matter more.

## Work through file distribution

Split a file into verifiable pieces. Peer A has pieces 1–5; B has 4–8. They exchange useful pieces rather than downloading every byte from the origin. The system needs trustworthy information about which pieces belong to the file and checks that received pieces match that description. A malicious peer can otherwise waste bandwidth or distribute wrong bytes.

If everyone downloads pieces 1–5 first, the remaining pieces may become scarce. Piece-selection rules can improve availability by spreading scarce pieces, though they add protocol decisions. Peers can leave without notice, so locate alternative sources and resume partial transfers.

## How to optimize

Select peers using observed reachability, useful pieces, throughput, and load rather than assuming the nearest address is always fastest. Bound concurrent connections and upload usage so sharing does not overwhelm a participant's device or network.

Plan for peers behind routers and firewalls. Discovery, relays, or other connection assistance may be needed, creating dependencies and sometimes bandwidth costs. P2P does not guarantee that every pair can directly connect.

## How to verify improvement

Measure completion time, origin bandwidth saved, failed connections, and behavior when peers depart. Include low-upload and malicious peers. A successful lab transfer among permanently reachable peers does not prove that a public deployment will be robust.

## Optional further reading

- [Additional explanation](https://www.spiceworks.com/tech/networking/articles/what-is-peer-to-peer/)

Optional references provide more detail; they are not required to follow this lesson.
