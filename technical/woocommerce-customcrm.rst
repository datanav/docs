=================================
WooCommerce to CustomCRM Dataflow
=================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to CustomCRM Order
------------------------------------
Every WooCommerce Order will be synchronized with a CustomCRM Order.

Once a link between a WooCommerce Order and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - CustomCRM Order Property
     - CustomCRM Data Type


WooCommerce Product to CustomCRM Product
----------------------------------------
Every WooCommerce Product will be synchronized with a CustomCRM Product.

Once a link between a WooCommerce Product and a CustomCRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a CustomCRM Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - CustomCRM Product Property
     - CustomCRM Data Type

