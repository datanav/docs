.. _custom_data_sink:

===========================
Creating a Custom Data Sink
===========================

The last extension point is the ability to create custom sinks. A custom data sink is a sink service that exposes an internal Sesam stream of JSON objects consumed by a :ref:`pipe <concepts-pipes>` to an external service over HTTP.

Sinks can be used to sit in front of legacy systems for which no Sesam adaptor exists. The main job of these sinks is to make
the legacy system appear to be idempotent.

Just as with the :ref:`Custom Data Source <custom_data_source>` and the :ref:`Custom Transform <custom_data_transform>` you need to define a system (such as the :ref:`HTTP system <url_system>` or the :ref:`Microservice system <microservice_system>`) connected to an external service.

Custom Data Sink - The URL system
---------------------------------

The configuration of the custom URL sink is very similar to the :ref:`custom URL source <custom_url_source>`. The configurations below defines a :ref:`URL system <url_system>` for the remote service with a :ref:`JSON sink <json_sink>` connected to it in the pipe.

.. code-block:: json
  :linenos:

    {
      "_id": "custom-url-system",
      "type": "system:url",
      "url_pattern": "http://localhost:5000/api/%s"
    }

    {
      "_id": "custom-sink-pipe",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "my-dataset"
      },
      "sink": {
        "type": "json",
        "system": "custom-url-system",
        "url": "entities"
      }
    }

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-6 p-1

    :badge:`Tutorials, badge-success text-white`
    
    **Custom Data Sink - The URL System**

    Look closer into how to create a custom data sink using the URL System. 

 
    .. link-button:: tutorial-custom-data-ssink-url-system.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|

Custom Data Sink - The Microservice system
------------------------------------------

The microservice custom sink works the same way as the microservice custom source, only now with data being passed from a Sesam pipe's sink to the microservice thgou the :doc:`JSON push sink <json-push>`. 

.. code-block:: json
  :linenos:

    {
      "_id": "custom-sink-pipe",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "my-dataset"
      },
      "sink":{
        "type": "json",
        "system": "custom-microservice-system",
        "url": "/my-sink-endpoint"

      }
    }

    {
      "_id": "custom-microservice-system",
      "type": "system:microservice",
      "docker": {
        "environment": {
          "some-other-variable": "some-other-value",
          "some-variable": "some-value"
        },
        "image": "my-image-url",
        "port": 5000
      }
    }


There are some tips on how to create a microservice in :ref:`Microservices in Sesam <microservices_in_sesam>`. In addition to those, the following templates for custom microservice data sinks are available:

    - The `ASP.NET template <https://github.com/sesam-io/aspnet-datasink-template>`__.  This template uses ASP.NET 1.0 and .NET Core 1.0, and is fully cross platform.

    - The `Python template <https://github.com/sesam-io/python-datasink-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.

    .. tip::

        When using the JSON push sink to send entities from Sesam to the microservice Sesam includes each entity's :ref:`reserved fields <reserved_fields>`. There might very well be use for them in the microservice, but if there is not these may have to be removed before sending the data from the microservice to the target system. This may be especially prudent for entities with ``“_deleted”: true``. This means the entity is marked as deleted in Sesam and might require some extra functionality to be handeled in the microservice.

        When Sesam sends data through the JSON push sink it sends the data in batches. In addition Sesam will always send one final batch without any data inside it. Therefore, if you have a JSON push sink batch size of 100 (the default value) and try to send 150 entities Sesam will send three different batches. The first batch will contain 100 entities, the second 50 entities and the last one 0 entities. This is good to have in mind when setting up the microservice.

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-6 p-1

    :badge:`Tutorials, badge-success text-white`
    
    **Custom Data Sink - The Microservice System**

    Look closer into how to create a custom data sink using the Microservice System. 

 
    .. link-button:: tutorial-custom-data-sink-microservice-system.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|
