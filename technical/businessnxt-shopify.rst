===============================
BusinessNxt to Shopify Dataflow
===============================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Order to Shopify Order
----------------------------
Every Visma Order will be synchronized with a Shopify Order.

Once a link between a Visma Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - name
     - name
     - "string"


Visma Product to Shopify Sesamproduct
-------------------------------------
Every Visma Product will be synchronized with a Shopify Sesamproduct.

Once a link between a Visma Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - description
     - variants.title
     - "string"
   * - priceQuantity
     - sesam_priceExclVAT
     - "string"
   * - quantityPerUnit
     - variants.inventory_quantity
     - "integer"

