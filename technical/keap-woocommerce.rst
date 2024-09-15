============================
Keap to WooCommerce Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to WooCommerce Product
-----------------------------------
Every Keap Product will be synchronized with a WooCommerce Product.

Once a link between a Keap Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - product_name
     - name
     - "string"
   * - product_price
     - sale_price
     - "string"

