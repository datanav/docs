==========
Open Sesam
==========

.. contents:: Table of Contents
   :depth: 2
   :local:

Sesam is designed for anyone to be able to collect, connect, and share data. Open Sesam is a provided as
a way for people to host, enrich and publish data for free. The data they publish can be open data that is
used by many others, it can be some samples that can demonstrate the value of Sesam, or just a simple way
to expose structured data on the web.

When a user signs up for Sesam they automatically get an account in Open Sesam. This allows them to upload
data, transform that data, connect it with any other data in open sesam and then publish that dataset for
others to use.

All datasets created in Open Sesam are discoverable through the Sesam Open Data Registry. This registry
has metadata about all datasets, including license information, name, description, when it was published,
and tags. Each dataset has a dataset page that has links to the actual data and a sample of the data.

We encourage people to refine and enrich existing datasets with new data. Existing data can be combined
and transformed using the powerful data transformation language. The results of transformation is new
datasets that are published and made available.

The following sections provides some quick guides on how to publish, discover and enrich using Open Sesam. We
also recommend reading the `Concepts <https://docs.sesam.io/concepts.html>`_ and `Getting Started <https://docs.sesam.io/overview.html#getting-started>`_ sections of the documentation. 

Discovering data
----------------

Anyone can search for existing datasets in the `Sesam Open Data Registry <https://registry.sesam.io/>`_.

The data is published and can be consumed according to the :ref:`JSON source <json_source>` specifications.

Once a dataset has been found, the user can quickly preview the data using the ``Preview URL`` link. This
will display the first 10 entities in that dataset.

A copy of the dataset can also be downloaded using the ``Data URL`` link.

Remember that data in Sesam is changing whenever the underlying data changes. If you want to consume
the datasets in a continuous fashion, we recommend that you sign up and use Sesam to handle the data.

Publishing data
---------------

To publish data to Sesam the user first needs to create an account on the `Sesam Portal <https://portal.sesam.io/>`_.

Once signed up, they will have access to ``Open Sesam`` as well as a few selected read-only tutorials.

Selecting the open sesam service instance will show an empty data hub that can be used to consume, reshape and publish
data. The other service instances are read only and show some typical usages of Sesam.

Uploading Json Data
~~~~~~~~~~~~~~~~~~~


Creating an HTTP Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~

To upload a dataset to Sesam it is first necessary to create an endpoint that can receive the data. This is done by defining an `Http DataSource <https://docs.sesam.io/configuration.html#the-http-endpoint-source>`_. This can be done either via the management studio or via the API. 

A new Http Endpoint go to can be added by creating a pipe with the following definition; but remember to change the "_id" property to be something more unique.

::

  {
      "_id": "mypipe",
      "type": "pipe",
      "source": {
          "type": "http_endpoint"
      }
  }


Your Json Data
~~~~~~~~~~~~~~

Data posted to Sesam should be in the form:

::

  [
     {
        "_id" : "entity-id-0",
        ... any other valid json
     },

     {
        "_id" : "entity-id-1",
        ... any other valid json
     }

     ... more json objects ...
  ]


The only requirement is that each JSON object has a property called "_id" that contains the entiity id. These id values are up to you to decide, but should be unique within a DataSet.


Sending the Data
~~~~~~~~~~~~~~~~

Now this is setup you can use CURL to upload a JSON file from your computer:

Sesam is secure by default so to POST data to the endpoint you will need to authenticate against the portal to aquire a JWT token that can be used in a CURL request. The following steps guide you through doing this process.

Create a text-file with the email and password you use to log in to Sesam:

::

  echo "email=YOUR_EMAIL_ADDRESS&password=YOUR_PASSWORD" > cred.txt

Download the authorization token for the specified email and password and store it in an environment variable:

::

  export SESAM_AUTH_HEADER="Authorization: Bearer $(curl -d @cred.txt https://instance-guid.sesam.cloud/api/jwt)"

Make an alias to run curl with the authorization token:

::

  alias curlJWT='curl -H "$SESAM_AUTH_HEADER"


The URL of the http endpoint is of the form:

::

  https://982ae5c5.sesam.cloud/api/receivers/mypipe/entities


Note that 'mypipe' needs to be changed to match the '_id' of the http endpoint pipe created in the earlier step. The first part of the URL (982ae5c5) may also differ. Check your Open Sesam instance to see the correct value.

Then test you can talk to Sesam form curl with:

::

  curlJWT https://982ae5c5.sesam.cloud/api/pipes

Finally, use upload your JSON file with:

::
  
  curlJWT -X POST -H "Content-Type: application/json" --data @your-file.json https://982ae5c5.sesam.cloud/api/receivers/mypipe/entities

More detailed information about how to publish data according to the :doc:`JSON Push Protocol <json-push>` can be found in these :ref:`examples <json_push_examples>`.

Checking the Data
~~~~~~~~~~~~~~~~~

If this succeeds then a new dataset will be listed on your Open Sesam instance and will contain the uploaded entities. You can upload the JSON as many times as you want. Only changes will be reflected. 

Adding Metadata
---------------

Additional metadata for the dataset can be made available in the registry by adding the following
metadata configuration to the pipe config:

::

  {
     "_id": "myendpoint",
     "type": "pipe",
     "source": {
         "type": "http_endpoint"
     },
     "sink": {
         "type": "dataset",
         "dataset": "mydataset"
     }
     "metadata": {
         "registry": {
             "description": "Solar power metering from my roof",
             "keywords": [ "electricity", "solar" ],
             "license": "CC"
         }
     }
  }


Enriching data
--------------

The user can also publish new data by combining or enriching existing datasets in new ways.

The registry must first be added as a system:

::

   {
       "_id": "myregistry",
       "type": "system:url",
       "base_url": "https://registry.sesam.io"
   }

The user can then set up a pipe to fetch an existing dataset (the url is provided in the registry):

::

   {
       "_id": "mydatasetcopy",
       "type": "pipe",
       "source": {
           "type": "json",
           "system": "myregistry",
           "url": "/data/b5f58848/mydataset"
       }
   }

The user can then enrich this data and produce a new dataset that is intended to be published:

::

   {
       "_id": "mydataset_qa",
       "type": "pipe",
       "source": {
           "type": "dataset",
           "dataset": "mydatasetcopy"
       },
       "transform": {
           "type": "dtl",
           "rules": {
               "default": [
                   ["filter",
                       ["eq", "GOOD", "_S.quality"]
                   ]
               ]
           }
       },
       "metadata": {
           "registry": {
               "description": "Quality controlled solar power metering from my roof",
               "keywords": [ "electricity", "solar", "qa" ],
               "license": "CC"
           }
       }
   }

Note that every dataset is automatically published, including intermediate steps like ``mydatasetcopy``
above. If you want to hide your data, you can set up a private subscription in the Sesam Portal.

