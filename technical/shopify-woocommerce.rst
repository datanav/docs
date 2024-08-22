====================
Shopify to  Dataflow
====================

Generated: 2024-08-22 07:43:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to  Products
----------------------------
Before any synchronization can take place, a link between a Shopify Product and a  Products must be established.

A new  Products will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into .

Once a link between a Shopify Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Products Property
     -  Data Type


Shopify Order to  Orders
------------------------
Every Shopify Order will be synchronized with a  Orders.

Once a link between a Shopify Order and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Orders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Orders Property
     -  Data Type
   * - billing_address.address1
     - billing.address_1
     - "string"
   * - billing_address.address1
     - shipping.address_1
     - "string"
   * - billing_address.address2
     - billing.address_2
     - "string"
   * - billing_address.address2
     - shipping.address_2
     - "string"
   * - billing_address.city
     - billing.city
     - "string"
   * - billing_address.city
     - shipping.city
     - "string"
   * - billing_address.country
     - billing.country
     - "string"
   * - billing_address.country
     - shipping.country
     - "string"
   * - billing_address.province_code
     - billing.state
     - "string"
   * - billing_address.province_code
     - shipping.state
     - "string"
   * - billing_address.zip
     - billing.postcode
     - "string"
   * - billing_address.zip
     - shipping.postcode
     - "string"
   * - currency
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - customer.id
     - id
     - "string"
   * - id
     - id
     - "string"
   * - line_items.price
     - line_items.price
     - "string"
   * - line_items.product_id
     - line_items.product_id
     - "string"
   * - line_items.quantity
     - line_items.quantity
     - "string"
   * - line_items.title
     - line_items.name
     - "string"
   * - shipping_address.address1
     - billing.address_1
     - "string"
   * - shipping_address.address1
     - shipping.address_1
     - "string"
   * - shipping_address.address2
     - billing.address_2
     - "string"
   * - shipping_address.address2
     - shipping.address_2
     - "string"
   * - shipping_address.city
     - billing.city
     - "string"
   * - shipping_address.city
     - shipping.city
     - "string"
   * - shipping_address.country
     - billing.country
     - "string"
   * - shipping_address.country
     - shipping.country
     - "string"
   * - shipping_address.province_code
     - billing.state
     - "string"
   * - shipping_address.province_code
     - shipping.state
     - "string"
   * - shipping_address.zip
     - billing.postcode
     - "string"
   * - shipping_address.zip
     - shipping.postcode
     - "string"


Shopify Product variant to  Products
------------------------------------
Every Shopify Product variant will be synchronized with a  Products.

Once a link between a Shopify Product variant and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product variant and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product variant Property
     -  Products Property
     -  Data Type
   * - variants.price
     - sale_price
     - "string"
   * - variants.sku
     - sku
     - "string"

