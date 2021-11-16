
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

| Mention all built in system types, is there a common denominator?
| refer to appendix/documentation for more information

“Type”: “system_XXXX”

.. seealso::

  TODO

.. _tasks-for-systems-novice-2-2:

Tasks for Systems: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~
