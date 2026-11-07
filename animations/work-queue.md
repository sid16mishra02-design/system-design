# Work queues: absorb bursts and survive worker crashes

[← Animation index](README.md)

**Problem:** Decouple uploads from thumbnail processing without duplicating the durable result.

**Scenario:** A thumbnail worker crashes after saving output but before acknowledgement.

The full system map stays visible as the highlighted path and component states change. Every stage lasts one second and the sequence repeats automatically. Values are illustrative; playback speed is not system timing.

![Work queues: absorb bursts and survive worker crashes](../assets/animations/work-queue.gif)

## Read the same sequence without motion

1. **Accept work durably.** The upload service enqueues a stable thumbnail job. Do not claim durable acceptance before the selected handoff actually guarantees it.
   Job ID survives retries; The image itself must be durable.
2. **Return before processing.** The uploader receives acceptance while the thumbnail remains pending. Asynchronous completion shortens the initiating request, not the total work.
   Pending is not completed; Bound producer admission if needed.
3. **One worker receives it.** Worker A receives J42 under the queue acknowledgement policy. Competing workers share work; one delivery is not a lifetime exactly-once guarantee.
   Track in-flight jobs; Lease or timeout is product-specific.
4. **Save the durable result.** A creates thumbnail 42 and receives a storage acknowledgement. A deterministic output key makes a repeat recognizable.
   Result identity is stable; Write completion must be durable.
5. **Crash before acknowledgement.** A crashes before acknowledging; J42 remains unacknowledged. The queue cannot infer a successful business effect from a missing acknowledgement.
   Output already exists; Redelivery may follow timeout.
6. **Redeliver to another worker.** After the applicable timeout, B receives the same J42. This is the same logical job, not a new thumbnail request.
   Stable ID is preserved; Do not blindly create another effect.
7. **Recognize finished work.** B verifies the existing complete output instead of conflicting with it. Deduplication and the durable side effect need a coherent recovery rule.
   Partial output needs a policy; A marker alone may not prove success.
8. **Complete and monitor.** B safely acknowledges J42; the queue can retire it. Scale consumers against backlog age and downstream capacity, not queue length alone.
   Bound repeated failures; Steady arrival must fit capacity.

**Design tradeoff:** A queue absorbs bursts but adds waiting and cannot solve a sustained processing-capacity deficit.

[View all states as still images](../assets/animations/work-queue-steps.png)

## Related lessons

- [Message Brokers](../curriculum/07-asynchronous-communication/01-message-brokers.md)
- [Message Queues](../curriculum/07-asynchronous-communication/02-message-queues.md)
