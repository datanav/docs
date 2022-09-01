.. _durable-data:

Durable Data
============

For cloud subscriptions, data is backed up to an external service once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This might not a huge problem when Sesam is pulling data from sources, as the data that was lost can be pulled again. For pipes with http_endpoint sources and non-idempotent sinks, this will most likely be a problem. In our cloud subscriptions you now have the possibility to request that a pipes data is stored in three replicas. This reduces the likelihood of data loss. Note that this incurs a 3x increase in data size for the pipes that has this feature enabled.

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
       resilient to data-loss, but will also incur an additional cost, see :ref:`Durable Data <durable-data>`
       for more details.
     - ``false``

Pricing
-------

Durable data is a paid feature. Activating it will increase the data consumption of durable pipes by 3x.