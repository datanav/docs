===============================
Shopify to WooCommerce Dataflow
===============================

Generated: 2024-09-24 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Order to WooCommerce Order
----------------------------------
Every Shopify Order will be synchronized with a WooCommerce Order.

Once a link between a Shopify Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type


Shopify Sesamproduct to WooCommerce Product
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a WooCommerce Product.

Once a link between a Shopify Sesamproduct and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - sesam_priceExclVAT
     - sale_price
     - "string"
   * - title
     - name
     - "string"
   * - variants.sku
     - sku
     - "string"

