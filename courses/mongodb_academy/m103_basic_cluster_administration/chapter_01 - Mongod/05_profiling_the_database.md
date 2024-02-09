# Profiling the Database

## Table of contents

- [Profiling the Database](#profiling-the-database)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Settings:](#settings)
  - [Commands](#commands)
    - [Get Profiler Level](#get-profiler-level)
    - [Set Profiler Level](#set-profiler-level)

## Introduction

- Ref: [Database Profiler](https://docs.mongodb.com/manual/tutorial/manage-the-database-profiler/).
- The database profiler collects detailed information about Database Commands executed against a running `mongod` instance. This includes CRUD operations as well as configuration and administration commands.
- The profiler writes all the data it collects to a `system.profile` collection, a capped collection in each profiled database.
- Directly related to database logs, it is used to debug slow operations.
- Enabled in database level (each database has its own profile configurations)
- Makes possible to Restore the data for all operations on a given database (CRUD, administrative, and configuration operations).

## Settings:

| Level | Description                                                                         |
| :---- | :---------------------------------------------------------------------------------- |
| 0     | Profiler off. It does not collect any data. This is the default value.              |
| 1     | The Profiles collects data only for slow operations (> slowms - 100 ms in default). |
| 2     | The Profiler collects data for all operations.                                      |

- Obs.: Level 2 can generates too much output information, what increase the chance of overheat the server.

## Commands

### Get Profiler Level

```js
db.getProfilingLevel()
```

### Set Profiler Level

```js
db.setProfilingLevel(1, { "slowms": 200 })
```