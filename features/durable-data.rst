.. _durable-data:

Durable Data
============

In our cloud subscriptions you now have the possibility to request that a pipes data is stored in three replicas. This reduces the likelihood of data loss. 


Use case
--------

For cloud subscriptions, data is backed up to an external service once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This might not a critical problem when Sesam is pulling data from sources, as the data that was lost can be pulled again. For pipes with http_endpoint sources and non-idempotent sinks, this will most likely be a problem.

Example
^^^^^^^
Data is pushed to Sesam by an external system when the cloud service where the Sesam node runs have an health issue and goes down. When Sesam is backed up some data could be lost and Sesam will not have any automated way to ask for the data since last backup to be sent again.

Sesam writes data to an invoice system that is non-idempotent.

After a disaster recovery Sesam will go back to the last backup and rebuild it’s datasets from that point. In this use-case the last backup is from 10:00, sesam sends data on an invoice at 12:00, then a disaster recovery event happens at 12:30. Sesam will then rewind to the latest backup at 10:00 and reprocess all data from after that point. In effect sending the same invoice data twice.

.. important::

  We suggest you enable durable pipes if:

  #. You are pushing data to sesam. 
  #. All inbound pipes that are pushed too should have durable data turned on to mitigate the risk of data loss
  #. Non-idompotent endpoint
  #. Endpoint pipes and share pipes writing data to the endpoints must both have durable data enabled
  #. Endpoint pipes were duplicated data transfers could be problematic. (we recommend that all sources to be idempotent, if possible)

How to enable
-------------
Durable data can be enabled on a pipe by setting the pipe’s metadata.durable property to true.

.. code-block:: json
  :emphasize-lines: 18,19

    {
      "_id": "enhetsregisteret-company-collect",
      "type": "pipe",
      "source": {
        "type": "json",
        "system": "enhetsregisteret",
        "url": "/enhetsregisteret"
      },
      "transform": {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "_id", "_S.orgnr"]
          ]
        }
      },
    "metadata": {
        "durable": true
      },
      "add_namespaces": false,
      "namespaced_identifiers": false
    }

   
Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Default

   * - ``metadata.durable``
     - Boolean
     - When set to true, this pipe will store its state and data on a high-durability disk. This makes the pipe more
       resilient to data-loss.
     - ``false``

Pricing
-------

Durable data is a paid feature. Activating it will increase the data consumption of durable pipes by 3x.