# Replication Commands

## Table of contents

- [Replication Commands](#replication-commands)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Commands](#commands)
    - [status](#status)
    - [isMaster](#ismaster)
    - [serverStatus](#serverstatus)
    - [printReplicationInfo](#printreplicationinfo)

## Introduction

- Some commands to gather information from and about a replica set.

## Commands

### status

- Used to report on the overall health of each node in the set.
- Get its data from the heartbeat sent between members.
- Because it relies on heartbeats for this data, it may actually be a few seconds out of date.
- This command gives us the most recent information for each specified node.
  - **up time**: the number of seconds this note has been running for.
  - **optime**: the last time the node applied an operation from its **oplog**.
  - **self`**: if the command was run from the respective node.

```js
rs.status()
```

### isMaster

- Describes the role of the node where we ran this command from.
- Gives us some information about the replica set itself.
- The output is easier to read than `rs.status()` just because its output is shorter.
- Gives us the name of the primary node in the set regardless of where we ran this command from.
- As a side note, this is the command that the drivers use to discover each node's role in the replica set.

```js
rs.isMaster()
```

### serverStatus

- Gives us a lot of information about the MongoD process, including the replication section (called **repl**).
- **repl** section is very similar to the output of `rs.isMaster()`.
- Show the **rbid** field (not included in `rs.isMaster()`), which counts the number of rollbacks that have occurred on this node.

```js
db.serverStatus()['repl']
```

### printReplicationInfo

- Shows information about the **oplog** o the currently connected node.
- It gives the exact time stamps for the first and last events that occurred in the **oplog** for that node.
- So this is a quick report on the current length of the **oplog** in time and in megabytes.

```js
rs.printReplicationInfo()
```