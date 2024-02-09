# Roles

## Table of contents

- [Roles](#roles)
  - [Table of contents](#table-of-contents)
  - [Built-In Roles](#built-in-roles)
    - [Built-in Roles for database level](#built-in-roles-for-database-level)
      - [Database User (application users)](#database-user-application-users)
      - [Database Administrator](#database-administrator)
      - [Cluster Administrator](#cluster-administrator)
      - [Backup/Restore](#backuprestore)
      - [Super User](#super-user)
    - [Built-in roles for all database level](#built-in-roles-for-all-database-level)
      - [Database User (application users)](#database-user-application-users-1)
      - [Database Administrator](#database-administrator-1)
      - [Super User](#super-user-1)
  - [Custom Roles](#custom-roles)
    - [Patterns](#patterns)
      - [Security Officer Pattern](#security-officer-pattern)
      - [Database Administrator Pattern](#database-administrator-pattern)
      - [Database Restrictions Pattern](#database-restrictions-pattern)

## Built-In Roles

- Pre-packaged MongoDB roles.

### Built-in Roles for database level

#### Database User (application users)

- `read`
- `readWrite`

#### Database Administrator

- `dbAdmin`
- `userAdmin`
- `dbOwner`

#### Cluster Administrator

- `clusterAdmin`
- `clusterManager`
- `clusterMonitor`
- `hostManager`

#### Backup/Restore

- `backup`
- `restore`

#### Super User

- `root`

### Built-in roles for all database level

#### Database User (application users)

- `readAnyDatabase`
- `readWriteAnyDatabase`

#### Database Administrator

- `dbAdminAnyDatabase`
- `userAdminAnyDatabase`

#### Super User

- `root`

## Custom Roles

- Tailored roles to attend specific needs of sets of users.

### Patterns

#### Security Officer Pattern

- After create the root user, the first thing we should do is create a `security_officer` user in `admin` database with `userAdmin` role for the `admin` database.

  - It will do the all users complete management.
  - It cannot administrate data.

```js
db.createUser(
  {
    "user": "security_officer",
    "pwd": "h3ll0th3r3",
    "roles": [
      {
        "db": "admin",
        "role": "userAdmin"
      }
    ]
  }
);
```

#### Database Administrator Pattern

- After create the `security_officer` user, we should create a `dba` user in `admin` database with `dbAdmin` role for the `any` database.

  - It will do the complete DDA (Data Definition Language) management for specified databases.
  - It cannot administrate users.
  - It cannot do DML (Data Modification Language) processes.
    - It cant modify | create | remove specific data.

```js
db.createUser(
  {
    "user": "dba",
    "pwd": "c1lynd3rs",
    "roles": [
      {
        "db": "any",
        "role": "dbAdmin"
      }
    ]
  }
);
```

#### Database Restrictions Pattern

- After create the `dba` user, we can create users with roles restrict to specific databases.

- The example creates a user to complete manage data and users for the specified database.

```js
db.createUser(
  {
    "user": "m103_dba",
    "pwd": "c1lynd3rs",
    "roles": [
      {
        "db": "m103",
        "role": "dbOwner"
      }
    ]
  }
);
```

- The example creates a `readWrite` user for the `applicationData` database in `admin` source authentication.

```js
db.createUser(
  {
    "user": "m103-application-user",
    "pwd": "m103-application-pass",
    "roles": [
      {
        "db": "applicationData",
        "role": "readWrite"
      }
    ]
  }
);
```
