[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN ORIGINAL TOPIC -->
# Circuit breaker

The circuit breaker is a design pattern used to detect failures and encapsulates the logic of preventing a failure from constantly recurring during maintenance, temporary external system failure, or unexpected system difficulties.

![circuit-breaker](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-IV/circuit-breaker/circuit-breaker.png)

The basic idea behind the circuit breaker is very simple. We wrap a protected function call in a circuit breaker object, which monitors for failures. Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error, without the protected call being made at all. Usually, we'll also want some kind of monitor alert if the circuit breaker trips.

## Why do we need circuit breaking?

It's common for software systems to make remote calls to software running in different processes, probably on different machines across a network. One of the big differences between in-memory calls and remote calls is that remote calls can fail, or hang without a response until some timeout limit is reached. What's worse is if we have many callers on an unresponsive supplier, then we can run out of critical resources leading to cascading failures across multiple systems.

## States

Let's discuss circuit breaker states:

### Closed

When everything is normal, the circuit breakers remain closed, and all the requests pass through to the services as normal. If the number of failures increases beyond the threshold, the circuit breaker trips and goes into an open state.

### Open

In this state circuit breaker returns an error immediately without even invoking the services. The Circuit breakers move into the half-open state after a certain timeout period elapses. Usually, it will have a monitoring system where the timeout will be specified.

### Half-open

In this state, the circuit breaker allows a limited number of requests from the service to pass through and invoke the operation. If the requests are successful, then the circuit breaker will go to the closed state. However, if the requests continue to fail, then it goes back to the open state.
<!-- END ORIGINAL TOPIC -->

<!-- BEGIN ANIMATION -->
## Watch the sequence

<details>
<summary>Open the looping animation</summary>

![Circuit breaker: closed, open, half-open](../../assets/animations/circuit-breaker.gif)

</details>

[Read the numbered steps](../../animations/circuit-breaker.md) · [View the still sequence](../../assets/animations/circuit-breaker-steps.png)
<!-- END ANIMATION -->

## Make it concrete

### Stop repeating a failing dependency call

Suppose payment calls repeatedly time out. Opening a breaker temporarily stops new calls; limited half-open probes later test recovery. A timeout bounds one call, while the breaker reacts to a failure pattern.

Choose thresholds from observed traffic, and separate unrelated dependencies. Use bounded retries and backoff so probes do not become a new flood. A checkout can show payment pending or unavailable; inventing a successful charge is not a safe fallback.

**Check:** which response preserves business correctness while the payment breaker is open?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
