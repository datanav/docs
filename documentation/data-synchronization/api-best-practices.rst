.. api-best-practices:

API Best practices
==================

#. Continuation support:

	#. Support for querying only the changes since last request. 

	#. Expose last modified timestamp of the data, this timestamp needs to be reliable.

#. Support for deletion tracking:

	#. Return entities that are deleted from the source, marked with a specific attribute that the entity is deleted.

#. Supported data types should be as similar to the underlying data model as possible.

#. Avoid complex entities when possible.

#. Idempotent endpoints:

	#. A call to the API should yield the same result, no matter how many times the same call is applied.

#. A stable API:

	#. Backward compatible API, don’t remove old methods.

	#. Notify consumers of changes to the API.

#. Standardized authentication mechanism, preferably Oauth 2.0. 