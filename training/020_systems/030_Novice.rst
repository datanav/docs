
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  System authentication methods...

  - should ....

Looking at systems from an isolated point of view, these can differ quite a bit when it comes to authentication methods. The system of type microservice supports a wealth of different authentication methods whereas other systems such as for example the Oracle system uses a default authentication method consisting of the parameters: ``username``, ``password``, ``host``and ``database``.

The Oracle system is one of Sesam's many in-built systems. Sesam's in-built systems will typically have a default authentication method and also a more limited set of choices when it comes to choosing an authentication method for one of these systems. The authentication example with the Oracle system is a typical scenario when connecting to a relational database, albeit many more exist i.e: SQL, MsSQL, PostgreSQL.        

As such, you should be aware of the fact that different systems in Sesam will have different authentication methods that vary quite substantially.

Enten har du støtte for det, ellers kan du bygge det selv...

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

| Mention all built in system types, is there a common denominator?
| refer to appendix/documentation for more information

“Type”: “system_XXXX”

.. seealso::

  TODO

.. _tasks-for-systems-novice-2-2:

Tasks for Systems: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~
