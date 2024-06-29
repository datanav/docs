=======================
Shopify to Wix Dataflow
=======================

Generated: 2024-06-29 00:00:01

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
   * - variants.price
     - priceData.price
     - N/A
   * - variants.title
     - name
     - "string"

