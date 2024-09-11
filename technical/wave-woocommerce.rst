============================
Wave to WooCommerce Dataflow
============================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WaveWave Financial Invoice to WooCommerceWoocommerce Order
----------------------------------------------------------
Every WaveWave Financial Invoice will be synchronized with a WooCommerceWoocommerce Order.

Once a link between a WaveWave Financial Invoice and a WooCommerceWoocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Invoice and a WooCommerceWoocommerce Order:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Invoice Property
     - WooCommerceWoocommerce Order Property
     - WooCommerceWoocommerce Data Type
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - items.price
     - line_items.price
     - "string"
   * - items.quantity
     - line_items.quantity
     - "string"


WaveWave Financial Product to WooCommerceWoocommerce Product
------------------------------------------------------------
Every WaveWave Financial Product will be synchronized with a WooCommerceWoocommerce Product.

Once a link between a WaveWave Financial Product and a WooCommerceWoocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Product and a WooCommerceWoocommerce Product:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Product Property
     - WooCommerceWoocommerce Product Property
     - WooCommerceWoocommerce Data Type
   * - name
     - name
     - "string"
   * - unitPrice
     - sale_price
     - "string"

