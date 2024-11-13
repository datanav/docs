==========================
Shopify to WebCRM Dataflow
==========================

Generated: 2024-11-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Order to WebCRM Quotationline
-------------------------------------
Every Shopify Order will be synchronized with a WebCRM Quotationline.

Once a link between a Shopify Order and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - WebCRM Quotationline Property
     - WebCRM Data Type


Shopify Sesamproduct to WebCRM Products
---------------------------------------
Every Shopify Sesamproduct will be synchronized with a WebCRM Products.

Once a link between a Shopify Sesamproduct and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - sesam_priceExclVAT
     - ProductPrice
     - "string"
   * - variants.inventory_quantity
     - ProductQuantity
     - "string"

