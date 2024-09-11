================================
Business Nxt to Shopify Dataflow
================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to Shopify Order
----------------------------------
Every BusinessNxt Order will be synchronized with a Shopify Order.

Once a link between a BusinessNxt Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - name
     - name
     - "string"


BusinessNxt Product to Shopify Sesamproduct
-------------------------------------------
Every BusinessNxt Product will be synchronized with a Shopify Sesamproduct.

Once a link between a BusinessNxt Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
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

