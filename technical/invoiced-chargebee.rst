==============================
Invoiced to Chargebee Dataflow
==============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Chargebee Business_entity
-------------------------------------------------------
Every Invoiced Customers company will be synchronized with a Chargebee Business_entity.

Once a link between a Invoiced Customers company and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Invoiced Lineitem to Chargebee Order
------------------------------------
Every Invoiced Lineitem will be synchronized with a Chargebee Order.

Once a link between a Invoiced Lineitem and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - items.amount
     - order_line_items.unit_price
     - "string"
   * - items.description
     - order_line_items.description
     - "string"
   * - items.quantity
     - order_line_items.amount
     - "string"


Invoiced Customers person to Chargebee Customer
-----------------------------------------------
Every Invoiced Customers person will be synchronized with a Chargebee Customer.

Once a link between a Invoiced Customers person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Chargebee Customer Property
     - Chargebee Data Type


Invoiced Invoices to Chargebee Order
------------------------------------
Every Invoiced Invoices will be synchronized with a Chargebee Order.

Once a link between a Invoiced Invoices and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currency
     - currency_code
     - "string"
   * - customer
     - customer_id
     - "string"


Invoiced Items to Chargebee Item
--------------------------------
Every Invoiced Items will be synchronized with a Chargebee Item.

Once a link between a Invoiced Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Chargebee Item Property
     - Chargebee Data Type

