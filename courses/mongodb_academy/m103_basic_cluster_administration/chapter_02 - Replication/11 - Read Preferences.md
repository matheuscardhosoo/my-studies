# Read Preferences

## Table of contents

- [Read Preferences](#read-preferences)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Command](#command)
  - [Modes](#modes)
    - [primary](#primary)
    - [primaryPreferred](#primarypreferred)
    - [secondary](#secondary)
    - [secondaryPreferred](#secondarypreferred)
    - [nearest](#nearest)
  - [When use Read Preferences?](#when-use-read-preferences)

## Introduction

- Read preference allows your applications to route read operations to specific members of a replica set.
- Read preference is principally a driver side setting.

## Command

- Querying something with Read Preferences as "secondaryPreferred":
  - The preference can be changed for any other preference.

```js
db.products.find({...}).readPref("secondaryPreferred")
```

- With secondary reads, always keep in mind that depending on the amount of replication latency in a replica set, you can receive stale data.
- The big drawback of using a read preference, other than primary, is the potential for stale read operations.

## Modes

### primary

  - Routes all read operations to the primary only.
  - Default mode.

### primaryPreferred

  - Routes read operations to the primary.
  - But if the primary is unavailable, such as during an election or fail-over event, the application can route reads to an available secondary member instead.

### secondary

  - Routes read operations only to the secondary members in the replica set.

### secondaryPreferred

  - Routes read operations to the secondary members.
  - But if no secondary members are available, the operation then routes to the primary.

### nearest

  - Routes read operations to the replica set member with the least network latency to the host, regardless of the members type.
  - This typically supports geographically local read operations.
  - Geographically distributed replica sets are more likely to suffer from stale reads, for example, than a replica set where all the members are in the same geographic region, or even the same data center.

## When use Read Preferences?

| Scenario                                                  | Tradeoff                         | Read Preference        |
| --------------------------------------------------------- | -------------------------------- | ---------------------- |
| Read from primary only                                    | Secondaries are for availability | **primary**            |
| If the primary is unavailable, read from a secondary      | Possible to read stale data      | **primaryPreferred**   |
| Read from the secondary members only                      | Possible to read stale data      | **secondary**          |
| If all secondaries are unavailable, read from the primary | Possible to read stale data      | **secondaryPreferred** |
| Application's read from the geographically closest member | Possible to read stale data      | **nearest**            |
