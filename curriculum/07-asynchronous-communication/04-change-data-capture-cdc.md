# Change Data Capture (CDC)

[← Category](README.md) · [Schedule](../../SCHEDULE.md)

## Turn database changes into downstream updates

CDC observes changes in a database and makes them available to other systems. A common implementation reads the database's change log and produces insert, update, and delete records.

Example: a product price changes in the main database. A CDC pipeline carries that change to a search index. Search can then reflect the new price without the application separately writing both systems on every request.

The search index can lag behind the database. A consumer may also see a change again after recovery, so repeated processing must be safe. An initial snapshot, ongoing log position, and restart behavior all matter.

CDC describes changed data, not necessarily business intent. A changed order status row is not automatically the same contract as an explicitly defined OrderShipped event. Schema changes can affect consumers as well.

**Check:** replacing two application writes with CDC removes one coordination pattern; it does not make downstream views instantly consistent or remove the need to handle duplicate changes.

## Optional further reading

- [Additional explanation](https://algomaster.io/learn/system-design/change-data-capture-cdc)
- [PostgreSQL: logical decoding](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html)

The lesson above is complete enough for this curriculum; external links are for deeper study.
