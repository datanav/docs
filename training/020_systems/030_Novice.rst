
.. _systems-novice-2-2:

Novice
------

.. _systems-as-a-pipe-source-2-2:

Systems as a pipe source
~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Systems as a pipe source...

  - should provide streams of entities as input to the pipes they are connected to
  - can provide entities with **any** shape
  - must provide Sesam with a unique identifier called ``_id``

Using a system as a pipe source defines the possibilities this pipe has when
pulling data. Sesam supports implementing multiple different `system types <https://docs.sesam.io/configuration.html#systems>`_, i.e: JSON, SQL, microservice etc. Each system, regardless of type, will have a defined set of implementation functionalities which can be set in its DTL configuration. As such, the intended usage in Sesam should be taken into consideration when implementing a System.

When a system is used as a pipe source, certain aspects come into consideration. Namely, that a `source <https://docs.sesam.io/configuration.html#sources>`_ should provide streams of entities as input to the pipes it is connected to. The entities that are provided can take any shape, i.e: they can have nested dictionaries. The only required property for entities within Sesam is the ``_id`` which is used as a unique identifier.    

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`source_section`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

.. _systems-as-a-pipe-sink-2-2:

Systems as a pipe sink
~~~~~~~~~~~~~~~~~~~~~~

Same as above only with system as a sink. What is a system in the
context of a sink? What does the pipe see? What does the system see?
(1-N)

.. seealso::

  TODO

.. _authentication-methods-2-2:

System Authentication methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Default authentication methods built in for systems handling URLS
  $SECRET()
| Basic, Oauth2, JWT, microservices

| Authentication methods for specific systems: ?? worth mentioning
| SQL, oracle

.. seealso::

  TODO

.. _system-types-2-2:

System Types
~~~~~~~~~~~~

.. sidebar:: Summary

  System types...

  - in Sesam vary quite substantially
  - have a set of supported functionality
  - vary in origin, but when implemented in Sesam all system types are represented as JSON

Extending on systems, the types of systems Sesam provide vary quite substantially. In order for you to work efficiently in a given Sesam node, you should familiarize yourself with these different system types as they will have varying functional possibilites. A comprehensive list is provided below to make sure you know which system types exist:

- `The SQL systems <https://docs.sesam.io/configuration.html#the-sql-systems>`_
- `The Oracle system <https://docs.sesam.io/configuration.html#the-oracle-system>`_
- `The Oracle TNS system <https://docs.sesam.io/configuration.html#the-oracle-tns-system>`_
- `The MSSQL system <https://docs.sesam.io/configuration.html#the-mssql-system>`_
- `The Microsoft Azure SQL Data Warehouse system <https://docs.sesam.io/configuration.html#the-microsoft-azure-sql-data-warehouse-system>`_
- `The MySQL system <https://docs.sesam.io/configuration.html#bulk-operations-in-microsoft-sql-server-and-azure-sql-data-warehouse-systems>`_
- `The PostgreSQL system <https://docs.sesam.io/configuration.html#the-postgresql-system>`_
- `The LDAP system <https://docs.sesam.io/configuration.html#the-ldap-system>`_
- `The SMTP system <https://docs.sesam.io/configuration.html#the-smtp-system>`_
- `The Solr system <https://docs.sesam.io/configuration.html#the-solr-system>`_
- `The Elasticsearch system <https://docs.sesam.io/configuration.html#the-elasticsearch-system>`_
- `The Twilio system <https://docs.sesam.io/configuration.html#the-twilio-system>`_
- `The URL system <https://docs.sesam.io/configuration.html#the-url-system>`_
- `The REST system <https://docs.sesam.io/configuration.html#the-rest-system>`_
- `The Mircoservice system <https://docs.sesam.io/configuration.html#the-microservice-system>`_  

Regardless of system type in Sesam its configuration will always be JSON. Important to consider in this aspect is that JSON is schemaless, which results in self-contained systems and makes for easier implementation in Sesam.  

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

.. _tasks-for-systems-novice-2-2:

Tasks for Systems: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~
