# Latency vs Throughput vs Bandwidth

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Start with a familiar situation

A checkout counter takes two minutes to serve one customer. That is **latency**: how long an operation takes. All counters together serve 100 customers in an hour. That is **throughput**: how much work finishes per unit of time. The doorway has a physical capacity. Think of **bandwidth** as a connection's capacity for moving data, usually measured in bits per second.

In an app, a request taking 200 milliseconds has 200 ms latency. If the service completes 500 requests each second, its throughput is 500 requests/second. These measure different things; neither number determines the other by itself.

More bandwidth helps when moving large files, but may not fix a slow database query. More simultaneous workers can improve throughput while each individual request still takes the same time. Once resources are overloaded, waiting time can increase latency.

**Check your understanding:** a server completes twice as many requests per second, but each still takes 200 ms. Throughput improved; individual-request latency did not.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/latency-vs-throughput)

The lesson above is complete enough for this curriculum; external links are for deeper study.
