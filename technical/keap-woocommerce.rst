============================
Keap to Woocommerce Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Woocommerce Product
-----------------------------------
Every Keap Product will be synchronized with a Woocommerce Product.

Once a link between a Keap Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - product_name
     - name
     - "string"
   * - product_price
     - sale_price
     - "string"

