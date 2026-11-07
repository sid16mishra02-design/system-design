# An address update and duplicated data

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![An address update and duplicated data](../assets/animations/normalization.gif)

</details>

## Read the same sequence without motion

1. A normalized current view refers to the customer rather than copying every field.
2. An order can also retain the delivery address used at purchase time.
3. The customer changes their current address to B.
4. A live join sees B; the past delivery snapshot should still show A.
5. Choose duplication by meaning and access pattern, not a universal rule.

[View all states as still images](../assets/animations/normalization-steps.png)

## Related lessons

- [Normalization and Denormalization](../curriculum/03-databases/07-normalization-and-denormalization.md)
