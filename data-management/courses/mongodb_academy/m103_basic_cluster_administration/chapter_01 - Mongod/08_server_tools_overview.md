# Server Tools Overview

## Table of contents

- [Server Tools Overview](#server-tools-overview)
  - [Table of contents](#table-of-contents)
  - [MongoDB package](#mongodb-package)
    - [Main Applications](#main-applications)
    - [Tools in MongoDB package](#tools-in-mongodb-package)
  - [MongoStat](#mongostat)
  - [MongoRestore e MongoDump](#mongorestore-e-mongodump)
  - [MongoExport and MongoImport](#mongoexport-and-mongoimport)

## MongoDB package

### Main Applications

- **MongoD**: MongoDB core application.
- **MongoS**: MongoDB cluster-core application (replicas and partitions administrations).
- **Mongo**: Iterative MongoDB shell.

### Tools in MongoDB package

- Use the below command to list:

```shell
find /usr/bin -name "mongo*"
```

- These are the all the applications:
  - mongofiles
  - mongotop
  - mongoimport
  - mongodb-compass
  - mongostat
  - mongod
  - mongoperf
  - mongoreplay
  - mongodump
  - mongo
  - mongoexport
  - mongos
  - mongorestore

## MongoStat

- Utility designed to give quick statistics on a running MongoD or Mongos process.
- Returns mongo statistics periodically (default equal to 1 second).
- The command below connect to a specific database:

```shell
mongostat --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin
```

- The following information are shown:

  - **insert**: number of insert per second.
  - **query**: number of query per second.
  - **update**: number of update per second.
  - **delete**: number of delete per second.
  - **getmore**: number of getmore per second.
  - **command**: number of command per second.
  - **dirty**: percentage of dirty bytes in the cache.
  - **used**: percentage of currently-used bytes in the cache.
  - **flushes**: 
  - **vsize**: total amount of virtual memory used by the process.
  - **res**: total amount of resonant memory used by the process.
  - **qrw**: 
  - **arw**: 
  - **net_in**: amount of input network traffic.
  - **net_out**: amount of output network traffic.
  - **conn**: number of current connections.
  - **time**: current timestamp.

## MongoRestore e MongoDump

- Used to import and export dump files to/from MongoDB collections.
- These dump files are BSON.
- It is very quick, because MongoDB data is already in JSON format and MongoDump simply needs to make a copy and export.
- The dump process generates a `dump/` folder with specified database and collection as BSON and some metadata.

- The following command make a dump from admin database.

```shell
mongodump --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin
```

- The following command drop a collection and restore it from a dump from a BSON file.

```shell
mongorestore --drop --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin dump/
  ```

## MongoExport and MongoImport

- Used to export and import JSON files from/to MongoDB collections.

- The following command export the data from system.users database to a db.json file.

```shell
mongoexport --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --db system --collection users -o db.json
```

- The following commands drop and import the data from db.json file to a system.users database.

```shell
mongoimport --drop --host 192.168.103.100:27000 -u m103-admin -p m103-pass --authenticationDatabase admin --db system --collection users  db.json
```

```shell
mongoimport --drop --port 27000 -u m103-application-user  -p m103-application-pass --authenticationDatabase admin --db applicationData --collection products /dataset/products.json
```
