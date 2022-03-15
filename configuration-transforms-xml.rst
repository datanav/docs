.. _xml_transform:

XML transform
-------------

This transform will render entities on the form described in the :ref:`XML endpoint sink <xml_endpoint_sink>` to a string and
embed it in the entity, which is then passed on to the transform chain.

Prototype
^^^^^^^^^

The properties are identical to the :ref:`XML endpoint sink <xml_endpoint_sink>`, except for the additional ``xml-property``:

::

    {
        "type": "xml",
        "root-attributes": {
           "xmlns": "http://www.example.org/ns1",
           "xmlsn:foo": "http://www.example.org/ns2",
           "xmlns:bar": "http://www.example.org/ns3"
        },
        "xml-property": "xml-property-to-use",
        "include-xml-decl": false,
        "skip-deleted-entities": true
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

   * - ``root-attributes``
     - Object
     - An object containing the attributes to include on the root element. This is where you typically declare
       your namespaces, schema and so on.
     -
     -

   * - ``include-xml-decl``
     - Boolean
     - If set to ``true`` includes a default XML header: ``<?xml version="1.0" encoding="UTF-8" standalone="yes"?>``
     - false
     -

   * - ``xml-property``
     - String
     - The property that will hold any XML generated
     -
     - Yes

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the XML output. The default is that
       deleted entities does not appear.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

This is how a XML transform would look like in the context of a pipe (source and sink configs omitted for brevity):

::

   {
       "_id": "my-pipe",
       "transform": {
           "type": "xml",
            "root-attributes": {
               "xmlns": "http://www.example.org/ns1",
               "xmlns:foo": "http://www.example.org/ns2"
            },
            "xml-property": "xml"
       }
   }

Given the input entity:

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

it will produce the transformed entity:

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
    }],
    "xml": "<foo:tag xmlns=\"http://www.example.org/ns1\" xmlns:foo=\" .. </foo:tag>"
  }

