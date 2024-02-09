# Replication Configuration Document

## Table of contents

- [Replication Configuration Document](#replication-configuration-document)
  - [Table of contents](#table-of-contents)
  - [Configuration Document](#configuration-document)
  - [Configuration structure:](#configuration-structure)
    - [_id](#_id)
    - [version](#version)
    - [members](#members)
      - [_id](#_id-1)
      - [host](#host)
      - [arbiterOnly](#arbiteronly)
      - [hidden](#hidden)
      - [priority](#priority)
      - [slaveDelay](#slavedelay)
    - [settings](#settings)

## Configuration Document

- **Document Type**: BSON.
- **Document Interface**: JSON.
- Where the Replica Set's configuration is defined.
- Is shared across all the member nodes.
- Can be manually set or by the mongodb shell commands (some examples below).

```js
rs.add()
rs.initiate()
rs.remove()
rs.reconfig()
rs.config()
```

## Configuration structure:

```json
{
  _id: <string>,
  version: <int>,
  members: [
    {
      _id: <int>,
      host: <string>,
      arbiterOnly: <boolean>,
      hidden: <boolean>,
      priority: <int>,
      slaveDelay: <int>
    },
    ...
  ],
  settings: {
    ...
  }
}
```

### _id

- The name of the Replica Set.
- It should match with the server defined Replica Set name. In case of different values, the server end up with an error message.

### version

- Integer that gets incremented every time the current configuration of replica set changes.
- Changes on topology, Replica Set configurations, or something like changing the number of votes of a given host, will automatically increment the **version** number.

### members

- Where the topology of our Replica Set is defined.
- Each element of the members array is a sub-document that contains the (replication) configuration of the node.

#### _id

- Member id.

#### host

- Comprised of the host name and port.

#### arbiterOnly

- This means that the node will not be holding any data, and its contribution to the set is to ensure quorum in elections.
- false by default.

#### hidden

- Sets the node in hidden role.
- An hidden node is not visible to the application, which means that every time we emit something like an RS is master command, this node will not be listed.
- false by default.

#### priority

- Integer value that allows us to set a hierarchy within the replica set.
- Between 0 and 1,000.
- Members with **higher priority** tend to be elected as primaries more often.
- A change in the **priority** of a node will trigger an election because it will be perceived as a topology change.
- Setting **priority** to 0 effectively excludes that member from ever becoming a primary.
- **arbiterOnly** or **hidden** imply that the **priority** needs to be set to 0.

#### slaveDelay

- Determines a replication delay interval in seconds.
- 0 by default.
- These delayed members maintain a copy of data reflecting a state in some point in the past, applying that delay in seconds.
- **slaveDelay** implies that the respective node will be **hidden**, and the **priority** will be set to 0.

### settings

- Other configurations.