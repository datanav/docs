========================================
WooCommerce to Business Central Dataflow
========================================

Generated: 2024-09-21 00:00:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Business Central Customers (organisation data)
----------------------------------------------------------------------
Every WooCommerce Customer will be synchronized with a Business Central Customers (organisation data).

Once a link between a WooCommerce Customer and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


WooCommerce Customer to Business Central Customers (human data)
---------------------------------------------------------------
Every WooCommerce Customer will be synchronized with a Business Central Customers (human data).

Once a link between a WooCommerce Customer and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
   * - email
     - email
     - "string"


WooCommerce Order to Business Central Salesorderlines
-----------------------------------------------------
Every WooCommerce Order will be synchronized with a Business Central Salesorderlines.

Once a link between a WooCommerce Order and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


WooCommerce Order to Business Central Salesorders
-------------------------------------------------
Every WooCommerce Order will be synchronized with a Business Central Salesorders.

Once a link between a WooCommerce Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Central Salesorders Property
     - Business Central Data Type


WooCommerce Product to Business Central Items
---------------------------------------------
Every WooCommerce Product will be synchronized with a Business Central Items.

Once a link between a WooCommerce Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"
   * - price
     - unitCost
     - N/A
   * - sale_price
     - unitPrice
     - N/A

