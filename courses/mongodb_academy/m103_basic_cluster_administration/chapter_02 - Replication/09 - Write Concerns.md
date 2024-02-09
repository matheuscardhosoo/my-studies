# Write Concerns

## Table of contents

- [Write Concerns](#write-concerns)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Concepts](#concepts)
    - [Durability](#durability)
    - [Majority](#majority)
  - [Benefits](#benefits)
  - [Trade-off](#trade-off)
  - [Write Concern Levels](#write-concern-levels)
  - [Write Concern Options](#write-concern-options)
    - [level](#level)
    - [wtimeout](#wtimeout)
    - [journal](#journal)
  - [Write Concern Command](#write-concern-command)

## Introduction

- Ref: [Write Concern](https://docs.mongodb.com/manual/reference/write-concern/).
- Write concern describes the level of acknowledgment requested from MongoDB for write operations to a **standalone mongod** or to **replica sets** or to **sharded clusters**.
  - For **sharded clusters** in particular, write concern is pushed down to the shard level.
- In general, the core write commands all support write concern as an optional parameter.
- No matter the specified what write concern, MongoDB always replicates data to every data-bearing node in the cluster.

## Concepts

### Durability

- Means that the write has propagated to the number of replica set member nodes specified in the write concern.

### Majority

- Here is defined as a simple majority of replica set members (divide by two, and round up).

## Benefits

- Higher levels of acknowledgment produce a stronger durability guarantee.
- The more replica set members that acknowledge the success of a write, the more likely that the write is durable in the event of a failure.

## Trade-off

- Higher levels of acknowledgment increases the durability time.
- More durability requires more time to achieve the specified durability guarantee since you have to wait for those acknowledgments.

## Write Concern Levels

|    Level     | Meaning                                                                                                                                                                              |
| :----------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      0       | **Fire-and-forget strategy**. The application doesn't wait for any acknowledgments, so the write might succeed or fail. It only checks that it can connect to the node successfully. |
|      1       | (Default) The application waits for an acknowledgment from a single member of the replica set, specifically, the primary.                                                            |
|      >1      | Increase the number of acknowledgments to include one or more secondary members. Higher levels of write concern correspond to a stronger guarantee of write durability.              |
|   majority   | Simple majority of replica set members.                                                                                                                                              |
| Replica tags | -                                                                                                                                                                                    |

## Write Concern Options

### level

- Abbreviation: `w`
- Write concern level.

### wtimeout

- Maximum amount of time the application waits before marking an operation as failed.
- Hitting a `wtimeout` error does not mean that the write operation itself has failed. It only means that the application did not get the level of durability that it requested.

### journal

- Abbreviation: `j`
- Requires that each replica set member to receive the write and commit to the journal filed for the write to be considered acknowledged.
- Starting with **MongoDB 3.2.6**, a write concern of majority actually implies `j = true`.
- The advantage of setting `j = true` for any given write concern is that you have a stronger guarantee that not only were the writes received, they've been written to an on-disk journal.
- If you set `j = false`, or if **journaling** is disabled on the **mongod**, the node only needs to store the data in memory before reporting success.

## Write Concern Command

- Using the default option:
  - It returns `OK` if the primary node responds `OK`.

```js
db.products.insert({...})
```

- Using the `majority` option:
  - It returns `OK` if the majority of nodes respond `OK`.
  - If some nodes are down, it updates the majority value. 

```js
db.products.insert({...}, { "writeConcern": { "w": "majority" } })
```

- Using the `3` option:
  - It returns `OK` if 3 of the nodes respond `OK`.
  - If some nodes are down resulting in a total less than 3, the write operation will block the system until any secondary comeback to respond.

```js
db.products.insert({...}, { "writeConcern": { "w": 3 } })
```

- Using the `3` option and `wtimeout` equal to 60:
  - It returns `OK` if 3 of the nodes respond `OK`.
  - If some nodes are down resulting in a total less than 3, it will return a error when reach the `wtimeout`.
    - The operation as completed, but doesn't reach the goal. The unhealthy node will receive the new document when it is brought back online.

```js
db.products.insert({...}, { "writeConcern": { "w": "3", "wtimeout": 60 } })
```
