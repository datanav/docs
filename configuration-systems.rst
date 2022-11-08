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

.. code-block:: json

    {
        "_id": "a_system_id",
        "type": "system:some-type-of-system",
        "name": "The Foo System",
        "description": "This is a description of the system",
        "comment": "This is a comment",
        "worker_threads": 10,
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
     - A human readable name for this system.
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



.. toctree::
   :hidden:
   :maxdepth: 1

   SQL systems <configuration-systems-sql>
   Oracle system <configuration-systems-oracle>
   Oracle TNS system <configuration-systems-oracle-tns>
   Legacy Microsoft SQL Server system <configuration-systems-mssql-legacy>
   Microsoft SQL Server system <configuration-systems-mssql>
   MySQL system <configuration-systems-mysql>
   PostgreSQL system <configuration-systems-postgresql>
   LDAP system <configuration-systems-ldap>
   SMTP system <configuration-systems-smtp>
   Solr system <configuration-systems-solr>
   Elasticsearch system <configuration-systems-elasticsearch>
   Twilio system <configuration-systems-twilio>
   URL system <configuration-systems-url>
   REST system <configuration-systems-rest>
   Microservice system <configuration-systems-microservice>