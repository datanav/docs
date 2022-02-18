==========================
Developer Extension Points
==========================


There are many native Sesam components for collecting, transforming and using data. Sometimes however, there may be
custom :ref:`data sources <source_section>`, :ref:`transforms <transform_section>` and :ref:`sinks <sink_section>` that
are needed. To help in these situations there are well defined patterns and integration points that can be used.

Integration is done through standardised RESTful protocols. Services supporting these protocols can be built as
micro-services that can be easily connected to Sesam.

As well as writing services from scratch there are also a number of starter service implementations that can be copied
and changed. These are open source and can be cloned from the Sesam open source repository.

Creating a Custom Data Source
-----------------------------

A data source service is one that exposes data from an existing system as a stream of JSON objects over HTTP.
Data from the custom service can easily be consumed and written into a Dataset.

The basic requirements on the custom service are very simple. The service must expose a single resource that returns all
the data from the underlying system as a stream of JSON objects. Optionally, and it is recommended that this is
implemented, the resource can accept a single query parameter called ''since''. This is a token that can be used by the
service to only return entities that have changed on or later than indicated in the since token.

The JSON objects (in Sesam called an :doc:`entity <entitymodel>`) produced by the source must also adhere to a few
simple rules:

    - Entities MUST have an '_id' property.
    - Entities MAY have an '_deleted' property. It defaults to false if ommitted.
    - Entities MAY have an '_updated' property. If present this will be used when Sesam invokes the since parameter on subsequent calls.
    - Any other properties starting with '_' are reserved and will not be stored in Sesam.

Here is an example entity:

::

    {
        "_id" : "1",
        "_deleted" : false,
        "_updated" : 0
    }

and another one:

::

    {
        "_id" : "e-8786763",
        "_deleted" : false,
        "_updated" : "2016-03-03T00:00:00Z"
    }

A response must expose the entities as a JSON array. The following is a simple example of this:

::

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


The service can be run anywhere providing that it can be contacted over HTTP from the Sesam Service. To configure Sesam
to consume the feed into a dataset in Sesam the following sytem and pipe configuration can be used.

The configuration defines a :ref:`URL system <url_system>` for the remote service. This specifies the ``base_url`` of
the service. This is helpful if the service is serving several different collections of data. Then if the service moves
the base url can be updated in just one place.

The pipe is defined as just a simple ``json`` pipe. It expects a resource containing JSON data packed in a JSON array.
Note that in the example below we have set ``supports_since`` to ``true``.

::

    {
        "_id": "custom-remote-service",
        "name": "custom remote service",
        "type": "system:url",
        "base_url": "http://localhost:5000/api/"
    },

    {
        "_id": "custom-datasource-to-dataset",
        "name": "Custom Data Source into Hub",
        "type": "pipe",

        "source": {
            "type": "json",
            "system": "custom-remote-service",
            "name": "custom-json-source",
            "supports_since" : true,
            "url": "entities"
        },

        "sink": {
            "type": "dataset",
            "name": "remote-objects-dataset",
            "dataset": "Custom:Objects"
        },

        "pump": {
           "type": "datasync",
           "name": "custom-datasource-to-dataset-pump",
           "schedule_interval": 5
        }
    }


To help write data source components a set of starter templates have been created for several languages. Each template
comes with a runnable service that exposes a simple set of in-memory objects as JSON using the protocol described above.
Each service also comes with a `Dockerfile <https://www.docker.com/>`_ to allow quick packaging and deployment of the
custom service alongside Sesam.

The templates that are relevant to building new data sources are:

    - The `ASP.NET template <https://github.com/sesam-io/aspnet-datasource-template>`__.  This template uses ASP.NET 1.0 and .NET Core 1.0, and is fully cross platform.

    - The `Python template <https://github.com/sesam-io/python-datasource-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.

    - The `Java template <https://github.com/sesam-io/java-datasource-template>`_. Requires Java 8 and uses the `Spark <http://sparkjava.com/>`_ micro framework.

    - The `NodeJS template <https://github.com/sesam-io/nodejs-datasource-template>`_. Requires NodeJS v4 or later.


Pushing Data Into The Hub
-------------------------

An alternative to getting Sesam to pull data is that a client can also push data to the hub. The steps for doing this
are quite straight forward.

The first step is to define a push receiver endpoint in Sesam. The :ref:`HTTP Endpoint Source <http_endpoint_source>`
should be configured to allow the custom service to push JSON data to Sesam. This endpoint supports the :doc:`JSON push protocol <json-push>`.

An examples would be:

::

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


Once this is configured any custom code, event handler, or queue reader can post data to Sesam. The data will be stored
into a dataset called 'my-endpoint'.


Creating a Custom Transform
---------------------------

:ref:`DTL <dtl_transform>` and the other :ref:`transform types <transform_section>` provide support for the majority
of data transformation uses cases. However, there are times when a special kind of transform needs to be performed.
Typically, this is a transform where some external service should be contacted in order to convert a value. In these
cases it is possible to develop a micro-service that can be called synchronously from the transform pipeline.

The custom transform is configured as an :ref:`HTTP transform <http_transform>`. This is defined as part of the
transformation pipeline of a :ref:`pipe <pipe_section>`.

The service that data is sent to as part of this transform is where the custom code should reside. To help build these
transforms template projects for common languages are provided.

The following templates are available:

    - The `Python template <https://github.com/sesam-io/python-transform-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.

The transform will stream an array of JSON objects to the registered endpoint and expect back a list of entities.

The result of the HTTP transform is passed along the transformation pipeline and into the sink.


Creating a Custom Data Sink
---------------------------

The last extension point is the ability to create custom sinks. These are not sinks that run in the Sesam service but
are micro-services to which a generic JSON push sink can send data.

To set up a custom sink a micro-service that implements the :doc:`JSON push protocol <json-push>` should be
developed and running.

Once this is running it is possible to define a pipe in Sesam where the sink is a :ref:`JSON Push Sink <json_sink>`.
All data read from the pipe will be pushed to the sink.

Sinks can be used to sit in front of legacy systems for no Sesam adaptor exists. The main job of these sinks is to make
the legacy system appear to be idempotent.

To help build these transforms template projects for common languages are provided.

The following templates are available:

    - The `ASP.NET template <https://github.com/sesam-io/aspnet-datasink-template>`__.  This template uses ASP.NET 1.0 and .NET Core 1.0, and is fully cross platform.

    - The `Python template <https://github.com/sesam-io/python-datasink-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.
