.. _architecture-and-concepts-novice-1-2:

Architecture and Concepts: Novice
---------------------------------

.. _joining-data-1-2:

Joining Data
~~~~~~~~~~~~

The value of joining data

Short overview of what data joining is

1-1, 1-n, n-m

.. _make-namespaced-identifiers-for-foreign-keys-make-ni-1-2:

Make namespaced identifiers for foreign keys - make-ni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _full-outer-join-merge-1-2:

Full outer Join - Merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full outer join is something you will experience in the Sesam terminology as a "merge". A merge, like the full outer join, retains all entries from i.e. two merged data objects. Graphically, a full outer join will look like the following:

.. figure:: ./media/Full_Outer_Join.png
   :align: center
   :alt: Figure – Full Outer Join

   Figure – Full Outer Join

A note on the handling of null values. In Sesam null values are not existing. Meaning, as opposed to a full outer join which will populate empty entries in the join between tables with null values, the merge in Sesam will by default never have to do this. To exemplify, look at the below example: 

.. code-block:: json
	
	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5]
	}
	{			
	  "_id": "second_entity:bar",
	  "second_entity:value": 1,
	  "second_entity:string":"This is retained",
	  "second_entity:values": [1, 3, 4, 6]
	}

and the merged result, if we choose to retain the first "_id" of the above two data objects and join the data on the value property:

.. code-block:: json

	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5],
	  "second_entity:value": 1,
	  "second_entity:string":"This is retained",
	  "second_entity:values": [1, 3, 4, 6],
	  "$ids": [
	    "~:first_entity:foo",
	    "~:second_entity:bar"
	  ]
	}

What should immediately get your attention would be the "$ids" property in the merged result. Sesam utilizes this property to keep track of which "_id"s have been merged and as such aids in data governance, as you do your data modelling.  


.. _left-join-hops-1-2:

Left Join - Hops
~~~~~~~~~~~~~~~~

Data is appended to the output

.. _global-1-2:

Global
~~~~~~

Golden – the best truth about common attributes of a concept collected
from multiple sources

Coalesce, prioritization of source data (master data)


.. _generic-input-pipes-custom-output-pipes-1-2:

Generic input pipes, custom output pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write about where globals fit into the bigger picture of data flows, how
do pipes going in look and how do pipes going out look?

.. _filter-entities-on-the-way-out-1-2:

Filter entities on the way out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Filter gives the ability to stop entities from being sent by providing
  a logical gate.
| On the other hand, it can make sure you only send the entities you
  wish to receive in an endpoint.

| Makes sure the endpoint only receives the entities they want.
| Can stop entities from triggering events they shouldn’t trigger.

| + + many examples
| filtering on source data
| on target data (from hops f.ex) – typical example, hop to
  global-classification and map status, if cancelled then filter

.. _tag-your-entities-categorization-of-sub-concepts-1-2:

Tag your entities - Categorization of sub-concepts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extra:type - usually added into the globals to separate what entities about the same thing do & mean.

.. _customize-data-structure-for-endpoints-1-2:

Customize data structure for endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Sesam has transformative functions to add, remove,Copy the attributes
  you want the end system to receive.
| All changes to attributes you add to the target will cause an entity
  update.

Referring to namespace 1.1.15 to know property origin, rename, add, copy

.. _change-tracking-data-delta-1-2:

Change tracking & data delta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`All entities stored inside sesam have a
\_hash <https://docs.sesam.io/entitymodel.html?highlight=_hash>`__
value. This is a quantification of an entity and is calculated every
time an entity is processed by a pipe. If the \_hash value changes or is
new, the entity will be stored as a new version in dataset. We call this
change in \_hash value a data-delta.

Any data-delta for an entity in a dataset causes downstream pipes to see
this as a new sequence number they haven’t yet read. This in turn makes
the pipe process the entity. If the processed entity does not exist or
gets a new \_hash in the output of the pipe, it will cause an update to
the output dataset.

.. _tasks-for-architecture-and-concepts-novice-1-2:

Tasks for Architecture and Concepts: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
