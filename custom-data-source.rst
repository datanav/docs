.. _custom_data_source:

=============================
Creating a Custom Data Source
=============================

A custom data source service is one that exposes data from an existing system as a stream of JSON objects over HTTP.
Data from the custom service can easily be consumed by a :ref:`Pipe <concepts-pipes>` and written into a :ref:`Dataset <concepts-datasets>`.

The basic requirements on the custom service are very simple. The service must expose a single resource that returns all
the data from the underlying system as a stream of JSON objects. 

Optionally, and it is recommended that this is implemented, the resource can accept a single query parameter called ‘’since’’. This is a token that can be used by the service to only return entities that have changed on or later than indicated in the since token. The ’’since’’ parameter is further explained in the :ref:`JSON pull protocol <json_pull>`. For endpoints that does not support a since query parameter, but does support other query parameters to locate changes in the resource a :ref:`Microservice system <microservice_system>` provides more agile ways of importing only changes from the resource. 

The JSON objects (in Sesam called an :doc:`entity <entitymodel>`) produced by the source must also adhere to a few
simple rules related to the :ref:`reserved fields <reserved_fields>` and the stucture of the batch:

    - Entities MUST have an '_id' property.
    - Entities MAY have an '_deleted' property. It defaults to false if ommitted.
    - Entities MAY have an '_updated' property. If present this will be used when Sesam invokes the since parameter on subsequent calls.
    - Any other properties starting with '_' are reserved and will not be stored in Sesam.
    - A response must expose entities as a JSON Array.

Here is an example entity:

.. code-block:: json
  :linenos:

    {
        "_id" : "1",
        "_deleted" : false,
        "_updated" : 0
    }

and another one:

.. code-block:: json
  :linenos:

    {
        "_id" : "e-8786763",
        "_deleted" : false,
        "_updated" : "2016-03-03T00:00:00Z"
    }

The following is a simple example of a response of entities exposed as a JSON array:

.. code-block:: json
  :linenos:

    [
        {
            "_id" : "1",
            "_deleted" : false,
            "_updated" : 0
        },

        {
            "_id" : "2",
            "_deleted" : false,
            "_updated" : 1
        }
    ]


The source service can be run anywhere providing that it can be contacted over HTTP from the Sesam service. To configure Sesam
to consume the feed into a dataset in Sesam, see the sections below.

.. _custom_url_source:

Custom Data Source - The URL system
-----------------------------------

The configuration below defines a :ref:`URL system <url_system>` for the remote service. Inside the configuration we have specified the ``url_pattern`` of
the service. This is helpful if the service is serving several different collections of data since each pipe connecting to the system can point to their own specific endpoint. Also, if the service moves
the base url can be updated in just one place.

The pipe's source is defined as a :ref:`JSON source <json_source>`. It expects a resource containing JSON data packed in a JSON array. 
Note that in the example below we have set ``supports_since`` to ``true``, which means we expect the resource endpoint to support the since parameter for requesting deltas, i.e. only updated data. We have also specified a pipe specific ``url``. This URL will be attached to the system's ``url_pattern`` to form the complete URL for that request.

.. code-block:: json
  :linenos:

    {
        "_id": "custom-source-pipe",
        "type": "pipe",
        "source": {
            "type": "json",
            "system": "custom-url-system",
            "supports_since" : true,
            "url": "entities"
        }
    }

    {
      "_id": "custom-url-system",
      "type": "system:url",
      "url_pattern": "http://localhost:5000/api/%s"
    }


.. _custom_data_source_microservice:

Custom Data Source - The Microservice system
--------------------------------------------

If the built-in :ref:`URL system <url_system>` is not enough to cover your required functionality, a microservice could be a good solution. When creating a microservice as a custom data source there are a few thing to bare in mind in order to gain optimal functionality.

To set up a microservice custom source a microservice that implements the :doc:`JSON push protocol <json-push>` should be
developed and running.

Once this is running it is possible to define a pipe in Sesam where the source is a :ref:`JSON source <json_source>`. All data read by the microservice will be sent to the source, preferable as a stream.

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-6 p-1

    :badge:`Tutorials, badge-success text-white`
    
    **Custom Data Source - The Microservice System**

    Look closer into how to create a custom data source with a microservice. 

 
    .. link-button:: tutorial-custom-data-source-microservice.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|

In order to help write data source components, a set of starter templates have been created for several languages. Each template
comes with a runnable service that exposes a simple set of in-memory objects as JSON using the protocol described above.
Each service also comes with a `Dockerfile <https://www.docker.com/>`_ to allow quick packaging and deployment of the
custom service alongside Sesam.

The templates that are relevant to building new data sources are:

    - The `ASP.NET template <https://github.com/sesam-io/aspnet-datasource-template>`__.  This template uses ASP.NET 1.0 and .NET Core 1.0, and is fully cross platform.

    - The `Python template <https://github.com/sesam-io/python-datasource-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.

    - The `Java template <https://github.com/sesam-io/java-datasource-template>`_. Requires Java 8 and uses the `Spark <http://sparkjava.com/>`_ micro framework.

    - The `NodeJS template <https://github.com/sesam-io/nodejs-datasource-template>`_. Requires NodeJS v4 or later.

