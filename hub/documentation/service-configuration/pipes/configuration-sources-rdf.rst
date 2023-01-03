
.. _rdf_source:

RDF source
----------

The RDF data source is able to read `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ data
in `N-Triples <https://www.w3.org/TR/2014/REC-n-triples-20140225/>`_, `Turtle <https://www.w3.org/TR/turtle/>`_, `N3 <https://www.w3.org/TeamSubmission/n3/>`_ or `RDF/XML <https://www.w3.org/TR/rdf-syntax-grammar/>`_ format and turn this into entities.

See the :doc:`../../../rdf-support` document for more detail on working with RDF in Sesam.

It will transform triples on the form ``<subject-uri> <predicate-uri> "value" OR <object-uri>`` into
entities on the form:

::

    {
        "_id": "<subject-uri>",
        "<predicate-uri>": "value" OR "~robject-uri"
    }


`RDF Blank Nodes <https://en.wikipedia.org/wiki/Blank_node>`_ (aka BNodes) will be turned into child entities.

Prototype
^^^^^^^^^

::

    {
       "type": "rdf",
       "system": "url--or-microservice-system-id",
       "url": "url-to-rdf-file",
       "sort_lists": true,
       "format": "nt-ttl-or-xml"
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

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the ``RDF`` file to load - it can contain multiple subjects
       (with ``blank node`` hierarchies) and each unique non-blank subject will
       result in a single root entity.
     -
     - Yes

   * - ``format``
     - String
     - The type of ``RDF`` file referenced by the ``url`` property. It is
       an enumeration that can take following recognized values: ``"nt"`` for
       N-Triples, ``"ttl"`` for Turtle, ``"n3"`` for N3 or ``"xml"`` for ``RDF/XML`` files.
     - "nt"
     -

   * - ``sort_lists``
     - Boolean
     - If the ``sort_lists`` is set to ``true`` any resulting entity properties containing lists of values (due to
       them having the same RDF predicate) will be sorted, making the output predictable. This applies in a recursive
       fashion.
     - true
     -

   * - ``is_sorted``
     - Boolean
     - Indicates that the input data is sorted on RDF subject. If the ``is_sorted`` is set to ``true`` and the
       ``format`` property is ``nt`` (N-Triples), the RDF source will attempt to parse the input data sequentially and
       emit a new entity when the RDF subject changes, without loading the entire RDF file into memory first.
       Note that the input data cannot contain `RDF Blank Nodes <https://en.wikipedia.org/wiki/Blank_node>`_ (aka
       BNodes) in this case. The property has no effect on formats other than ``nt``.
     - false
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the RDF source does not return any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "rdf",
            "url": "http://www.snee.com/rdf/elvisimp.rdf",
            "format": "xml",
        }
    }
