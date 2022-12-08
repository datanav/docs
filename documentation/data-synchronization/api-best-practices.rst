.. api-best-practices:

API Best practices
==================

- Continuation support:

  - Support for querying only the changes since last request. 

  - Expose last modified timestamp of the data, this timestamp needs to be reliable.

- If API cannot provide continuation support, provide support for querying or searching, or support for webhooks or other means of signalling.

- Support for deletion tracking:

  - Soft deletes, return entities that are deleted from the source, marked with a specific attribute that the entity is deleted.

- Supported entity types should be as similar as possible to the entity types in the underlying data model.

- Idempotent endpoints:

  - A call to the API should yield the same result, no matter how many times the same call is applied.

- A stable API:

  - Backward compatible API, don’t remove old methods.

  - Notify consumers of changes to the API.

- Standardized authentication mechanism, preferably Oauth 2.0. 