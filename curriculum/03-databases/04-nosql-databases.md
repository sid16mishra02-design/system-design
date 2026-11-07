[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN INQUIRY -->
## Try solving this first

Products have different attributes, sessions are fetched by identifier, and recommendations explore relationships. Would one representation suit all three? What would you measure before choosing?
<!-- END INQUIRY -->

<!-- BEGIN ORIGINAL TOPIC -->
# NoSQL databases

NoSQL is a broad category that includes any database that doesn't use SQL as its primary data access language. These types of databases are also sometimes referred to as non-relational databases. Unlike in relational databases, data in a NoSQL database doesn't have to conform to a pre-defined schema. NoSQL databases follow [BASE consistency model](09-acid-and-base-consistency-models.md#base).

Below are different types of NoSQL databases:

### Document

A document database (also known as a document-oriented database or a document store) is a database that stores information in documents. They are general-purpose databases that serve a variety of use cases for both transactional and analytical applications.

**Advantages**

- Intuitive and flexible
- Easy horizontal scaling
- Schemaless

**Disadvantages**

- Schemaless
- Non-relational

**Examples**

- [MongoDB](https://www.mongodb.com)
- [Amazon DocumentDB](https://aws.amazon.com/documentdb)
- [CouchDB](https://couchdb.apache.org)

### Key-value

One of the simplest types of NoSQL databases, key-value databases save data as a group of key-value pairs made up of two data items each. They're also sometimes referred to as a key-value store.

**Advantages**

- Simple and performant
- Highly scalable for high volumes of traffic
- Session management
- Optimized lookups

**Disadvantages**

- Basic CRUD
- Values can't be filtered
- Lacks indexing and scanning capabilities
- Not optimized for complex queries

**Examples**

- [Redis](https://redis.io)
- [Memcached](https://memcached.org)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb)
- [Aerospike](https://aerospike.com)

### Graph

A graph database is a NoSQL database that uses graph structures for semantic queries with nodes, edges, and properties to represent and store data instead of tables or documents.

The graph relates the data items in the store to a collection of nodes and edges, the edges representing the relationships between the nodes. The relationships allow data in the store to be linked together directly and, in many cases, retrieved with one operation.

**Advantages**

- Query speed
- Agile and flexible
- Explicit data representation

**Disadvantages**

- Complex
- No standardized query language

**Use cases**

- Fraud detection
- Recommendation engines
- Social networks
- Network mapping

**Examples**

- [Neo4j](https://neo4j.com)
- [ArangoDB](https://www.arangodb.com)
- [Amazon Neptune](https://aws.amazon.com/neptune)
- [JanusGraph](https://janusgraph.org)

### Time series

A time-series database is a database optimized for time-stamped, or time series, data.

**Advantages**

- Fast insertion and retrieval
- Efficient data storage

**Use cases**

- IoT data
- Metrics analysis
- Application monitoring
- Understand financial trends

**Examples**

- [InfluxDB](https://www.influxdata.com)
- [Apache Druid](https://druid.apache.org)

### Wide column

Wide column databases, also known as wide column stores, are schema-agnostic. Data is stored in column families, rather than in rows and columns.

**Advantages**

- Highly scalable, can handle petabytes of data
- Ideal for real-time big data applications

**Disadvantages**

- Expensive
- Increased write time

**Use cases**

- Business analytics
- Attribute-based data storage

**Examples**

- [BigTable](https://cloud.google.com/bigtable)
- [Apache Cassandra](https://cassandra.apache.org)
- [ScyllaDB](https://www.scylladb.com)

### Multi-model

Multi-model databases combine different database models (i.e. relational, graph, key-value, document, etc.) into a single, integrated backend. This means they can accommodate various data types, indexes, queries, and store data in more than one model.

**Advantages**

- Flexibility
- Suitable for complex projects
- Data consistent

**Disadvantages**

- Complex
- Less mature

**Examples**

- [ArangoDB](https://www.arangodb.com)
- [Azure Cosmos DB](https://azure.microsoft.com/en-in/services/cosmos-db)
- [Couchbase](https://www.couchbase.com)
<!-- END ORIGINAL TOPIC -->

## Make it concrete

Documents can represent varied product attributes; key-value records can serve sessions; graphs can explore relationships. NoSQL is a collection of models, not one universal design.

Sketch reads and writes before choosing. Organize identifier-based access around the key. For relationship-heavy requests, check the product's actual query and indexing support.

Choose partition keys that spread traffic, not merely records. Verify transaction scope, consistency, schema rules, and limits for the specific database. NoSQL does not automatically mean no schema, no transactions, or unlimited horizontal scale. Identify which queries your representation makes expensive.

### Ask what a single request must retrieve

For a session store, a request may need exactly one record by session ID. A key-value model can match that operation closely. A product catalog with varying attributes may suit documents, but “show all products with this attribute” still requires a supported access path. A collection of documents does not automatically make arbitrary searches cheap.

Next ask what must change together. If an order updates several records, inspect the actual product's transaction boundaries and behavior during failures. Do not infer those guarantees from the NoSQL label.

Keep the first design simple enough to operate. Adding a specialized store can be worthwhile for a demonstrated query need; it also adds backup, synchronization, and incident response work. **Try again:** where would you place a frequently updated inventory count if stale copies could allow two buyers to claim the last item?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
