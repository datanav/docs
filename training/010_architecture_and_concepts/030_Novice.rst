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

Global datasets lie at the heart of a well managed Sesam architecture. They are created by global pipes and often consist of aggregated data from several different sources enabling a higher level of semantic structure to a Sesam node. A global dataset is your "one place to go" to find all the data related to a specific concept.

Creating global datasets allows you to:

- 	Semantically group and structure data
		A semantic grouping of the data makes the data itself easier to understand and more intuitive to work with, both in terms of existing architecture and new projects. For existing architectures, separating your data into relatable and recognizable structures allows for more efficient support and error handling. To have all raw source data related to a concept (ie. customer data) directly upstream from a pipe substantially decreases the time you need to localize and to correct a potential issue. 
		Semantic grouping also makes your Sesam architecture more scalable and results in fewer active connections over time.   

-	Setup master data management - Golden records
		One effect of global datasets is the ability to perform active master data management through setting golden records. Golden records are where Sesam architectures may localize and prioritize their master data in order to create a flexible system-wide model. Through golden records you may prioritize which system knows a specific type of data best, which system knows it second best and so on. By ordering systems based on their quality of data for a specific data type Sesam may ensure the highest quality of data possible. Another benefit of golden records are their reusability. Once their logic has been created a golden record may be used by any project downstream from its global dataset, thus saving both time and energy.

		Golden records are created with the ``["coalesce"]`` function, as shown in the example below.



	A global pipe, "global-person", has three source datasets, crm-person, hr-person and economy-person. The crm-person dataset has high quality work experience data and medium quality hours logged data. The hr-person dataset has high quality personal information and the economy-person dataset has high quality hours logged data. In our global pipe "global-person" we wish to set 3 golden records: email, weekly-hours-billed and hours-pr-project. By using the "coalesce" function we may specify which source dataset has the master data for which specific variable.

	For example we might assume that hr-person should be master for "email", crm-person should be master for "hours-pr-project" and economy-person should be master for weeky-hours-billed. This may be setup by the following logic:

.. code-block:: json
  :linenos:

  ["add", "email",
    ["coalesce",
      ["list", "_S.hr-person:email", "_S.crm-person:Email", "_S.economy-person:e-mail"]
    ]
  ]

In this case, all three source datasets have an email property. If the email property from hr-person is not null it will be used for our global property. If it is null then the Email property from crm-person will be evaluated, and so on. 

.. code-block:: json
  :linenos:	

  ["add", "hours-pr-project",
    ["coalesce",
      ["list", "_S.crm-person:hours-pr-project", "_S.economy-person:hours-pr-project"]
  ]


  ["add", "weekly-hours-billed",
    ["coalesce",
      ["list", "_S.economy-person:weekly-hours-billed", "_S.crm-person:weekly-hours-billed"]
    ]
  ] 

The dataset hr-person does not contain any data regarding "hours-pr-project" or "weekly-hours-billed" and can therefore be left out of the prioritations. 


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
