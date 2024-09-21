===========================
WooCommerce to Wix Dataflow
===========================

Generated: 2024-09-21 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Product to Wix Products
-----------------------------------
Every WooCommerce Product will be synchronized with a Wix Products.

Once a link between a WooCommerce Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
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

