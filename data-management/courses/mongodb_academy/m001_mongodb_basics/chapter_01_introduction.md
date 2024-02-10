# Introduction

## Table of contents

- [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [JSON](#json)
    - [Structure](#structure)
  - [MongoDB Structure](#mongodb-structure)
    - [Document](#document)
  - [Filtering and Searching](#filtering-and-searching)

## JSON

- Ref.: [JSON spec](https://www.json.org/json-en.html).
- MongoDB document representation.
- Support any type of hierarchy.

### Structure

- Key:
  - Access index.
  - Surround by double quotes.
  - Keys and values must be separated by colons.
  - Fields are separated from one another by commas.

- Value:
  - Supported types:
    - **null**: No-type representation.
    - **String**: Values surrounded by double quotes.
    - **Decimal number**: Float point and common numbers.
    - **Boolean**: `true` or `false`.
    - **Array**:
      - Values surrounded by square brackets.
      - Ordered comma separated list of values.
      - A single Array can receive values from different types.
    - **Objects**:
      - Values surrounded by brackets.
      - Pairs of key-values separated by comma (similar to the JSON structure itself).
- Example:

```json
{
    "string": "It's a string value",
    "number": 0,
    "float_number": 0.1,
    "boolean": true,
    "null": null,
    "array": [
        "It's a string value",
        0,
        0.1,
        true,
        null,
        {
            "type": "It's a object value",
        }
    ],
    "object": {
        "string": "It's a string value",
        "number": 0,
        "float_number": 0.1,
        "boolean": true,
        "null": null,
        "array": [
            "It's a array value"
        ]
    }
}
```

## MongoDB Structure

- Database serves as a namespace of collections.
- Collection stores individual records (Documents).
- Document is the basic MongoDB structure (similar to the Table concept to SQL DBs).
- Access control can be implemented in Database, Collection or Document levels.

![MongoDB Hierarchy](./images/database_collection_document_hierarchy.png)

### Document

- Schema statistically described.

- Simple data types:
  - int32.
  - double.
  - string.
  - date.

- Special data types:
  - document:
    - MongoDB permits multiple levels of nested documents.
    - MongoDB search by fields inside of any level of nested documents.
  - array:
    - Indexed values of multiple data types.
  - aggregated data structure:
    - Mix of data types that has a meaning for third-party programs.
    - Examples:
      - Geo-spatial Data.

## Filtering and Searching

- MongoDB uses JSON structure to filter or search documents in a collection.
  - Different operations are supported in json filter language.

```js
// Equal
{bikeid: 16500}

// Greater than | Less than
{bikeid: {$gt: 16500,$lt: 17000}}

// Greater than or equal | Less than or equal
{bikeid: {$gte: 16500,$lte: 17000}}
```
