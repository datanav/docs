==========================
Wave to Chargebee Dataflow
==========================

Generated: 2024-11-11 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Chargebee Business_entity
------------------------------------------
Every Wave Customer will be synchronized with a Chargebee Business_entity.

Once a link between a Wave Customer and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Wave Customer (human data) to Chargebee Customer
------------------------------------------------
Every Wave Customer (human data) will be synchronized with a Chargebee Customer.

Once a link between a Wave Customer (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type


Wave Invoice to Chargebee Order
-------------------------------
Every Wave Invoice will be synchronized with a Chargebee Order.

Once a link between a Wave Invoice and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currency.code
     - currency_code
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - items.description
     - order_line_items.description
     - "string"
   * - items.price
     - order_line_items.unit_price
     - "string"
   * - items.quantity
     - order_line_items.amount
     - "string"


Wave Product to Chargebee Item
------------------------------
Every Wave Product will be synchronized with a Chargebee Item.

Once a link between a Wave Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Chargebee Item Property
     - Chargebee Data Type


Wave Customer to Chargebee Address
----------------------------------
Every Wave Customer will be synchronized with a Chargebee Address.

Once a link between a Wave Customer and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Chargebee Address Property
     - Chargebee Data Type


Wave Customer to Chargebee Customer
-----------------------------------
Every Wave Customer will be synchronized with a Chargebee Customer.

Once a link between a Wave Customer and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Chargebee Customer Property
     - Chargebee Data Type


Wave Customer (location data) to Chargebee Address
--------------------------------------------------
Every Wave Customer (location data) will be synchronized with a Chargebee Address.

Once a link between a Wave Customer (location data) and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (location data) and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer (location data) Property
     - Chargebee Address Property
     - Chargebee Data Type


Wave Customer (human data) to Chargebee Customer
------------------------------------------------
Every Wave Customer (human data) will be synchronized with a Chargebee Customer.

Once a link between a Wave Customer (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Wave Invoice to Chargebee Order
-------------------------------
Every Wave Invoice will be synchronized with a Chargebee Order.

Once a link between a Wave Invoice and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Chargebee Order Property
     - Chargebee Data Type


Wave Product to Chargebee Item
------------------------------
Every Wave Product will be synchronized with a Chargebee Item.

Once a link between a Wave Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Chargebee Item Property
     - Chargebee Data Type

