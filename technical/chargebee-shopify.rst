=============================
Chargebee to Shopify Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Shopify Customer
--------------------------------------
Every Chargebee Customer will be synchronized with a Shopify Customer.

Once a link between a Chargebee Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Shopify Customer Property
     - Shopify Data Type
   * - email
     - email
     - "string"
   * - first_name
     - first_name
     - "string"
   * - last_name
     - last_name
     - "string"


Chargebee Item to Shopify Sesamproduct
--------------------------------------
Every Chargebee Item will be synchronized with a Shopify Sesamproduct.

Once a link between a Chargebee Item and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Shopify Sesamproduct Property
     - Shopify Data Type


Chargebee Order to Shopify Order
--------------------------------
Every Chargebee Order will be synchronized with a Shopify Order.

Once a link between a Chargebee Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - currency_code
     - currency
     - "string"
   * - customer_id
     - customer.id
     - "string"
   * - order_line_items.amount
     - line_items.quantity
     - "integer"
   * - order_line_items.unit_price
     - line_items.price
     - "string"

