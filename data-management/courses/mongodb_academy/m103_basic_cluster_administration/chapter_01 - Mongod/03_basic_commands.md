# Basic Commands

## Table of contents

- [Basic Commands](#basic-commands)
  - [Table of contents](#table-of-contents)
  - [Shell wrappers](#shell-wrappers)
  - [User management commands](#user-management-commands)
    - [Examples](#examples)
      - [Create User](#create-user)
      - [Drop User](#drop-user)
  - [Collection Management Commands](#collection-management-commands)
    - [Examples](#examples-1)
      - [Rename Collection](#rename-collection)
      - [Create Index](#create-index)
      - [Drop Collection](#drop-collection)
  - [Database Administration Commands](#database-administration-commands)
    - [Examples](#examples-2)
      - [Drop Database](#drop-database)
      - [Create Collection](#create-collection)
  - [Diagnostic Commands](#diagnostic-commands)
    - [Examples](#examples-3)
      - [Server Status](#server-status)
  - [Generic Command](#generic-command)
  - [Explain Command](#explain-command)

## Shell wrappers

- `db.<method>()`
  - It wrappers the commands that acts in the db instance.
  - `db.<collection>.<method>()`
    - It wrappers the commands that acts in the conllection.
- `rs.<method>()`
  - It wrappers the commands that control the replica set deployment and management.
- `sh.<method>()`
  - It wrappers the commands that control the sharded cluster deployment and management.

## User management commands

- Ref: [User Management Commands](https://docs.mongodb.com/manual/reference/command/nav-user-management/).

### Examples

#### Create User

```js
db.createUser(
  {
    "user": "user-name",
    "pwd": "user-passord",
    "roles": [
      {
        "role": "role-name",
        "db": "db-name"
      }
    ]
  }
);
```

#### Drop User

```js
db.dropUser(
  {
    "user": "user-name"
  }
);
```

## Collection Management Commands

- Ref: [Collection Methods](https://docs.mongodb.com/manual/reference/method/js-collection/).

### Examples

#### Rename Collection

```js
db.<collection>.renameCollection()
```

#### Create Index

```js
db.<collection>.createIndex(
  {
    "product": 1
  },
  {
    "name": "name_index"
  }
)
```

#### Drop Collection

```js
db.<collection>.drop()
```

## Database Administration Commands

- Ref: [Administration Commands](https://docs.mongodb.com/v5.0/reference/command/#administration-commands).

### Examples

#### Drop Database

```js
db.dropDatabase()
```

#### Create Collection

```js
db.createCollection()
```

## Diagnostic Commands

- Ref: [Diagnostic Commands](https://docs.mongodb.com/v5.0/reference/command/#diagnostic-commands).

### Examples

#### Server Status

```js
db.serverStatus()
```

## Generic Command

- Ref: [db.runCommand()](https://docs.mongodb.com/v5.0/reference/method/db.runCommand/).

```js
db.runCommand(
  {
    "createIndexes": <collection>
  },
  {
    "indexes": [
      {
        "key": {
          "product": 1
        }
      },
      {
        "name": "name_index"
      }
    ]
  }
);
```

## Explain Command

- Ref: [Explain Results](https://docs.mongodb.com/manual/reference/explain-results/).