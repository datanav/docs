Extract reference properties as reference/classification entities
-----------------------------------------------------------------
Having references as separate entities makes it possible to merge them with other reference entities from other systems and make it possible to map data from one system to another in the connect phase.

To extract entities you will have to use the :ref:`create <dtl-transforms>` transform function. To pick a subset of your extracted entities, you should use :ref:`filtering <dtl-transforms>`.

.. warning::

  If you do a full scan for :ref:`deletion tracking <deletion_tracking>`, then subset in the source will still create entities that are not in the latest versions of that subset, therefore :ref:`subset <dataset_source>` **should** not be used in conjunction with create.