In the following configurations we will see how the :ref:`JSON source <json_source>` in combination with the :ref:`Microservice system <microservice_system>` can be used to create a Custom Data Source.

.. code-block:: json
  :linenos:

    {
      "_id": "custom-source-pipe",
      "type": "pipe",
      "source": {
        "type": "json",
        "system": "custom-microservice-system",
        "url": "/my-source-endpoint"
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



Passing variables to a microservice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
In Sesam there are three typical ways of passing variables from Sesam into a microservice: 

- By setting environmental variables directly to the Docker container in which the microservice runs. These are defined as docker specific parameters in the :ref:`microservice system configuration <microservice_system>`.
- Through `dynamic URL's <https://stackoverflow.com/questions/35107885/how-to-generate-dynamic-urls-in-flask>`_. An example of these can be seen in the tutorial :ref:`Custom Data Source - The Microservice System - Import data <tutorial_custom_data_source_microservice>`.
- Through the request parameters  in the :ref:`JSON pull <json_pull>` and :ref:`JSON push <json_push>` protocols.

Environmental variables are usually system specific varables, i.e. they are used throughout the whole microservice and not for a spesific endpoint. Example of these might be access tokens, base URL's or headers. 

Variables through dynamic URL's are generally pipe spesific variables that are only used for specific endpoints. These include variables such as endpoint URL's or entity data that are specific for that pipe.

The request parameters are set variables containing information about the the request and state of the pipe such as batch information and since values. 

Logs from a microservice
^^^^^^^^^^^^^^^^^^^^^^^^

The best way to display information from the microservice in Sesam is to set up logging statements inside the microservice (an example of this can be seen in line 30 in the microservice template above). These logs can later be viewed in the microservice system's **Status page**. You will also be able to see some error messages and full tracebacks in the **execution logs** of the pipes executing the microservice's routes. These messages can however be hard to read, and does not always log all the needed information.   

Change tracking
^^^^^^^^^^^^^^^

Whenever possible we advise to always setup a microservice to only import changes and not full imports. This will drastically reduce the time it takes for a microservice to import data, and therefore also make data available to target systems much faster. In Sesam we refer to this as change tracking :ref:`Change Tracking <concepts-change-tracking>` and how to enable Change Tracking for microservices can be read about in detail in the section covering :ref:`Continuation support for Microservices <continuation_support_microservices>`.

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-8 p-1

    :badge:`Tutorials, badge-success text-white`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Learn about continuation support**

    Look closer into continuation support and change tracking for data imported from a microservice. 

    When finished with this tutorial you will have learned to include the necessary logic for implementing continuation support in a Sesam microservice as well as added the corresponding support inside a Sesam input pipe. 

    |
    
    .. link-button:: tutorial-custom-data-source-microservice.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|

Memory awareness
^^^^^^^^^^^^^^^^

An other important concept to be aware of if memory usage of your microservices. This both entails the total memory of the Docker container in which the microservice runs as well as the required memory to GET and POST data to and from Sesam. You can yourself decide how much MB of RAM to allocate for a Docker container through the :ref:`Microservice system configuration <microservice_system>`, but be aware that Docker container memory usage could affect the whole Sesam instance if misused and should therefore be thoroughly considered before changed. 

For container size we advise to create as minimalistic containers as possible (especially when concidering container OS), and for the required memory when importing/exporting data we suggest to stream data directly to Sesam instead of storing it in the Docker container.  

The following streaming examples are available:

- `Simple OData <https://github.com/sesam-community/simple-odata>`_
- `rest-transform <https://github.com/sesam-community/rest-transform>`_


Pushing Data Into The Hub
-------------------------

An alternative to getting Sesam to pull data is that a client can also push data to the hub. The steps for doing this
are quite straight forward.

The first step is to define a push receiver endpoint in Sesam. The :ref:`HTTP Endpoint Source <http_endpoint_source>`
should be configured to allow the custom service to push JSON data to Sesam. This endpoint supports the :doc:`JSON push protocol <json-push>`.

An example would be:

.. code-block:: json
  :linenos:

    {
        "_id": "my-endpoint",
        "type": "pipe",
        "source": {
            "type": "http_endpoint"
        }
    }


The the following URL can be used as an endpoint to receive JSON according to the :doc:`JSON push protocol <json-push>`.

::

    http://localhost:9042/api/receivers/my-endpoint/entities


Once this is configured any custom code, event handler, or queue reader can post data to Sesam.

    .. important::

        The http endpoint source works much like source with since support in that every time data is pushed to the source from an external provider, Sesam registers this as stream of changes. One of the effects of this is that data that used to be included in the push, but is not anymore, is not marked as deleted automatically downstream. You can read about how to avoid this :ref:`here <pattern_source_only_deltas>`  

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-6 p-1

    :badge:`Tutorials, badge-success text-white`
    
    **Custom Data Source - Pushing Data Into the Hub**

    Look closer into how to create a custom data source that pushed data into the hub. 

 
    .. link-button:: tutorial-custom-data-source-microservice.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|