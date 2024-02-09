# Targeted Queries vs Scatter Gather

## Table of contents

- [Targeted Queries vs Scatter Gather](#targeted-queries-vs-scatter-gather)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Targeted Query](#targeted-query)
  - [Scatter Gather](#scatter-gather)
  - [Example](#example)

## Introduction

- Using m103 database and showing its collections:

```js
use m103
show collections
```

## Targeted Query

- Targeted queries require the shard key as part of the query predicate.
- For compound shard keys, it can be a prefix of the shard key up to the entire shard key. But that's only if you're using a very wide shard range, or if you have a hashed shard key.
- Ranged queries on the shard key may end up with similar performance to a scatter gather query, depending on how wide your range is.
- Targeted query with `explain()` output:

```js
db.products.find({"sku" : 1000000749 }).explain()
```

- That means for this specific query, not only was MongoS able to target a subset of shards, it was able to retrieve the entire results set from a single shard without needing to merge the results.

## Scatter Gather

- Without the shard key, the MongoS must perform a scatter gather query.
- This means that the Mongo must check in with every single shard in the cluster.
- The scatter gather queries are going to be the slowest, compared to a targeted query.
- Scatter gather query with explain() output:

```js
db.products.find( {
  "name" : "Gods And Heroes: Rome Rising - Windows [Digital Download]"
}).explain()
```

- Name isn't in our shard key, so this is necessarily a scatter gather query.
- So this is a scatter gather query, and required a merge.

## Example

- Given a collection that is sharded on the following shard key:

```json
{ "sku" : 1, "name" : 1 }
```

- The following queries results in a targeted query:

```js
db.products.find({ "sku" : 1337 })
db.products.find({ "sku" : 1337, "name": "MongoHacker" })
db.products.find({ "name": "MongoHacker", "sku" : 1337 })
```

- The following queries results in a scatter gather:

```js
db.products.find({ "name": "MongoHacker"})
```
