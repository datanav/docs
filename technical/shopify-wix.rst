=======================
Shopify to Wix Dataflow
=======================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Sesamproduct to Wix Products
------------------------------------
Every Shopify Sesamproduct will be synchronized with a Wix Products.

Once a link between a Shopify Sesamproduct and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Wix Products Property
     - Wix Data Type
   * - sesam_priceExclVAT
     - priceData.price
     - N/A
   * - title
     - name
     - "string"
   * - variants..sku
     - sku
     - "string"
   * - variants.price
     - priceData.price
     - N/A
   * - variants.sku
     - sku
     - "string"

