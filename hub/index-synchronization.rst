Synchronization
===============

One of the benefits of :ref:`Sesam's generic data model <dynamic_data_model>` is that Sesam puts no demands on data coming into the platform as long as the data is represented in a standard JSON based format. Sesam comes with a multitude of built-in connectors and settings ready for use that helps our customers both import and export data from the platform, but also control when and how this synchronization should occur.

Sesam also supports custom microservices for those occasions where extra functionality is needed.

In this section you will learn how to synchronize your data streams into and out from the platform such that all enterprise data needed inside Sesam may flow continuously and seamlessly.

.. rubric:: In this section:

.. toctree::
   :maxdepth: 1

   API Best Practices <documentation/data-synchronization/api-best-practices>
   Bi-directional synchronization <bidirectional-synchronization>
   Connectors <index-connectors>
   Cron Expressions <cron-expressions>
   Developer Extension Points <extension-points>
   JSON Pull Protocol <json-pull>
   JSON Push Protocol <json-push>
   Non-idempotency <idempotency>
   Patterns <documentation/data-synchronization/data-synchronization-patterns>
   RDF Support <rdf-support>
   Source Datatype Mapping <source-datatype-mapping>
