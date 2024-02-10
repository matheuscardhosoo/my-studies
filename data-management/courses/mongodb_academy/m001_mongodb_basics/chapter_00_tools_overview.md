# Tools Overview

## Table of contents

- [Tools Overview](#tools-overview)
  - [Table of contents](#table-of-contents)
  - [MongoDB Atlas](#mongodb-atlas)
    - [Cluster](#cluster)
    - [Subscriptions](#subscriptions)
    - [Why use Atlas](#why-use-atlas)
  - [MongoDB Compass](#mongodb-compass)
  - [Mongo Shell](#mongo-shell)

## MongoDB Atlas

- Platform that provides an interface to manage and deploy MongoDB across cloud providers and reagions.
- Database as Cloud Service.
- Atlas helps us to easily setup and manage MongoDB instances.
- Atlas handles replication (maintains redundant copies of data to increase availability).

### Cluster

- Groups of servers that store data.
- The main deployment object.
- Implements a Replica Set.
  - A cluster composed by multiple servers with the same data.
  - Redundant copies are created for each object in a set.
  - Set replication grants data availability.

### Subscriptions

- Free Tier subscription to setup a database, view, and modify data.
  - Three-server replica set with 512 MBs of storage.
  - Cluster never expire.
  - Access to a subnet of Atlas features (Chart, Stitch).
- Also used for large scale deployments with other subscription options.

### Why use Atlas

- Simplicity of set-up.
  - Atlas automatic deploys and manages clusters.
- Easy access to different cloud providers and regions.
- Free access to experiment with new tools and features.

## MongoDB Compass

- Graphical User Interface for exploring data.
- No need for formal knowledge of the MongoDB query syntax.
- Uses:
  - Optimize queries.
  - Manage indexes.
  - Explore data.
- Two methods to connect to your deployment:
  - Using the connection string.
  - Filling out deployment information in individual fields.

## Mongo Shell

- Interactive JavaScript interface to MongoDB.
- To start without connect it:

```shell
mongo --nodb
```

- Connecting to a Host:
  - `HOST="mongodb+srv://cluster0-jxeqq.mongodb.net/test"`
  - `USER="m001-student"`
  - `PASSWORD="m001-mongodb-basics"`

```shell
mongo $HOST --username $USER -password $PASSWORD
```

- Closing the Host connection:

```mongo
exit
```
