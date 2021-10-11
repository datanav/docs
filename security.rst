.. _security:

========
Security
========

.. contents:: Table of Contents
   :depth: 2
   :local:


------------
Introduction
------------

There are two different security domains in Sesam.

1. The most visible one is the security-features that deal with
:ref:`users, roles and permissions<security_subscriptions_users_roles_and_permissions>` in Sesam.
These control which persons are allowed to do what. This is very similar to how the
permissions-settings on most file-systems work.

2. In addition to the user-centric security-features, we also have the concept of
:ref:`secrets<secrets_manager>` in Sesam. Secrets are used for things like database passwords.

These two domains are explained in more detail below.


.. _security_subscriptions_users_roles_and_permissions:

-------------------------------------------
Subscriptions, Users, Roles and Permissions
-------------------------------------------

The ability to perform actions in the Sesam Portal is controlled by assigning Roles to Users.
The Roles is assigned in the scope of a specific Subscription, so a User can have different Roles
in different Subscriptions.

The ability to perform actions in the Sesam node is controlled by assigning Permissions to Roles.
This is assigned in the various "Permissions" pages in the GUI.

When a user tries to perform an action on a Sesam node, they must first log in via the Sesam Portal.
The Portal will generate a JSON Web Token for the user; this is a datastructure that identifies the user
and that contains a list of all the roles of the user.

Inside the node, each pipe, system and dataset can be protected by assigning permissions to roles. The
permissions of each user is then determined by iterating over the user's roles and checking the
permissions granted to each role.

We will explain how the permissions checks is done via an example. Lets assume that a person wants to
look at the contents of the dataset "dataset1"
in the subscription "subA":

  1. A person logs in to the Sesam Portal.
  2. The Sesam Portal backend checks that the email and password matches an existing User.
  3. The Sesam Portal backend examines the Roles the User has been assigned and sends the back a list of the 
     Subscriptions that the User has a Role in.
  4. The person selects the Subscription "subA" in the GUI
  5. The GUI requests a JWT (Json Web Token) for the "subA".
  6. The Sesam Portal backend creates a JWT that contains the User's Roles in "subA" and signs the JWT
     with the Sesam Portals private encryption key.
  7. The GUI now connects to the Sesam node that is associated with "subA" with the JWT in the
     "Authorization" http request header.
  8. The Sesam node verifies that the JWT is valid by using the Sesam Portal's public encryption key to
     check that the signature on the JWT is ok. The Sesam node now knows which Roles the User has.
  9. The person selects the "dataset1" dataset in the GUI. The GUI sends a request to the
     Sesam node asking for the content of the dataset.
  10. The Sesam node loads the ACL (Access Control List) that has been defined for the dataset. The
      node looks through the ACL to figure out if the current User has been granted the "Read data"
      permission.
  11. If the current User has the required permission, the Sesam node return the contents of the dataset
      in the http response. If not, the Sesam node sends a "403 Forbidden" http response instead.


Sesam node runtime
~~~~~~~~~~~~~~~~~~
When a user creates a pipe, the pipe inherits the roles of that user. The list of roles is
stored as part of the pipe-config. At runtime, a permission-check is made to check if the pipe is
allowed to do what it is attempting to do. This includes checking if the pipe is allowed to read
from its source system, and to write to its target system.

If the permission checks fail, the pipe-run will fail and an error will be displayed on the pipe's
page in the GUI.


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

You can upload your secrets using the command line client (or via the web API using a HTTP client such as ``curl`` or ``wget``).

You can either specify that the secrets should only be visible for one specific System by specifying the id of the System:

::

  sesam put-secrets my_system_id my-system-secrets.json

, or you can make the secrets "global" and available for all systems:

::

  sesam put-secrets my-secrets.json


You can also list which secrets the Sesam secret manager is currently aware of:

::

  sesam get-secrets my_system_id

  ["system-secret-property", "another-system-secret-property"]

::

  sesam get-secrets

  ["secret-property", "another-secret-property"]

The values of the secrets are stored internally in a strongly encrypted form using a key that is unique to each instance
of Sesam. Note that once uploaded to the Secrets manager, you cannot extract the original value(s) of the secret(s) so
you must store them in a secure fashion off-site.


The lifetime of secrets
~~~~~~~~~~~~~~~~~~~~~~~

Global secrets lives until they are explicitly deleted.

System secrets lives until they are explicitly deleted, or until the System is removed. So, if you delete and re-add
a System, you have to upload all the System-local secrets again.


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
