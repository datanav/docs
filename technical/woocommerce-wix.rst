===========================
WooCommerce to Wix Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Wix Currencies
-----------------------------------
Every WooCommerce Order will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the WooCommerce Order will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A WooCommerce Order will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wix Currencies Property
   * - currency
     - code

Once a link between a WooCommerce Order and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wix Currencies Property
     - Wix Data Type


WooCommerce Order to Wix Orders
-------------------------------
Every WooCommerce Order will be synchronized with a Wix Orders.

Once a link between a WooCommerce Order and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wix Orders Property
     - Wix Data Type


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

