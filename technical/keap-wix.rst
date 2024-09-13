====================
Keap to Wix Dataflow
====================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Wix Products
----------------------------
Every Keap Product will be synchronized with a Wix Products.

Once a link between a Keap Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Wix Products Property
     - Wix Data Type
   * - product_name
     - name
     - "string"
   * - product_price
     - priceData.price
     - N/A

