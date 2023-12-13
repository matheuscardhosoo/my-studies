# NoSQL - Distilled

---

### Book Details

- **Title**: NoSQL - Distilled
- **Author**: Pramod J. Sadalage, Martin Fowler
- **Publisher**: Addison-Wesley
- **Published**: 2012-08-01
- **ISBN-10**: 0321826620
- **Amazon Link**: 
  - [**English Edition**](https://www.amazon.com/NoSQL-Distilled-Emerging-Polyglot-Persistence/dp/0321826620)
  - [**Portuguese Edition**](https://www.amazon.com.br/NoSQL-Essencial-Emergente-Persist%C3%AAncia-Poliglota-ebook/dp/B07V5635ZQ)

---

## Chapter 1. Why NoSQL?

### 1.1. The Value of Relational Databases

- **Persistent data**: when compared to file systems, relational databases provide a much more flexible and powerful way to store and query data.
- **Concurrency**: relational databases provide manage concurrency and provide transactional guarantees.
- **Inter-application Integration**: data can be shared between applications using a common database or syncing data between databases.
- **A Mostly Standard Model**: the relational model is a standard model that is implemented by many vendors.

### 1.2. Impedance Mismatch

- **Object-Relational Impedance Mismatch**: the difference between the relational model and the in-memory data structures of the programming language.
- The relational model is organized around relations (tables) and tuples (rows).
  - A tuple is a set of name-value pairs.
    - Values in tuples have to be simple (e.g. no nested objects, no arrays, etc.)
  - A relation is a set of tuples with the same set of attributes.
  - All operations are performed on relations (which leads to a mathematically relational algebra).
- On the other hand, the in-memory data structures of the programming language are organized around objects identified by its memory address.
- This foundational difference leads to a mismatch between the relational model and the in-memory data structures of the programming language.
- This mismatch leads to a lot of boilerplate code to map between the relational model and the in-memory data structures of the programming language. Furthermore, the abstractions can become a problem of their own when people try too hard to ignore the database and query performance suffers.

### 1.3. Application and Integration Databases

- **Integration Database**: a database that is used by multiple applications.
  - A big  reason for the success of relational databases during the 80s and 90s was the need for integration databases. The relational model was a good fit for this use case because it provided a standard model that could be used by multiple applications in a consistent way.
  - But, this approach has its own problems:
    - **Data/Schema Integration**: the data/schema of the database has to be designed to support all the applications that use it. This leads to a lot of compromises and a lot of unused data.
    - **Performance**: the database has to be tuned to support all the applications that use it. This leads to a lot of compromises and performance problems.
- **Application Database**: a database that is used by a single application.
  - This approach is much more common today because it avoids the problems of integration databases, bringing the focus back to the application and giving more flexibility to the database choice.
  - It's only possible because of the rise of the web protocols and the fact that most applications are now accessed through APIs. This makes it possible to have multiple applications with their own databases that share data through their APIs.
    - This approach is called **Service-Oriented Architecture** (SOA) and deals with different integration problems than the integration databases (like consistency along distributed data, availability, etc.).
    - In a first moment, this approach was executed by separating the application into two parts **Presentation Tier** and **Business Data Tier** which communicate each other using the HTTP protocol to exchange data in a format like XML or JSON.
      - This provided more flexibility for the structure of the data that was being exchanged between the two tiers.

### 1.4. Attack of the Clusters

- **Cluster**: a group of computers that work together to provide a single service.
1. **Dot-com boom**: the early 2000s saw the burst of the 1990s dot-com bubble, leading to questions about the economic future of the Internet.
2. **Increase in Web Scale**: Despite the dot-com bubble burst, the 2000s saw a dramatic increase in the scale of web properties. Websites began tracking activity and structure in detail, leading to large sets of data.
3. **Growth in Data and Users**: The growth in data was accompanied by a growth in users, requiring more computing resources.
4. **Scaling Up vs Scaling Out**: To handle the increase in data and traffic, two options were available: scaling up (bigger machines, more processors, disk storage, and memory) or scaling out (using lots of small machines in a cluster).
5. **Clusters and Relational Databases**: As large properties moved towards clusters, it revealed that relational databases are not designed to be run on clusters. This led to technical issues and increased licensing costs.
6. **Google and Amazon's Influence**: Google and Amazon, both capturing huge amounts of data and running large clusters, considered alternative routes to data storage. They produced influential papers about their efforts: BigTable from Google and Dynamo from Amazon.
   - **BigTable**: a distributed storage system for managing structured data that is designed to scale to a very large size: petabytes of data across thousands of commodity servers.
   - **Dynamo**: a highly available key-value storage system that some of Amazon's core services use to provide an "always-on" experience.
7. **New Databases for Clusters**: As more information about what Google and Amazon had done became available, people began to explore creating databases designed to live in a world of clusters, posing a serious threat to the dominance of relational databases.

### 1.5. The Emergence of NoSQL

- **Origin of the term NoSQL**: The term "NoSQL" first appeared in the late 90s as the name of an open-source relational database. The current usage of "NoSQL" that we recognize today traces back to a meetup on June 11, 2009 in San Francisco.
- **Definition of NoSQL**: NoSQL has never had a strong definition. Common characteristics of databases that tend to be called "NoSQL" include the absence of SQL, most are open-source projects, are oriented to operate on clusters, operate without a schema, and are based on the needs of the early 21st century web properties.
- **Interpretation of the term NoSQL**: Most people who talk about NoSQL say that it really means "Not Only SQL". However, this interpretation has some problems.
- **Contribution of NoSQL**: The most important contribution of NoSQL is opening up the range of options for data storage. This is often referred to as polyglot persistence - using different data stores in different circumstances.
- **Use of NoSQL**: Organizations need to shift from integration databases to application databases. NoSQL is seen as a good choice for application databases.
- **Reasons to consider NoSQL**: The two main reasons for considering NoSQL are to handle data access with sizes and performance that demand a cluster and to improve the productivity of application development by using a more convenient data interaction style.

### 1.6. Key Points

- Relational databases have been a successful technology for twenty years, providing persistence, concurrency control, and an integration mechanism.
- Application developers have been frustrated with the impedance mismatch between the relational model and the in-memory data structures.
- There is a movement away from using databases as integration points towards encapsulating databases within applications and integrating through services.
- The vital factor for a change in data storage was the need to support large volumes of data by running on clusters. Relational databases are not designed to run efficiently on clusters.
- NoSQL is an accidental neologism. There is no prescriptive definition— all you can make is an observation of common characteristics.
- The common characteristics of NoSQL databases are - Not using the relational model
  - Running well on clusters
  - Open-source
  - Built for the 21st century web estates
  - Schemaless
  - The most important result of the rise of NoSQL is Polyglot Persistence.

## Chapter 2. Aggregate Data Models

- **Definition of Data Model**: The data model is the method through which we perceive and manipulate our data. It is different from the storage model, which is about how the database stores and manipulates the data internally.
- **Use of Data Model**: In conversation, the term "data model" often refers to the model of the specific data in an application. However, in the context of this book, "data model" refers to the model by which the database organizes data.
- **Relational Data Model**: The dominant data model of the last couple of decades is the relational data model, visualized as a set of tables with rows and columns.
- **Shift to NoSQL**: NoSQL represents a shift away from the relational model. Each NoSQL solution uses a different model, categorized into four types: key-value, document, column-family, and graph.
- **Aggregate Orientation**: The first three NoSQL models (key-value, document, column-family) share a common characteristic called aggregate orientation.

### 2.1. Aggregates

- **Relational Model**: This model divides information into tuples or rows. It's a simple structure that doesn't allow for nesting of tuples or lists within tuples.
- **Aggregate Orientation**: This approach allows for more complex data structures. It's useful for operating on data units that have a more complex structure than a set of tuples.
- **Key-Value, Document, and Column-Family Databases**: These databases use the aggregate orientation approach. They handle operations on a cluster more easily due to the aggregate structure.
- **Domain-Driven Design**: The term "aggregate" comes from this design approach. An aggregate is a collection of related objects treated as a unit for data manipulation and consistency management.
- **Aggregates and Database Operations**: Aggregates make it easier for databases to handle operations like replication and sharding. They are also easier for programmers to work with as they often manipulate data through aggregate structures.

#### 2.1.1. Example of Relations and Aggregates

Let’s assume we have to build an e-commerce website; we are going to be selling items directly to customers over the web, and we will have to store information about users, our product catalog, orders, shipping addresses, billing addresses, and payment data. We can use this scenario to model the data using a relation data store as well as NoSQL data stores and talk about their pros and cons.

##### Relational Model

```mermaid
classDiagram
    Customer "1" -- "*" Order
    Customer "1" -- "*" Billing Address
    Billing Address "*" -- "1" Address
    Order "1" -- "*" Order Payment
    Order "1" -- "*" Order Item
    Order "1" -- "1" Address : shipping address
    Order Payment "*" -- "1" Billing Address
    Order Item "*" -- "1" Product

    Customer : name
    Address : street
    Address : city
    Address : state
    Address : postalCode
    Order Payment : card number
    Order Item : price
    Product : name
```

##### 2-Aggregation Model

```mermaid
classDiagram
    Customer "1" -- "*" Order
    Customer "1" -- "[*]" Address : billing address
    Order "1" -- "[*]" Payment : order payment
    Order "1" -- "[*]" Order Item
    Order "1" -- "[1]" Address : shipping address
    Payment "1" -- "[1]" Address : billing address
    Order Item "*" -- "1" Product

    Customer : name
    Address : street
    Address : city
    Address : state
    Address : postalCode
    Payment : card number
    Order Item : price
    Product : name
```

```json
// in customers
{
    "id": 1,
    "name": "Martin",
    "billingAddress": [
        {
            "city": "Chicago"
        }
    ]
}
```

```json
// in orders
{
    "id": 99,
    "customerId": 1,
    "orderItems": [
        {
            "productId": 27,
            "price": 32.45,
            "productName": "NoSQL Distilled"
        }
    ],
    "shippingAddress": {
        "city": "Chicago"
    },
    "orderPayment": [
        {
            "ccinfo": "1000-1000-1000-1000",
            "txnId": "abelif879rft",
            "billingAddress": {
                "city": "Chicago"
            }
        }
    ]
}
```

The two main aggregates are 'customer' and 'order'.
- The 'customer' aggregate contains a list of billing addresses.
- The 'order' aggregate contains a list of order items, a shipping address, and payments. Each payment also contains a billing address.

An address record appears three times in the data, but it's treated as a value and copied each time to prevent changes to the shipping or billing address. This approach differs from a relational database where a new row would be created instead of updating existing address rows.

The relationship between 'customer' and 'order' is not within either aggregate, but between them. Similarly, the link from an 'order item' would cross into a separate 'product' aggregate, which is not detailed in the example.

The product name is shown as part of the 'order item', demonstrating denormalization, a common practice with aggregates to minimize the number of aggregates accessed during a data interaction.

##### 1-Aggregation Model

```mermaid
classDiagram
    Customer "1" -- "[*]" Order
    Customer "1" -- "[*]" Address : billing address
    Order "1" -- "[*]" Payment : order payment
    Order "1" -- "[*]" Order Item
    Order "1" -- "[1]" Address : shipping address
    Payment "1" -- "[1]" Address : billing address
    Order Item "*" -- "1" Product

    Customer : name
    Address : street
    Address : city
    Address : state
    Address : postalCode
    Payment : card number
    Order Item : price
    Product : name
```

```json
// in customers
{
    "customer": {
        "id": 1,
        "name": "Martin",
        "billingAddress": [
            {
                "city": "Chicago"
            }
        ],
        "orders": [
            {
                "id": 99,
                "customerId": 1,
                "orderItems": [
                    {
                        "productId": 27,
                        "price": 32.45,
                        "productName": "NoSQL Distilled"
                    }
                ],
                "shippingAddress": {
                    "city": "Chicago"
                },
                "orderPayment": [
                    {
                        "ccinfo": "1000-1000-1000-1000",
                        "txnId": "abelif879rft",
                        "billingAddress": {
                            "city": "Chicago"
                        }
                    }
                ],
            }
        ]
    }
}
```

This emphasizes the importance of considering data access patterns when defining aggregate boundaries in your application data model. The way you group your data into aggregates can vary based on how you typically manipulate your data.

For instance, if you often access a customer along with all their orders, it might be beneficial to put all orders into the customer aggregate. Conversely, if you usually work with one order at a time, it might be better to have separate aggregates for each order.

The choice of how to draw your aggregate boundaries is context-specific and can vary even within a single system. This flexibility is one reason why some developers prefer to work with systems that don't enforce a specific aggregate structure (aggregate ignorance).

#### 2.1.2. Consequences of Aggregate Orientation

- **Aggregate Entities**: The relational model lacks the concept of aggregate entities, which are groups of related data items that are treated as a single unit for data manipulation and consistency purposes.

- **Aggregate-Oriented Databases**: These databases provide clearer semantics for aggregates by focusing on the unit of interaction with the data storage. The definition of an aggregate is not a logical data property, but rather depends on how the data is used by applications.

- **Aggregate-Ignorant Databases**: Relational and graph databases are considered aggregate-ignorant because they don't have a concept of aggregate within their data model. This can be beneficial when the same data is used in many different contexts, as it allows for more flexibility in viewing and manipulating data.

- **Benefits of Aggregate Orientation**: Aggregate orientation can improve performance when running on a cluster by minimizing the number of nodes that need to be queried. It also provides important information to the database about which data items should be stored together.

- **Transactions and Aggregates**: While relational databases support ACID transactions that can manipulate any combination of rows from any tables, aggregate-oriented databases typically only support atomic manipulation of a single aggregate at a time. This can limit the scope of atomicity, but it's often sufficient for most use cases.

- **Consistency**: The topic of consistency in databases is more complex than whether a database supports ACID transactions or not. Other factors, such as how data is divided into aggregates, also play a role.

### 2.2. Key-Value and Document Data Models

- **Aggregate Orientation**: Key-value and document databases are strongly aggregate-oriented, meaning they are primarily constructed through aggregates. Each aggregate has a key or ID used to access the data.

- **Key-Value vs Document Databases**: Key-value databases treat aggregates as opaque blobs, while document databases see a structure in the aggregate. Key-value databases offer more freedom in what can be stored, while document databases provide more flexibility in access.

- **Accessing Aggregates**: In key-value stores, aggregates can only be accessed by their key. In contrast, document databases allow queries based on the fields in the aggregate, partial retrieval of the aggregate, and indexing based on the contents of the aggregate.

- **Blurring Lines**: The distinction between key-value and document databases can blur in practice. For example, key-value databases may allow structures for data beyond just an opaque aggregate, and document databases may use an ID field for key-value style lookups.

- **Expectations**: Generally, with key-value databases, we expect to look up aggregates using a key. With document databases, we mostly expect to submit queries based on the internal structure of the document.

### 2.3. Column-Family Stores

- **BigTable and Influences**: Google's BigTable, a NoSQL database, has influenced later databases like HBase and Cassandra. It's often referred to as a column store due to its data model.

- **Column Stores**: Column stores, like C-Store, store data by groups of columns for all rows as the basic storage unit. This is beneficial when writes are rare, but there's a need to read a few columns of many rows at once.

- **Column-Family Databases**: BigTable and its successors are referred to as column-family databases. They store groups of columns (column families) together but abandon the relational model and SQL.

- **Column-Family Model**: This model is a two-level aggregate structure. The first key is often a row identifier, and the row aggregate is formed of a map of more detailed values, referred to as columns.

- **Column Families**: Column-family databases organize their columns into column families. Each column is part of a single column family, and the column acts as a unit for access.

- **Data Structure**: The data can be structured in two ways: row-oriented, where each row is an aggregate with column families representing chunks of data within that aggregate; or column-oriented, where each column family defines a record type with rows for each of the records.

- **Cassandra's Approach**: Cassandra views things slightly differently. A row in Cassandra only occurs in one column family, but that column family may contain supercolumns—columns that contain nested columns.

- **Wide and Skinny Rows**: Column-family databases can have wide rows with many columns (modeling a list) and skinny rows with few columns (defining a record type).

- **Sort Order**: Column families can define a sort order for their columns, allowing access to orders by their order key and access ranges of orders by their keys.

### 2.4. Summarizing Aggregate-OrientedDatabases

- **Aggregate-Oriented Data Models**: These models are common in NoSQL databases and are characterized by the use of aggregates indexed by a key for lookup. They are crucial for running on a cluster, as they ensure all data for an aggregate is stored together on one node.
  - **Atomic Unit for Updates**: The aggregate acts as the atomic unit for updates, providing a degree of transactional control.

- **Key-Value Data Model**: This model treats the aggregate as an opaque whole, allowing only key lookup for the entire aggregate. It does not support running a query or retrieving a part of the aggregate.

- **Document Model**: This model makes the aggregate transparent to the database, enabling queries and partial retrievals. However, due to the lack of a schema, the database cannot optimize the storage and retrieval of parts of the aggregate based on its structure.

- **Column-Family Models**: These models divide the aggregate into column families, which the database can treat as units of data within the row aggregate. This imposes some structure on the aggregate, allowing the database to improve its accessibility.

### 2.5. Further Reading

- **Domain-Driven Design**: This book by Eric Evans is the definitive work on domain-driven design. It introduced the concept of aggregates and aggregate roots, which are the basis for the aggregate-oriented data model.

### 2.6. Key Points

- An aggregate is a collection of data that we interact with as a unit. Aggregates form the boundaries for ACID operations with the database.

- Key-value, document, and column-family databases can all be seen as forms of aggregate-oriented database.

- Aggregates make it easier for the database to manage data storage over clusters.

- Aggregate-oriented databases work best when most data interaction is done with the same aggregate; aggregate-ignorant databases are better when interactions use data organized in many different formations.

## Chapter 3. More Details on Data Models

### 3.1. Relationships

- **Aggregates and Data Access:** Aggregates group together commonly accessed data. However, the way data is accessed can vary, affecting how aggregates should be structured. For example, some applications may need to access a customer's entire order history, while others may need to process orders individually.

- **Relationships Between Aggregates**: There can be relationships between different aggregates, such as a customer and their orders. These relationships can be represented by embedding the ID of one aggregate within another. However, this approach makes the database ignorant of the relationship.

- **Database Awareness of Relationships**: Many databases, including key-value stores and document stores, provide ways to make these relationships visible to the database. This can be useful for forming indexes and queries, and for supporting partial retrieval and link-walking capabilities.

- **Updates and Atomicity**: Aggregate-oriented databases treat the aggregate as the unit of data retrieval, and only support atomicity within a single aggregate. If multiple aggregates are updated at once, handling a failure partway through becomes the developer's responsibility.

- **Operating Across Multiple Aggregates**: Working with multiple aggregates can be challenging with aggregate-oriented databases. While there are ways to manage this, the fundamental complexity remains.

- **Relational Databases and Complex Relationships**: While relational databases can handle complex relationships, they also have their limitations. As the number of joins in a query increases, writing SQL and managing performance can become difficult.

### 3.2. Graph Databases

- **Graph Databases**: Unlike most NoSQL databases, graph databases are not primarily designed for cluster operation. They are designed to handle small records with complex interconnections, making them ideal for data with complex relationships like social networks, product preferences, or eligibility rules.

- **Data Model**: The fundamental data model of a graph database is nodes connected by edges. There is a lot of variation in how data can be stored in nodes and edges, with some databases allowing additional attributes or storing Java objects.

- **Query Operations**: Graph databases provide query operations designed for their graph structure. This allows for efficient traversal of relationships, shifting most of the work from query time to insert time. This is beneficial when query performance is more important than insert speed.

- **Finding Data**: Data in a graph database is typically found by navigating through the network of edges. Some nodes can be indexed by an attribute for a starting point, but most query work is expected to be navigating relationships.

- **Comparison with Aggregate-Oriented Databases**: Graph databases differ significantly from aggregate-oriented databases due to their emphasis on relationships. They are more likely to run on a single server and require ACID transactions to cover multiple nodes and edges for consistency. The main similarity is their rejection of the relational model.

- **Example of a graph structure**:
    - Nodes: Alice, Bob, Charlie, David
    - Edges: Knows, Friend, Likes, Loves
    - Relationships:
        - Alice Knows Bob
        - Bob is a Friend of Charlie
        - Charlie Likes David
        - David Loves Alice
    - Possible queries:
        - Find all of Alice's friends
        - Find all of Alice's friends who like David
        - Find all of Alice's friends who like David and are loved by David

```mermaid
graph TB
    A[Person: Alice]
    B[Person: Bob]
    C[Person: Charlie]
    D[Person: David]
    
    A -- Knows --> B
    B -- Friend --> C
    C -- Likes --> D
    D -- Loves --> A
```

### 3.3. Schemaless Databases

- **Schemaless Databases**: NoSQL databases are often schemaless, meaning they do not require a predefined structure for the data they store. This contrasts with relational databases, which require a defined schema before data can be stored.

- **Flexibility of Schemaless Databases**: Schemaless databases allow for more flexibility in data storage. They can store any data under any key, document, column, or node. This flexibility is beneficial when the data to be stored is not fully known in advance or when the data structure may change over time.

- **Handling Nonuniform Data**: Schemaless databases handle nonuniform data more efficiently than relational databases. They allow each record to contain just what it needs, avoiding the need for null values or meaningless columns.

- **Implicit Schema in Programs**: Despite the schemaless nature of NoSQL databases, programs that access the data often rely on an implicit schema. They assume certain field names and data types, which can lead to problems if the assumptions do not match the actual data.

- **Problems with Implicit Schema**: Having an implicit schema in the application code can make it difficult to understand the data structure without examining the code. It also prevents the database from using the schema to optimize data storage and retrieval, and from validating the data.

- **Shifting the Schema to Application Code**: In a schemaless database, the schema is essentially shifted into the application code. This can cause problems if multiple applications access the same database, but these problems can be mitigated with certain approaches, such as encapsulating all database interaction within a single application.

- **Changing Relational Schemas**: Contrary to common criticism, relational schemas can be changed at any time with standard SQL commands. However, schemaless databases may still be preferred for nonuniform data.

- **Impact of Schemalessness on Database Structure Changes**: Schemalessness affects how a database's structure can be changed over time. Changes must be controlled to ensure old and new data can be accessed easily. The flexibility of schemalessness applies only within an aggregate; changing aggregate boundaries is as complex as in the relational case.

### 3.4. Materialized Views

- **Aggregate-Oriented Data Models**: These models have advantages in storing and accessing data as a unit, but can be disadvantageous when needing to access individual elements within the aggregate.

- **Relational Databases and Views**: Relational databases can support different data access methods due to their lack of aggregate structure. They use views, which are computations over base tables, to present data differently from how it's stored.

- **Materialized Views**: These are views that are computed in advance and cached on disk. They are useful for data that is read frequently but can tolerate being slightly outdated. 

- **Materialized Views in NoSQL Databases**: NoSQL databases may not have views, but they can have precomputed and cached queries, often referred to as materialized views. These are particularly important for aggregate-oriented databases when dealing with queries that don't align well with the aggregate structure.

- **Strategies for Building Materialized Views**: There are two main strategies - the eager approach, where the materialized view is updated simultaneously with the base data, and the batch approach, where materialized views are updated at regular intervals.

- **Building Materialized Views Outside the Database**: Materialized views can be built outside the database by reading the data, computing the view, and saving it back to the database. Alternatively, some databases support building materialized views internally.

- **Materialized Views within the Same Aggregate**: Materialized views can be used within the same aggregate to provide summary information, reducing the need to transfer the entire document for a query. This is a common feature in column-family databases and allows for atomic operations on the materialized view.

### 3.5. Modeling for Data Access

1. **Embedding All Data for a Customer**: The text begins by discussing a model where all data related to a customer, including details, billing addresses, payments, and orders, is embedded within a single object in a key-value store. This allows for easy retrieval of all customer-related data, but requires parsing on the client side to access specific information.

```json
// Customer Object
{
    "id": "Customer ID",
    "details": {
        "name": "Martin"
    },
    "billingAddresses": [
        {
            "city": "Chicago"
        }
    ],
    "payments": [
        {
            "type": "debit",
            "ccinfo": "1000-1000-1000-1000"
        }
    ],
    "orders": [
        {
            "orderDate": "Nov-20-2011",
            "shippingAddress": {
                "city": "Chicago"
            },
            "payments": [
                {
                    "ccinfo": "1000-1000-1000-1000",
                    "txnId": "abelif879rft"
                }
            ],
            "items": [
                {
                    "productId": 27,
                    "price": 32.45
                }
            ]
        }
    ]
}
```

```mermaid
---
title: Embed all the objects for customer and their orders.
---
flowchart TB
    subgraph "Customer (key = id | value = Object)"
        subgraph "Details (value = Object)"
        end
        subgraph "Billing Addresses (value = List[Object])"
        end
        subgraph "Payments (value = List[Object])"
        end
        subgraph "Orders (value = List)"
            subgraph "Order (value = Object)"
                subgraph "Shipping Address (value = Object)"
                end
                subgraph "Payments (value = List[Object])"
                end
                subgraph "Items (value = List)"
                    subgraph "Product (key = productId | value = Object)"
                    end
                end
            end
        end
    end
```

2. **Separating Customer and Order Data**: The text then discusses a model where customer and order data are stored separately, with references (like order IDs) used to link related data. This allows for more efficient querying but requires maintaining references between objects.

```json
// Customer Object
{
    "id": "Customer ID",
    "details": {
        "name": "Martin"
    },
    "billingAddresses": [
        {
            "city": "Chicago"
        }
    ],
    "payments": [
        {
            "type": "debit",
            "ccinfo": "1000-1000-1000-1000"
        }
    ],
    "orders": [
        {
            "orderId": 99
        }
    ]
}
```

```json
// Order Object
{
    "id": "Order Id",
    "customerId": "Customer ID",
    "orderDate": "Nov-20-2011",
    "shippingAddress": {
        "city": "Chicago"
    },
    "payments": [
        {
            "ccinfo": "1000-1000-1000-1000",
            "txnId": "abelif879rft"
        }
    ],
    "items": [
        {
            "productId": 27,
            "price": 32.45
        }
    ]
}
```

```mermaid
---
title: Customer is stored separately from Order.
---
flowchart TB
    subgraph "Customer (key = id | value = Object)"
        subgraph "Details (value = Object)"
        end
        subgraph "Billing Addresses (value = List[Object])"
        end
        subgraph "Payments (value = List[Object])"
        end
        subgraph "Orders (value = List)"
            subgraph "Order (key = orderId | value = Object)"
            end
        end
    end

    subgraph "Order (key = id | value = Object)"
        subgraph "Shipping Address (value = Object)"
        end
        subgraph "Payments (value = List[Object])"
        end
        subgraph "Items (value = List)"
            subgraph "Product (key = productId | value = Object)"
            end
        end
    end
```

3. **Using Aggregates for Analytics**: The text discusses how aggregates can be used to facilitate analytics, such as identifying which orders contain a particular product. This involves denormalizing the data to allow for faster access to relevant information.

```json
[
    {
        "productId": 27,
        "orders": {
            99,545,897,678
        }
    },
    {
        "productId": 29,
        "orders": {
            199,545,704,819
        }
    }
]
```

4. **Removing Order References from the Customer Object**: The text discusses a model where references to orders are removed from the customer object, allowing for updates to orders without needing to update the customer object. This is possible in document stores, which allow querying within documents.

```json
// Customer Object
{
    "id": "Customer ID",
    "details": {
        "name": "Martin"
    },
    "billingAddresses": [
        {
            "city": "Chicago"
        }
    ],
    "payments": [
        {
            "type": "debit",
            "ccinfo": "1000-1000-1000-1000"
        }
    ]
}
```

```json
// Order Object
{
    "id": "Order Id",
    "customerId": "Customer ID",
    "orderDate": "Nov-20-2011",
    "shippingAddress": {
        "city": "Chicago"
    },
    "payments": [
        {
            "ccinfo": "1000-1000-1000-1000",
            "txnId": "abelif879rft"
        }
    ],
    "items": [
        {
            "productId": 27,
            "price": 32.45
        }
    ]
}
```

5. **Modeling for Column-Family Stores**: The text discusses how to model data for column-family stores, emphasizing the importance of designing the model based on query requirements rather than write requirements. The text suggests denormalizing data during write operations to make querying easier.

```mermaid
---
title: Conceptual view into a column data store
---
flowchart TB
    subgraph "Customer (key = id | value = Object)"
        subgraph "Details (value = Object)"
        end
        subgraph "Orders (value = List[Object])"
        end
    end
    subgraph "Order (key = id | value = Object)"
        subgraph "Shipping Address (value = Object)"
        end
        subgraph "Payments (value = List[Object])"
        end
        subgraph "Items (value = List)"
            subgraph "Product (key = productId | value = Object)"
            end
        end
    end
```

6. **Using Graph Databases**: Finally, the text discusses how to model data using graph databases, where objects are modeled as nodes and relationships between them are modeled as edges. This allows for easy traversal of relationships, which can be useful for tasks like product recommendation or pattern detection.

```mermaid
---
title: Graph model of e-commerce data
---
graph TB
    A[Customer]
    B[Address]
    C[Product]
    D[OrderPayment]
    E[Order]
    
    A -- BILLED_TO --> B
    A -- BELONGS_TO --> D
    C -- PURCHASED --> A
    C -- PART_OF --> E
    E -- SHIPPED_TO --> B
    E -- PAID_WITH --> D
```

### 3.6. Key Points

- Aggregate-oriented databases make inter-aggregate relationships more difficult to handle than intra-aggregate relationships.

- Graph databases organize data into node and edge graphs; they work best for data that has complex relationship structures.

- Schemaless databases allow you to freely add fields to records, but there is usually an implicit schema expected by users of the data.

- Aggregate-oriented databases often compute materialized views to provide data organized differently from their primary aggregates. This is often done with map-reduce computations.

## Chapter 4. Distribution Models

- **NoSQL and Scalability**: The initial focus is on the key advantage of NoSQL databases: their ability to scale out across a large cluster of servers, which is particularly beneficial as data volumes increase.

- **Benefits and Costs of Scaling Out**: Scaling out can provide the ability to handle larger quantities of data, process greater read or write traffic, and maintain availability in the face of network issues. However, it also introduces complexity, making it a strategy to consider only when the benefits outweigh the costs.

- **Data Distribution Strategies**: The text introduces two main strategies for data distribution: replication and sharding. Replication involves copying the same data across multiple nodes, while sharding involves distributing different data across different nodes.

- **Replication Techniques**: The text further breaks down replication into two forms: master-slave and peer-to-peer. It outlines a plan to discuss these techniques in increasing order of complexity: single-server, master-slave replication, sharding, and finally peer-to-peer replication.

### 4.1. Single Server

- **Single-Server Distribution**: The simplest form of data distribution, recommended for its ease of management and simplicity for application developers.

- **NoSQL on Single-Server**: Despite many NoSQL databases being designed for cluster operation, using them in a single-server model can be beneficial if the data model suits the application, such as with graph databases or aggregate processing.

- **Complex Distribution Schemes**: While the rest of the chapter will discuss more complex distribution schemes, the single-server approach is preferred when possible, despite the greater volume of discussion dedicated to the more complex options.

### 4.2. Sharding

```mermaid
---
title: Sharding puts different data on separate nodes, each of which does its own reads and writes.
---
graph TB
    subgraph "Database Cluster"
        subgraph shard_1 ["Shard 1"]
            S1D1((♦️))
        end
        subgraph shard_2 ["Shard 2"]
            S2D1((♣️))
            S2D2((♥️))
        end
        subgraph shard_3 ["Shard 3"]
            S3D1((♠️))
        end
    end

    A1{"Application R/W\n♦️"} <-- R/W --> shard_1
    A2{"Application R/W\n♣️"} <-- R/W --> shard_2
    A3{"Application R/W\n♥️"} <-- R/W --> shard_2
    A4{"Application R/W\n♠️"} <-- R/W --> shard_3
```

- **Sharding**: A technique used to distribute different parts of a dataset across different servers for improved horizontal scalability.

- **Ideal Case of Sharding**: The ideal scenario is when different users interact with different server nodes, each user only communicates with one server, leading to faster responses and balanced load across servers.

- **Data Clumping and Aggregate Orientation**: The text talks about the importance of grouping data that is accessed together on the same node (data clumping) and how aggregate orientation can help achieve this.

- **Data Arrangement on Nodes**: Several factors can improve performance when arranging data on nodes, such as placing data close to where it's accessed and evenly distributing aggregates across nodes.

- **Sharding in Application Logic**: Historically, sharding has been done as part of application logic, which can complicate the programming model. However, many NoSQL databases now offer auto-sharding, which simplifies this process.

- **Performance and Resilience**: Sharding can improve both read and write performance, but it doesn't necessarily improve resilience. While it can limit the impact of a node failure to only the users of the data on that shard, it can also decrease resilience if used alone.

- **Sharding Implementation**: The text warns that implementing sharding is not a step to be taken lightly. It advises starting with a single-server configuration and only moving to sharding when load projections indicate it's necessary. It also emphasizes the importance of implementing sharding well before it's needed to avoid potential issues.

### 4.3. Primary-Secondary Replication

```mermaid
---
title: Data is replicated from Primary to Secondary. The Primary services all writes; reads may come from either Primary or Secondary.
---
graph TB
    subgraph "Database Cluster"
        subgraph node_1 ["Primary Node"]
            S1D1((♦️))
            S1D2((♣️))
            S1D3((♥️))
            S1D4((♠️))
        end
        subgraph node_2 ["Secondary Node"]
            S2D1((♦️))
            S2D2((♣️))
            S2D3((♥️))
            S2D4((♠️))
        end
        subgraph node_3 ["Secondary Node"]
            S3D1((♦️))
            S3D2((♣️))
            S3D3((♥️))
            S3D4((♠️))
        end
    end


    A1{"Application R/W\n♦️ ♣️ ♥️ ♠️"} <-- R/W --> node_1
    node_1 --> node_2
    node_1 --> node_3
    node_2 -- R --> A2{"Application R\n♦️ ♣️ ♥️ ♠️"}
    node_3 -- R --> A3{"Application R\n♦️ ♣️ ♥️ ♠️"}
```

- **Primary-Secondary Replication**: Data is replicated across multiple nodes. The primary node is the authoritative source for the data and handles updates, while secondary nodes are synchronized with the primary.

- **Scaling and Read-Intensive Datasets**: Primary-secondary replication is beneficial for scaling read-intensive datasets. By adding more secondary nodes and routing read requests to them, the system can handle more read requests. However, the system's ability to process updates and propagate them is still limited by the primary node's capacity.

- **Read Resilience and Failure Handling**: Another advantage of primary-secondary replication is read resilience. If the primary node fails, secondary nodes can still handle read requests. The system can quickly appoint a new primary from the secondary nodes, speeding up recovery after a failure.

- **Hot Backup and Resilience**: All read and write traffic can go to the primary while the secondary acts as a hot backup. This setup provides the convenience of a single-server configuration with greater resilience, especially useful for handling server failures gracefully.

- **Primary Node Appointment**: Primary nodes can be appointed manually or automatically. Automatic appointment allows the cluster to automatically appoint a new primary when the current one fails, reducing downtime.

- **Read and Write Paths**: To achieve read resilience, the application should have separate read and write paths. This setup allows the system to handle a failure in the write path while still being able to read.

- **Replication and Inconsistency**: Replication offers many benefits, but it also introduces the risk of inconsistency. Different clients reading from different secondary nodes might see different values if changes haven't propagated to all secondary nodes yet. This issue is discussed further in the section on "Consistency".

### 4.4. Peer-to-Peer Replication

```mermaid
---
title: Peer-to-peer replication has all nodes applying reads and writes to all the data.
---
graph TB
    subgraph "Database Cluster"
        subgraph node_1 ["Node 1"]
            S1D1((♦️))
            S1D2((♣️))
            S1D3((♥️))
            S1D4((♠️))
        end
        subgraph node_2 ["Node 2"]
            S2D1((♦️))
            S2D2((♣️))
            S2D3((♥️))
            S2D4((♠️))
        end
        subgraph node_3 ["Node 3"]
            S3D1((♦️))
            S3D2((♣️))
            S3D3((♥️))
            S3D4((♠️))
        end
    end


    A1{"Application R/W\n♦️ ♣️ ♥️ ♠️"} <-- R/W --> node_1
    A2{"Application R/W\n♦️ ♣️ ♥️ ♠️"} <-- R/W --> node_2
    A3{"Application R/W\n♦️ ♣️ ♥️ ♠️"} <-- R/W --> node_3
    node_1 <--> node_2
    node_1 <--> node_3
    node_2 <--> node_3
```

- **Primary-Secondary Replication Limitations**: The primary node is a potential bottleneck and a single point of failure.

- **Peer-to-Peer Replication**: All nodes are equal, can accept writes, and the loss of any node doesn't prevent data access.

- **Benefits and Complications**: Peer-to-peer replication offers benefits like resilience to node failures and improved performance with added nodes. However, it also introduces complications, primarily related to data consistency.

- **Write-Write Conflict**: The risk of write-write conflict arises when two different places can be written to simultaneously, leading to potential inconsistencies.

- **Handling Write Inconsistencies**: There are two broad options for handling write inconsistencies. One is to coordinate replicas during a write to avoid conflict, and the other is to cope with an inconsistent write and merge them based on a policy.

- **Consistency vs Availability Trade-off**: These points are at the ends of a spectrum where we trade off consistency for availability.

### 4.5. Combining Sharding and Replication

#### 4.5.1. Primary-Secondary Replication X Sharding

- **Multiple Primary Nodes with Unique Data Items**: The system has multiple primary nodes, but each data item is primarily controlled by a single node.

- **Node Configuration**: Nodes can be configured to serve as a primary for some data and secondary for others, or nodes can be dedicated solely to primary or secondary roles.

```mermaid
---
title: Using primary-secondary replication together with sharding
---
graph TB
    subgraph "Database Cluster"
        subgraph node_1 ["[ Primary - Shards: ♦️ ♣️ ]"]
            S1D1((♦️))
            S1D2((♣️))
        end
        subgraph node_2 ["[ Secondary - Shards: ♣️ ♠️ ]"]
            S2D1[♣️]
            S2D2[♠️]
        end
        subgraph node_3 ["[ Primary - Shards: ♠️ ]"]
            S3D1((♠️))
        end
        subgraph node_4 ["[ Primary - Shards: ♥️ ]\n[ Secondary - Shards: ♦️ ]"]
            S4D1((♥️))
            S4D2[♦️]
        end
        subgraph node_5 ["[ Secondary - Shards: ♣️ ♥️ ]"]
            S5D1[♣️]
            S5D2[♥️]
        end
        subgraph node_6 ["[ Secondary - Shards:  ♠️ ]"]
            S6D1[♠️]
        end

        node_1 -- ♣️ --> node_2
        node_1 -- ♦️ --> node_4
        node_1 -- ♣️ --> node_5
        node_3 -- ♠️ --> node_2
        node_3 -- ♠️ --> node_6
        node_4 -- ♥️ --> node_5
    end
```

#### 4.5.2. Peer-to-Peer Replication X Sharding

- **Cluster Configuration**: Considering a column-family databases setup, there could be tens or hundreds of nodes in a cluster with data sharded across them. 

- **Replication Factor**: A replication factor of 3 is suggested as a good starting point, meaning each shard is present on three nodes. 

- **Node Failure Handling**: If a node fails, the shards on that node will be rebuilt on the other nodes.

```mermaid
---
title: Using peer-to-peer replication together with sharding
---
graph TB
    subgraph "Database Cluster"
        subgraph node_1 ["[ Shards: ♦️ ♣️ ]"]
            S1D1((♦️))
            S1D2((♣️))
        end
        subgraph node_2 ["[ Shards: ♣️ ♠️ ]"]
            S2D1((♣️))
            S2D2((♠️))
        end
        subgraph node_3 ["[ Shards: ♠️ ]"]
            S3D1((♠️))
        end
        subgraph node_4 ["[ Shards: ♥️ ♦️ ]"]
            S4D1((♥️))
            S4D2((♦️))
        end
        subgraph node_5 ["[ Shards: ♣️ ♥️ ]"]
            S5D1((♣️))
            S5D2((♥️))
        end
        subgraph node_6 ["[ Shards:  ♠️ ]"]
            S6D1((♠️))
        end

        node_1 <-- ♣️ --> node_2
        node_1 <-- ♦️ --> node_4
        node_1 <-- ♣️ --> node_5
        node_2 <-- ♣️ --> node_5
        node_2 <-- ♠️ --> node_3
        node_2 <-- ♠️ --> node_6
        node_3 <-- ♠️ --> node_6
        node_4 <-- ♥️ --> node_5
    end
```

### 4.6. Key Points

- There are two styles of distributing data (a system may use either or both techniques):
  - Sharding distributes different data across multiple servers, so each server acts as the single source for a subset of data.
  - Replication copies data across multiple servers, so each bit of data can be found in multiple places.

- Replication comes in two forms:
  - Primary-secondary replication makes one node the authoritative copy that handles writes while secondaries synchronize with the primary and may handle reads.
  - Peer-to-peer replication allows writes to any node; the nodes coordinate to synchronize their copies of the data.

- Primary-secondary replication reduces the chance of update conflicts but peer-to-peer replication avoids loading all writes onto a single point of failure.
