=============================
Shopify to Customerp Dataflow
=============================

Generated: 2024-09-10 14:20:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Customerp. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Order to Customerp Order
--------------------------------
Every Shopify Order will be synchronized with a Customerp Order.

Once a link between a Shopify Order and a Customerp Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Customerp Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Customerp Order Property
     - Customerp Data Type


Shopify Sesamproduct to Customerp Product
-----------------------------------------
Every Shopify Sesamproduct will be synchronized with a Customerp Product.

Once a link between a Shopify Sesamproduct and a Customerp Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Customerp Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Customerp Product Property
     - Customerp Data Type

