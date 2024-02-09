# Failover and Elections

## Table of contents

- [Failover and Elections](#failover-and-elections)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Rolling upgrades](#rolling-upgrades)
  - [Election](#election)
    - [When a new primary is elected](#when-a-new-primary-is-elected)
    - [Algorithm](#algorithm)
  - [Priority](#priority)
    - [Changing Node Priority](#changing-node-priority)

## Introduction

- The primary node is the first point of contact for any client communicating to the database. Even if secondaries go down, the client will continue communicating with the node acting as primary until the primary is unavailable.
- Non-replicated data is rolled back after system normalization.
- If all nodes of a replica set failed remaining only one, this one can't become a primary because does not exist other node to give it a vote. So, the replica set has only a secondary node.

## Rolling upgrades

- A rolling upgrade just means we're upgrading one server at a time, starting with the secondaries. It is great because it allows us to perform updates while maximizing availability to any clients using the database.
- It's necessary to run `rs.stepDown()` to force a new election, turning the old primary node into a secondary that can be updated.

## Election

- Elections take place whenever there's a change in topology.
- An election may or may not elect a new primary.
- The method to figure out which secondary will run for election begins with priority and whichever node has the latest copy of the data.
- A replica set should has a odd number of nodes, making possible avoid the situation where two nodes run for election simultaneously (because it eliminate the possibility to result in a draw).
- Now a tie is not the end of the world, because the nodes will just start over and hold another election.
- The problem with repeating elections over and over is that any applications accessing the data will have to pause all activity and wait until a primary is elected.

### When a new primary is elected

- Anytime the current primary node becomes unavailable.
- When the current primary node steps down to be a secondary.

### Algorithm

1. A node with equivalent priority and the latest copy of the data automatically vote itself when a election begins.
2. Then it's going to ask the other two nodes for their support in the election.
3. The other nodes evaluate the candidate and decide if will give them votes.
4. If it gets the majority of votes, it become the primary.

## Priority

- Priority is essentially the likelihood that a node will become the primary during an election.
- The default primary for a node is 1, and any node with priority 1 or higher can be elected primary.
- We can increase the priority of a node if we want it to be more likely at this node becomes primary. But changing this value alone does not guarantee that.
- We can also set the priority of node to be 0 if we never want that node to become primary.
  - A priority 0 node can still vote in elections, but it can't run for election.
  - A node with priority 0 is classified as passive.

### Changing Node Priority

- Connected in a primary node.
- Storing replica set configuration as a variable cfg:

```js
cfg = rs.conf()
```
- Setting the priority of a node to 0, so it cannot become primary (making the node "passive"):

```js
cfg.members[2].priority = 0
```
- Updating our replica set to use the new configuration cfg:

```js
rs.reconfig(cfg)
```
- Checking the new topology of our set:

```js
rs.isMaster()
```
- Forcing an election in this replica set (although in this case, we rigged the election so only one node could become primary):

```js
rs.stepDown()
```
- Checking the topology of our set after the election:

```js
rs.isMaster()
```
