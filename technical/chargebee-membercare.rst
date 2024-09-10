================================
Chargebee to Membercare Dataflow
================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Currency to Membercare Companycategories
--------------------------------------------------
Every Chargebee Currency will be synchronized with a Membercare Companycategories.

Once a link between a Chargebee Currency and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - Membercare Companycategories Property
     - Membercare Data Type


Chargebee Customer to Membercare Persons
----------------------------------------
Every Chargebee Customer will be synchronized with a Membercare Persons.

Once a link between a Chargebee Customer and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Membercare Persons Property
     - Membercare Data Type
   * - first_name
     - firstname
     - "string"
   * - last_name
     - lastname
     - "string"


Chargebee Item to Membercare Products
-------------------------------------
Every Chargebee Item will be synchronized with a Membercare Products.

Once a link between a Chargebee Item and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Membercare Products Property
     - Membercare Data Type


Chargebee Item_family to Membercare Companycategories
-----------------------------------------------------
Every Chargebee Item_family will be synchronized with a Membercare Companycategories.

Once a link between a Chargebee Item_family and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Membercare Companycategories Property
     - Membercare Data Type


Chargebee Order to Membercare Invoices
--------------------------------------
Every Chargebee Order will be synchronized with a Membercare Invoices.

Once a link between a Chargebee Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - order_line_items.amount
     - invoiceItems.quantity
     - "string"
   * - order_line_items.description
     - invoiceItems.description
     - "string"
   * - order_line_items.unit_price
     - invoiceItems.unitPrice
     - "string"


Chargebee Address to Membercare Countries
-----------------------------------------
Every Chargebee Address will be synchronized with a Membercare Countries.

Once a link between a Chargebee Address and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Membercare Countries Property
     - Membercare Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to Membercare Companies
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Membercare Companies.

Once a link between a Chargebee Business_entity and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Chargebee Customer to Membercare Countries
------------------------------------------
Every Chargebee Customer will be synchronized with a Membercare Countries.

Once a link between a Chargebee Customer and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billing_address.country
     - name
     - "string"

