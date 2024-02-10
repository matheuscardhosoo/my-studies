# Introduction

## Table of contents

- [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [Concepts](#concepts)
    - [BASE](#base)
    - [Idempotency](#idempotency)
    - [Replication](#replication)
    - [MongoDB Context](#mongodb-context)
      - [Replication](#replication-1)
      - [Idempotency](#idempotency-1)
      - [Primary Node](#primary-node)
      - [Secondary nodes](#secondary-nodes)
  - [Types](#types)

## Concepts

### BASE

- **BASE** principle:
  - Basic Availability.
  - Soft-state.
  - Eventual consistency
- NoSQL databases (like MongoDB) follow the BASE principles and its variations.

### Idempotency

- Multiples calls of the same command in the same context generate the same result (deterministic commands).

### Replication

- Maintain multiple copies of the same data.
- Improve availability using redundancy.

### MongoDB Context

#### Replication

- Since the database itself doesn't grants the data **Availability**, **Replication** is necessary to cover this gap.
- In MongoDB, **Replication** is given by a group of nodes that have copies of the same data.
- By default, MongoDB uses asynchronous Statement-based replication.

#### Idempotency

- Database operation reduce.
- Every command is transformed before to be saved in oplog.
- Only single and simple operations area saved and used in replica process.

#### Primary Node

- By default, all data is handled in on the **primary node**.
- The remaining (**secondary nodes**) nodes asynchronously sync the data (part or total) from/to **primary node**.

#### Secondary nodes

- Total or partial replicas from the **primary node**,
- Can become a **primary node** if this gone down.
- **Secondary nodes** vote in each other (**election**) to define which will become the **primary node** (**failover**).
- Once the node comes back up, it simply sync the last copy of the data and rejoin the replica set.

## Types

- Ref: [Statement-Based Replication vs Binary Replication](https://university.mongodb.com/videos/y/yutpUgJMkk4).
- **Binary replication**: replicate the database in a low operation level, reapplying all the low-lever operations created from the original statement.
- **Statement-based replication**: replicate the database in a high operation level, reapplying all the high-level reduced statements.

|                                     | Binary replication | Statement-based replication |
| ----------------------------------- | ------------------ | --------------------------- |
| Log type                            | Binary log         | Oplog (OPeration log)       |
| Replicated unit                     | Bytes              | Operations                  |
| Performance                         | High               | Medium                      |
| Memory usage                        | Low                | Medium                      |
| System dependency                   | Yes                | No                          |
| Architecture dependency             | Yes                | No                          |
| Database service version dependency | Yes                | No                          |
