.. _sparql_source:

SPARQL source
-------------

The SPARQL source fetches `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ data about subjects from a
`triplestore <https://en.wikipedia.org/wiki/Triplestore>`_ exposing a `SPARQL compliant <https://www.w3.org/TR/rdf-sparql-query/>`_ endpoint.
The endpoint of the source is configured either directly or implicitly by a :ref:`URL system <url_system>`. The source uses
two SPARQL queries to construct entities; the fragment query is a SPARQL ``SELECT`` query that gets a list of subjects
to get data for and their modification times and a fragment query, which is a SPARQL ``CONSTRUCT`` query that
gathers all relevant statements about a particular subject. The latter is then used to generate the stream of entities.

See the :doc:`../../../rdf-support` document for more detail on working with RDF in Sesam.

Prototype
^^^^^^^^^

::

    {
        "type": "sparql",
        "system": "url-system-id",
        "url": "sparql-endpoint",
        "fragments_query": "SPARQL select query",
        "fragment_query": "SPARQL construct query"
        "initial_since_value": "0001-01-01T00:00:00Z"
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
     - The id of the :ref:`URL System <url_system>` component to use.
     -
     - Yes

   * - ``fragments_query``
     - List<String> or String
     - A SPARQL ``SELECT`` query that should return exactly two bound variables: ``id`` which should contain a unique subject
       and ``updated`` which should contain its modification time in ISO UTC format (or "0001-01-01T00:00:00Z" if not
       available in the data). If you would like the source to have continuation support, then you must include a filter based on the
       ``updated`` content compared to the current since moniker. You must use a variable expansion ``${since}`` for this
       purpose. The query result set should always be ordered by the "?updated" variable. If a list of strings is given,
       they will be converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``fragment_query``
     - List<String> or String
     - A SPARQL ``CONSTRUCT`` query that should return all the relevant statements for a particular subject selected
       by the ``fragments_query`` query. The query should use the expansion variable "${uri}" to filter or select
       the correct subject to construct the statements to return.  If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``initial_since_value``
     - String
     - A string literal to use when querying the triplestore the first time.
     - "0001-01-01T00:00:00Z"
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the SPARQL source does not return any entities. Normally, any previously synced
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
     - ``false`` (Dynamic: ``true`` if ``${since}`` in ``fragments_query``)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

::

    {
        "source": {
            "type": "sparql",
            "url": "http://localhost:8890/sparql",
            "fragments_query": [
                "PREFIX sdshare: <http://www.sdshare.org/2012/extension/>",
                "SELECT DISTINCT ?id ?updated WHERE {",
                 "    ?id sdshare:lastmodified ?updated",
                 "} FILTER (?updated >= \"${since}\"^^xsd:dateTime) ORDER BY ?updated",
            ],
            "fragment_query": [
                "CONSTRUCT { ?subject ?property ?value } WHERE {",
                "  ?subject ?property ?value .",
                "} FILTER (?subject = <${uri}>)",
            ]
        },
    }
