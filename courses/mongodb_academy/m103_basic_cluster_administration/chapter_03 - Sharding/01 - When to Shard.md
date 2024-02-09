# When to Shard

## Table of contents

- [When to Shard](#when-to-shard)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Economical Indicator](#economical-indicator)
    - [Situation](#situation)
    - [What to check](#what-to-check)
    - [Evaluation](#evaluation)
      - [Vertical Scaling](#vertical-scaling)
      - [Horizontal Scaling](#horizontal-scaling)
  - [Operational Indicator](#operational-indicator)
    - [Evaluation](#evaluation-1)
      - [Vertical Scaling](#vertical-scaling-1)
      - [Horizontal Scaling](#horizontal-scaling-1)
  - [Geographic Indicator](#geographic-indicator)

## Introduction

- It is necessary to consider some indicators before apply a **Sharding Cluster**:
  - Is it economically viable compared to **Vertical Scale**?
  - How does it impact your operational tasks?
  - Do you need to geo-distribute your data?
- Geo-distributed data is significantly simple to manage using zone sharding.

## Economical Indicator

### Situation

- When we need to address a throughput performance or volume bottleneck, which are generally the technical drivers for adding more resources to your system.

### What to check

- Can we still add more resources and scale up?
  - We need to validate that adding more of those vertical resources (such as adding more CPU, network, memory, or disk to your existing servers) is economically viable and possible.

### Evaluation

#### Vertical Scaling

- In beginning stages (small set of servers with low/average performance, where nodes can easily improve), **Vertical Scaling** probably would be the option.
- You are still able to do so in economical viable manner, but you will eventually reach a point where vertical scaling is no longer economically viable or it's very difficult to say impossible to accomplish.
#### Horizontal Scaling

- At this point, it is probably easier to create new instances than to improve current ones.
- In addition, new instances increase performance linearly, while vertical scaling shows signs of saturation.

## Operational Indicator

### Evaluation

#### Vertical Scaling

- Isn't always easy to apply considering that all server components are directly or indirectly connected.
- One improvement done probably would request some others in different scales and sectors (due to system coupling).
#### Horizontal Scaling

- Balances service load between multiple machines, providing a linear performance improvement with safe support for action (since the same schema already has been used).
  - It simplifies the scaling process and avoid unexpected load issues.

- In such a scenario, having horizontal scale and distributing that amount of data across different shards, will allow getting horizontal performance gains like parallelization of the backup, restore, and initial sync processes.
  - This same scenario will also impact positively your operational workload.
  - There are workloads that intrinsically play nicer in distributed deployments that sharing offers, like single threaded operations that can be parallelized and geographically distributed data.

- Data that needs to be stored in specific regional locations or will benefit from being co-located with the clients that consume such data.

## Geographic Indicator

- Zone sharding allows us to easily distribute data that needs to be co-located.