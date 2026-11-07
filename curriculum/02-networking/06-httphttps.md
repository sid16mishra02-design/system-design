# HTTP/HTTPS

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## A request and its response

HTTP defines how a client asks for a resource or operation and how a server responds. A request includes a method, path, headers, and sometimes a body. The response includes a status, headers, and sometimes a body.

Example: `GET /products/42` asks for a product. `POST /orders` can submit an order. A successful order response might return `201 Created` and the new order's identifier.

**HTTPS is HTTP protected by TLS**, or Transport Layer Security, the protocol protecting the connection. TLS encrypts data in transit and normally lets the client verify the server's identity. It does not decide whether the signed-in user owns a particular order; the application must still check authorization.

An HTTP response and a business result are different layers. A network timeout does not prove an order was never created: the response might have been lost after the server committed it. Retrying a write therefore needs deliberate duplicate handling.

**Check:** HTTPS protects a password while it travels over the connection. It does not automatically protect a poorly secured database where the application stores it.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/http-https)

The lesson above is complete enough for this curriculum; external links are for deeper study.
