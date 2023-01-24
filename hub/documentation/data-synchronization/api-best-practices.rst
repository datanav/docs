.. _api-best-practices:

API Best practices
==================

- Continuation support:

  - Support for querying only the changes since last request. 

  - Expose last modified timestamp of the data, this timestamp needs to be reliable.

- If your API cannot provide continuation support then either provide support for querying or searching. Alternatively provide support for webhooks or other means of signalling.

- Support for deletion tracking:

  - Soft deletes, return entities that are deleted from the source, marked with a specific attribute that the entity is deleted.

- Supported entity types should be as similar as possible to the entity types in the underlying data model.

- Idempotent endpoints:

  - A call to the API should yield the same result, no matter how many times the same call is applied.

- A stable API:

  - Backward compatible API, don't remove old methods.

  - Notify consumers of changes to the API.

- Standardized authentication mechanism

  - for ease of use and security, the OAuth 2.0 protocol using `Authorization Code flow <https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow>`_ is most preferred (note: because our application needs to securely talk to the system on behalf of the user in the background, the `OAuth 2.0 Implicit flow <https://oauth.net/2/grant-types/implicit/>`_ is not supported)
  - to serve as an authentication provider for Sesam Talk (enable "Login via" your system), supporting OAuth 2.0 Authorization Code flow is a requirement
  - a simpler api key/token can also be used for systems that don't need to serve as an authentication provider