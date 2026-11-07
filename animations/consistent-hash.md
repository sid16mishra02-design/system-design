# Consistent hashing: a node joins

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Consistent hashing: a node joins](../assets/animations/consistent-hash.gif)

</details>

## Read the same sequence without motion

1. Keys go clockwise to the next node. Key K at 170 maps to C at 260.
2. K is owned by C before the new node joins.
3. D joins at 200 degrees, between B and C.
4. K at 170 now meets D first. Move the affected range from C to D.
5. A key at 80 still maps to B. Not every key needs to move.

[View all states as still images](../assets/animations/consistent-hash-steps.png)

## Related lessons

- [Consistent Hashing](../curriculum/03-databases/12-consistent-hashing.md)
