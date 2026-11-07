# API Design

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Make the contract predictable

Start with what clients need to do and the data they exchange. Then choose clear operations, validation rules, response formats, and failure behavior.

For an order service:

- `POST /orders` submits an order. Validate quantities and check the caller's permissions.
- `GET /orders/{id}` retrieves one order after checking ownership or another explicit access rule.
- `GET /orders?cursor=...` retrieves a bounded page instead of every order at once. The cursor is a bookmark telling the server where the next page starts.

Separate a transport failure from a business rejection. A timeout means the client lacks a response; “out of stock” is a known business result. Retriable writes need a duplicate-handling rule, such as an idempotency key.

Use consistent error shapes so clients can respond sensibly. Avoid exposing internal database details accidentally. Changing field meanings can break clients even if the URL stays the same; plan compatibility and version changes deliberately.

**Check:** a response saying “success” is incomplete unless the contract states what succeeded. Was the order durably created, or merely accepted for later processing?

## Optional further reading

- [Additional explanation](https://abdulrwahab.medium.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f)

The lesson above is complete enough for this curriculum; external links are for deeper study.
