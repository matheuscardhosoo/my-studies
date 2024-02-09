# Read Concerns

## Table of contents

- [Read Concerns](#read-concerns)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Read Concern Levels](#read-concern-levels)
    - [Local](#local)
    - [Available](#available)
    - [Majority](#majority)
    - [Linearizeable](#linearizeable)
  - [When use Read Concerns?](#when-use-read-concerns)
    - [Fast + Latest Data](#fast--latest-data)
    - [Fast + Safest Data](#fast--safest-data)
    - [Latest Data + Safest Data](#latest-data--safest-data)

## Introduction

- Ref: [Read Concern](https://docs.mongodb.com/manual/reference/read-concern/).
- **Read concern** is a companion to write concern.
- Allows us to control the consistency and isolation properties of the data read from replica sets and replica set shards.
- Provides a way of dealing with the issue of data durability during a failover event.
- The read operation only returns data acknowledged as having been written to a number of replica set members specified in the read concern.
- A document that does not meet the specified read concern is not a document that is guaranteed to be lost.
  - It just means that at the time of the read, the data had not propagated to enough nodes to meet the requested durability guarantee.
- Read concern doesn't prevent deleting data using a CRUD operation, such as delete.

## Read Concern Levels

### Local

- The query returns data from the instance with no guarantee that the data has been written to a majority of the replica set members (i.e. may be rolled back).
- Any data freshly written to the primary qualifies for local read concern.
- There are no guarantees that the data will be safe during a failover event.
- The default for read operations against the primary.

### Available

- The query returns data from the instance with no guarantee that the data has been written to a majority of the replica set members (i.e. may be rolled back).
- The same as **local** read concern for replica set deployments.
- The default for read operations against secondary members.
- The main difference between **local** and **available** read concern is in the context of sharded clusters.

### Majority

- The query returns the data that has been acknowledged by a majority of the replica set members.
- The documents returned by the read operation are durable, even in the event of failure.
- The only way that documents returned by a read concern **majority** read operation could be lost is if a majority of replica set members went down and the documents were not replicated to the remaining replica set members, which is a very unlikely situation, depending on your deployment architecture.
- Provides the stronger guarantee compared to local or available writes.
- The trade-off is that you may not get the freshest or latest data in your cluster.
- The **MMAPv1 storage engine** does not support read concern of majority.

### Linearizeable

- Added in **MongoDB 3.4**.
- The query returns data that reflects all successful majority-acknowledged writes that completed prior to the start of the read operation.
- The query may wait for concurrently executing writes to propagate to a majority of replica set members before returning results.

## When use Read Concerns?

- Depends on the application requirements.
- **Fast**, **safe**, or the **latest data in your cluster**.

### Fast + Latest Data

- **local** or **available**.
- If you want **fast** reads of **the latest data**.
- But you are going to lose your durability guarantee.

### Fast + Safest Data

- **majority**.
- If you want **fast** reads of **the safest data**.
- But again, you may not be getting the latest written data to your cluster.

### Latest Data + Safest Data
- **linearizeable**.
- If you want **safe reads** of **the latest data** at the time of the read operation.
- But it's more likely to be slower.
- And it's single document reads only.
