# Queries in a Sharded Cluster

## Table of contents

- [Queries in a Sharded Cluster](#queries-in-a-sharded-cluster)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Route Process](#route-process)
  - [Merge Process](#merge-process)
    - [Sort](#sort)
    - [Limit](#limit)
    - [Skip](#skip)

## Introduction

- More about routing Aggregation queries in a sharded cluster on the [MongoDB sharding docs](https://docs.mongodb.com/manual/core/aggregation-pipeline-sharded-collections/).

- MongoS is the principal interface point for your client applications. All queries must be redirected to it.

## Route Process

- In route process, the first thing that the MongoS does is determine the list of shards that must receive the query.

- Depending on the query predicate, the MongoS as either targets every shard in the cluster or a subset of shards in the cluster.
  - If the query predicate includes the shard key, then the MongoS can specifically target only those shards that contain the shard key value or values specified in the query predicate.
    - These targeted queries are very efficient.
  - If the query predicate does not include the shard key, or has generally very wide in scope, such as a range to query that spans multiple or all shards, than the MongoS has to target every shard in the cluster.
    - These scatter gather operations can be slow, depending on factors such as the number of shards and your cluster.

- Whether we're doing targeted or scatter gather queries, the MongoS opens a cursor against each of the targeted shards.
- Each cursor executes the query predicate, and returns any data returned by the query for that shard.

## Merge Process

- With the results from each targeted shard, the MongoS merges all of the results together to form the total set of documents that fulfills this query, and then returns that set of documents to the client application.
- The MongoS also has specific behavior when it comes to cursor operators, such as `sort`, `limit` and `skip`.
  - If you're using aggregation, there's more specific behavior depending on the pipeline you've created.

### Sort

- The MongoS pushes the `sort` down to each shard in the cluster and then performs a `merge sort` of the results.

### Limit

- The MongoS pushes the `limit` down to each shard in the cluster, and then reapplies that limit after merging the returned results.

### Skip

- The MongoS performs the skipping on the merged set of results, and doesn't push anything down to the shard level.
- When used in conjunction with a `limit`, the MongoS will pass the `limit` plus the value of the `skip` to the shards to ensure a sufficient number of documents are returned to the MongoS to apply the final `limit` and `skip` successfully.
