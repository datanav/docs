====================
Shopify to  Dataflow
====================

Generated: 2024-09-02 11:05:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Sesamproduct to  Products
---------------------------------
Every Shopify Sesamproduct will be synchronized with a  Products.

Once a link between a Shopify Sesamproduct and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Products Property
     -  Data Type
   * - sesam_priceExclVAT
     - product_price
     - "string"
   * - title
     - product_name
     - "string"
   * - variants.sku
     - sku
     - "string"
   * - variants.title
     - product_desc
     - "string"

