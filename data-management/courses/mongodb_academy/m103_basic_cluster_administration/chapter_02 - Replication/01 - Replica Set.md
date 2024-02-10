# Replica Set

## Table of contents

- [Replica Set](#replica-set)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Primary Node](#primary-node)
  - [Secondary Node](#secondary-node)
  - [Arbiter Node](#arbiter-node)
  - [Hidden Node](#hidden-node)
  - [Delayed Node](#delayed-node)
  - [oplog](#oplog)
  - [Asynchronous replication](#asynchronous-replication)
    - [PV1](#pv1)
      - [Leader Election](#leader-election)
        - [Algorithm](#algorithm)
      - [Log Replication](#log-replication)
        - [Algorithm](#algorithm-1)

## Introduction

- **Replica Sets** or **Replica Groups** are instances of **mongods** that share copies of the same information between them.
- The members of a **Replica Set** can perform one of two different roles: **primary node** or **secondary node**.
- Should always have at least an odd number of nodes (least 3 nodes). In case of even number, it is necessary to make sure that the majority is consistently available.
- The list of members in their configurations defines the **Replica Set Topology**.
- Any topology change (adding, failing or changing members or set configuration) will trigger an election.
- The **Replica Set** configuration is defined in one of the nodes and then shared between all members through the replication mechanism.
- Now, **Replica Sets** can go up to 50 members (useful for geographical distribution of redundant nodes).
- Only a maximum of 7 members can be voting members.
- Supports **hidden** and **delayed nodes** (useful for backup strategies).

## Primary Node

- All reads and all writes are served by this node.
- Every time an application writes some data to the **Replica Set**, that is handled by the primary node and then data gets replicated to the secondary nodes.

## Secondary Node

- The responsibility of this node is to replicate all of the information, and then serve as a high availability to node in case of failure of the primary.

## Arbiter Node

- Apart from a **primary** or **secondary** role, a replica set member can also be configured as an **arbiter**.
- An **arbiter** is a member that holds no data.
- Serves as a tiebreaker between **secondaries** in an election.
- As it has no data, it can never become primary.
- **It causes significant consistency issues in distributed data systems**.
- **The usage of arbiters is a very sensitive and potentially harmful option in many deployments**.

## Hidden Node

- Nodes set to not appear in common replication process.
- The purpose of a **hidden node** is to provide specific read-only workloads, or have copies over your data which are hidden from the application.

## Delayed Node

- Nodes set with a delay in their replication process.
- The purpose of having **delayed node** is to allow resilience to application level corruption, without relying on cold backup files to recover from such an event.
- Hot backups (easy and fast recover option).

## oplog

- The **oplog** is a segment based lock that keeps track of all write operations acknowledged by the replica sets.
- Every time a write is successfully applied to the primary node, it will get recorded in the **oplog in its idempotent form**.
- It gets the data from the primary through an asynchronous replication mechanism.

## Asynchronous replication

- Versions: PV1 (default, current), PV0.
- The different versions of the replication protocol will vary slightly on the way durability and availability will be forced throughout the set.

### PV1

- This protocol is based out of the RAFT protocol.
- **Entities**: **leader** (Primary node), **followers** (Secondary node), and **candidates**.
- Ref: [**Simple Raft Protocol**](http://thesecretlivesofdata.com/raft/).
- Ref: [**Consensus Algorithm**](https://raft.github.io/)
- Ref: [**The Raft Paper**](https://raft.github.io/raft.pdf)

#### Leader Election

- Only one **leader** can be elected per term.
- **Timeout**: The election timeout is the amount of time a follower waits until becoming a candidate (randomized to be between 150ms and 300ms).
- **Request Vote**: Message sent by **candidate** to others **followers** requesting votes.
- **Heartbeat Messages**:  Append Entries messages sent by **leader** to its **followers** (and responded by them) to map the available nodes.
- **Heartbeat Timeout**: interval between **Heartbeat Messages**.

##### Algorithm

1. The election timeout counter starts.
2. After the election timeout ends, the **followers** become **candidates** and starts a new election term.
3. The **candidates** send out **Requests Vote** messages to other nodes.
4. Once a **follower** has not voted yet, it returns the request and restart the election timeout.
5. The **leader** sends its **Heartbeat Messages**.
6. This election term will continue until a **follower** stops receiving heartbeats and becomes a candidate.

#### Log Replication

- Uses **oplogs** to transmit the operations.
- Once we have a **leader** elected, we need to replicate all changes of our system to all nodes.
- This is done by using the same **Append Entries** messages that was used for heartbeats.
- An entry is committed once a majority of **followers** acknowledge it and a response is sent to the client.
- It stays uncommitted if not reach the majority of nodes.
- Uncommitted operations are rolled back if it does not match the leader's log.

##### Algorithm

1. All nodes begin as **followers**.
2. (Leader Election) If no **leader** exists, **followers** can become **candidates** requesting votes from other nodes. The node with the majority of votes became the **leader**.
3. (Log Replication) All input operations are sent to **leader** by oplog and replicated to **followers**.
