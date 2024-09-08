==========================
Webcrm to Shopify Dataflow
==========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Products to Shopify Sesamproduct
---------------------------------------
Every Webcrm Products will be synchronized with a Shopify Sesamproduct.

Once a link between a Webcrm Products and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - ProductPrice
     - sesam_priceExclVAT
     - "string"
   * - ProductQuantity
     - variants.inventory_quantity
     - "integer"

