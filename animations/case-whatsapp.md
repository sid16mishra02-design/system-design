# Design example: accepted is not yet delivered

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Design example: accepted is not yet delivered](../assets/animations/case-whatsapp.gif)

</details>

## Read the same sequence without motion

1. The sender submits one logical message using a stable message identifier.
2. Persist the message and recovery state before promising durable acceptance.
3. Acknowledge acceptance, which is different from recipient delivery.
4. Use a recoverable handoff for delivery work; do not lose work between stores.
5. An online recipient receives M42; offline clients need later retrieval.
6. A retry or reconnect can repeat M42. Deduplicate at the durable/client boundary.

[View all states as still images](../assets/animations/case-whatsapp-steps.png)

## Related lessons

- [WhatsApp](../practice/whatsapp.md)
