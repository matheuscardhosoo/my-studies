# Deeper Dive into the MongoDB Query Language

## Table of contents

- [Deeper Dive into the MongoDB Query Language](#deeper-dive-into-the-mongodb-query-language)
  - [Table of contents](#table-of-contents)
  - [Query operators](#query-operators)
    - [Query Selectors](#query-selectors)
      - [Comparison](#comparison)
      - [Logical](#logical)
      - [Element](#element)
      - [Evaluation](#evaluation)
      - [Geo-spatial](#geo-spatial)
      - [Array](#array)
      - [Bitwise](#bitwise)
      - [Comments](#comments)
    - [Projection Operators](#projection-operators)

## Query operators

- [Query and Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/).
- Applied to all CRUD operations.

### Query Selectors

#### Comparison

- `"$eq"`: Matches values that are equal to a specified value.
- `"$gt"`: Matches values that are greater than a specified value.
- `"$gte"`: Matches values that are greater than or equal to a specified value.
- `"$in"`: Matches any of the values specified in an array.
- `"$lt"`: Matches values that are less than a specified value.
- `"$lte"`: Matches values that are less than or equal to a specified value.
- `"$ne"`: Matches all values that are not equal to a specified value.
- `"$nin"`: Matches none of the values specified in an array.

```js
db.movieDetails.find(
  {
    "runtime": {
      "$gt": 90,
      "$lt": 120
    },
    "tomato.meter": {
      "$gte": 95,
      "$lte": 100
    },
    "rated": {
      "$ne": "UNRATED"
    },
    "rated": {
      "$in": [
        "G",
        "PG"
      ]
    }
  },
  {
    "_id": 0,
    "title": 1,
    "runtime": 1
  }
);
```

#### Logical

- `"$and"`: Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.
- `"$not"`: Inverts the effect of a query expression and returns documents that do not match the query expression.
- `"$nor"`: Joins query clauses with a logical NOR returns all documents that fail to match both clauses.
- `"$or"`: Joins query clauses with a logical OR returns all documents that match the conditions of either clause.

```js
db.movieDetails.find(
  {
    "$or": [
      {
        "tomato.meter": {
          "$gt": 95
        }
      },
      {
        "metacritic": {
          "$gt": 88
        }
      }
    ],
    "$and": [
      {
        "metacritic": {
          "$ne": null
        }
      },
      {
        "metacritc": {
          "$exists": true
        }
      }
    ]
  }
);
```

```js
db.movieDetails.find(
  {
    "$or": [
      {
        "cast": "Jack Nicholson"
      },
      {
        "cast": "John Huston"
      }
    ],
    "viewerRating": {
      "$gt": 7
    },
    "mpaaRating": "R"
  }
);
```

#### Element

- `"$exists"`: Matches documents that have the specified field.
- `"$type"`: Selects documents if a field is of the specified type.

```js
db.movieDetails.find(
  {
    "tomato.consensus": {
      "$exists": false
    },
    "tomato.consensus": {
      "$ne": null
    },
    "genres": {
      "$type": "array"
    }
  }
);
```

#### Evaluation

- `"$expr"`: Allows use of aggregation expressions within the query language.
- `"$jsonSchema"`: Validate documents against the given JSON Schema.
- `"$mod"`: Performs a modulo operation on the value of a field and selects documents with a specified result.
- `"$regex"`: Selects documents where values match a specified regular expression.
- `"$text"`: Performs text search.
- `"$where"`: Matches documents that satisfy a JavaScript expression.

  ```js
  db.movieDetails.find(
    {
      "awards.text": {
        "$regex": /^Won.*/
      }
    }
  );
  ```

#### Geo-spatial

- `"$geoIntersects"`: Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports $geoIntersects.
- `"$geoWithin"`: Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support `"$geoWithin"`.
- `"$near"`: Returns geospatial objects in proximity to a point. Requires a geospatial index. The 2dsphere and 2d indexes support `"$near"`.
- `"$nearSphere"`: Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index. The 2dsphere and 2d indexes support `"$nearSphere"`.

#### Array

- `"$all"`: Matches arrays that contain all elements specified in the query.
  - It does not consider the order.
  - Ignore extra values in analyzed array.

  ```js
  db.movieDetails.find(
    {
      "genres": {
        "$all": [
          "Comedy",
          "Crime",
          "Drama"
        ]
      }
    }
  );
  ```

- `"$elemMatch"`: Selects documents if element in the array field matches all the specified `"$elemMatch"` conditions.
  - Applies the conditions for each element array.

  ```js
  db.movieDetails.find(
    {
      "boxOffice": {
        "$elemMatch": {
          "country": "Germany",
          "revenue": {
            "$gt": 16
          }
        }
      }
    }
  );
  ```

  ```js
  db.scores.find(
    {
      "results": {
        "$elemMatch":{
          "$gte": 70,
          "$lt": 80
        }
      }
    }
  );
  ```

- `"$size"`: Selects documents if the array field is a specified size.

  ```js
  db.movieDetails.find(
    {
      "genres": {
        "$size": 1
      }
    }
  );
  ```

#### Bitwise

- `"$bitsAllClear"`: Matches numeric or binary values in which a set of bit positions all have a value of 0.
- `"$bitsAllSet"`: Matches numeric or binary values in which a set of bit positions all have a value of 1.
- `"$bitsAnyClear"`: Matches numeric or binary values in which any bit from a set of bit positions has a value of 0.
- `"$bitsAnySet"`: Matches numeric or binary values in which any bit from a set of bit positions has a value of 1.

#### Comments

- `"$comment"`: Adds a comment to a query predicate.

### Projection Operators

- `"$"`: Projects the first element in an array that matches the query condition.
- `"$elemMatch"`: Projects the first element in an array that matches the specified $elemMatch condition.
- `"$meta"`: Projects the document’s score assigned during $text operation.
- `"$slice"`: Limits the number of elements projected from an array. Supports skip and limit slices.
