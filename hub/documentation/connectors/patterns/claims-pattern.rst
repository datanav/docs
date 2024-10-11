.. _claims:

Claims pattern
--------------

In some cases, such as in :ref:`time-based masterdata management <time-based-masterdata-management>`, we required more information about a property than just the value. 

Much like the :ref:`namespace <whatis-namespaces>` of a property can tell us some information about where the property comes from we might have a need to know more about each property, e.g.:

- Which entity the value comes from
- When the value last updated
- When was the value created
- Which entity was the origin of the entity (was it inserted by Sesam based on an other entity)

In order to include more metadata for a property we can introduce *claims*.

A claim simply replaces the value of a property with a dictionary of metadata, the original value being one of the metadata included. This restructuring of the ``<property>: <value>`` pair is done in the ``-enrich`` pipes and is kept in addition to the original raw data from the source system.

Example 

::

  "<namespace>:<property>": 
    {
      "<namespace>:value": "<value>",
      "<namespace>:$last-modified": "~t1987-09-11:T06:55:07.456827Z"
    }

In the example above we have restructured a ``<property>: <value>`` pair to become a ``<property>: claim`` pair where the claim hold the original value information as well as additional metadata. In this case the additional metadata relates to when the property value was last updated.