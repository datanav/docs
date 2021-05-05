.. _architecture-and-concepts-novice-1-2:

Architecture and Concepts: Novice
---------------------------------

.. _joining-data-1-2:

Joining Data
~~~~~~~~~~~~

When working with data, you will often find yourself in situations where you need to join data. By joining data you get a comprehensive representation of a data object that has relations to other isolated data objects. In general, you join data because it gives you a more complete picture of a data object and its relation to other data objects. This allows you to work more efficiently and logically when you model your data towards a target state.

In Sesam you will also experience the need for joining data, and this is a functionality Sesam excels at. To outline the different possibilities when joining data, given the two data objects "foo" and "bar", the below example will be used. It draws upon the Sesam syntax and as such is something you will be using down the road. Here goes:

.. code-block:: json

	{
	  "_id": "foo",
	  "value": 1,
	  "values": [1, 2, 4, 5]
	}
	{
	  "_id": "bar",
	  "value": 1,
	  "values": [1, 3, 4, 6]
	}

There are four different kinds of joins. In the below outline, "eq" is an abreviation for equals and "foo.value" is to denote that you search in the "foo" data object in the key "value":

- One-to-one join: ["eq", "foo.value", "bar.value"]
- One-to-many: ["eq", "foo.value", "bar.values"]
- Many-to-one: ["eq", "foo.values", "bar.value"]
- Many-to-many: ["eq", "foo.values", "bar.values"]

The rule for joins is very simple: if any of the values overlap, then the join succeeds.

All of the four joins given above succeed for the two data objects given, because they all have overlapping values, i.e. the values 1 and 4.

.. _make-namespaced-identifiers-for-foreign-keys-make-ni-1-2:

Make namespaced identifiers for foreign keys - make-ni
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _full-outer-join-merge-1-2:

Full outer Join - Merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All data from input ends up in output


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
