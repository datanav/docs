==============================
Woocommerce to Webcrm Dataflow
==============================

Generated: 2024-09-03 09:00:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to  Quotationline
-----------------------------------
Every Woocommerce Order will be synchronized with a  Quotationline.

Once a link between a Woocommerce Order and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Quotationline Property
     -  Data Type
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


Woocommerce Product to  Products
--------------------------------
Every Woocommerce Product will be synchronized with a  Products.

Once a link between a Woocommerce Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     -  Products Property
     -  Data Type
   * - price
     - ProductCostPrice
     - "string"
   * - sale_price
     - ProductPrice
     - "string"

