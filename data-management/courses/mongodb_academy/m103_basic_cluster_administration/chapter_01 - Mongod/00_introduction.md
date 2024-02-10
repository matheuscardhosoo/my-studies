# Introduction

## Table of contents

- [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [What](#what)
  - [How to communicate with](#how-to-communicate-with)
    - [Command line](#command-line)
  - [Default configurations](#default-configurations)
    - [Access Port](#access-port)
    - [Data and Journaling Path (dbpath)](#data-and-journaling-path-dbpath)
    - [Authentication](#authentication)
    - [Bind IP](#bind-ip)
  - [Launching Mongod](#launching-mongod)

## What

- Ref: [MongoD](https://docs.mongodb.com/manual/reference/program/mongod/)
- The main MongoDB process.
- Runs into Daemon mode (meant to be run in background without user direct interactions).
- Handles connections, requests and persists data.
- Manage the database security, distribution and consistence for multiple servers.
- Interacts only with the database client.

## How to communicate with

### Command line

- To connect to mongod log output.

```shell
mongod
```

- To interact with mongod using the database client.
  - `HOST=192.168.103.100:27000`
  - `USER=m103-admin`
  - `PASSWORD=m103-pass`

```shell
mongo admin --host $HOST -u $USER -p $PASSWORD
```

## Default configurations

### Access Port

- Default: `27017`
- The port on which mongod will listen for client connections.
- To set a different port:

```shell
mongod --port <port number>
```

### Data and Journaling Path (dbpath)

- Default: `/data/db`
- Stores data and journaling information.
- To set a different `dbpath`:

```shell
mongod --dbpath <directory path>
```

### Authentication

- Default: disabled.
- Enables authentication to control which users can access the database.
- When auth is specified, all database clients who want to connect to mongod first need to authenticate.
- To enable the auth option:

```shell
mongod --auth
```

### Bind IP

- Default: none.
- Allows us to specify which IP addresses mongod should bind to.
- When mongod binds to an IP address, clients from that address are able to connect to mongod.
- If using the bind_ip option with external IP addresses, it's recommended to enable auth to ensure that remote clients connecting to mongod have the proper credentials.
- To bind multiple addresses and/or hosts:

```shell
mongod --bind_ip localhost,123.123.123.123
```

## Launching Mongod

- To launch a mongod instance:
  - `PORT='2700'`
  - `DBPATH='/data/db'`
  - `IP='localhost','192.168.103.100'`
  - That authentication is enable.

```shell
mongod --port $PORT --dbpath $DBPATH --auth --bind_ip $IP
```

```shell
mongod --port '27000' --dbpath '/data/db' --auth --bind_ip 'localhost','192.168.103.100'
```

- The equivalent configuration file.

  ```YAML
  storage:
    dbPath: "/data/db"

  net:
    port: 27000
    bindIp : "localhost,192.168.103.100"

  security:
    authorization: enabled
  ``

- To create a new user in database:
  - Role: root on admin database.
  - Username: `m103-admin`.
  - Password: `m103-pass`.

```shell
mongo admin --host localhost:27000 --eval '
  db.createUser({
    user: "m103-admin",
    pwd: "m103-pass",
    roles: [
      {role: "root", db: "admin"}
    ]
  })
'
```
