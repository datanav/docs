================================
Membercare to Chargebee Dataflow
================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companycategories to Chargebee Currency
--------------------------------------------------
Every Membercare Companycategories will be synchronized with a Chargebee Currency.

Once a link between a Membercare Companycategories and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companycategories and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Membercare Companycategories Property
     - Chargebee Currency Property
     - Chargebee Data Type


Membercare Countries to Chargebee Currency
------------------------------------------
Every Membercare Countries will be synchronized with a Chargebee Currency.

Once a link between a Membercare Countries and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Countries and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Membercare Countries Property
     - Chargebee Currency Property
     - Chargebee Data Type


Membercare Invoices to Chargebee Order
--------------------------------------
Every Membercare Invoices will be synchronized with a Chargebee Order.

Once a link between a Membercare Invoices and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - invoiceItems.description
     - order_line_items.description
     - "string"
   * - invoiceItems.quantity
     - order_line_items.amount
     - "string"
   * - invoiceItems.unitPrice
     - order_line_items.unit_price
     - "string"


Membercare Organizations to Chargebee Business_entity
-----------------------------------------------------
Every Membercare Organizations will be synchronized with a Chargebee Business_entity.

Once a link between a Membercare Organizations and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Membercare Persons to Chargebee Customer
----------------------------------------
Every Membercare Persons will be synchronized with a Chargebee Customer.

Once a link between a Membercare Persons and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - firstname
     - first_name
     - "string"
   * - lastname
     - last_name
     - "string"


Membercare Products to Chargebee Item
-------------------------------------
Every Membercare Products will be synchronized with a Chargebee Item.

Once a link between a Membercare Products and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Chargebee Item Property
     - Chargebee Data Type


Membercare Companies to Chargebee Business_entity
-------------------------------------------------
Every Membercare Companies will be synchronized with a Chargebee Business_entity.

Once a link between a Membercare Companies and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - companyName
     - name
     - "string"

