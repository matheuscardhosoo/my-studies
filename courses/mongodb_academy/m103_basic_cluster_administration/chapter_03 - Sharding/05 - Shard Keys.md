# Shard Keys

## Table of contents

- [Shard Keys](#shard-keys)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [How the shard key is used to distribute data](#how-the-shard-key-is-used-to-distribute-data)
  - [Distributed read operations](#distributed-read-operations)
  - [Shard Key Index](#shard-key-index)
  - [Sharding Operation](#sharding-operation)
  - [Steps for sharding](#steps-for-sharding)

## Introduction

- Indexed field or fields that MongoDB uses to partition data in a sharded collection, and distribute it across the shards in your cluster.
- MongoDB uses the **shard key** to divide collection documents into logical groupings that MongoDB then distributes across our sharded cluster.
- MongoDB refers to these groupings as **chunks**.
- The **shard key** must be present in every document in the collection, and every new document inserted.

## How the shard key is used to distribute data

- The value of the field or fields we choose as **shard key** help to define the inclusive lower bound, and the exclusive upper bound of each chunk.
  - lower bound <= **data** < upper bound.
- Every time that a new document is written to the collection, the MongoS router checks which shard contains the appropriate chunk for that documents key value, and routes the document to that shard only.

## Distributed read operations

- Shard keys also support distributed read operations.
- If **shard key** is part of the search, MongoDB can redirect the query to only those chunks, and therefore, shards that contain the related data.
- Ideally, the **shard key** should support the majority of queries you run on the collection. That way, the majority of read operations can be targeted to a single shard.
- Without the **shard key** in the query, the MongoS router would need to check each shard in the cluster to find the documents that match the query.

## Shard Key Index

- The **shard key** should be an **index field or fields** in collection.
- This is a hard requirement. It isn't possible to select a field or fields for **shard key** if does not exist an index for them.

## Sharding Operation

- Sharding is a permanent operation. In other words, it isn't possible to unshard a collection.
- Once the **shard key** has been selected it isn't possible to change it.
- As of MongoDB 4.2, the **shard key value** is mutable, even though the **shard key** itself is immutable ([Shard Key documentation](https://docs.mongodb.com/manual/core/sharding-shard-key/index.html)).

## Steps for sharding

- Connecting to MongoS:

```shell
mongo --port 26000 --username m103-admin --password m103-pass --authenticationDatabase admin
```

- Using the chosen database and showing its collections:

```js
use m103
show collections
```

- Using `sh.enablesharding`, specifying the name of the database, to enable sharding:
  - This does not automatically shard your collections. It just means that the collections in this particular database are eligible for sharding.
  - This won't affect other databases in your MongoDB cluster.

```js
sh.enableSharding("m103")
```

- Using `db.collection.createindex` to create the shard key index:
  - It's necessary already known the attribute we want to index. So we can use the `db.collection.findOne()` to check a document sample.
  - Remember, we're going to substitute collection here with the name of the collection we want to create the index on.

```js
db.collection.createIndex( { "attributeName" : 1 } )
```

- Using `sh.shardCollection` to specify the full path to the collection, and the shard key to shard the specified Collection.

```js
sh.shardCollection("m103.collection", {"attributeName" : 1 } )
```

- Checking the status of the sharded cluster:

```js
sh.status()
```
