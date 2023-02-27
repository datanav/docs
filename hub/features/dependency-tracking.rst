.. _dependency_tracking:

:badge:`Free feature,badge-success badge-pill`

Dependency Tracking
===================

One of the really smart things that Sesam can do is understand complex dependencies in the transforms. This is best described with an example. Imagine a dataset of customers and a dataset of addresses. Each address has a property ``customer_id`` that is the primary key of the customer entity to which it belongs. A user creates a DTL transform that processes all customers and creates a new ``customer-with-address`` structure that includes the address as a property. To do this they can use the :ref:`hops <hops_dtl_function>` function to connect the customer and address. This DTL transform forms part of a pipe and so when a customer entity is updated, added, or deleted it will be at the head of the dataset log and get processed the next time the pump runs. But what if the address changes? In that case we would want to put the entity at the head of the pipe again, in order to capture the updated address information. But can we do that if the address information is in a different dataset?

This is a problem of cache invalidation of complex queries. With Sesam, we have solved this problem thanks to our dedicated transform language. DTL allows Sesam to inspect the transform to see where the dependencies are. By understanding the dependencies Sesam can create data structures and events that know that a change in a hopped to dataset effects the dataset that is the source of the transform. In the example above, Sesam knows that a change to an address should put a corresponding customer entity at the front of the dataset log again. Once it is at the front of the log, it will be pulled the next time the pump is run. A new customer entity containing the updated address will be sent to the target.

.. NOTE::

   Only pipes that use the :ref:`dataset source <dataset_source>` supports dependency tracking. The primary reason for that is a technical one; the tracked entities need to be looked up by id before a specific point in time and fed through the pipe. This is currently only implemented for the ``dataset`` source type. It is unlikely that it can be implemented for other source types as those have latency and ambiguity issues.

.. NOTE::

   If you have multiple (chained) DTL transforms on a pipe, dependency tracking will only be enabled for hops located in the first transform of the chain. If you need to have multiple DTL transforms in a pipe, for instance if you have interleaved HTTP or REST transforms, then a work-around is to split the pipe into multiple pipes so the hops that require dependency tracking are located in the first DTL transform in one of them.