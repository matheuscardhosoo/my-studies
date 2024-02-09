# Introduction and Setup

## Table of contents

- [Introduction and Setup](#introduction-and-setup)
  - [Table of contents](#table-of-contents)
  - [Course curriculum](#course-curriculum)
  - [Vagrant Environment](#vagrant-environment)
    - [Why](#why)
    - [How](#how)

## Course curriculum

- Deploying MongoDB.
- Administration tools.
- Mongod.
  - MongoDB Core.
  - Request and access manage.
  - Logs.
  - Availability.
  - Reication.
  - Scalability.
    - Sharding.

## Vagrant Environment

### Why

- Sandbox environment.
- Avoid dependency and system troubleshooting.

### How

- Install Vagrant and VirtualBox.
- Create the vagrant-env.

```shell
# To configure and start.
vagrant up --provision

# To start.
vagrant up

# To connect.
vagrant ssh

# To stop.
vagrant halt

# To validate.
validate_box
```
