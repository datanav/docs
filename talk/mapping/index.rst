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

Attributes
^^^^^^^^^^

- **Organization ID:** A unique identifier for each organisation. For example: a unique organisation number
- **Name:** The name of the organisation.
- **Type:** The type or category of the organisation (e.g., corporation, non-profit, government agency).
- **Industry:** The industry or sector to which the organisation belongs.
- **Address:** The physical location or mailing address of the organisation.
- **Contact Information:** Contact details such as phone numbers, email addresses, and website URLs.
- **Hierarchy/Structure:** Information about the organisational hierarchy and structure, including parent-child relationships.
- **Registration Information:** Details related to legal registration, incorporation, or relevant certifications.
- **Size:** The size or scale of the organisation, often measured by factors like the number of employees or annual revenue.
- **Associated People:** Individuals associated with the organisation, such as employees, executives, or key contacts. See :ref:`model_association_types`.

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

Attributes
^^^^^^^^^^

- **Product ID:** A unique identifier for each product.
- **Name:** The name or title of the product.
- **Description:** A detailed description of the product, including its features and specifications.
- **Price:** The cost or value associated with the product.
- **Category:** The category or type to which the product or the service belongs.
- **Availability:** The current status of the product, indicating whether it is in stock or out of stock.
- **Manufacturer/Brand:** The company or brand that produces or provide the product.
- **SKU (Stock Keeping Unit):** A unique code used to track and manage inventory.

.. admonition:: **Examples of products**

	- A pair of shoes
	- An hourly service fee
	- A hairdryer
	- A transportation fee

.. _model_association_types:

Association types
-----------------

Todo