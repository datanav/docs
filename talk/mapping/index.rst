.. _mapping:

=======
Mapping
=======


Introduction
------------

Sesam Talk employs a unified global data model, encompassing diverse entity types such as humans, organizations, products, assets, and more. This model acts as a central data model, facilitating the mapping of various data before seamlessly sharing it across different systems

.. admonition:: **Examples**

	- A **contact** from an ERP system will be mapped in our global model as a **Human**. It will then flow to a CRM system as a **contact**.
	- A **supplier** from an ERP system will me mapped in our global model as an **organisation**. It will then flow to a CRM system as a **company**.


.. _model_human:

Human
-----
A **human** typically refers to individual entities, representing people within the system. This data type may include information such as personal details, phone numbers, emails, roles, and other relevant attributes associated with individuals.

.. admonition:: **Examples of humans**

	- Contact
	- Employee
	- Customer that is a private person
	- User


.. _model_organisations:

Organisations
-------------

An **organization** refers to an entity that represents a business entity or a structured group of business entities. This entity type includes information such as the organisation's name, contact details, and other relevant attributes that help define and characterise the entity within the system.

.. admonition:: **Examples of organisations**

	- Company
	- Supplier
	- Customer that is a business organisation
	- Department

.. _model_customer:

Customer??
==========
todo customer when org has a closed deal

.. _model_products:

Products
--------

A **Product** is a representation of an item, or a service that can be bought, sold, or used. The entity encapsulates various attributes and characteristics that describe the item, providing a structured way to organise and manage information about products within a system. 

.. admonition:: **Examples of products**

	- A pair of shoes
	- An hourly service fee
	- A hairdryer
	- A transportation fee

Agreement
---------

An **agreement** is a representation of a formal understanding, contract, or arrangement between parties.

.. admonition:: **Examples of agreements**

	- A deal or a closed sale
	- A quote associated with a closed sale
	- A contract

	