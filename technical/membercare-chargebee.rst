================================
MemberCare to Chargebee Dataflow
================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companycategories to Chargebee Currency
--------------------------------------------------
Every MemberCare Companycategories will be synchronized with a Chargebee Currency.

Once a link between a MemberCare Companycategories and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Chargebee Currency Property
     - Chargebee Data Type


MemberCare Countries to Chargebee Currency
------------------------------------------
Every MemberCare Countries will be synchronized with a Chargebee Currency.

Once a link between a MemberCare Countries and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Chargebee Currency Property
     - Chargebee Data Type


MemberCare Invoices to Chargebee Order
--------------------------------------
Every MemberCare Invoices will be synchronized with a Chargebee Order.

Once a link between a MemberCare Invoices and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
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


MemberCare Organizations to Chargebee Business_entity
-----------------------------------------------------
Every MemberCare Organizations will be synchronized with a Chargebee Business_entity.

Once a link between a MemberCare Organizations and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


MemberCare Persons to Chargebee Customer
----------------------------------------
Every MemberCare Persons will be synchronized with a Chargebee Customer.

Once a link between a MemberCare Persons and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - firstname
     - first_name
     - "string"
   * - lastname
     - last_name
     - "string"


MemberCare Products to Chargebee Item
-------------------------------------
Every MemberCare Products will be synchronized with a Chargebee Item.

Once a link between a MemberCare Products and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Chargebee Item Property
     - Chargebee Data Type


MemberCare Companies to Chargebee Business_entity
-------------------------------------------------
Every MemberCare Companies will be synchronized with a Chargebee Business_entity.

Once a link between a MemberCare Companies and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - companyName
     - name
     - "string"

