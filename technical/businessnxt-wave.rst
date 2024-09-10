============================
Businessnxt to Wave Dataflow
============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Order to Wave Invoice
---------------------------------
Every Businessnxt Order will be synchronized with a Wave Invoice.

Once a link between a Businessnxt Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - invoiceDate
     - invoiceDate
     - N/A
   * - name
     - title
     - "string"


Businessnxt Product to Wave Product
-----------------------------------
Every Businessnxt Product will be synchronized with a Wave Product.

Once a link between a Businessnxt Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - unitPrice
     - "string"

