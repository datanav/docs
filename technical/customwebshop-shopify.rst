=================================
CustomWebshop to Shopify Dataflow
=================================

Generated: 2024-09-11 07:55:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomWebshop to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomWebshop Order to Shopify Order
------------------------------------
Every CustomWebshop Order will be synchronized with a Shopify Order.

Once a link between a CustomWebshop Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomWebshop Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - CustomWebshop Order Property
     - Shopify Order Property
     - Shopify Data Type


CustomWebshop Product to Shopify Sesamproduct
---------------------------------------------
Every CustomWebshop Product will be synchronized with a Shopify Sesamproduct.

Once a link between a CustomWebshop Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomWebshop Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - CustomWebshop Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

