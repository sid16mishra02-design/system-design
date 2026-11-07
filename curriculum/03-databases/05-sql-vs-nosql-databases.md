[← Category](README.md) · [Schedule](../../SCHEDULE.md)

> **Reading note:** some statements in the preserved passage need clarification. Read [Make it concrete](#make-it-concrete) with it.

<!-- BEGIN ORIGINAL TOPIC -->
# SQL vs NoSQL databases

In the world of databases, there are two main types of solutions, SQL (relational) and NoSQL (non-relational) databases. Both of them differ in the way they were built, the kind of information they store, and how they store it. Relational databases are structured and have predefined schemas while non-relational databases are unstructured, distributed, and have a dynamic schema.

## High-level differences

Here are some high-level differences between SQL and NoSQL:

### Storage

SQL stores data in tables, where each row represents an entity and each column represents a data point about that entity.

NoSQL databases have different data storage models such as key-value, graph, document, etc.

### Schema

In SQL, each record conforms to a fixed schema, meaning the columns must be decided and chosen before data entry and each row must have data for each column. The schema can be altered later, but it involves modifying the database using migrations.

Whereas in NoSQL, schemas are dynamic. Fields can be added on the fly, and each _record_ (or equivalent) doesn't have to contain data for each _field_.

### Querying

SQL databases use SQL (structured query language) for defining and manipulating the data, which is very powerful.

In a NoSQL database, queries are focused on a collection of documents. Different databases have different syntax for querying.

### Scalability

In most common situations, SQL databases are vertically scalable, which can get very expensive. It is possible to scale a relational database across multiple servers, but this is a challenging and time-consuming process.

On the other hand, NoSQL databases are horizontally scalable, meaning we can add more servers easily to our NoSQL database infrastructure to handle large traffic. Any cheap commodity hardware or cloud instances can host NoSQL databases, thus making it a lot more cost-effective than vertical scaling. A lot of NoSQL technologies also distribute data across servers automatically.

### Reliability

The vast majority of relational databases are ACID compliant. So, when it comes to data reliability and a safe guarantee of performing transactions, SQL databases are still the better bet.

Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

## Reasons

As always we should always pick the technology that fits the requirements better. So, let's look at some reasons for picking SQL or NoSQL based database:

**For SQL**

- Structured data with strict schema
- Relational data
- Need for complex joins
- Transactions
- Lookups by index are very fast

**For NoSQL**

- Dynamic or flexible schema
- Non-relational data
- No need for complex joins
- Very data-intensive workload
- Very high throughput for IOPS
<!-- END ORIGINAL TOPIC -->

## Make it concrete

### Use it: decide from operations, not labels

An order system needs relationships, integrity rules, and multi-record updates. A catalog may need flexible product documents. Either choice still needs evidence about its queries, transaction guarantees, and operational limits.

### Apply and improve

Write a small workload: create an order, list recent orders, and update stock. Compare how each candidate represents these operations and enforces their invariants. Measure representative queries and writes before assuming one category is faster.

Avoid adding two database types simply because each sounds appropriate. Cross-store consistency, backups, and monitoring add work.

SQL columns can be nullable; NoSQL includes structured graph and key-value models, not only document collections.

Self-check: name the requirement that would make you reconsider your choice.

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
