===============================
WooCommerce to Shopify Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Product to Shopify Product
--------------------------------------
Before any synchronization can take place, a link between a WooCommerce Product and a Shopify Product must be established.

A new Shopify Product will be created from a WooCommerce Product if it is connected to a WooCommerce Order that is synchronized into Shopify.

Once a link between a WooCommerce Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Shopify Product Property
     - Shopify Data Type


WooCommerce Customer to Shopify Customer
----------------------------------------
Every WooCommerce Customer will be synchronized with a Shopify Customer.

Once a link between a WooCommerce Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Shopify Customer Property
     - Shopify Data Type
   * - billing.address_1
     - default_address.address1
     - "string"
   * - billing.address_2
     - default_address.address2
     - "string"
   * - billing.city
     - default_address.city
     - "string"
   * - billing.country
     - default_address.country
     - "string"
   * - billing.postcode
     - default_address.zip
     - "string"
   * - billing.state
     - default_address.province_code
     - "string"
   * - email
     - email
     - "string"
   * - last_name
     - last_name
     - "string"
   * - shipping.address_1
     - default_address.address1
     - "string"
   * - shipping.address_2
     - default_address.address2
     - "string"
   * - shipping.city
     - default_address.city
     - "string"
   * - shipping.country
     - default_address.country
     - "string"
   * - shipping.postcode
     - default_address.zip
     - "string"
   * - shipping.state
     - default_address.province_code
     - "string"


WooCommerce Order to Shopify Order
----------------------------------
Every WooCommerce Order will be synchronized with a Shopify Order.

Once a link between a WooCommerce Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - billing.address_1
     - billing_address.address1
     - "string"
   * - billing.address_1
     - shipping_address.address1
     - "string"
   * - billing.address_2
     - billing_address.address2
     - "string"
   * - billing.address_2
     - shipping_address.address2
     - "string"
   * - billing.city
     - billing_address.city
     - "string"
   * - billing.city
     - shipping_address.city
     - "string"
   * - billing.country
     - billing_address.country
     - "string"
   * - billing.country
     - shipping_address.country
     - "string"
   * - billing.postcode
     - billing_address.zip
     - "string"
   * - billing.postcode
     - shipping_address.zip
     - "string"
   * - billing.state
     - billing_address.province_code
     - "string"
   * - billing.state
     - shipping_address.province_code
     - "string"
   * - currency
     - currency
     - "string"
   * - customer_id
     - customer.id
     - "string"
   * - line_items.name
     - line_items.title
     - "string"
   * - line_items.price
     - line_items.price
     - "string"
   * - line_items.product_id
     - line_items.product_id
     - "integer"
   * - line_items.quantity
     - line_items.quantity
     - "integer"
   * - shipping.address_1
     - billing_address.address1
     - "string"
   * - shipping.address_1
     - shipping_address.address1
     - "string"
   * - shipping.address_2
     - billing_address.address2
     - "string"
   * - shipping.address_2
     - shipping_address.address2
     - "string"
   * - shipping.city
     - billing_address.city
     - "string"
   * - shipping.city
     - shipping_address.city
     - "string"
   * - shipping.country
     - billing_address.country
     - "string"
   * - shipping.country
     - shipping_address.country
     - "string"
   * - shipping.postcode
     - billing_address.zip
     - "string"
   * - shipping.postcode
     - shipping_address.zip
     - "string"
   * - shipping.state
     - billing_address.province_code
     - "string"
   * - shipping.state
     - shipping_address.province_code
     - "string"


WooCommerce Product to Shopify Sesamproduct
-------------------------------------------
Every WooCommerce Product will be synchronized with a Shopify Sesamproduct.

Once a link between a WooCommerce Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - name
     - title
     - "string"
   * - sale_price
     - sesam_priceExclVAT
     - "string"
   * - sku
     - variants.sku
     - "string"

