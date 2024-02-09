# Balancing

## Table of contents

- [Balancing](#balancing)
  - [Table of contents](#table-of-contents)
  - [Concepts](#concepts)
  - [Process](#process)
  - [Performance Impact](#performance-impact)
  - [Commands](#commands)

## Concepts

- More about scheduling the balancer on the [MongoDB Sharding docs](https://docs.mongodb.com/manual/tutorial/manage-sharded-cluster-balancer/#sharding-schedule-balancing-window).

- MongoDB splits the sharded collections into chunks of data. As data are inserted into the collection, the number of chunks on any given shard will grow.
- The MongoDB balancer identifies which shards have too many chunks and automatically move chunks across shards in the sharded cluster in an attempt to achieve even data distribution.
- Currently, the balancer process runs on the primary member of the config server replica set.
  - In prior versions the MongoS was responsible for running the balancer process.

## Process

- The balancer process checks the chunked distribution of data across the sharded cluster and looks for certain migration thresholds. If it detects that there is an imbalance, it starts a balancer round.
- The balancer can migrate chunks in parallel.
- A given shard cannot participate in more than one migration at a time.
  - `Number of migrations in balance round` = `Number of shards` // `2`
  - A second round can be done if any shard stay out of migration process.
- These rounds happen consecutively until the balancer process detects that the cluster is as evenly distributed as possible.
- Typically, the MongoS handles initiating a chunk split, but the balancer is fully capable of performing splits. It will do so if it detects chunks that need to be split or as a part of defining chunk ranges for zone sharding.

## Performance Impact

- The balancer already has behavior built in to minimize workload disruption, such as the one chunk per shard limitation. To that end, MongoDB surfaces a number of methods for controlling the behavior of the balancer.

## Commands

- It's possible to start or stop the balancer at any time.
  - If a request to stop the balancer is received in the middle of a round, then the balancer stops only after that balancing round completes.
  - The command allows to set a time limit timeout value for how long to wait to stop or start the balancer. The interval defines how long the client should wait before checking the balancer status again.

```js
sh.stopBalancer(timeout, interval)
sh.startBalancer(timeout, interval)
```

- Enable/disable the balancer:
  - It takes a boolean and is either on or off.

```js
sh.setBalancerState(boolean)
```

- There is also a process for scheduling a time window for when this sharded cluster balancer can run. It does require modifying the config database.
