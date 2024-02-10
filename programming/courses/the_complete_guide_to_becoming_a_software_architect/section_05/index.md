# 5. Working with System Requirements

## 5.1. Table of contents

- [5. Working with System Requirements](#5-working-with-system-requirements)
  - [5.1. Table of contents](#51-table-of-contents)
  - [5.2. Introduction to Requirements](#52-introduction-to-requirements)
  - [5.3. The Two Types of Requirements](#53-the-two-types-of-requirements)
    - [5.3.1. Functional Requirements](#531-functional-requirements)
    - [5.3.2. Non-Functional Requirements](#532-non-functional-requirements)
  - [5.4. Architects & Functional Requirements](#54-architects--functional-requirements)
  - [5.5. Non-Functional Requirements](#55-non-functional-requirements)
    - [5.5.1 Performance](#551-performance)
      - [General question](#general-question)
      - [Data driven analysis](#data-driven-analysis)
      - [Some rules](#some-rules)
      - [Latency](#latency)
        - [General question:](#general-question-1)
        - [Examples:](#examples)
      - [Throughput](#throughput)
        - [General question:](#general-question-2)
        - [Examples:](#examples-1)
      - [Latency $\times$ Throughput](#latency-times-throughput)
    - [5.5.2 Load](#552-load)
      - [General question:](#general-question-3)
      - [Notes](#notes)
      - [Throughput $\times$ Load](#throughput-times-load)
      - [Examples:](#examples-2)
    - [5.5.3 Data Volume](#553-data-volume)
      - [General question:](#general-question-4)
      - [Helps with:](#helps-with)
      - [Examples:](#examples-3)
    - [5.5.4 Concurrent Users](#554-concurrent-users)
      - [General question:](#general-question-5)
      - [Concurrent Users $\times$ Load](#concurrent-users-times-load)
    - [5.5.5 SLA (Service Level Agreement)](#555-sla-service-level-agreement)
      - [General question:](#general-question-6)
      - [Examples](#examples-4)
      - [Notes](#notes-1)
  - [5.6. Who Defines Non-Functional Requirements?](#56-who-defines-non-functional-requirements)
  - [5.7. Conclusion](#57-conclusion)

## 5.2. Introduction to Requirements

- Types of Requirements.
- Levels of abstraction.

## 5.3. The Two Types of Requirements

### 5.3.1. Functional Requirements

- General question:

  > What the System should do?

- Specific questions:
  - What is the business flow of the system?
    - i.e.: login, store photos, receiving and crunching telemetry data.

  - What the business services should the system have?
    - i.e.: logging service, data access service, telemetry receiver service, telemetry control service.

  - What does the user interface of the system looks like?

- Extremely important for the process. No system should be designed and built without them.

### 5.3.2. Non-Functional Requirements

- General question:

  > What the System deal with?

- Describes aspects of the system operation and aren't tied to a specific behavior of logic.
- The most interesting point for the Architect, because they affects a lot the Architecture.
- The most common Non-Functional Requirements:
  - Performance.
  - Load.
  - Data Volume.
  - Concurrent Users.
  - SLA.

## 5.4. Architects & Functional Requirements

- Mainly associated with features development, this less important than the Non-Functional Requirements, but needs to be equal considered by the Architect.

## 5.5. Non-Functional Requirements

- Describe what is the expected environment for the system with emphasis on edge cases.

### 5.5.1 Performance

#### General question

> What is the required performance for the system?

#### Data driven analysis

- Always talk in numbers
- What is fast? 
- Usually the client doesn't known the exact values that define the performance. So, as an Architect you should help him to discover.

#### Some rules

- If there is an end user, the task must be completed less than 1 second.
  - The human doesn't differentiate times lesser than this.

- If it is a business-to-business system, we should consider even 100 ms per task.
  - Little time difference can cause a big impact when we have multiple machine loops.

- The data driven analysis should be done together with the Client and the System Analyst.

#### Latency

##### General question:

> How much time does it take to perform a single task?

##### Examples:

> How much time will it take for the API to save the user data in the database?<br>
> How much time will it take to read a single file from the filesystem?

#### Throughput

##### General question:

> How many tasks can be performed in a given time unit?

##### Examples:

> How many users can be saved in the database in a minute?<br>
> How many files can be read in a second?

#### Latency $\times$ Throughput

- Example: Saving user data.

| Metric | Value | Note |
| ------ | ----- | ---- |
| Latency | $1$ Second | It's slow but is only an example. |
| Throughput (in $1$ minute) | $> 1000$ users' data | In a well designed system, the requests are processed in parallel and in a "efficient way". |
| Throughput (in $1$ minute) | $< 60$ users' data | In a ill system (buggy, with memory leaks, no-concurrent, etc). |

### 5.5.2 Load

#### General question:

> What the application have to withstand without crashing?

#### Notes

- Users can tolerate a slowdown when there is a load but they won't like it if the system crash and burn.
- Always plan for the extreme cases (look at peak numbers).
- It's common differ the regular situations' load from the extreme situations' load.
#### Throughput $\times$ Load

- Throughput is related to the performance of the system.
- Load is related to the availability of the system.

#### Examples:

- For a web API based application, the load will usually be defined as:
  > How many concurrent requests are going to be received by the system without cashing.

| Metric | Value |
| ------ | ----- |
| Throughput | 100 requests $/$ second |
| Load | 500 requests without crashing |

### 5.5.3 Data Volume

#### General question:

> How much data the system will accumulate over the time?

#### Helps with:

- Deciding on Database type.
- Designing optimizing queries considering the data volume for each entity.
- Store planning.
  > (Initial/Pre-loaded data) How much data is required at the day one?<br>
  > (Data growth) What is the forecasted data growth?

#### Examples:

| Metric | Value |
| ------ | ----- |
| Initial data | 500 MB |
| Data growth (per year) | 2 TB |

### 5.5.4 Concurrent Users

#### General question:

> How many users will be using the system simultaneously?

#### Concurrent Users $\times$ Load

- Concurrent Users includes "Dead Times" (when no action is performed).
    > How many **users** will be using the system simultaneously?<br>
    > After an API request, how much time the user is analyzing the requested data in the Front-End (without do any other request)?

- Load includes only effective time.
    > How many **requests** will be performed by the system simultaneously?<br>
    > How much time the request take to get the data from the database and return it to the user?

- Rule of Thumb: Concurrent Users $=$ Load $\times 10$

### 5.5.5 SLA (Service Level Agreement)

#### General question:

> What is the required uptime for the system (in percentage)?<br>
> Given a time interval, how much time the service must be available?

#### Examples

- SLA $= 99.99\%$
  - In a year:
    - Hours in a year: $8760$ hours
    - Downtime: $8760 \times 99.99\% = 0.88$ hours

#### Notes

- The time that the system is available.
- It doesn't consider the time while the system is unavailable because it is updating.
- Usually the Client doesn't know to define a value for this metric, exaggerating it (with a no realistic value). So, it is important to align the Client expectation about SLA, explaining the cost for a high SLA and adjusting it for system s real necessity.


## 5.6. Who Defines Non-Functional Requirements?

- The Client/System Analyst usually doesn't know "how to define"/"what is" the Non-Functional Requirements.
- Architect roles:
  - Be a guide in the discussion about Non-Functional Requirements.
  - Framing the requirements' boundaries.
  - Discuss numbers (to define real numbers).

## 5.7. Conclusion

- Define what the system will have to deal with.
- Client won't be able to define the Non-Functional Requirements.
- **Never** begin working on a system without Non-Functional Requirements in place.
