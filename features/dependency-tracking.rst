.. _dependency-tracking:

:badge:`Free feature,badge-success badge-pill`

Dependency Tracking
===================

One of the really smart things that Sesam can do is to understand complex dependencies in DTL. This is best described with an example. Imagine a dataset of customers and a dataset of addresses. Each address has a property ``customer_id`` that is the primary key of the customer entity to which it belongs. A user creates a DTL transform that processes all customers and creates a new ``customer-with-address`` structure that includes the address as a property. To do this they can use the :ref:`hops <hops_dtl_function>` function to connect the customer and address. This DTL transform forms part of a pipe and as such when a customer entity is updated, added or deleted it will be at the head of the dataset log and gets processed the next time the pump runs. But what if the address changes? As far as the expected output the customer itself has also changed.

This is in essence a problem of cache invalidation of complex queries. With Sesam, we have solved this problem. We are empowered to solve the problem thanks to our dedicated transform language. This allows us to introspect the transform to see where the dependencies are. Once we understand the dependencies we can create data structures and events that are able to understand that a change to an address should put a corresponding customer entity at the front of the dataset log again. Once it is there it will be pulled the next time the pump is run and a new customer entity containing the updated address is exposed.

.. NOTE::

   Only pipes that use the :ref:`dataset source <dataset_source>` supports dependency tracking. The primary reason for that is a technical one; the tracked entities need to be looked up by id before a specific point in time and fed through the pipe. This is currently only implemented for the ``dataset`` source type. It is unlikely that it can be implemented for other source types as those have latency and ambiguity issues.

.. NOTE::

   Dependency Tracking only works in the first transform/DTL chain.