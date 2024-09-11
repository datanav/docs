=============================
CustomERP to Shopify Dataflow
=============================

Generated: 2024-09-11 08:00:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomERP to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Order to Shopify Order
-----------------------------
Every Custom Order will be synchronized with a Shopify Order.

Once a link between a Custom Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Custom Order Property
     - Shopify Order Property
     - Shopify Data Type


Custom Product to Shopify Sesamproduct
--------------------------------------
Every Custom Product will be synchronized with a Shopify Sesamproduct.

Once a link between a Custom Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Custom Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

