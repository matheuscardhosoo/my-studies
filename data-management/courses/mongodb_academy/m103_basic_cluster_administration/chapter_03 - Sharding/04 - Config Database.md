# Config Database

## Table of contents

- [Config Database](#config-database)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Checking `config`](#checking-config)
  - [Collections](#collections)
    - [`databases`](#databases)
    - [`collections`](#collections-1)
    - [`shards`](#shards)
    - [`chunks`](#chunks)
    - [`mongos`](#mongos)

## Introduction

- First thing you need to know about the Config Database is that you should generally never write any data to it.
- It's maintained internally by MongoDB, and it's used internally.
- All `sh.status()` information are actually stored in the there.


## Checking `config`

- Connecting to MongoS:

```shell
mongo --port 26000 --username m103-admin --password m103-pass --authenticationDatabase admin
```

- Switch to config DB:

```js
use config
```

## Collections

### `databases`

- Query `config.databases`:

```js
db.databases.find().pretty()
```

- So this is going to return each database in our cluster as one document.
- It's going to give us the **primary shard** for each database, and the partition here is just telling us whether or not sharding has been enabled on this database.

### `collections`

- Query `config.collections`:

```js
db.collections.find().pretty()
```

- So this is only going to give us information on collections that have been sharded.
- But for those collections, it will tell us the **shard key** that we used.

### `shards`

- Query `config.shards`:

```js
db.shards.find().pretty()
```

- This one's going to tell us about the shards in our cluster.
- And here, you can see the hostname contains the replica set name because these shards are deployed as replica sets.

### `chunks`

- Query `config.chunks`:

```js
db.chunks.find().pretty()
```

- The `chunks` collection is possibly the most interesting collection in this whole database.
- So each chunk for every collection in this database is returned to us as one document.
- The inclusive minimum and the exclusive maximum define the chunk range of the shard key values. That means that any document in the associated collection who's shard key value falls into this chunks range will end up in this chunk, and this chunk only.
  - MinKey, here, means the lowest possible value of sale price or negative infinity, if you want to think about it that way.

### `mongos`

- Query `config.mongos`:

```js
db.mongos.find().pretty()
```

- The `mongos` (config) database also some information on the MongoS process currently connected to this cluster, because we can have any number of them.
- It gives us a lot of information on it, including the MongoS version that's running on the MongoS.
