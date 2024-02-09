# local

## Table of contents

- [local](#local)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Standalone mode](#standalone-mode)
    - [startup_log](#startup_log)
  - [Replica Set](#replica-set)
    - [Collections on all mongod Instances](#collections-on-all-mongod-instances)
      - [local.statup_log](#localstatup_log)
    - [Collections on Replica Set Members](#collections-on-replica-set-members)
      - [local.system.replset](#localsystemreplset)
      - [local.system.minvalid](#localsystemminvalid)
      - [local.oplog.rs](#localoplogrs)
        - [Replication Window](#replication-window)
        - [Status](#status)

## Introduction

- Database for **Configuration Data** (related to the replication process and other instance-specific data).
- Parallel to **admin** database (comprises all the **Administration Data**).
- **local** changes are not written to the **oplog**.
- Since only changes written to the **oplog** are replicated, **local** changes won't be replicated.

## Standalone mode

- **local** has only one collection.

### startup_log

- Holds the start up log of this particular node.

## Replica Set

- **local** has the following collections.

### Collections on all mongod Instances

#### local.statup_log

- On startup, each **mongod** instance inserts a document into **startup_log** with diagnostic information about the **mongod** instance itself and host information.
- This information is primarily useful for diagnostic purposes.

### Collections on Replica Set Members

#### local.system.replset

- Holds the replica set's configuration object as its single document.

#### local.system.minvalid

- Contains an object used internally by Replica Sets to track replication status.

#### local.oplog.rs

- The central point of our replication mechanism. It holds the **oplog**.
- Created after initiating a node and adding it to a replica set.
- Keep track of all statements being replicated in the replica set.
- Every single piece of information and operations that need to be replicated will be logged in this collection.
- Every node in replica set has its own **oplog** with different sizes.
- **oplog** is **idempotent**: it stores operation as simple as possible, transforming complexes operations in multiple simple operations.
- It's a **capped** collection (the size of this collection is limited to a specific size).
- It accumulates the operations and statements until it reaches the oplog size limit. Once that happens, the first operations in our oplog start to be overwritten with newer operations.
- By default, the oplog collection will take 5% of your free disk, but this value can also be set by configuring it through the **oplogSize** in megabytes under the replication section of our configuration file.

```YAML
replication:
  oplogSize: 15
```

##### Replication Window

- The time node takes to fill in fully its oplog and start rewriting the early statements.
- The oplog size will determine the replication window.
- Is a important aspect to monitor because it impacts how much time the replica set can afford a node to be down without requiring any human intervention to auto recover.
- Once a node go down and return after some time, it can replicate other nodes oplog to apply lost operations.
- If delayed node does not find its state inside of other oplogs, it enters in recovery mode and wait for a user intervention.
- To sum up, the replication window measured in hours will be proportional to the load of your system.
- However, if our oplog size is larger and able to accommodate more changes in the system, we can afford our nodes to be down for longer and still be able to reconnect once they're being brought back up again.

##### Status

- In mongoshell, querying the oplog after connected to a replica set:

```js
use local
db.oplog.rs.find()
```

- Storing oplog stats as a variable called stats:

```js
var stats = db.oplog.rs.stats()
```

- Verifying that this collection is capped (it will grow to a pre-configured size before it starts to overwrite the oldest entries with newer ones):

```js
stats.capped
```

- Getting current size of the oplog:

```js
stats.size
```

- Getting size limit of the oplog:

```js
stats.maxSize
```

- Getting current oplog data (including first and last event times, and configured oplog size):

```js
rs.printReplicationInfo()
```
