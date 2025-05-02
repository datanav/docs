.. _system_section:

Systems
=======

A system component represents a computer system that can provide data entities. Its task is to provide common properties
and services that can be used by several data sources, such as connection pooling, authentication settings,
communication protocol settings and so on.

You can manage any secret property values you do not want to be exposed in the API (or in log files) by using the :ref:`Secrets manager API <secrets_manager>`.

Note: as with pipe components, you are not allowed to use the forward slash character ("``/``") in system id's.

All systems share a number of common properties:

Prototype
---------

.. code-block :: json

    {
        "_id": "a_system_id",
        "type": "system:some-type-of-system",
        "name": "The Foo System",
        "description": "This is a description of the system",
        "comment": "This is a comment",
        "worker_threads": 10,
        "permissions": [
           ["allow", ["group:Foo"], ["some_permission"]],
           ["deny", ["group:OtherGroup"], ["some_other_permission"]]
        ],
        "metadata": {
           "some_key": "some_value"
        }
    }

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``_id``
     - String
     - A unique ID identifying the system. Any pipe sink or source that uses the system must have a corresponding
       ``system`` property matching this value.
     -
     - Yes

   * - ``name``
     - String
     - A human readable name for this system
     -
     -

   * - ``description``
     - String or list of strings
     - A human readable description of the component (optional).
     -
     -

   * - ``comment``
     - String or list of strings
     - A human readable comment on the component (optional).
     -
     -

   * - ``metadata``
     - Object<string, Object>
     - A object providing metadata for the system. The keys are strings while the values can be any valid JSON object
       (literals, lists or other objects).
     -
     -

   * - ``worker_threads``
     - Integer
     - The maximum number of concurrent pipes running using this system
     - 10
     -

   * - ``permissions``
     - List of ACL elements
     - This property should contain a list of ACL definitions (itself a 3-element list (tuple) of
       "ALLOW"|"DENY",[list,of,groups,or,roles],[list,of,permissions]) that defines
       which permissions should be applied to the system when it's uploaded and instantiated. See the example
       configuration in the :ref:`pipe metadata <pipe_metadata>` section for how this should be formatted.
     -
     -

Type of systems
---------------

.. toctree::
   :maxdepth: 1

   Elasticsearch system <configuration-systems-elasticsearch>
   LDAP system <configuration-systems-ldap>
   Legacy Microsoft SQL Server system <configuration-systems-mssql-legacy>
   Microservice system <configuration-systems-microservice>
   Microsoft SQL Server system <configuration-systems-mssql>
   MySQL system <configuration-systems-mysql>
   Oracle system <configuration-systems-oracle>
   Oracle TNS system <configuration-systems-oracle-tns>
   PostgreSQL system <configuration-systems-postgresql>
   REST system <configuration-systems-rest>
   SMTP system <configuration-systems-smtp>
   SQL systems <configuration-systems-sql>
   Solr system <configuration-systems-solr>
   Twilio system <configuration-systems-twilio>
   URL system <configuration-systems-url>
