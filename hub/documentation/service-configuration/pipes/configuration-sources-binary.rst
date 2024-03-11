
.. _binary_source:

Binary source
-------------

The binary source uses a highly optimized protocol to transfer data from one Sesam instance to another. The protocol is binary and subject to change.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "system": "system-id",
       "type": "binary",
       "url": "url-to-remote-sesam-dataset",
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
     - The id of the :ref:`URL system <url_system>` component to use. Authentication and authorization towards the remote Sesam instance needs to be set up using roles, JWTs and headers in the URL system.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the ``binary`` data to load. Note that the remote endpoint must be another Sesam endpoint.
     -
     - Yes

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between the remote endpoint and this pipe. If enabled, a pipe
       run is scheduled as soon as the remote dataset(s) changes. It does not interrupt any already running pipes.
     - ``false``
     -

   * - ``page_size``
     - Integer(>=1)
     - If the page size is specified then the source will download the data across multiple requests until there is no more data left to download. Recommended page size is 50.000.
     - No paging
     -

   * - ``subset``
     - Array
     - | An ``eq`` DTL expression where the left hand side is the index expression and the right hand side is the value that represents the subset. If the subset is specified then only entities that are in that subset will be read from the source.
       |
       | Example: ``["eq", "_S.category", "tank"]``

       .. NOTE:: For this to work the source dataset must have materialised the index used in the expression.
     -
     - No
