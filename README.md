### Koffie Labs Backend Coding Challenge - Submission

#### Objective

Implement a simple [FastAPI](https://fastapi.tiangolo.com) backend to decode VINs, powered by the [vPIC API](https://vpic.nhtsa.dot.gov/api/) and backed by a [SQLite](https://www.sqlite.org/index.html) cache.

#### Routes

`/lookup`

This route receives an input VIN and performs the following steps:
- Validate input VIN as 17 alphanumeric characters.
- Attempt to return the VIN and additional properties if the VIN is available in the in-memory cache.
- Attempt to return the VIN and additional properites using the vPIC API. Cache the VIN in memory for future lookups.
- Return a 404 error for an invalid VIN.

Invalid VIN's are also cached in-memory with an attribute indicating they are invalid so that repeated lookups of the same invalid VIN do not repeatedly hit the vPIC API.

`/remove`

This route receives an input VIn and performs the following steps:
- Validate input VIN as 17 alphanumeric characters.
- Check if the VIN is present in the in-memory cache.
- Remove the VIN from the in-memory cache if present.
- Return a response indicating whether the VIN was succesfully removed.

`/export`

This route exports the in-memory cache as a Parquet file which the client downloads.

#### Local Usage
- `cd` to the top-level `app` directory.
- Start the server with `uvicorn app.main:app`
- Access the API locally from `localhost:8000/api/v1/`
- Access the OpenAPI docs from `localhost:8000/docs`
