# API Design

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

One customer has a million orders, and a client asks to list them. Should one response contain everything? If you divide results into pages, how do equal creation times and concurrent inserts affect the next page? What must a continuation marker mean, and how do you stop a user changing it to read another customer’s orders?
<!-- END INQUIRY -->

## Make the contract predictable

Start with what clients need to do and the data they exchange. Then choose clear operations, validation rules, response formats, and failure behavior.

For an order service:

- `POST /orders` submits an order. Validate quantities and check the caller's permissions.
- `GET /orders/{id}` retrieves one order after checking ownership or another explicit access rule.
- `GET /orders?cursor=...` retrieves a bounded page instead of every order at once. The cursor is a bookmark telling the server where the next page starts.

Separate a transport failure from a business rejection. A timeout means the client lacks a response; “out of stock” is a known business result. Retriable writes need a duplicate-handling rule, such as an idempotency key.

Use consistent error shapes so clients can respond sensibly. Avoid exposing internal database details accidentally. Changing field meanings can break clients even if the URL stays the same; plan compatibility and version changes deliberately.

**Check:** a response saying “success” is incomplete unless the contract states what succeeded. Was the order durably created, or merely accepted for later processing?

## Where this comes into play

Use explicit API design whenever clients will outlive one implementation version. A predictable contract reduces repeated integrations, accidental information exposure, and uncertainty during failures.

## Work through a list endpoint

Suppose an account has a million orders. Returning every row consumes database work, memory, bandwidth, and client processing. Instead, enforce a maximum page size and return a continuation cursor. Use a stable ordering, such as creation time plus a unique identifier, so equal timestamps have a tie-breaker.

Concurrent inserts and deletes can still affect the view while a client pages through it. State whether the API offers a stable snapshot or a changing live list. A cursor is not automatically an immutable snapshot, and an encoded cursor should not grant access to someone else's data.

## How to optimize the contract

Bound payload size, expensive filters, and query complexity. Select indexes or data models for real access patterns rather than exposing arbitrary internal queries. Consider conditional reads or caching where the representation and access policy permit it.

Add idempotency behavior to operations that clients may safely retry, and define which errors are worth retrying. Preserve compatibility: adding a required field or changing a field's meaning can break an older client even when the endpoint path is unchanged.

## How to verify improvement

Test a large dataset, equal ordering values, concurrent changes, invalid cursors, unauthorized access, and repeated writes. Compare bytes transferred, database rows examined, and end-to-end latency. A smaller response is helpful only if clients can still complete the intended task correctly.

## Optional further reading

- [Additional explanation](https://abdulrwahab.medium.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f)

Optional references provide more detail; they are not required to follow this lesson.
