# API gateway: derive the boundary from the screen

[← Animation index](README.md)

**Problem:** Choose where routing, shared request policies, and screen-specific composition belong.

**Scenario:** Five services expose fifty APIs; this screen needs three results from different services.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![API gateway: derive the boundary from the screen](../assets/animations/api-gateway.gif)

## Read the same sequence without motion

1. **Start with three calls.** The client calls only the three APIs this screen needs. Fifty available APIs do not prove that a gateway is required.
   Independent calls can overlap.; Two other services are not queried..
2. **Handle a slow response.** Details and stock arrive, but reviews exceed the screen deadline. Someone must own partial results even when the network calls are simple.
   Which results are required?; Where is the screen deadline?.
3. **Notice repeated work.** Mobile and web clients both need routing, credentials, and failure policies. Choose a boundary because a responsibility is repeated or fragile.
   Do not add components by API count.; A small client can keep direct calls..
4. **Introduce an entry point.** A gateway routes a stable public request after shared policy checks. Gateway routing and response composition are separate responsibilities.
   Services still check resource access.; Routing alone does not merge results..
5. **Compose only if useful.** A screen-specific aggregator requests the three independent results concurrently. One client request can contain several downstream calls and their failure risks.
   BFF is optional screen-specific logic.; Extra hops still add overhead..
6. **Apply a response deadline.** The aggregator receives required facts while reviews remain unavailable. A partial-result policy makes the failure visible instead of inventing data.
   Reviews may be optional on this screen.; Never invent unavailable stock..
7. **Return an honest screen.** The client receives details, stock, and an explicit unavailable-review status. The screen contract determines whether partial success is useful.
   Preserve status for missing sections.; Buying needs authoritative stock rules..
8. **Account for the new risk.** If the entry path fails, all requests using that path are affected. Redundancy and recovery must match the dependency the design introduced.
   Use redundant entry points if required.; Measure added and downstream latency..
9. **Defend your choice.** Keep the simplest arrangement that satisfies the actual screen and service requirements. Revisit your first sketch: what became simpler, and what new failure did you accept?
   Direct calls can remain reasonable.; Gateway plus BFF is not mandatory..

**Design tradeoff:** An entry point simplifies client routing; optional aggregation adds coordination, latency, and a failure dependency.

[View all states as still images](../assets/animations/api-gateway-steps.png)

## Related lessons

- [API Gateway](../curriculum/06-api-fundamentals/03-api-gateway.md)
