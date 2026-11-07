# Which way do live updates travel?

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Which way do live updates travel?](../assets/animations/realtime-protocols.gif)

</details>

## Read the same sequence without motion

1. Long polling: browser sends a request; the server may hold its response.
2. A response arrives; the browser starts another request for later updates.
3. Separate SSE example: server events arrive over a streaming HTTP response.
4. Separate WebSocket example: after setup, the browser can send a message.
5. The server can send messages back on the same WebSocket connection.

[View all states as still images](../assets/animations/realtime-protocols-steps.png)

## Related lessons

- [Long polling, WebSockets, Server-Sent Events (SSE)](../curriculum/06-api-fundamentals/06-long-polling-websockets-server-sent-events-sse.md)
- [Long polling vs WebSockets](../practice/TRADEOFFS.md)
