.. _schema-inferencing:

Schema inferencing
==================

Data in Sesam is dynamically typed. Properties can be added or removed and their types changed over time. Schema validation can be enforced, but it is optional. This dynamism makes the system agile. Automatic schema inferencing is enabled by default. Sesam tracks the changes to entities and will automatically generate a schema for the source entities and sink entities of pipes. In practice this means that you can see the structure of the data that went into the pipe and the data that came out of the pipe. This feature is the foundation that :ref:`property lineage <property-lineage>` builds on.