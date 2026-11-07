# Two buyers, one remaining ticket

[← Animation index](README.md)

This is one illustrative scenario, not a complete implementation or a simulation of all failure modes. The related lesson explains assumptions and tradeoffs.

<details>
<summary>Open the looping animation</summary>

![Two buyers, one remaining ticket](../assets/animations/atomic-stock.gif)

</details>

## Read the same sequence without motion

1. There is one unit of product 42. Both buyers want it.
2. A performs an atomic update WHERE product_id = 42 AND quantity > 0.
3. B executes the same conditional update after A.
4. Only A may confirm a reservation from these results.
5. Related changes need a suitable transaction; external payment is another boundary.

[View all states as still images](../assets/animations/atomic-stock-steps.png)

## Related lessons

- [Transactions](../curriculum/03-databases/08-transactions.md)
- [ACID and BASE consistency models](../curriculum/03-databases/09-acid-and-base-consistency-models.md)
