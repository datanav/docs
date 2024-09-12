=====================
Keap to Wave Dataflow
=====================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Wave Product
----------------------------
Every Keap Product will be synchronized with a Wave Product.

Once a link between a Keap Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Wave Product Property
     - Wave Data Type
   * - product_desc
     - description
     - "string"
   * - product_name
     - name
     - "string"
   * - product_price
     - unitPrice
     - "string"

