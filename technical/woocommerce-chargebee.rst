=================================
Woocommerce to Chargebee Dataflow
=================================

Generated: 2024-09-03 08:55:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to  Customer
---------------------------------
Every Woocommerce Customer will be synchronized with a  Customer.

Once a link between a Woocommerce Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     -  Customer Property
     -  Data Type
   * - billing.address_1
     - billing_address.line1
     - "string"
   * - billing.city
     - billing_address.city
     - "string"
   * - billing.country
     - billing_address.country
     - "string"
   * - billing.postcode
     - billing_address.zip
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - last_name
     - "string"
   * - shipping.address_1
     - billing_address.line1
     - "string"
   * - shipping.city
     - billing_address.city
     - "string"
   * - shipping.country
     - billing_address.country
     - "string"
   * - shipping.postcode
     - billing_address.zip
     - "string"


Woocommerce Order to  Order
---------------------------
Every Woocommerce Order will be synchronized with a  Order.

Once a link between a Woocommerce Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Order Property
     -  Data Type
   * - currency
     - currency_code
     - "string"
   * - customer_id
     - customer_id
     - "string"
   * - line_items.price
     - order_line_items.unit_price
     - "string"
   * - line_items.quantity
     - order_line_items.amount
     - "string"


Woocommerce Product to  Item
----------------------------
Every Woocommerce Product will be synchronized with a  Item.

Once a link between a Woocommerce Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a  Item:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     -  Item Property
     -  Data Type

