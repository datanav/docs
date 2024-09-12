==========================
WebCRM to Shopify Dataflow
==========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Products to Shopify Sesamproduct
---------------------------------------
Every WebCRM Products will be synchronized with a Shopify Sesamproduct.

Once a link between a WebCRM Products and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - ProductPrice
     - sesam_priceExclVAT
     - "string"
   * - ProductQuantity
     - variants.inventory_quantity
     - "integer"

