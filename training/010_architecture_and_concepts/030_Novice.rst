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

.. _customize-data-structure-for-outbound-flow-1-2:

Customize data structure for outbound flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When data moves through Sesam in a dataflow from inbound towards the outbound stage of data modelling, it is typically necessary to transform your data so that it aligns to the schema your target system requires for consumption. Typical functions used when modelling data in the outbound stage could be: ``["add"], ["remove"], ["rename"], ["copy"].``

As an example, the below data is produced by the global pipe named "global-person":

.. code-block:: json

	{
	  "global-person:country": "DK",
	  "global-person:id": 40,
	  "global-person:phone": "1-894-115-3398",
	  "global-person:position": "Engineer",
	  "mssql-accounts:positions": ["Engineer", "Salesmanager", "Accountant", "CTO"],
	  "mssql-accounts:hobbies": "Builds LEGO"
	}   

The shape of the data does not immediately satisfy your needs, as you are only interested in working with the properties whose key starts with the namespace "global-person:". To solve this you choose to use the copy function where you can define what namespaces you are interested in. This would in DTL look like the following: ``["copy", "global-person:*"]`` and would produce the following data:

.. code-block:: json

	{
	  "global-person:country": "DK",
	  "global-person:id": 40,
	  "global-person:phone": "1-894-115-3398",
	  "global-person:position": "Engineer"
	} 

After looking at the current shape and what your target system requires, you realise that you only need to pass on the properties "position", "id" and "phone". In addition, you recognize that the first letter of the keys must be in capital. To solve this in DTL, you would do the following: ``["remove", "country"]`` and ``["rename", "phone", "Phone"]``, ``["rename", "id", "Id"]``, ``["rename", "position", "Position"].`` Based on the declared DTL functions, this would produce the following:

.. code-block:: json

	{
	  "global-person:Id": 40,
	  "global-person:Phone": "1-894-115-3398",
	  "global-person:Position": "Engineer"
	} 

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
