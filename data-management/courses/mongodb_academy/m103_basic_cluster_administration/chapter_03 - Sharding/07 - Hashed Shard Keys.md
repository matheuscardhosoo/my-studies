# Hashed Shard Keys

## Table of contents

- [Hashed Shard Keys](#hashed-shard-keys)
  - [Table of contents](#table-of-contents)
  - [Concepts](#concepts)
  - [How it works](#how-it-works)
  - [When to use it](#when-to-use-it)
  - [Drawbacks](#drawbacks)

## Concepts

- **Hashed shard key** is a shard key where the underlying index is hashed.
- To create a hashed shard:

```js
sh.enableSharding("<database>")
db.collection.createIndex({"<field>": "hashed"})
sh.shardCollection("<database>.<collection>", {"<shar key field>": "hashed"})
```

## How it works

- With a **hashed shard key**, MongoDB first hashes the shard key value, then uses that hash value to decide which chunk to place the document in.
- MongoDB doesn't store the shard key values as hashes. Instead, the underlying index backing the shard key itself is hashed.
- How MongoDB uses the hashed index for partitioning the data? So, it ends up with a more even distribution across the sharded cluster.

## When to use it

- Use with **monotonically change single fields shard keys**.
- The hash function make the data be randomly and uniformly distributed.
  - Consequently, it distributes the workload in the same way.

## Drawbacks

- Since everything is hashed now, documents within a range of shard key values are likely to be completely distributed across the sharded cluster. So ranged queries on the shard key field will now have to hit multiple shards, instead of a single shard.
  - It doesn't combine with range queries.
- MongoDB lose the ability to use features like zone sharding for the purpose of geographically isolated reads and writes.
  - If everything is randomly distributed across every shard in the cluster, there's no real way to isolate data into groupings like geography.
- It isn't possible to create hashed compound indexes.
  - MongoDB only hashes a single field shard key.
- The value in the hashed index must not be an array.
- Hashed shard key's do not support fast sorts, targeted queries on ranges of shard key values, or geographically isolated workloads.
- Finally, because the index is using hashed values, MongoDB loses the performance an index can provide for sorting documents on the shard key.
