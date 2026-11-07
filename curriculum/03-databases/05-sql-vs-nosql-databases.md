[← Category](README.md) · [Schedule](../../SCHEDULE.md)

> **Reading note:** some statements in the preserved passage need clarification. Read [Make it concrete](#make-it-concrete) with it.

<!-- BEGIN INQUIRY -->
## Try solving this first

The team argues for days: finance wants relational tables, catalog wants flexible documents, and leadership wants “web scale.” Nobody has written the three operations the product must perform. For creating an order, browsing varied products, and reserving the last item, which access pattern or guarantee actually forces a choice—and could one store still be enough?
<!-- END INQUIRY -->

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

Choose from operations and guarantees, not SQL/NoSQL labels. Orders may need relationships and multi-record invariants; catalogs may need varied attributes. SQL columns can be nullable; NoSQL includes structured graph and key-value models, not only documents.

Compare creating an order, listing recent orders, and updating stock in candidate products. Measure queries and writes and verify transaction guarantees. Adding two stores also adds consistency, backup, and monitoring work.

### Compare two concrete workloads

An order must refer to a real customer and reserve stock without breaking a business invariant. A product description must hold different attributes for books and shoes. These are requirements, not instructions to choose two databases. Some relational products handle flexible data, and some nonrelational products support strong transactions.

For each candidate, sketch the same reads and writes, including a failure halfway through checkout. Ask how constraints are enforced, which query becomes expensive, and how recovery works. Test representative data sizes and request distributions rather than comparing labels in isolation.

Begin with one store when it meets both needs. Add another when the benefit is specific enough to justify synchronizing facts across systems. **Decision test:** what exact operation or guarantee would fail if you kept your simpler design? If you cannot name one, more technology may not improve it.

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
