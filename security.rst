========
Security
========

.. contents:: Table of Contents
   :depth: 2
   :local:


------------
Introduction
------------

TODO

.. _secrets_manager:

-------------------
The secrets manager
-------------------

Managing secrets
~~~~~~~~~~~~~~~~

System configuration properties that contain secrets are managed by the Sesam Secrets manager API. See the
:ref:`API reference <api-reference>` for its documentation.

You can use this API to upload or delete secrets to be used in :ref:`system components configuration <system_section>`.
The secrets should be in a JSON document as either a list of objects or a single object:

::

  {
    "secret-property": "secret-value",
    "another-secret-property": "another-secret-value"
  }

You can upload your secrets using the command line client (or via the web API using a HTTP client such as ``curl`` or ``wget``):

::

  sesam put-secrets my-secrets.json

You can also list which secrets the Sesam secret manager is currently aware of:

::

  sesam get-secrets

  ["secret-property", "another-secret-property"]

The values of the secrets are stored internally in a strongly encrypted form using a key that is unique to each instance
of Sesam. Note that once uploaded to the Secrets manager, you cannot extract the original value(s) of the secret(s) so
you must store them in a secure fashion off-site.

Using secrets
~~~~~~~~~~~~~

Once you have uploaded your secrets to the Secrets manager, you can start using them in your :ref:`system configuration <system_section>`
by substituting the configuration property value(s) using a special syntax.

An example: given a existing system configuration:

::

   {
     "_id": "my-system",
     "type": "oracle",
     "host": "my-db-server",
     "username": "my-user",
     "password": "my-password",
     "..": ".."
   }

Extract the secret properties into a separate JSON document, and give them names you can remember:

::

  {
      "my-system-host": "my-db-server",
      "my-system-username": "my-user",
      "my-system-password": "my-password"
  }

Save the JSON document to a .json file and store it securely off site. Then upload it to the Secret manager using the
sesam api. You can then substitute the original secret values in the system configuration with the substitution keys
using the "$SECRET(key)" syntax:

::

   {
     "_id": "my-system",
     "type": "oracle",
     "host": "$SECRET(my-system-host)",
     "username": "$SECRET(my-system-username)",
     "password": "$SECRET(my-system-password)",
     "..": ".."
   }

The substituted secret values are only used as-needed during run time, and their values will never be exposed in
the API (or log files).

You can also compose a property that consists of several secrets:

::

   {
     "_id": "my-system",
     "type": "url",
     "base_url": "http://$SECRET(my-system-username):$SECRET(my-system-password)@example.com",
     "..": ".."
   }

Note that when using properties that contain multiple secrets, you cannot nest secret values inside each other, and the
resulting property will always be a string. Secrets can be combined with environment variables, but they cannot be nested.
See the chapter on :ref:`configuration environment variables <environment_variables>` for details.

Secrets applies only to System configuration entities.
