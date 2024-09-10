==============================
Woocommerce to Webcrm Dataflow
==============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Webcrm Quotationline
-----------------------------------------
Every Woocommerce Order will be synchronized with a Webcrm Quotationline.

Once a link between a Woocommerce Order and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - line_items.sku
     - QuotationLineCostPrice
     - "string"
   * - line_items.sku
     - QuotationLineDiscount
     - "string"
   * - line_items.sku
     - QuotationLinePrice
     - "string"
   * - line_items.sku
     - QuotationLineQuantity
     - "string"
   * - line_items.sku
     - QuotationLineVatPercentage
     - "string"


Woocommerce Product to Webcrm Products
--------------------------------------
Every Woocommerce Product will be synchronized with a Webcrm Products.

Once a link between a Woocommerce Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - price
     - ProductCostPrice
     - "string"
   * - sale_price
     - ProductPrice
     - "string"

