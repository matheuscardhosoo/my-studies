# Reconfiguring a Running Replica Set

## Table of contents

- [Reconfiguring a Running Replica Set](#reconfiguring-a-running-replica-set)
  - [Table of contents](#table-of-contents)
  - [Pre-env setup](#pre-env-setup)
  - [Env setup](#env-setup)

## Pre-env setup

- Starting each node with its appropriate configuration file (in vagrant).

```shell
mongod -f node1.conf
mongod -f node2.conf
mongod -f node3.conf
```
- Connecting to node1:

```shell
mongo --host "m103-example/192.168.103.100:27011" -u "m103-admin" -p "m103-pass" --authenticationDatabase "admin"
  ```

## Env setup

- Node 4 (node4.conf):

```YAML
storage:
  dbPath: /var/mongodb/db/node4
net:
  bindIp: 192.168.103.100,localhost
  port: 27014
systemLog:
  destination: file
  path: /var/mongodb/db/node4/mongod.log
  logAppend: true
processManagement:
  fork: true
replication:
  replSetName: m103-example
```

- Arbiter (arbiter.conf):

```YAML
storage:
  dbPath: /var/mongodb/db/arbiter
net:
  bindIp: 192.168.103.100,localhost
  port: 28000
systemLog:
  destination: file
  path: /var/mongodb/db/arbiter/mongod.log
  logAppend: true
processManagement:
  fork: true
replication:
  replSetName: m103-example
```

- Starting each node with its appropriate configuration file (vagrant).

```shell
mkdir /var/mongodb/db/node4
mkdir /var/mongodb/db/arbiter
mongod -f node4.conf
mongod -f arbiter.conf
```

- Adding news nodes (hosts) and arbiter to replica set:

```js
rs.add("m103:27014")
rs.addArb("m103:28000")
```

- Getting an overview of the replica set topology:

```js
rs.isMaster()
```

- Removing the arbiter from our replica set:

```js
rs.remove("m103:28000")
```

- Assigning the current configuration to a shell variable we can edit, in order to reconfigure the replica set:

```js
cfg = rs.conf()
```

- Editing our new variable cfg to change topology - specifically, by modifying cfg.members:

```js
cfg.members[3].votes = 0
cfg.members[3].hidden = true
cfg.members[3].priority = 0
```

- Updating our replica set to use the new configuration cfg:
- Bear in mind that re-config might trigger an election depending on what's in the new configuration.
- It does not require any of the nodes to restart.
- It does not require anr of the configuration files to be updated.

```js
rs.reconfig(cfg)
```
