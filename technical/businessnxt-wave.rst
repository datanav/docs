============================
BusinessNxt to Wave Dataflow
============================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to Wave Invoice
---------------------------------
Every BusinessNxt Order will be synchronized with a Wave Invoice.

Once a link between a BusinessNxt Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - invoiceDate
     - invoiceDate
     - N/A
   * - name
     - title
     - "string"


BusinessNxt Product to Wave Product
-----------------------------------
Every BusinessNxt Product will be synchronized with a Wave Product.

Once a link between a BusinessNxt Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - unitPrice
     - "string"

