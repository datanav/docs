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

Continuing along the lines of joining data, namespaced identifiers (NIs) come into play. NIs in Sesam are used to reference an identifier or a NI in a related dataset. In order to create them, you can use either of the two functions: ["make-ni"] or ["ni"].

In the below example, ["make-ni"] will be used. A NI in Sesam works like a foreign key in a relational database. As such, it shows the relation between data objects and enables the joining of these. The pipe config presented in the below example, shows exactly this:  

.. code-block:: json

	{
	  "_id": "mssql-accounts",
	  "type": "pipe",
	  "source": {
	    "type": "sql",
	    "system": "sesam-training",
	    "table": "accounts"
	  },
	  "transform": {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["copy", "*"],
	        ["add", "rdf:type",
	          ["ni", "mssql-accounts", "accounts"]
	        ],
	        ["make-ni", "mssql-contacts", "phone"]
	      ]
	    }
	  }
	}

and will result in the following dataset when run. For the purpose of spacing, only one entity is shown:

.. code-block:: json

	{
	  "mssql-accounts:country": "DK",
	  "mssql-accounts:id": 40,
	  "mssql-accounts:phone": "1-894-115-3398",
	  "mssql-accounts:phone-ni": "~:mssql-contacts:1-894-115-3398",
	  "mssql-accounts:position": "CEO",
	  "rdf:type": "~:mssql-accounts:accounts"
	}


As can be seen in the above dataset, the property with the key "mssql-accounts:phone-ni" is the result of the function ["make-ni"] as defined in the above pipe config. The value can be used to join data between the pipes "mssql-accounts" and "mssql-contacts" so that data can be merged to create complete representations of a related set of data objects. In Sesam, a merge is typically done on different datasets in the global stage of data modelling.

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

In addition to a full outer join it is also relevant to talk about the left join. This is because you in the Sesam terminology will use something we call "hops". The hops is similar to a left join, in that it appends data and returns data even if there are no matches for a particular entry in the join. As such, in cases where you append data, null values in Sesam are retained. A graphical representation of the left join can be viewed in the below figure:

.. figure:: ./media/Left_Join.png
   :align: center
   :alt: Figure – Left Join

   Figure – Left Join

To illustrate the graphical representation of a left join, the following practical example has been drafted:

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
	{			
	  "_id": "third_entity:the_runt",
	  "third_entity:value": 1,
	  "third_entity:string":"Third's the charm"
	}

When applying the hops, our point of reference will be the first data object from the above and we will name the new property "left_join_result". We will choose to join the data on the "value" property present in all of the above three data objects in order to return the "values" property. Albeit, the "values" property is only present on the first two data objects. The expected result can be seen below:

.. code-block:: json

	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5],
	  "first_entity:left_join_result": [{"second_entity:values": [1, 3, 4, 6], null}]
	}

As stated earlier, it is important to note that in this case, null values will be returned if the hops is not possible between individual data objects, which can be seen in the new property "left_join_result", where the last entry is null.  

.. _global-1-2:

Global
~~~~~~

Golden – the best truth about common attributes of a concept collected
from multiple sources

Coalesce, prioritization of source data (master data)


.. _guidelines-inbound-and-outbound-pipes-1-2:

Guidelines - inbound and outbound pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As established above, an important aspect when modelling data in Sesam is the use of globals. Albeit before reaching the global stage and after completion of the global stage, when modelling your data the following guidelines apply:

Inbound pipes
#####################

As data enters Sesam it is handled in inbound pipes. An inbound pipe should be as generic as possible with regards to the amount of shaping done on the data that flows through to its dataset. The reason being, in order for you to make the best possible modelling decisions downstream, you should look at the "raw" data first to get a complete understanding of the condition of the data. In addition, we want to assume as little as possible about how the data will be used by current and future recipients. Therefore,
if we start shaping and customizing data too soon in the flow, it's much harder, if not impossible, to reuse the data for different purposes later. A rule of thumb is therefore to minimize the amount of DTL used in an inbound pipe and try to just copy everything, or close to everything. Special cases can occur when you need to do some shaping of the data before reaching the global stage. In such cases, you should aim at making the minimal required DTL changes in order for the data to retain as much of its original integrity as possible.

Outbound pipes
######################

