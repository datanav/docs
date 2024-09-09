============================
Woocommerce to Keap Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Product to Keap Product
-----------------------------------
Every Woocommerce Product will be synchronized with a Keap Product.

Once a link between a Woocommerce Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Keap Product Property
     - Keap Data Type
   * - name
     - product_name
     - "string"
   * - sale_price
     - product_price
     - "string"

