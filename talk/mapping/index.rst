.. _mapping:

=======
Mapping
=======


Introduction
------------

Sesam Talk employs a unified global data model, encompassing diverse entity types such as humans, organizations, products, assets, and more. This model acts as a central data model, facilitating the mapping of various data before seamlessly sharing it across different systems

.. admonition:: **Examples**

    - TODO replace ERP and CRM system with an actual ERP and CRM systems for better examples.
	- A **contact** from an ERP system will be mapped in our global model as a **Human**. It will then flow to a CRM system as a **contact**.
	- A **supplier** from an ERP system will me mapped in our global model as an **organisation**. It will then flow to a CRM system as a **company**.

TODO link each type to their wikidata page

.. _model_asset:

Asset
-----

https://www.wikidata.org/wiki/Q46737

Items or resources, such as valuables, machinery, or real estate.

.. admonition:: **Examples of assets**

    - TODO qualify these examples with an actual system

.. _model_human:

Human
-----

https://www.wikidata.org/wiki/Q5

A human being, regardless of role.

.. admonition:: **Examples of humans**

    - TODO qualify these examples with an actual system
	- Contact
	- Employee
	- Customer that is a private person
	- User


.. _model_organisation:

Organisation
------------

https://www.wikidata.org/wiki/Q43229

Any type of group or association of individuals who are joined together either formally or legally.

.. admonition:: **Examples of organisations**

    - TODO qualify these examples with an actual system
	- Company
	- Supplier
	- Customer that is a business organisation
	- Department

.. _model_customer:

Customer
========
todo customer when org or human is associated with a closed deal

.. _model_product:

Product
-------

https://www.wikidata.org/wiki/Q2424752

A product is the item offered for sale. A product can be a service or an item.

.. admonition:: **Examples of products**

    - TODO this is not a list of data types but examples of instances, makes no sense
	- A pair of shoes
	- An hourly service fee
	- A hairdryer
	- A transportation fee

.. _model_agreement:

Agreement
---------

https://www.wikidata.org/wiki/Q321839

An agreement such as orders, invoices, that is intended to be enforceable by law.

.. admonition:: **Examples of agreements**

    - TODO qualify these examples with an actual system
	- A deal or a closed sale
	- A quote associated with a closed sale
	- A contract

.. _model_location:

Location
--------

https://www.wikidata.org/wiki/Q115095765

A position, place or site that something is in or where something happens.

.. admonition:: **Examples of a location**

    - TODO this is not a list of data types but examples of instances, makes no sense, we need to explain where we find locations in real life data types from real systems
	- Location ID: FR1234567
	- Name: Paris
	- Type: City
	- Geographical coordinates: 48.8566° N, 2.3522° E
	- Hierarchy: Capital city of France

.. _model_classification:

Classification
--------------

https://www.wikidata.org/wiki/Q13582682

Classification and grouping used as controlled vocabularies.

.. admonition:: **Examples of classifications**

    - TODO

.. _model_documentation:

Documentation
-------------

https://www.wikidata.org/wiki/Q788790

A permanent record of information in written, photographic, or other form.

.. admonition:: **Examples of documentation**

    - TODO

.. _model_occurrence:

Occurence
---------

https://www.wikidata.org/wiki/Q1190554

Something that occurs in a certain place during a particular interval of time.

.. admonition:: **Examples of occurences**

    - TODO

.. _model_task:

Task
----

https://www.wikidata.org/wiki/Q759676

A piece of work to be done.

.. admonition:: **Examples of tasks**

    - TODO