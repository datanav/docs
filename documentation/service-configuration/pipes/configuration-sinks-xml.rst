
.. _xml_endpoint_sink:

XML endpoint sink
-----------------

This is a data sink that registers an HTTP publisher endpoint
that one can get the entities in XML format from.

A pipe that references the ``XML endpoint`` sink will not pump any
entities; the only way for entities to flow through the pipe is by retrieving them from the endpoint using the HTTP protocol.

It exposes the URL:

.. list-table::
   :header-rows: 1
   :widths: 100

   * - URL

   * - ``http://localhost:9042/api/publishers/mypipe/xml``
   * - ``http://localhost:9042/api/publishers/mypipe/xml/some_filename.xml``

Note that the shape of the entities must conform to certain criteria, see the :ref:`notes <expected_xml_entity_shape>`
later in the section.

The exposed URL may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-xml>`_ for the full details.

Note that you can optionally specify the filename to use in the ``Content-Disposition`` header of the HTTP response as
the last path element of the URL.

Prototype
^^^^^^^^^

::

    {
        "type": "xml_endpoint",
        "wrapper": "wrapper-tag",
        "root-attributes": {
           "xmlns": "http://www.example.org/ns1",
           "xmlsn:foo": "http://www.example.org/ns2",
           "xmlns:bar": "http://www.example.org/ns3"
        },
        "include-xml-decl": false,
        "skip-deleted-entities": true,
        "filename": "my_data.xml"
        "content_disposition": "attachment"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``wrapper``
     - String
     - If included, the XML produced from all entities will wrapped in a single top level tag with the value
       of this property (``<wrapper-value>..entity-tags..</wrapper-value>``)
     -
     -

   * - ``root-attributes``
     - Object
     - An object containing the attributes to include on the root element (i.e. on the ``wrapper`` tag if it is defined,
       or on the tag defined on the first entity level). This is where you typically declare your namespaces, schema
       and so on.
     -
     -

   * - ``include-xml-decl``
     - Boolean
     - If set to ``true`` includes a default XML header: ``<?xml version="1.0" encoding="UTF-8" standalone="yes"?>``
     - false
     -

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the XML output. The default is that
       deleted entities does not appear.
     - true
     -

   * - ``byte_order_mark``
     - Boolean
     - If ``true`` the sink will emit a UTF-8 byte order mark (BOM) to the start of the file/stream. I should only be
       used in conjunction with a UTF-8 encoding.
     - ``false``
     -

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``attachment``
     -


.. _expected_xml_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^
The entities must be transformed into a particular form before being piped to the XML endpoint sink. The general form
expected is:

::

  {
    "_id": "1",
    "name": "Entity 1",
    "id": "entity-1",
    "<foo:tag>": [{
        "id": "child",
        "name": "Child entity",
        "<section>": [
          {"<from>": "0"},
          {"<to>": "999"}
        ]
    }]
  }

There must be exactly one property starting with '<' and ending with '>' in an entity, although it can contain
child entities in as many levels as you want (also in lists).

All non-tag properties, except those beginning with a ``_`` letter will be included as attribute values on the tag
specified. A "tag"-property value can either be a single literal, a single object or a list of objects. Note that
any non-object items in lists are ignored (i.e. lists, literals and null values).

The property names must be valid XML attribute or tag names (`QNames <https://en.wikipedia.org/wiki/QName>`_).
All literal values in tags or attributes will be `XML escaped <https://www.liquid-technologies.com/XML/EscapingData.aspx>`_.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities`` publisher endpoint and read the entities from the ``my-entities``
dataset:

::

  {
     "sink": {
         "type": "xml_endpoint",
         "wrapper": "baz",
         "root-attributes": {
            "xmlns": "http://www.example.org/ns1",
            "xmlsn:foo": "http://www.example.org/foo",
            "xmlns:xsi": "http://www.w3.org/2000/10/XMLSchema-instance",
            "xsi:schemaLocation": "http://example.com/myschema.dtd",
            "zoo": "bar"
         },
         "filename": "example.xml"
     }
  }

The following output will be produced (here reformatted/pretty-printed):

::

    <baz xmlns="http://www.example.org/ns1"
         xmlns:foo="http://www.example.org/foo"
         xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance"
         xsi:schemaLocation="http://example.com/myschema.dtd"
         zoo="bar">
      <foo:tag name="Entity 1"
               id="entity-1">
         <section id="child"
                  name="Child entity">
            <from>0</from>
            <to>999</to>
         </section>
      </foo:tag>
    </baz>

The XML document will be available at ``http://localhost:9042/api/publishers/my-entities/xml``  (or alternatively
``http://localhost:9042/api/publishers/my-entities/xml/some_other_filename.xml``)
