.. _sink_section:

Sinks
=====

Sinks are at the receiving end of pipes and are responsible for
writing entities into an internal dataset or a target system.

Sinks can support batching by implementing specific methods and
accumulating entities in a buffer before writing the batch. The size of
each batch can be specified using the ``batch_size`` property on the
pipe. See the section on :ref:`batching <pipe_batching>` for more
information.

Prototype
---------

The following *JSON* snippet shows the general form of a sink definition.

::

    {
        "type": "a-sink-type",
        "comment": "This is a comment"
    }


The only universally required property is ``type``.

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

   * - ``type``
     - String
     - The type of the sink, the allowed types are described below
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the sink (optional).
     -
     -

Type of sinks
-------------
.. toctree::
   :maxdepth: 1

   Conditional sink <configuration-sinks-conditional>
   Dataset sink <configuration-sinks-dataset>
   JSON push sink <configuration-sinks-json>
   SDShare push sink <configuration-sinks-sdshare>
   SMS message sink <configuration-sinks-sms>
   Solr sink <configuration-sinks-solr>
   Elasticsearch sink <configuration-sinks-elasticsearch>
   SPARQL sink <configuration-sinks-sparql>
   SQL sink <configuration-sinks-sql>
   Email Message sink <configuration-sinks-email>
   Null sink <configuration-sinks-null>
   HTTP endpoint sink <configuration-sinks-http>
   CSV endpoint sink <configuration-sinks-csv>
   XML endpoint sink <configuration-sinks-xml>
   REST sink <configuration-sinks-rest>
