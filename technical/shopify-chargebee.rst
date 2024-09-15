=============================
Shopify to Chargebee Dataflow
=============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Chargebee Item
---------------------------------------
Every Shopify Inventoryitem will be synchronized with a Chargebee Item.

Once a link between a Shopify Inventoryitem and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Chargebee Item Property
     - Chargebee Data Type


Shopify Product to Chargebee Item
---------------------------------
Every Shopify Product will be synchronized with a Chargebee Item.

Once a link between a Shopify Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Chargebee Item Property
     - Chargebee Data Type


Shopify Customer to Chargebee Customer
--------------------------------------
Every Shopify Customer will be synchronized with a Chargebee Customer.

Once a link between a Shopify Customer and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - default_address.country_name
     - billing_address.country
     - "string"
   * - email
     - email
     - "string"
   * - first_name
     - first_name
     - "string"
   * - last_name
     - last_name
     - "string"


Shopify Order to Chargebee Order
--------------------------------
Every Shopify Order will be synchronized with a Chargebee Order.

Once a link between a Shopify Order and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currency
     - currency_code
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - line_items.price
     - order_line_items.unit_price
     - "string"
   * - line_items.quantity
     - order_line_items.amount
     - "string"


Shopify Sesamproduct to Chargebee Item
--------------------------------------
Every Shopify Sesamproduct will be synchronized with a Chargebee Item.

Once a link between a Shopify Sesamproduct and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - title
     - name
     - "string"

