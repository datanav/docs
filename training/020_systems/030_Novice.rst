
.. _systems-novice-2-2:

Novice
------

.. _systems-as-a-pipe-source-2-2:

Systems as a pipe source
~~~~~~~~~~~~~~~~~~~~~~~~

System configuration (mostly) defines the possibilities pipes have to
pull data.

We need to write about what a system is in the context of a pipe source,
with not only configs but explanations. Keep it simple don’t go into too
many system types (json & SQL?). Write more text than configurations,
draw stuff. (1-N)

.. seealso::

  TODO

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

| Mention all built in system types, is there a common denominator?
| refer to appendix/documentation for more information

“Type”: “system_XXXX”

.. seealso::

  TODO

.. _tasks-for-systems-novice-2-2:

Tasks for Systems: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~
