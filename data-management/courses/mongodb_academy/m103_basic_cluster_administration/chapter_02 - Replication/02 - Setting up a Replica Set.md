# Setting Up a Replica Set

## Table of contents

- [Setting Up a Replica Set](#setting-up-a-replica-set)
  - [Table of contents](#table-of-contents)
  - [Goals](#goals)
  - [Key-File Authentication](#key-file-authentication)
  - [DB Path](#db-path)
  - [Configuration files](#configuration-files)
    - [Node 1 (node1.conf)](#node-1-node1conf)
    - [Node 2 (node2.conf)](#node-2-node2conf)
    - [Node 3 (node3.conf)](#node-3-node3conf)
  - [Starting Replica Set](#starting-replica-set)

## Goals

- Initiate a local replica set.
- Independently launching three **mongod** processes and enable them to communicate with each other to replicate data.

## Key-File Authentication

- Typically these **mongod** instances would be running on different machines, but because they're running on the same machine, they're all just going to share the same key-file and use the same one to authenticate with one another.
- Typically this key file would be copied on to each machine where each **mongod** was running.
- Implicit enables `authorization` config.
- Creating the key-file and setting permissions on it:

```shell
sudo mkdir -p /var/mongodb/pki/
sudo chown vagrant:vagrant /var/mongodb/pki/
openssl rand -base64 741 > /var/mongodb/pki/m103-keyfile
chmod 400 /var/mongodb/pki/m103-keyfile
```

## DB Path

- Each node has its own dbPath.
- Creating the dbPath folder:

```shell
mkdir -p /var/mongodb/db/node1
mkdir -p /var/mongodb/db/node2
mkdir -p /var/mongodb/db/node3
```

## Configuration files

- Each node has its own configuration file, so it is necessary to create them individually.

- Starting each node with its appropriate configuration file.

```shell
mongod -f node1.conf
mongod -f node2.conf
mongod -f node3.conf
```

### Node 1 (node1.conf)

```YAML
storage:
  dbPath: /var/mongodb/db/node1
net:
  bindIp: 192.168.103.100,localhost
  port: 27011
security:
  authorization: enabled
  keyFile: /var/mongodb/pki/m103-keyfile
systemLog:
  destination: file
  path: /var/mongodb/db/node1/mongod.log
  logAppend: true
processManagement:
  fork: true
replication:
  replSetName: m103-example
```

### Node 2 (node2.conf)

```YAML
storage:
  dbPath: /var/mongodb/db/node2
net:
  bindIp: 192.168.103.100,localhost
  port: 27012
security:
  keyFile: /var/mongodb/pki/m103-keyfile
systemLog:
  destination: file
  path: /var/mongodb/db/node2/mongod.log
  logAppend: true
processManagement:
  fork: true
replication:
  replSetName: m103-example
```

### Node 3 (node3.conf)

```YAML
storage:
  dbPath: /var/mongodb/db/node3
net:
  bindIp: 192.168.103.100,localhost
  port: 27013
security:
  keyFile: /var/mongodb/pki/m103-keyfile
systemLog:
  destination: file
  path: /var/mongodb/db/node3/mongod.log
  logAppend: true
processManagement:
  fork: true
replication:
  replSetName: m103-example
```

## Starting Replica Set

- It is necessary to enable the communication between the nodes.
- Connecting to node1:

```shell
mongo --port 27011
```

- Initiating the replica set (necessary for only for one node):

```js
rs.initiate()
```

- Creating a user:
  - However, we have client authentication enabled, so it is not possible to add other nodes to the set until we create a user and then connect as that user.

```js
use admin
db.createUser({
  user: "m103-admin",
  pwd: "m103-pass",
  roles: [
    {role: "root", db: "admin"}
  ]
})
```

- Exiting the Mongo shell and connecting to the entire replica set:
  - In addition to authenticating with a username password, it is necessary to specify the name of the replica set in the host name. This will tell the mongo shell to connect directly to the replica set, instead of just the specified node.
  - It's going to use this node to discover what the current primary is of the replica set and then connect to that node instead.
  - In this case, there's only one node in the set and that node is the primary.

```shell
mongo --host "m103-example/192.168.103.100:27011" -u "m103-admin" -p "m103-pass" --authenticationDatabase "admin"
```

- Adding other members (host) to replica set:

```js
rs.add("m103:27012")
rs.add("m103:27013")
```

- Getting replica set status:

```js
rs.status()
```

- Getting an overview of the replica set topology:

```js
rs.isMaster()
```

- Stepping down the current primary to force a new election:

```js
rs.stepDown()
```