Following the flow of data as it leaves the global stage of modelling, the amount of DTL will increase in the preparation pipes. As you might recall, preparation pipes deliver data to the outbound pipes. It is therefore important to consider the state of the data as it enters an outbound pipe. The reason for this being, as with any inbound pipe, that you should aim at minimizing the amount of DTL needed to shape your data further. This will create robust consumable data that can be delivered seamlessly to your target systems as data flows through your outbound pipes. As with inbound pipes, special cases can occur, where you need to do some additional shaping before the data can be presented in a consumable shape for a given target system. Again, aim at making a minimal set of DTL changes. 

Summary
#######

The amount of DTL in a given pipe with respect to modelling stage in Sesam should increase until the point of modelling stage, where the intent of shaping data is primarily due to target system requirements, as visualized in the below *Figure - DTL Amount*. 

.. figure:: ./media/dtl-amount.png
   :align: center

   Figure – DTL Amount


.. _filter-entities-on-the-way-out-1-2:

Filter entities on the way out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filtering entities after the global stage of modelling is a common use case. Filtering gives the ability to work with subsets of a dataset. It is therefore often used when working on large datasets where you are only interested in a small section of the data. In addition, filtering is often used in outbound pipes as well. This is due to the fact that *_deleted* entities are processed continously as data flows through Sesam and do rarely leave Sesam when first introduced. The *_deleted* property is used in Sesam to flag whether an entity is deleted or not. As such an entity which is deleted will have the property: ``{"_deleted": true},`` whilst an entity that is not deleted will have the property: ``{"_deleted": false}.`` Additionally, *_deleted* entities are not usually something you would like to send to a target system. This is obviously not always the case, but in general that is how things tend to work.

Imagine you are working on a large dataset produced by a global pipe. You quickly recognize that the amount of data and all its properties is not that relevant to you. Therefore, one of the first things you do is to apply a filter on a specific key and value. This leaves you with a subset of the complete data. As you look closely at the state of the data, after having applied your first filter, you are not immediately satisfied. This makes you apply another filter to alter the state of the data further. Therefore, you decide to add a specific property given a specific condition; i.e., if the entity is of type: "Employee" - add properties "Salary", "Position" and "Goals". Finally, if it is not of type "Employee" apply a filter to exclude that entity. As illustrated, it is not unusual to use multiple filters in a DTL config, especially when the amount of DTL increases, and a need for stepwise filtering presents itself. 


.. _tag-your-entities-categorization-of-sub-concepts-1-2:

Tag your entities - Categorization of sub-concepts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extra:type - usually added into the globals to separate what entities about the same thing do & mean.

.. _customize-data-structure-for-endpoints-1-2:

Customize data structure for outbound flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An *outbound* dataflow consists of all pipes downstream from a global pipe. In these outbound dataflows it is typically necessary to transform your data so that it aligns with the schema that your target system requires for consumption. Typical functions used when transforming data in the outbound stage could be: ``["add"], ["remove"], ["rename"], ["copy"].``

As an example, the data presented below is produced by the pipe "global-person":

.. code-block:: json

	{
	  "global-person:country": "DK",
	  "global-person:id": 40,
	  "global-person:phone": "1-894-115-3398",
	  "global-person:position": "Engineer",
	  "crm-account:positions": ["Engineer", "Salesmanager", "Accountant", "CTO"],
	  "crm-account:hobbies": "Builds LEGO"
	}   

The shape of the data does not immediately satisfy your needs, as you are only interested in working with the properties whose key starts with the namespace "global-person:". To solve this you choose to use the copy function where you can define what namespaces you are interested in. In DTL this would be written as ``["copy", "global-person:*"]`` and would produce the following data:

.. code-block:: json

	{
	  "global-person:country": "DK",
	  "global-person:id": 40,
	  "global-person:phone": "1-894-115-3398",
	  "global-person:position": "Engineer"
	} 

After comparing the current shape of your data to the target system schema, you realize only the properties "id", "phone" and "position" are needed. In addition, you recognize that the first letter of the keys must be in capital. To solve this in DTL, you would do the following: ``["remove", "country"]`` and ``["rename", "phone", "Phone"]``, ``["rename", "id", "Id"]``, ``["rename", "position", "Position"].`` Based on the declared DTL functions, this would produce the following:

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

1. *Why is it important to remember to filter on _deleted entities in an outbound pipe?*
