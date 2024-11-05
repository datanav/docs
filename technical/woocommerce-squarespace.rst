========================
WooCommerce to  Dataflow
========================

Generated: 2024-11-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Product to  Inventory
---------------------------------
Every WooCommerce Product will be synchronized with a  Inventory.

Once a link between a WooCommerce Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     -  Inventory Property
     -  Data Type


WooCommerce Order to  Order
---------------------------
Every WooCommerce Order will be synchronized with a  Order.

Once a link between a WooCommerce Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a  Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     -  Order Property
     -  Data Type


WooCommerce Product to  Inventory
---------------------------------
Every WooCommerce Product will be synchronized with a  Inventory.

Once a link between a WooCommerce Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     -  Inventory Property
     -  Data Type
   * - sku
     - sku
     - "string"


WooCommerce Product to  Sesamproducts
-------------------------------------
Every WooCommerce Product will be synchronized with a  Sesamproducts.

Once a link between a WooCommerce Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     -  Sesamproducts Property
     -  Data Type
   * - name
     - name
     - "string"
   * - price
     - variants.pricing.basePrice.value
     - "string"
   * - sale_price
     - variants.pricing.salePrice.value
     - "string"
   * - sku
     - variants.sku
     - "string"

