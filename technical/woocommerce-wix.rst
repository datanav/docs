===========================
Woocommerce to Wix Dataflow
===========================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Product to Wix Products
-----------------------------------
Every Woocommerce Product will be synchronized with a Wix Products.

Once a link between a Woocommerce Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Wix Products Property
     - Wix Data Type
   * - name
     - name
     - "string"
   * - price
     - costAndProfitData.itemCost
     - N/A
   * - sale_price
     - priceData.price
     - N/A
   * - sku
     - sku
     - "string"

