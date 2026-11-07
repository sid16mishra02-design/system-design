[← Category](README.md) · [Schedule](../../SCHEDULE.md)

<!-- BEGIN ORIGINAL TOPIC -->
# Indexes

Indexes are well known when it comes to databases, they are used to improve the speed of data retrieval operations on the data store. An index makes the trade-offs of increased storage overhead, and slower writes (since we not only have to write the data but also have to update the index) for the benefit of faster reads. Indexes are used to quickly locate data without having to examine every row in a database table. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access to ordered records.

![indexes](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-II/indexes/indexes.png)

An index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives. So when we create an index on a column of a table, we store that column and a pointer to the whole row in the index. Indexes are also used to create different views of the same data. For large data sets, this is an excellent way to specify different filters or sorting schemes without resorting to creating multiple additional copies of the data.

One quality that database indexes can have is that they can be **dense** or **sparse**. Each of these index qualities comes with its own trade-offs. Let's look at how each index type would work:

## Dense Index

In a dense index, an index record is created for every row of the table. Records can be located directly as each record of the index holds the search key value and the pointer to the actual record.

![dense-index](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-II/indexes/dense-index.png)

Dense indexes require more maintenance than sparse indexes at write-time. Since every row must have an entry, the database must maintain the index on inserts, updates, and deletes. Having an entry for every row also means that dense indexes will require more memory. The benefit of a dense index is that values can be quickly found with just a binary search. Dense indexes also do not impose any ordering requirements on the data.

## Sparse Index

In a sparse index, index records are created only for some of the records.

![sparse-index](https://raw.githubusercontent.com/karanpratapsingh/portfolio/master/public/static/courses/system-design/chapter-II/indexes/sparse-index.png)

Sparse indexes require less maintenance than dense indexes at write-time since they only contain a subset of the values. This lighter maintenance burden means that inserts, updates, and deletes will be faster. Having fewer entries also means that the index will use less memory. Finding data is slower since a scan across the page typically follows the binary search. Sparse indexes are also optional when working with ordered data.
<!-- END ORIGINAL TOPIC -->

## Make it concrete

### Use it: find a customer's recent orders

A book index narrows where you look; it does not replace the pages. For `WHERE customer_id = ? ORDER BY created_at DESC`, an index beginning with those fields may avoid examining unrelated orders. The exact benefit depends on the database and query plan.

### Apply and improve

Inspect how many rows the query scans and returns. Compare its plan and timing before and after adding the candidate index using representative data. An index on city may help one filter but not every possible query.

Indexes consume space and add write work because inserts and updates must maintain them. Remove genuinely unused indexes only after checking the workloads they support.

Self-check: why can adding indexes speed reads while slowing order creation?

[Next topic in this category](README.md) · [Credits and license](../../ATTRIBUTION.md)
