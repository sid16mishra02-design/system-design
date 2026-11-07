# Design example: near a rider does not mean available

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Design example: near a rider does not mean available](../assets/animations/case-uber.gif)

</details>

## Read the same sequence without motion

1. The rider requests a trip with a pickup location.
2. Search intersecting spatial cells and filter by actual distance and freshness.
3. Check current availability and conditionally claim the driver.
4. Notify the selected driver and track acceptance or timeout.
5. Another request must not also claim D. Stale location data is not an assignment guarantee.
6. Expired offers need an explicit release/retry policy before another assignment.

[View all states as still images](../assets/animations/case-uber-steps.png)

## Related lessons

- [Uber](../practice/uber.md)
