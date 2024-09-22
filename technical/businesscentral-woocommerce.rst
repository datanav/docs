========================================
Business Central to WooCommerce Dataflow
========================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Items to WooCommerce Product
---------------------------------------------
Every Business Central Items will be synchronized with a WooCommerce Product.

Once a link between a Business Central Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - displayName
     - name
     - "string"
   * - unitCost
     - price
     - "string"
   * - unitPrice
     - sale_price
     - "string"


Business Central Salesorders to WooCommerce Order
-------------------------------------------------
Every Business Central Salesorders will be synchronized with a WooCommerce Order.

Once a link between a Business Central Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type

