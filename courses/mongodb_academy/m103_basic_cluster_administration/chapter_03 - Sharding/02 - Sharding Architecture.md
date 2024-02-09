# Sharding Architecture

## Table of contents

- [Sharding Architecture](#sharding-architecture)
  - [Table of contents](#table-of-contents)
  - [Clusters](#clusters)
  - [MongoS](#mongos)
  - [Collection Metadata](#collection-metadata)
  - [Config Servers](#config-servers)
  - [Shard Merge](#shard-merge)
  - [Primary shard](#primary-shard)
  - [Example](#example)

## Clusters

- Sharded clusters can receive any number of shards.
- Because of this, there can be several different shards.

## MongoS

- Client applications aren't going to communicate directly with the shards.
- Instead, the client connects to a **MongoS** service, and this routes queries to the correct shards.
- We can also have multiple **MongoS** processes to has high availability and/or service multiple applications at once.

## Collection Metadata

- **MongoS** knows exactly how the data is distributed based on **Collection Metadata**.
- The data is not stored on **MongoS**.

## Config Servers

- The **Collection Metadata** gets stored in **Config Servers**.
- Constantly keep track of where each piece of data lives in the cluster.
- This is especially important because the information contained on each shard might change with time.
- So **MongoS** queries the **Config Servers** often, in case a piece of data is moved.
- The **Config Servers** have to make sure that there's an even distribution of data across each part. So it redistributes the data based on consumption load.
- Not all the collections in a sharded cluster need to be distributed.

## Shard Merge

- When we query something from **MongoS** (or a randomly chosen shard in the cluster), this needs to execute the **Shard Merge** process, gathering results, and then maybe sort the results if the query mandated it.
- Once the **Shard Merge** is complete, the **MongoS** will return the results back to the client, but the client won't be aware of any of this.
- It will query this process like a regular **MongoD**.

## Primary shard

- Each database will be assigned a **Primary Shard**, and all the non-sharded collections on that database will remain on that shard.
- The **Config Servers** will assign a primary shard to each database once they get created.
  - But we can also change the **Primary Shard** of a database.
- The **Primary Shard** also has a few other responsibilities, specifically around merge operations for aggregation commands.

## Example

![Shard Cluster Example](images/shard_cluster_example.png)