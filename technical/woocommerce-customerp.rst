=================================
WooCommerce to CustomERP Dataflow
=================================

Generated: 2024-09-11 08:03:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to CustomERP. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to CustomERP Order
------------------------------------
Every WooCommerce Order will be synchronized with a CustomERP Order.

Once a link between a WooCommerce Order and a CustomERP Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a CustomERP Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - CustomERP Order Property
     - CustomERP Data Type


WooCommerce Product to CustomERP Product
----------------------------------------
Every WooCommerce Product will be synchronized with a CustomERP Product.

Once a link between a WooCommerce Product and a CustomERP Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a CustomERP Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - CustomERP Product Property
     - CustomERP Data Type

