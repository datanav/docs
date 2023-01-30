.. _completeness_feature:

:badge:`Free feature,badge-success badge-pill`

Completeness
============

Completeness is a feature that you typically enable on outgoing pipes. It makes sure that all pipes that this pipe is dependent on have run before it processes the source entities of this pipe. 

How it works
------------

The timestamp of the source entity is compared with the completeness timestamp that was inherited from its upstream and dependent pipes. 


Use cases
---------
Completeness effectively holds back the processing of source entities until it can be sure that dependent pipes have completed. 

This is useful when you want to have a final entity version before you send it to the target system. 

Using completeness also reduces the number of times you have to send the entity to the target system as there might be several state transitions until the entity can be considered complete.


Completeness
------------

When a pipe completes a successful run the sink dataset will inherit the smallest completeness timestamp value of the source datasets and the related datasets. Inbound pipes will use the current time as the completeness timestamp value (the :ref:`http_endpoint <http_endpoint_source>` can optionally get the completeness value from a request header). This mechanism has been introduced so that a pipe can hold off processing source entities that are more recent than the source dataset's completeness timestamp value. The propagation of these timestamp values is done automatically. Individual datasets can be excluded from completeness timestamp calculation via the ``exclude_completeness`` property on the pipe.  One can enable the completeness filtering feature on a pipe by setting the ``completeness`` property on the :ref:`dataset source <dataset_source>` to ``true``.

It is also possible to use the completeness timestamp value of one or more upstream datasets instead of the value from the source dataset; this is done by setting the ``completeness`` property on the :ref:`dataset source <dataset_source>` to an array of the upstream dataset ids. If the array contains more than one dataset-id, the smallest completeness timestamp value is used.

.. WARNING::

   Completeness is implicitly incompatible with full rescans as they do not necessarily expose all the latest entities. This means that if deletion tracking is performed by the pipe that has completeness set to ``true`` then the non-covered entity ids will get deleted from the sink dataset. This may or may not be a problem depending on the use-case. Deletion tracking is only performed by pipes with ``dataset`` sinks currently. Set ``deletion_tracking`` to ``false`` on the ``dataset`` sink if you do not want deletion tracking to be performed.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

       .. _exclude_completeness:
   * - ``exclude_completeness``
     - List<String>
     - A list of dataset ids that should not contribute to the completeness timestamp value. Any
       dataset listed in this property will be ignored when calculating the dataset sink
       completeness timestamp value.

       .. NOTE::

         If all datasets are excluded a new completeness timestamp value will be generated in this pipe.
     - ``[]``
     - No

        .. _include_completeness:
   * - ``include_completeness``
     - List<String>
     - A list of dataset ids that *should* contribute to the completeness timestamp value. All
       datasets listed in this property will be used when calculating the dataset sink
       completeness timestamp value. If this property is not specified, it defaults to a list of all the datasets in the
       pipe's source and transforms, with the exception of datasets that are also specified in ``exclude_completeness``.

       .. NOTE::

         If both ``exclude_completeness`` and ``include_completeness`` specify the same dataset id,
         ``exclude_completeness`` will take priority so that the dataset does not contribute to the sink
         completeness value.
     -
     - No
