# Query Language

## Table of contents

- [Query Language](#query-language)
  - [Table of contents](#table-of-contents)
  - [Introduction to CRUD](#introduction-to-crud)
    - [Create](#create)
      - [Insert One](#insert-one)
      - [Insert Many](#insert-many)
    - [Read](#read)
      - [Basic Equality](#basic-equality)
      - [Array Perfect Match](#array-perfect-match)
      - [Array Single Match](#array-single-match)
      - [Array Specified Position Match](#array-specified-position-match)
    - [Update](#update)
      - [Common update methods](#common-update-methods)
      - [Array update methods](#array-update-methods)
      - [Update One](#update-one)
      - [Update Many](#update-many)
      - [Replace One](#replace-one)
    - [Delete](#delete)
      - [Delete One](#delete-one)
      - [Delete Many](#delete-many)

## Introduction to CRUD

### Create

- Write operations.

#### Insert One

- Create a single document based on the input object.

```js
db.movieSchatch.insertOne(
  {
    _id: "tt0084726",
    title:"Start Trek II: The Wrath of Khan",
    year: 1982,
    type: "movie"
  }
);
```

#### Insert Many

- Create multiple documents based on the input list.
- Can be ordered or unordered inserts.
- Ordered inserts consider the input list sequence.
  - Errors break the execution pipeline and don't add any document after the broken one.
- Unordered inserts documents independently.
  - Errors block only broken document.

```js
db.movieSchatch.insertMany(
  [
    {
      _id : "tt0084726",
      title : "Star Trek II: The Wrath of Khan",
      year : 1982,
      type : "movie"
    },
    {
      _id : "tt0796366",
      title : "Star Trek",
      year : 2009,
      type : "movie"
    },
    {
      _id : "tt0084726",
      title : "Star Trek II: The Wrath of Khan",
      year : 1982,
      type : "movie"
    },
    {
      _id : "tt1408101",
      title : "Star Trek Into Darkness",
      year : 2013,
      type : "movie"
    },
    {
      _id : "tt0117731",
      title : "Star Trek: First Contact",
      year : 1996,
      type : "movie"
    }
  ],
  {
    ordered: false
  }
);
```

### Read

- Read operation.
- Batch of results are separated on sets that can be iterated using cursors (using `getMore()` command).
- By default, MongDB returns all document fields.
- `Projections` specifies the field that should be returned.
  - By default, `Projections` always return _id field.
  - _id needs to be explicitly exclude.
- Nested objects can be accessed using "." (dot) expression.

```js
db.movieDetails.find(
  {
    rated: "PG",
    "awards.nominations": 10
  },
  {
    _id: 0,
    title: 1
  }
);
```

#### Basic Equality

```js
db.movieDetails.find(
  {
    rated: "PG",
    "awards.nominations": 10
  }
);
```

#### Array Perfect Match

```js
db.movies.find(
  {
    cast: [
      "Jeff Bridges",
      "Tim Robbins"
    ]
  }
);
```

#### Array Single Match

```js
db.movies.find(
  {
    cast: "Jeff Bridges"
  }
);
```

#### Array Specified Position Match

```js
db.movies.find(
  {
    "cast.0": "Jeff Bridges"
  }
);
```

### Update

- Write operation.

#### Common update methods

- `$inc`: increments the specified field by the specified value.
- `$mul`: multiplies  the specified field by the specified value.
- `$rename`: renames the specified field.
- `$setOnInsert`: sets the value if the update results in insert.
- `$set`: completely update or set the specified attribute.
- `$unset`: completely remove the specified attribute.
- `$min`: only updates if the input is greater than the current value.
- `$max`: only updates if the input is less than the current value.

#### Array update methods

- `$addToSet`: Adds elements to array if it does not exist.
- `$pop`: Pop first/last array item.
- `$pullAll`: Remove all matching values from array.
- `$pull`: Remove all matching values from array.
- `$pushAll`: Adds several items to array.
- `$push`: Adds a item to array.
- `$upsert`: Create a document if it does not exist.


#### Update One

```js
db.movieDetails.updateOne(
  {
    title: "The Martian"
  },
  {
    $set: {
      poster: "Poster"
    }
  },
  {
    upert: true
  }
);
```

#### Update Many

```js
db.movieDetails.updateMany(
  {
    rated: null
  },
  {
    $unset: {
      rated: ""
    }
  }
);
```

#### Replace One

- Completely replace a document based on a filter.

```js
db.movieDetails.replaceOne(
  {
    rated: null
  },
  {},
)
```

### Delete

- Write operation.

#### Delete One

```js
db.movieDetails.deleteOne(
  {
    title: "The Martian"
  }
);
```

#### Delete Many

```js
db.movieDetails.deleteMany(
  {
    rated: null
  }
);
```
