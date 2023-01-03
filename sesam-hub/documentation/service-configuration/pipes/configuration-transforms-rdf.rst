
.. _rdf_transform:

RDF transform
-------------

This transform will render entities to a N-Triples string and embed it in the entity, which is then passed on
to the transform chain.

Prototype
^^^^^^^^^

::

    {
        "type": "rdf",
        "rdf-property": "rdf-property-to-use"
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

   * - ``rdf-property``
     - String
     - The property that will hold any RDF generated
     -
     - Yes


Example configuration
^^^^^^^^^^^^^^^^^^^^^

This is how a RDF transform would look like in the context of a pipe (source and sink configs omitted for brevity):

::

   {
       "_id": "my-pipe",
       "transform": {
           "type": "rdf",
            "rdf-property": "rdf"
       }
   }

Given the input entity:

::

  {
    "_id": "x:1",
    "x:name": "Entity 1",
    "x:id": "entity-1",
    "foo:prop": [{
        "x:id": "child",
    }]
  }


And these namespaces in the metadata configuration:

::

    "namespaces": {
        "default": {
            "x": "http://x.org/",
            "foo": "http://foo.org/",
        }
    }


it will produce the transformed entity:

::

  {
    "_id": "x:1",
    "x:name": "Entity 1",
    "x:id": "entity-1",
    "foo:child": [{
        "x:id": "child",
    }]
    "rdf": "<http://x.org/1> <http://x.org/name> \"Entity 1\".\n<http://x.org/1> <http://x.org/id> \"entity-1\".\n<http://x.org/1> <http://foo.org/child> _:x1.\n_:x1 <http://x.org/id> \"child\".\n"
  }
