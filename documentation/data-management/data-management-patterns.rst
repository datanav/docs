.. _data-management-patterns:

========================
Data Management patterns
========================

We've identified a set of patterns when working with problems related to Master Data Management in Sesam. We find it very useful to name these patterns as it makes it easier to refer to them when discussing challenges.

.. note::
  This document is subject to improvements as we continuesly are identifying new patters to enforce better master data management in Sesam.
  
Generic patterns
================

.. _pattern-rewriting-identity:

Rewriting identity
------------------
When rewriting ``_id`` you should always add a ``["add", "$original_id", "_S._id"]`` in order to be able to trace and debug. Multiple upstream entities could map to the same identity, and this can be very hard to figure out without this information. Also make sure you rewrite the identifier before you do any filtering.

Enrich patterns
===============

Extract foreign references as separate datatypes
------------------------------------------------
Don't make NIs to stuff that is outside your control, keep the namespace local to the system. Extract the properties to new separate datatypes. If you don't have them as objects you can't merge them with the same concept from other sources. Time is not a good candidate for NI. Postal codes are a good example. If you make a NI make it reference your own namespace. Use :ref:`create <dtl_transform-create>`.

Adding type information
-----------------------
Useful to pick out relevant subsets from the globals later. Add data type property (``rdf:type`` or ``$type``).

Splitting out lists of sub-objects
----------------------------------
Aggregate objects --- are the sub-objects part of the parent or can they live on their own? Use :ref:`create-child <dtl_transform-create-child>` and :ref:`emit_children <emit_children_transform>`.

Keep the data in its original structure
---------------------------------------
Data modeller expects data in the same structure as the system that produced it, and often need to send back the original structure.

Normalising data
----------------
Convert data to Sesam types and add them as new properties. Try to use different namespaces for the original data vs the normalised data.

Extract reference properties as reference/classification entities
-----------------------------------------------------------------
Having references as separate entities makes it possible to merge them with other reference entities from other systems and make it possible to map data from one system to another in the connect phase.

To extract entities you will have to use the :ref:`create <dtl-transforms>` transform function. To pick a subset of your extracted entities, you should use :ref:`filtering <dtl-transforms>`.

.. warning::

  If you do a full scan for :ref:`deletion tracking <deletion-tracking>`, then subset in the source will still create entities that are not in the latest versions of that subset, therefore :ref:`subset <dataset_source>` **should** not be used in conjunction with create.

Connect patterns
================

Cleaning data
-------------
Should be added as new properties, you might need the dirty data.

External merge
--------------
Hardcoded dataset with manually connected IDs, could also be an external source with manual input. Linking table. AI connected objects. `Duke <https://github.com/larsga/Duke>`_ is an example. Produces link objects.

Golden property based on priority
---------------------------------
Use :ref:`coalesce <coalesce_dtl_function>`.

Golden property based on last updated
-------------------------------------
Make sure you have a reliable timestamp from the source that you propagate. Think about feedback loops if data is synced back. Can be good to standardise on e.g. ``$last_updated``.

Golden property based on quality
--------------------------------
Make a normalised quality score across the sources you want to pick from, and pick the property from the source that has the most relevant score.

Feedback loop
-------------
Expensive hops or external transforms is best to do in a separate dataflow. This allows you to optimise what you process using subsets, the primary dataflow does not have to wait for this data, it will be processed later if it applied to the entity. Entities might be processed twice if the feedback affected the entity. Use the ``_id`` of the merge source as the identifier. Make sure the feedback is marked as deleted when the data that produced it no longer exists (otherwise entities will never be deleted due to the feedback entity itself).

Hungarian notation references
-----------------------------
When referencing from one global to another global, one can encode which global the reference points to in order to make it easier to understand what the reference is. E.g. a parent reference from global-person to global-person could be `parent-person-ni`. The reference name in this case is `parent` and the reference points to `global-person` and is of type `namespaced identifier`.

Transform patterns
==================

Late schema binding
-------------------
Ensure that transformations are done in accordance to the target schema. Bidirectional sync might not support patching, and you need the original object when sharing. When mapping, only use the namespace of the target system or the global namespace. Hops should be done on global properties. Use identifiers from the target system. If you reference other namespaces, you can no longer do all refactoring in the connect phase.

Defining hierarchies for recursion
----------------------------------
:ref:`Recursive hops <hops>` should be used when your data exhibits inverse relationships. Typically used when filtering on reference/classification properties.

An inverse relationship allows for you to `broaden or narrow <https://www.w3.org/TR/2005/WD-swbp-skos-core-guide-20051102/#sechierarchy>`_ the scope of your data.

When doing recursive hops, you should define the property ``max_depth`` to safeguard against never ending recursions.

Re-mapping references to target identifiers
-------------------------------------------
You use the "Extract reference properties as reference/classification entities" pattern so that you can remap references to target identifiers by hopping to the classification/reference dataset and use the property from the correct target namespace.
