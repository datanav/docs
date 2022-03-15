
.. _sdshare_sink:

SDShare push sink
-----------------

The SDShare push sink is similar to the :ref:`JSON push sink <json_sink>`, but instead of posting JSON it
translates the inbound entities to ``RDF`` and ``POSTs`` them in N-Triples form to a :ref:`HTTP endpoint <url_system>`
implementing the ``SDShare push protocol``.

Prototype
^^^^^^^^^

::

    {
        "type": "sdshare",
        "system":"url-system-id",
        "url": "url-to-http-endpoint",
        "graph": "uri-of-graph-to-post-to"
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
     - The id of the :ref:`URL system <url_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The full URL to HTTP service implementing the ``SDShare push protocol``.
     -
     - Yes

   * - ``graph``
     - String
     - A URI representing a graph to post the ``RDF ntriples`` to
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sdshare",
            "url": "http://localhost:8001/sdshare_push_service"
        }
    }
