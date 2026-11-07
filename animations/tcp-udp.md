# TCP and UDP: what a loss changes

[← Animation index](README.md)

**Problem:** Match delivery and ordering behavior to an application's timing requirements.

**Scenario:** Illustrative file bytes 1-3 and voice frames A-C each suffer one lost item.

The full system map stays visible as the highlighted path and component states change. Every stage lasts four seconds: the path moves, then the completed state pauses so you can read it. The sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![TCP and UDP: what a loss changes](../assets/animations/tcp-udp.gif)

## Read the same sequence without motion

1. **Two different deadlines.** A file and voice call each lose data. Should both wait for recovery?
   - **Why it matters:** Reason about this scenario before comparing the mechanism and its consequences.
   - **Notice:** Which data still has value if late; Who repairs a missing item.
2. **TCP delivers initial bytes.** The first TCP bytes arrive and become available to the file reader.
   - **Why it matters:** TCP presents a byte stream, not application message boundaries.
   - **Notice:** ACKs support transport recovery; Applications still frame their messages.
3. **A TCP gap holds later data.** Range 2 is lost; range 3 arrives but waits behind the missing bytes.
   - **Why it matters:** Ordered delivery can make a later arrival wait for earlier lost data.
   - **Notice:** Later bytes may be buffered; The sender detects or times out loss.
4. **TCP retransmits the gap.** Recovery supplies range 2, allowing the reader to consume ranges 2 and 3 in order.
   - **Why it matters:** Recovery costs time and network work; the connection can still eventually fail.
   - **Notice:** Delivery does not prove business commit; TCP can report errors or time out.
5. **UDP exposes an early frame.** Frame A reaches the UDP receiver and is available to the voice application.
   - **Why it matters:** UDP supplies datagrams without built-in ordering or retransmission.
   - **Notice:** Application sees datagram boundaries; No permanent delivery guarantee.
6. **One UDP frame disappears.** Frame B is lost, but C can arrive without UDP waiting for B.
   - **Why it matters:** A missing datagram does not impose TCP's ordered-stream wait.
   - **Notice:** UDP does not repair the loss itself; C may still be late for playback.
7. **The application chooses.** The voice player can conceal a gap or drop late sound according to its timing policy.
   - **Why it matters:** Less transport waiting shifts responsibility toward application design.
   - **Notice:** Recovery can be added above UDP; Reordering is an application choice.
8. **Design the whole protocol.** Check congestion handling, message size, loss behavior, and the application's own success response.
   - **Why it matters:** Neither UDP nor TCP alone establishes that a payment or other business operation succeeded.
   - **Notice:** Do not equate UDP with always faster; Measure under realistic loss and load.

**Design tradeoff:** Ordered recovery can delay later bytes; avoiding transport waits leaves more delivery policy to the application.

[View all states as still images](../assets/animations/tcp-udp-steps.png)

## Related lessons

- [TCP and UDP](../curriculum/02-networking/03-tcp-and-udp.md)
