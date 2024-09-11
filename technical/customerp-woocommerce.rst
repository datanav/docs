=================================
CustomERP to WooCommerce Dataflow
=================================

Generated: 2024-09-11 08:02:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomERP to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomERP Order to WooCommerce Order
------------------------------------
Every CustomERP Order will be synchronized with a WooCommerce Order.

Once a link between a CustomERP Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomERP Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - CustomERP Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type


CustomERP Product to WooCommerce Product
----------------------------------------
Every CustomERP Product will be synchronized with a WooCommerce Product.

Once a link between a CustomERP Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomERP Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - CustomERP Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type

