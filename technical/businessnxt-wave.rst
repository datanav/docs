===================================
Visma Business Nxt to Wave Dataflow
===================================

Generated: 2024-09-11 07:47:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Order to Wave Invoice
---------------------------
Every Visma Order will be synchronized with a Wave Invoice.

Once a link between a Visma Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - invoiceDate
     - invoiceDate
     - N/A
   * - name
     - title
     - "string"


Visma Product to Wave Product
-----------------------------
Every Visma Product will be synchronized with a Wave Product.

Once a link between a Visma Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - unitPrice
     - "string"

