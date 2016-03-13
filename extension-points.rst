==========================
Developer Extension Points
==========================


.. contents:: Table of Contents
   :depth: 2
   :local:

There are many native components for collecting, transforming and using data. Sometimes however, there may be custom datasources, transforms and sinks that are needed. To help in these situations there are well defined patterns and integration points that can be used.

Integration is done through standardised RESTful protocols. Services supporting these protocols can be built as micro-services that can be easily connected to Sesam.     

As well as writing services from scratch there are also a number of starter service implementations that can be copied and changed. These are open source and can be cloned from the Sesam open source repository.

Creating a Custom DataSource
----------------------------

A DataSource service is one that exposes data from an existing system as a stream of JSON objects over HTTP. Data from the custom service can easily be consumed and written into a Dataset. 

The basic requirements on the custom service are very simple. The service must expose a single resource that returns all the data from the underlying system as a stream of json objects. Optionally, and it is recommended that this is implemented, the resource can accept a single query parameter called ''since''. This is a token that can be used by the service to only return entities that have changed on or later than indicated in the since token. 

The JSON objects produced by the source must also adhere to a few simple rules:

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


The service can be run anywhere providing that it can be contacted over HTTP from the Sesam Service. To configure Sesam to consume the feed into a dataset in Sesam the following sytem and pipe configuration can be used.

The configuration defines a system for the remote service. This specifies the ''base_url'' of the service. This is helpful if the service is serving several different collections of data. Then if the service moves the base url can be updated in just one place. 

The pipe is defined as just as simple ''json'' pipe. It expects a resource containing JSON data packed in a JSON array. Note that in the example below we have set ''supports_since'' to ''true''.

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
	       "schedule_interval": 5000
	    }
    }


To help write datasource components a set of starter templates have been created for several languages. Each template comes with a runnable service that exposes a simple set of in-memory objects as JSON using the protocol described above. Each service also comes with a Dockerfile to allow quick packaging and deployment of the custom service alongside Sesam.

The templates that are relevant to building new datasources are:

	- The `asp.net 1.0 template <https://github.com/sesam-io/aspnet-datasource-template>`_.  This template using the latest version of asp.net 1.0 and .net core 1.0.

	- The `nodeJS template <https://github.com/sesam-io/nodejs-datasource-template>`_.


Pushing Data Into The Hub
-------------------------

An alternative to getting Sesam to pull data is that a client can also push data to the hub. 



Creating a Custom Transform
---------------------------





Creating a Custom Data Sink
---------------------------




Using the start templates
-------------------------







