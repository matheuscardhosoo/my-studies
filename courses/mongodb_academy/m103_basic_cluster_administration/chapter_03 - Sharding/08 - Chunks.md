# Chunks

## Table of contents

- [Chunks](#chunks)
  - [Table of contents](#table-of-contents)
  - [Concepts](#concepts)
  - [Bound definition](#bound-definition)
  - [Chunk size](#chunk-size)
  - [Shard Key Values Frequency](#shard-key-values-frequency)
  - [Jumbo Chunks](#jumbo-chunks)

## Concepts

- Chunks are logical groups of documents that are based out of the shard key-space, and have bounds associated to it.
- Group of shard rules stored in config servers.
- Looking in chunks collection (`db.chunks`) we can see:
  - **`ns`**: What is the name space that this chunk belongs to?
  - **`lastmod`** and **`lastmodEpoch`**: When was this chunk last modified?
  - **`shard`**: Which shard holds this chunk?
  - **`min`**: chunks lower bound (inclusive).
  - **`max`**: chunks upper bound (exclusive).
- The different values that shard key may hold will define the key-space of sharding collection.
- All documents of the same chunk live in the same shard.
- The number of chunks that the shard key allows may define the max number of shards of the system.

## Bound definition

- This initial chunk goes from **minKey** to **maxKey**.
- As time progresses, the cluster will split up that initial chunk into several others to allow data to be evenly distributed between shards.

## Chunk size

- The chunk size defines the shard key-space size.
  - One shard can have multiple chunks.
  - The number of chunks compensate the chunk size (inversely proportional).
- By default, MongoDB takes 64 megabytes as the default chunk size. That means that if a chunk is about more tha 64 megabytes, it will be split.
- We can define a chunk size between the values of one to 1024 megabyte.
- The chunk size is configurable during runtime. To do that, it's necessary to save a document with ID chunk size (with the determined chunk size in megabytes) in settings collection.
  - It doesn't change anything at first time. The component responsible for the thing is the MongoS, and since we have not given any indication or signal to MongoS that it needs to split anything-- because no new data came in-- it will basically do absolutely nothing. So, chunks will be updated in next MongoS operation.
  - MongoS updates chunks distribution on the fly.

```js
db.settings.save({"_id": "chunksize", "value": 2})
sh.status()
```

## Shard Key Values Frequency

- Another aspect that will be important for the number of chunks that we can generate will be the shard key values frequency.
- Please do consider the frequency of our shard key, to avoid situations like jumbo chunks as much as possible.

## Jumbo Chunks

- Jumbo chunks can be damaging because they are chunks which are way larger than the default or defined chunk size.
- The minute a chunk becomes larger than the defined chunk size, they will be marked as jumbo chunks.
- **Jumbo chunks cannot be moved**. If the balancer sees a chunk which is marked as jumbo, you will not even try to balance it.
