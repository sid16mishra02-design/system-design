[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN ORIGINAL TOPIC -->
# API Gateway

The API Gateway is an API management tool that sits between a client and a collection of backend services. It is a single entry point into a system that encapsulates the internal system architecture and provides an API that is tailored to each client. It also has other responsibilities such as authentication, monitoring, load balancing, caching, throttling, logging, etc.

![api-gateway](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-III/api-gateway/api-gateway.png)

## Why do we need an API Gateway?

The granularity of APIs provided by microservices is often different than what a client needs. Microservices typically provide fine-grained APIs, which means that clients need to interact with multiple services. Hence, an API gateway can provide a single entry point for all clients with some additional features and better management.

## Features

Below are some desired features of an API Gateway:

- Authentication and Authorization
- [Service discovery](../09-reliability-and-microservices/01-service-discovery.md)
- [Reverse Proxy](../02-networking/05-proxy.md#reverse-proxy)
- [Caching](../05-caching/01-caching.md)
- Security
- Retry and [Circuit breaking](../09-reliability-and-microservices/03-circuit-breaker.md)
- [Load balancing](../02-networking/08-load-balancing.md)
- Logging, Tracing
- API composition
- [Rate limiting](05-rate-limiting.md) and throttling
- Versioning
- Routing
- IP whitelisting or blacklisting

## Advantages

Let's look at some advantages of using an API Gateway:

- Encapsulates the internal structure of an API.
- Provides a centralized view of the API.
- Simplifies the client code.
- Monitoring, analytics, tracing, and other such features.

## Disadvantages

Here are some possible disadvantages of an API Gateway:

- Possible single point of failure.
- Might impact performance.
- Can become a bottleneck if not scaled properly.
- Configuration can be challenging.

## Backend For Frontend (BFF) pattern

In the Backend For Frontend (BFF) pattern, we create separate backend services to be consumed by specific frontend applications or interfaces. This pattern is useful when we want to avoid customizing a single backend for multiple interfaces. This pattern was first described by [Sam Newman](https://samnewman.io).

Also, sometimes the output of data returned by the microservices to the front end is not in the exact format or filtered as needed by the front end. To solve this issue, the frontend should have some logic to reformat the data, and therefore, we can use BFF to shift some of this logic to the intermediate layer.

![backend-for-frontend](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-III/api-gateway/backend-for-frontend.png)

The primary function of the backend for the frontend pattern is to get the required data from the appropriate service, format the data, and sent it to the frontend.

_[GraphQL](02-rest-graphql-grpc.md#graphql) performs really well as a backend for frontend (BFF)._

### When to use this pattern?

We should consider using a Backend For Frontend (BFF) pattern when:

- A shared or general purpose backend service must be maintained with significant development overhead.
- We want to optimize the backend for the requirements of a specific client.
- Customizations are made to a general-purpose backend to accommodate multiple interfaces.

## Examples

Following are some widely used gateways technologies:

- [Amazon API Gateway](https://aws.amazon.com/api-gateway)
- [Apigee API Gateway](https://cloud.google.com/apigee)
- [Azure API Gateway](https://azure.microsoft.com/en-in/services/api-management)
- [Kong API Gateway](https://konghq.com/kong)
<!-- END ORIGINAL TOPIC -->

## Make it concrete

### Where it helps

A mobile client calls one gateway, which routes `/orders` to the orders service and `/products` to the catalog. Shared authentication checks and request limits can live at this entry point instead of being independently implemented by every client.

### Apply it carefully

Suppose a product page needs catalog and stock data. A gateway can combine those responses, reducing client round trips. It also becomes responsible for deadlines and partial responses: what should the page show if stock is slow?

Keep business rules in the responsible service. Passing gateway authentication does not authorize a customer to read another customer's order. Bound request sizes, propagate request identifiers, and set downstream timeouts. Avoid unlimited retries, which can multiply traffic during an outage. Run redundant gateway instances and measure gateway latency separately from downstream latency.

**Check:** if the gateway fails, can clients reach any service through the supported entry path?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
