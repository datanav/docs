==================================
WooCommerce to Custom CRM Dataflow
==================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Custom CRM Order
-------------------------------------
Every WooCommerce Order will be synchronized with a Custom CRM Order.

Once a link between a WooCommerce Order and a Custom CRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Custom CRM Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Custom CRM Order Property
     - Custom CRM Data Type


WooCommerce Product to Custom CRM Product
-----------------------------------------
Every WooCommerce Product will be synchronized with a Custom CRM Product.

Once a link between a WooCommerce Product and a Custom CRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Custom CRM Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Custom CRM Product Property
     - Custom CRM Data Type

