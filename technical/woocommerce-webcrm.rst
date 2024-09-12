==============================
WooCommerce to WebCRM Dataflow
==============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to WebCRM Quotationline
-----------------------------------------
Every WooCommerce Order will be synchronized with a WebCRM Quotationline.

Once a link between a WooCommerce Order and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
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


WooCommerce Product to WebCRM Products
--------------------------------------
Every WooCommerce Product will be synchronized with a WebCRM Products.

Once a link between a WooCommerce Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - price
     - ProductCostPrice
     - "string"
   * - sale_price
     - ProductPrice
     - "string"

