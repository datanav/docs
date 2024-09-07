==========================
Shopify to Webcrm Dataflow
==========================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Order to Webcrm Quotationline
-------------------------------------
Every Shopify Order will be synchronized with a Webcrm Quotationline.

Once a link between a Shopify Order and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - line_items.price
     - QuotationLinePrice
     - "string"
   * - line_items.quantity
     - QuotationLineQuantity
     - "string"
   * - line_items.total_discount
     - QuotationLineDiscount
     - "string"


Shopify Sesamproduct to Webcrm Products
---------------------------------------
Every Shopify Sesamproduct will be synchronized with a Webcrm Products.

Once a link between a Shopify Sesamproduct and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - sesam_priceExclVAT
     - ProductPrice
     - "string"
   * - variants.inventory_quantity
     - ProductQuantity
     - "string"

