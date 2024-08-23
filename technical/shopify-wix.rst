=======================
Shopify to Wix Dataflow
=======================

Generated: 2024-08-23 07:59:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to Wix Products
-------------------------------
Every Shopify Product will be synchronized with a Wix Products.

Once a link between a Shopify Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Wix Products Property
     - Wix Data Type
   * - title
     - name
     - "string"
   * - variants.price
     - priceData.price
     - N/A
   * - variants.sku
     - sku
     - "string"
   * - variants.title
     - name
     - "string"


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
   * - title
     - name
     - "string"
   * - variants.price
     - priceData.price
     - N/A
   * - variants.sku
     - sku
     - "string"

