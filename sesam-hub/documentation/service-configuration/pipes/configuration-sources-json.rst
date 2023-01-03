.. _json_source:

JSON source
-----------


The JSON source can read entities from a `JSON <https://en.wikipedia.org/wiki/JSON>`_ resource available over
`HTTP <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ (i.e. served by a web server).
The service must conform to the :doc:`JSON Pull Protocol <../../../json-pull>`.

Consider using the more general :ref:`REST source <rest_source>` if you're interacting with a non-Sesam JSON capable
REST api.

If the ``supports_since`` property is set to *true*, then the ``since`` request parameter is added to the URL to
signal that we want only changes that happened after the since marker.

Prototype
^^^^^^^^^

::

    {
       "system": "system-id",
       "type": "json",
       "url": "url-to-json-data",
       "supports_signalling": false,
       "headers": {
           "some-header": "some-value"
       }
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
     - The id of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the ``JSON`` data to load. Note that the data must conform to the :doc:`JSON Pull Protocol <../../../json-pull>`.
     -
     - Yes

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.
     - ``false``
     -

   * - ``page_size``
     - Integer(>=1)
     - If the page size is specified then the source will download the data across multiple requests until there is no more data left to download. The ``limit`` request parameter is passed to the endpoint to cap the number of entities in each response.

       .. NOTE::

          Paging is only available if the source has ``supports_since``, ``is_chronological`` and ``is_since_comparable`` all set to ``true``.
     - No paging
     -

   * - ``subset``
     - Array
     - | An ``eq`` DTL expression where the left hand side is the index expression and the right hand side is the value that represents the subset. If the subset is specified then only entities that are in that subset will be read from the source.
       |
       | Example: ``["eq", "_S.category", "tank"]``

       .. NOTE:: For this to work the source must support subsets.
     -
     - No

   * - ``headers``
     - Dict<String,String>
     - A optional set of header values to set in HTTP request made using this source. Both keys and values must
       evaluate to strings.
     -
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the JSON source does not return any entities. Normally, any previously synced
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
            "type": "json",
            "system": "some-url-or-microservice-system",
            "url": "test.json",
        }
    }
