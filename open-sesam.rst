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

The following sections provide detailed guidance on how to publish, discover and enrich using Open Sesam.

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

To publish data according to the :doc:`JSON Push Protocol <json-push>`, the user can follow these
:ref:`examples <json_push_examples>`.

Additional metadata for the dataset can be made available in the registry by adding the following
metadata configuration:

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