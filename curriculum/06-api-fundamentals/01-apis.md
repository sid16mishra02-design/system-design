# APIs

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A contract between two parts of a system

An API, or application programming interface, specifies how one program asks another to do something. Its contract includes accepted inputs, outputs, errors, and relevant behavior.

Think of a restaurant menu: it describes what you can request without exposing the kitchen's internal workflow. For a shop, `GET /products/42` can return a product and `POST /orders` can request an order.

A useful order contract answers practical questions: Which fields are required? Who may create an order? What happens if stock runs out? If the client retries after a timeout, can an order be created twice?

An API is not the server or database itself. Its implementation can change while clients keep using the same agreed interface. Also, APIs are not limited to HTTP: libraries and operating systems expose APIs too.

**Check:** “we use REST” describes an interface style. It does not by itself define the order fields, authorization rules, error behavior, or duplicate-request policy.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/what-is-an-api)

The lesson above is complete enough for this curriculum; external links are for deeper study.
