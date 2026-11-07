# APIs

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A contract between two parts of a system

An API, or application programming interface, specifies how one program asks another to do something. Its contract includes accepted inputs, outputs, errors, and relevant behavior.

Think of a restaurant menu: it describes what you can request without exposing the kitchen's internal workflow. For a shop, `GET /products/42` can return a product and `POST /orders` can request an order.

A useful order contract answers practical questions: Which fields are required? Who may create an order? What happens if stock runs out? If the client retries after a timeout, can an order be created twice?

An API is not the server or database itself. Its implementation can change while clients keep using the same agreed interface. Also, APIs are not limited to HTTP: libraries and operating systems expose APIs too.

**Check:** “we use REST” describes an interface style. It does not by itself define the order fields, authorization rules, error behavior, or duplicate-request policy.

## Where this comes into play

An API is the boundary where independently developed parts agree on behavior. It can connect a mobile client to a shop, one service to another, or application code to a local library. The contract should remain understandable even when the implementation changes.

## Work through an order request

A client submits a basket, delivery address, and a request identifier. The service authenticates the caller, validates the fields, checks business rules, and records or rejects the order. A useful response includes a stable order identifier and an unambiguous status. If processing continues later, say “accepted” rather than claiming delivery or payment has already completed.

Now lose the response after the order is recorded. On retry, the caller needs a way to distinguish the same attempted operation from a new order. This is why behavior under retries is part of the API contract, not an internal database detail.

## How to optimize the boundary

Return only the fields needed for the operation and bound collection sizes. Avoid forcing clients into dozens of dependent calls for one screen; consider a suitable aggregate endpoint or another interface that fits the access pattern. Larger aggregate responses cost bandwidth and may combine data with different freshness needs.

Preserve authorization per operation. A faster endpoint that skips ownership checks is a broken contract. Keep error behavior consistent enough that callers can distinguish validation failure, permission failure, overload, and uncertain transport outcomes.

## How to verify improvement

Measure end-to-end tasks, not just endpoint speed: how many calls, transferred bytes, and retries are required to complete checkout? Verify old clients still work and that failed or repeated requests produce the documented business result.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/what-is-an-api)

Optional references provide more detail; they are not required to follow this lesson.
