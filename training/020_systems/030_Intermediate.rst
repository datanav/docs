
.. _systems-intermediate-2-2:

Intermediate
------------

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

.. sidebar:: Summary

  Systems as a pipe sink...

  - are responsible for writing entities to a target system
  - should consider batching and the size of each batch

As data is moving in the outbound stage of its dataflow, Sesam use sinks to expose data. Sinks are the receiving end of pipes and are responsible for writing entities to a target system.

Pipes support `batching <https://docs.sesam.io/configuration.html#pipe-batching>`_ if the sink supports batching. It does this by accumulating source entities in a buffer before writing these to transforms and the sink. The size of each batch can be specified by using the ``batch_size`` property in your pipe. The default batch size is usually 100, but this will vary depending on the source- and sink-type. As an example, the `REST sink <https://docs.sesam.io/configuration.html#rest-sink>`_ will for instance use a ``batch_size`` of one as a default value.

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`sink_section`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`pipe_section` > :ref:`pipe_batching`

.. _authentication-methods-2-2:

System Authentication methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  System authentication methods...

  - are defined for each system type
  - vary depending on your system
  - can be extended upon

    - by building and deploying a microservice system in `Docker <https://www.docker.com/>`_

Looking at systems from an isolated point of view, these can differ quite a bit when it comes to authentication methods. This is also true when you look at them within a Sesam node. Generally speaking, Sesam supports a wide range of in-built systems and their authentication methods, albeit if you need to use a system in Sesam which is not readily available, you can build it yourself as a microservice. This flexibility within Sesam is quite unique and as such ~no limitation exist.

As an example of an in-built system in Sesam, the `Oracle system <https://docs.sesam.io/configuration.html#the-oracle-system>`_´s authentication method requires providing the parameters: ``username``, ``password``, ``host`` and ``database`` in order to authenticate. This example is a typical scenario when connecting to a relational database management system (RDBMS), albeit many more exist such as SQL, MsSQL, PostgreSQL, SMTP, REST etc..

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

  :ref:`sesam-community`

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
- `The Legacy Microsoft SQL system <https://docs.sesam.io/configuration.html#legacy-microsoft-sql-system>`_
- `The Microsoft SQL Server system <https://docs.sesam.io/configuration.html#microsoft-sql-server-system>`_
- `The MySQL system <hhttps://docs.sesam.io/configuration.html#mysql-system>`_
- `The PostgreSQL system <https://docs.sesam.io/configuration.html#the-postgresql-system>`_
- `The LDAP system <https://docs.sesam.io/configuration.html#the-ldap-system>`_
- `The SMTP system <https://docs.sesam.io/configuration.html#the-smtp-system>`_
- `The Solr system <https://docs.sesam.io/configuration.html#the-solr-system>`_
- `The Elasticsearch system <https://docs.sesam.io/configuration.html#the-elasticsearch-system>`_
- `The Twilio system <https://docs.sesam.io/configuration.html#the-twilio-system>`_
- `The URL system <https://docs.sesam.io/configuration.html#the-url-system>`_
- `The REST system <https://docs.sesam.io/configuration.html#the-rest-system>`_
- `The Mircoservice system <https://docs.sesam.io/configuration.html#the-microservice-system>`_

Regardless of system type in Sesam its configuration will always be JSON. Important to consider in this aspect is that JSON is schemaless, which results in self-contained systems and makes for easier implementation in Sesam. All systems share a number of common properties, which are shown below:

.. code-block:: json
  :caption: Common System Properties

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

- ``_id`` a unique ID for your system (required)
- ``name`` a human readable name for your system
- ``description`` a description of the system
- ``comment`` a comment about the system
- ``metadata`` a set of keys and values adding metadata content to the system
- ``worker_threads`` an integer value setting the number of maximum concurrent running pipes using this system (default is 10)

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

.. _tasks-for-systems-intermediate-2-2:

Tasks for Systems: Intermediate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. *What does a system as a pipe source provide?*

#. *What should you consider when using systems as a pipe sink?*

#. *Does Sesam support different authentication methods?*

#. *Why should you familiarize yourself with system types in Sesam?*

#. *Pick a system type:*

      Make your system run in Sesam

      Use your system both as a pipe source and a pipe sink
