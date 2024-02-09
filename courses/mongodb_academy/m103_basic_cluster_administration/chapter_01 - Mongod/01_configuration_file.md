# Configuration File

## Table of contents

- [Configuration File](#configuration-file)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Main Options](#main-options)
  - [Examples](#examples)

## Introduction

- A `YAML` file containing the configuration options needed to run [MongoD](https://docs.mongodb.com/manual/reference/program/mongod/) or [MongoS](https://docs.mongodb.com/manual/reference/program/mongos/#mongodb-binary-bin.mongos).
  - `YAML`: "YAML Ain't Markup Language".
- An alternative for command line single approach.
- Improves the readability.
- Ref: [Command line options](https://docs.mongodb.com/manual/reference/program/mongod/#options).
- Ref: [Configuration file options](https://docs.mongodb.com/manual/reference/configuration-options).
- Invoking MongoD using configuration file:

```shell
mongod --config "/etc/mongod.conf"
```

## Main Options

| Command Line  | Config File                               | Mean                                                                                                        |
| :------------ | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `--dbpath`    | `storage.db`                              | Database main path.                                                                                         |
| `--logpath`   | `systemLog.path`, `systemLog.destination` | Database log path.                                                                                          |
| `--bind_ip`   | `net.bind_ip`                             | Need to be set to provide network access, otherwise the MongoD accepts only connections from the same host. |
| `--replSet`   | `replication.replSetName`                 | Starts the MongoD in replication mode.                                                                      |
| `--keyFile`   | `security.keyFile`                        | Sets intercluster auth security and user authentication enable.                                             |
| `--tlsPEMKey` | `net.tls.tlsPEMKey`                       | SSL encryption option.                                                                                      |
| `--tlsCAKey`  | `net.tls.tlsCAKey`                        | SSL encryption option.                                                                                      |
| `--tlsMode`   | `net.tlsMode`                             | SSL encryption option.                                                                                      |
| `--fork`      | `processManagement.fork`                  | Runs MongoD as a daemon instead of being tied toa a terminal session.                                       |

## Examples

```YAML
storage:
  dbPath: "/data/db"

systemLog:
  path: "/data/log/mongod.log"
  destination: "file"

replication:
  replSetName: M103

net:
  bindIp : "127.0.0.1,192.168.103.100"

tls:
  mode: "requireTLS"
  certificateKeyFile: "/etc/tls/tls.pem"
  CAFile: "/etc/tls/TLSCA.pem"

security:
  keyFile: "/data/keyfile"

processManagement:
  fork: true
```

```YAML
storage:
  dbPath: "/var/mongodb/db"

systemLog:
  path: "/var/mongodb/db/mongod.log"
  destination: "file"
  logAppend: true

operationProfiling:
  mode: "slowOp"
  slowOpThresholdMs: 50

net:
  port: 27000
  bindIp: "localhost,192.168.103.100"

security:
  authorization: enabled

processManagement:
  fork: true
```
