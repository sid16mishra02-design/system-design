[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

At midnight, two jobs update the same order: one cancels it while another marks it shipped. A reporting query scans a year of rows and blocks checkout writes. The schema has tables and keys, but that alone did not save the workflow. Which relationships and transitions must be constrained, and which query path needs deliberate design?
<!-- END INQUIRY -->

<!-- BEGIN ORIGINAL TOPIC -->
# SQL databases

A SQL (or relational) database is a collection of data items with pre-defined relationships between them. These items are organized as a set of tables with columns and rows. Tables are used to hold information about the objects to be represented in the database. Each column in a table holds a certain kind of data and a field stores the actual value of an attribute. The rows in the table represent a collection of related values of one object or entity.

Each row in a table could be marked with a unique identifier called a primary key, and rows among multiple tables can be made related using foreign keys. This data can be accessed in many different ways without re-organizing the database tables themselves. SQL databases usually follow the [ACID consistency model](09-acid-and-base-consistency-models.md#acid).

## Materialized views

A materialized view is a pre-computed data set derived from a query specification and stored for later use. Because the data is pre-computed, querying a materialized view is faster than executing a query against the base table of the view. This performance difference can be significant when a query is run frequently or is sufficiently complex.

It also enables data subsetting and improves the performance of complex queries that run on large data sets which reduces network loads. There are other uses of materialized views, but they are mostly used for performance and replication.

## N+1 query problem

The N+1 query problem happens when the data access layer executes N additional SQL statements to fetch the same data that could have been retrieved when executing the primary SQL query. The larger the value of N, the more queries will be executed, the larger the performance impact.

This is commonly seen in GraphQL and ORM (Object-Relational Mapping) tools and can be addressed by optimizing the SQL query or using a dataloader that batches consecutive requests and makes a single data request under the hood.

## Advantages

Let's look at some advantages of using relational databases:

- Simple and accurate
- Accessibility
- Data consistency
- Flexibility

## Disadvantages

Below are the disadvantages of relational databases:

- Expensive to maintain
- Difficult schema evolution
- Performance hits (join, denormalization, etc.)
- Difficult to scale due to poor horizontal scalability

## Examples

Here are some commonly used relational databases:

- [PostgreSQL](https://www.postgresql.org)
- [MySQL](https://www.mysql.com)
- [MariaDB](https://mariadb.org)
- [Amazon Aurora](https://aws.amazon.com/rds/aurora)
<!-- END ORIGINAL TOPIC -->

## Make it concrete

Customers, orders, and order items fit related tables. Keys identify rows; constraints reject invalid relationships or duplicate identifiers. Transactions group changes that must commit together.

Start with important queries. For a customer's newest orders, inspect a query plan and an index matching the filter and sort. Retrieve bounded results and only required columns. Keep transactions short to reduce contention, and parameterize input values. Relational structure does not make every query efficient.

### Turn the screen into queries

A customer's order-history screen needs that customer's latest orders, then the items belonging to those orders. Write those operations first. The data model should make ownership clear, while constraints protect relationships that the database can enforce. An order total and its line items may need to change within one transaction.

Now consider a report scanning every order from last year. It has a different access pattern from the interactive screen. An index designed for one customer's recent orders may not eliminate that scan. Check the plan and actual rows examined rather than assuming “SQL is slow.”

More indexes speed some reads but make inserts and updates maintain more structures. Start with the queries that matter, and measure before distributing the data across machines. **Check:** which correctness rule belongs in a constraint, and which business rule requires coordinated application work?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
