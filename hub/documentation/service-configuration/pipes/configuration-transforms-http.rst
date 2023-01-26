
.. _http_transform:

HTTP transform
--------------

This transform performs `HTTP POST <https://en.wikipedia.org/wiki/POST_(HTTP)>`_ requests to a HTTP capable
endpoint. The service at the endpoint then transforms the entities contained in the request body and returns them in
the `HTTP response message <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Response_message>`_ .

The HTTP endpoint must accept ``application/json`` and the response must also be ``application/json``.

The endpoint must support lists of entities only, i.e. it should expect to receive a
`JSON array <https://en.wikipedia.org/wiki/JSON>`_ and it should always return a JSON array. If the endpoint returns
anything other than a "2xx Success" `HTTP status code <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`_,
the transform will raise an exception.

The endpoint is free to decide how the entities are transformed. It'll just have to produce a list of zero or more
entities from the entities it was posted. This means that entities can be transformed, filtered out or new ones created.

Note that for most use cases you can and should use the more general and flexible :ref:`REST transform <rest_transform>` instead.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

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
     - Object
     - The URL to HTTP POST entities to.
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
     - An optional set of header values to set in the HTTP request. Both keys and values must
       evaluate to strings.
     -
     -

   * - ``side_effects``
     - Boolean
     - Set to ``false`` if the transform does not have side-effects. A side-effect means that it causes changes to the system that it talks to. The intention of this property is to prevent inadvertent changes to the system by features like pipe preview. You can set this to ``true`` if you're sure your transform is free from side-effects or if you don't mind changes happening when previewing a pipe.
     - ``true``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

  {
      "_id": "my-http-transform-service",
      "type": "system:url",
      "base_url": "http://localhost:8080/transforms/"
  },
  {
      "_id": "deduplicated-men",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "men"
      },
      "transform": {
          "type": "http",
          "system":"my-http-transform-service",
          "url": "http://localhost:8080/transforms/deduplicate",
          "batch_size": 5,
          "headers": {
                "some-header": "some-value"
          }
      }
