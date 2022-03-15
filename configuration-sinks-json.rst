
.. _json_sink:

JSON push sink
--------------

The JSON push sink implements a simple HTTP based protocol where
individual entities or lists of entities are ``POSTed`` as JSON data
to an :ref:`HTTP endpoint <url_system>`.

The protocol is described in additional detail in the :doc:`JSON Push
Protocol <json-push>` document. The serialisation of entities as JSON
is described in more detail :doc:`here <entitymodel>`.

Consider using the more general :ref:`REST sink <rest_sink>` if you're interacting with a non-Sesam JSON
capable REST api.

This sink is compatible with :ref:`The HTTP endpoint source
<http_endpoint_source>`.

This sink supports :ref:`batching <pipe_batching>`.

Prototype
^^^^^^^^^

::

    {
        "type": "json",
        "system": "url-system-id",
        "url": "url-to-http-endpoint",
        "headers": {
            "some-header": "some-value"
        },
        "batch_size": 100
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
     - The full URL to HTTP service implementing the ``JSON push protocol`` described.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to POST in each request. If there are
       more entities than this then they'll be split across multiple HTTP
       requests.
     - 100
     -

   * - ``headers``
     - Dict<String,String>
     - An optional set of header values to set in HTTP request made using this sink. Both keys and values must
       evaluate to strings.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "json",
            "url": "http://localhost:9042/api/receivers/foo/entities"
        }
    }

An example using a custom "application/json" content-type header needed by some non-standard compliant servers:

::

    {
        "sink": {
            "type": "json",
            "url": "http://localhost:9042/api/receivers/foo/entities",
            "headers": {
                "content-type": "application/json; charset=UTF-8"
            }
        }
    }

