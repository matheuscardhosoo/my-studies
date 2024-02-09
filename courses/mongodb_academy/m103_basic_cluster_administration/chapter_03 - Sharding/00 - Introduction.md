# Introduction

## Table of contents

- [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [Concepts](#concepts)
    - [Vertical Scaling](#vertical-scaling)
    - [Horizontal Scaling](#horizontal-scaling)
    - [Sharding](#sharding)
  - [Sharding in MongoDB](#sharding-in-mongodb)
  - [MongoS](#mongos)

## Concepts

- Ref: [Sharding in MongoDB](https://www.mongodb.com/basics/sharding)

### Vertical Scaling

- Vertical scaling refers to increasing the power of a single machine or single server through a more powerful CPU, increased RAM, or increased storage capacity.
- If physical limitations were not an issue, vertical scaling would be the method of choice due to its simplicity.
- In real life, it potentially become very expensive and no single machine can handle large modern-day workloads. 
- Automatically applied by cloud-based providers, but with some limitations.
  - They'll eventually put a limit on the possible hardware configurations, which would effectively limit our storage layer.

### Horizontal Scaling

- Also known as scale-out, it refers to adding nodes to share the data set and load.
- Horizontal scaling allows for near-limitless scaling to handle big data and intense workloads.

### Sharding

- Sharding is a method for distributing data across multiple machines, enabling **horizontal scaling** (as opposed to **vertical scaling**). 
- Sharding allows the dataset grown without worrying about being able to store it all on one server. Instead, it divides the dataset into pieces and then distribute the pieces across as many shards as we want.
- Multiple shards make up a **Sharded Cluster**.

## Sharding in MongoDB

- In order to guarantee high availability for a **Sharded Cluster**, it is necessary to deploy each shard as a replica set.
- This way, MongoDB ensures a level of fault tolerance against each piece of data regardless of which shard actually contains that data.
- MongoDB uses **MongoS** to provide the data of a **Sharded Cluster**.

## MongoS

- A router process that accepts queries from clients and then figures out which shard should receive that query.
- It is used in between a **Sharded Cluster** and its clients.
- Clients connect to MongoS instead of connecting to each shard individually.
- It is possible to have any number of **MongoS**'s processes so we can service many different applications or requests to the same **Sharded Cluster**.
- It uses the metadata about which data is contained on each shard. That metadata is stored on the **Config Servers**.
- In way to guarantee high availability for **Config Servers**, MongoDB replicates these metadata in a **Config Server Replica Set**.
