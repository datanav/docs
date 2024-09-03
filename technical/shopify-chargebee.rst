=============================
Shopify to Chargebee Dataflow
=============================

Generated: 2024-09-03 08:55:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to  Item
------------------------------
Every Shopify Inventoryitem will be synchronized with a  Item.

Once a link between a Shopify Inventoryitem and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Item:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Item Property
     -  Data Type


Shopify Product to  Item
------------------------
Every Shopify Product will be synchronized with a  Item.

Once a link between a Shopify Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Item:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Item Property
     -  Data Type


Shopify Customer to  Customer
-----------------------------
Every Shopify Customer will be synchronized with a  Customer.

Once a link between a Shopify Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Customer Property
     -  Data Type
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


Shopify Order to  Order
-----------------------
Every Shopify Order will be synchronized with a  Order.

Once a link between a Shopify Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Order Property
     -  Data Type
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


Shopify Sesamproduct to  Item
-----------------------------
Every Shopify Sesamproduct will be synchronized with a  Item.

Once a link between a Shopify Sesamproduct and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Item:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Item Property
     -  Data Type
   * - title
     - name
     - "string"

