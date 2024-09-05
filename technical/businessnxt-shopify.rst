===============================
Businessnxt to Shopify Dataflow
===============================

Generated: 2024-09-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Order to Shopify Order
----------------------------------
Every Businessnxt Order will be synchronized with a Shopify Order.

Once a link between a Businessnxt Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - name
     - name
     - "string"


Businessnxt Product to Shopify Sesamproduct
-------------------------------------------
Every Businessnxt Product will be synchronized with a Shopify Sesamproduct.

Once a link between a Businessnxt Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
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

