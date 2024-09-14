=============================
Business Nxt to Wave Dataflow
=============================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Order to Wave Invoice
----------------------------------
Every Business Nxt Order will be synchronized with a Wave Invoice.

Once a link between a Business Nxt Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - invoiceDate
     - invoiceDate
     - N/A
   * - name
     - title
     - "string"


Business Nxt Product to Wave Product
------------------------------------
Every Business Nxt Product will be synchronized with a Wave Product.

Once a link between a Business Nxt Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - unitPrice
     - "string"

