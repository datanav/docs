==============================
Custom CRM to Shopify Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom CRM to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom CRM Order to Shopify Order
---------------------------------
Every Custom CRM Order will be synchronized with a Shopify Order.

Once a link between a Custom CRM Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom CRM Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Custom CRM Order Property
     - Shopify Order Property
     - Shopify Data Type


Custom CRM Product to Shopify Sesamproduct
------------------------------------------
Every Custom CRM Product will be synchronized with a Shopify Sesamproduct.

Once a link between a Custom CRM Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom CRM Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Custom CRM Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

