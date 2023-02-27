.. _durable_data:
.. _durable-data:

:badge:`Paid feature,badge-info badge-pill`

Durable Data
============

By enabling durable data, Sesam will store the pipe data on a high-durability disk. This greatly reduces the likelihood of data loss.


Use case
--------

For cloud subscriptions, data is backed up to an external service once every 24 hours. During disaster recovery, data written in the last 24 hours can be lost. By using replicas and a high-durability disk for storage, the risk of data loss is greatly reduced. The risk of data loss should be acceptable when Sesam is pulling data from sources, as the data that was lost will be pulled again by Sesam. However for pipes with :ref:`HTTP endpoint source <http_endpoint_source>` and :doc:`non-idempotent <../idempotency>` sinks, data loss will most likely be a problem.


.. admonition:: When to enable

  We suggest you enable durable data in the following cases:

  #. All inbound pipes that are pushed to should have durable data enabled to mitigate the risk of data loss
  #. Non-idempotent endpoint pipes. Especially where duplicated data transfers could be an issue (we recommend that all sources be idempotent, if possible)
  #. Endpoint pipes and share pipes writing data to the endpoints must both have durable data enabled


Example
^^^^^^^
Data is being pushed to Sesam by an external system when the cloud service where the Sesam subscription runs has a health issue and goes down. When Sesam is backed up, some data could be lost and Sesam will not have an automated way to ask for the data since the last backup.

Sesam writes data to an invoice system that is non-idempotent.

After a disaster recovery Sesam will go back to the last backup and rebuild its datasets from that point. In this use case the last backup is from 10:00, Sesam sends data on an invoice at 12:00, then a disaster recovery event happens at 12:30. Sesam will then rewind to the latest backup at 10:00 and reprocess all data from after that point. In effect sending the same invoice data twice.


How to enable
-------------
Durable data can be enabled on a pipe by setting the pipe’s ``metadata.durable`` property to true. See the example below:

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
     - When set to true, this pipe will store its data and state on a high-durability disk. This makes the pipe more
       resilient to data-loss.
     - ``false``

Pricing
-------

Durable data is a paid feature. Activating it will increase the data consumption of durable pipes by 3x.
