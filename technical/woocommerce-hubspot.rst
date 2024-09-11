===============================
WooCommerce to Hubspot Dataflow
===============================

Generated: 2024-09-11 07:46:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Hubspot Lineitem
-------------------------------------
Every WooCommerce Order will be synchronized with a Hubspot Lineitem.

Once a link between a WooCommerce Order and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - line_items.name
     - properties.name
     - "string"
   * - line_items.price
     - properties.price
     - "string"
   * - line_items.quantity
     - properties.quantity
     - N/A


WooCommerce Product to Hubspot Product
--------------------------------------
Every WooCommerce Product will be synchronized with a Hubspot Product.

Once a link between a WooCommerce Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - name
     - properties.name
     - "string"
   * - price
     - properties.hs_cost_of_goods_sold
     - "string"
   * - sale_price
     - properties.price
     - "string"
   * - sku
     - properties.hs_sku
     - "string"

