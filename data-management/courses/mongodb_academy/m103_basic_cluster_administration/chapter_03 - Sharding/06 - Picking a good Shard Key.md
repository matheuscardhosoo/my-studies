# Picking a Good Shard Key

## Table of contents

- [Picking a Good Shard Key](#picking-a-good-shard-key)
  - [Table of contents](#table-of-contents)
  - [Recap](#recap)
  - [Basic Properties of shard key values](#basic-properties-of-shard-key-values)
    - [Cardinality](#cardinality)
    - [Frequency](#frequency)
    - [Monotonically Change](#monotonically-change)
  - [Read Isolation](#read-isolation)

## Recap

- **Database level**: Enable Sharding.
- **Collection level**: Shard data.
- It's possible to have both sharded and unsharded collections in the same database.

## Basic Properties of shard key values

- A shard key that can fulfill those properties is more likely to result in an even distribution of written data.
- Having a shard key that doesn't quite fulfill one of these property doesn't guarantee bad distribution of data, but it's not going to help.

### Cardinality

- Cardinality is the measure of the number of elements within a set of values.
- **Shard key** should have **high cardinality**.
  - Facilitates the data and workload distribution.
- In context of the shard key, it is the number of unique possible **shard key values**.
- The **cardinality** constrains the number of shards in a cluster.
  - **Low cardinality** = few shards.
  - **High cardinality** = many shards.
- Remember, chunks define boundaries based on **shard key values**, and a unique value can only exist on one chunk. Higher cardinality gives more chunks, and with more chunks the number of shards can also grow, not restraining the ability to grow the cluster.

### Frequency

- The **frequency** of a shard key represents how often a unique value occurs in the data.
- **Shard key** should have **low frequency**.
  - Guarantees an uniform distribution of data and workload.
  - Avoids the node overloading.

### Monotonically Change

- **Monotonically changing** here means that the possible shard key values for a new document changes at a steady and predictable rate.
  - Field that has numeric progression.
- **Shard key** should have **non-monotonically change**.
  - Timestamps, dates, the object ID, for example, are monotonically increasing.
  - So, they have a very high cardinality (lots of unique values) and very low frequency (nearly no repetition of those unique values) it ends up being a pretty bad shard key.

## Read Isolation

- MongoDB can route queries that include the shard key to specific chunks, whose range contains the specified shard key values. When choosing a shard key, we should consider whether our choice supports the queries we run most often.
- In case the fields in a query form a bad shard key, consider specifying a compound index as the underlying index for the shard key, where the extra field or fields provide high cardinality, low frequency, or are themselves non monotonically changing.
- So, without the shard key to guide it, MongoDB has to ask every single shard to check data for. These broadcast operations are scatter gather operations and can be pretty slow.
