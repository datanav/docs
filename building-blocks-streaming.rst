.. _concepts-streaming:

Streams of entities
===================

Sesam consumes and produces streams of :doc:`entities <entitymodel>`. An entity is very much like a JSON object and consists of a number of key-value pairs along with some special reserved property names. See the :doc:`entity data model <entitymodel>` document for more details about entities.

The following are two simple examples showing the shape of entities that can be consumed and exposed by Sesam.

.. code-block:: json
    :linenos:


    [
        {
            "_id": "1",
            "name": "Bill",
            "dob": "01-01-1980"
        },
        {
            "_id": "2",
            "name": "Jane",
            "dob": "04-10-1992"
        }
    ]

Streams of entities flow through :ref:`pipes<concepts-pipes>`. A pipe has an associated :ref:`pump<concepts-pumps>` that is scheduled to regularly pull data entities from the :ref:`source<concepts-sources>` , push them through  :ref:`transforms<concepts-transforms>` then send the results to the :ref:`sink<concepts-sinks>` .


.. NOTE::

   Sesam's service API is not built to serve a large number of concurrent clients. Sesam is primarily an asynchronous batching and stream processing system. The Service API is not meant to be used by user-facing applications that have low latency and high throughput requirements. For that reason we do not currently give any guarantees in this regard. In practice means that if you have such a requirement you should stream the data out of Sesam and host it in a dedicated publishing systems that can scale its endpoints.
