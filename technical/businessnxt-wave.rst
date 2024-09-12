=============================
Business Nxt to Wave Dataflow
=============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Country to Wave Country
------------------------------------
Every Business Nxt Country will be synchronized with a Wave Country.

Once a link between a Business Nxt Country and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Country and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Nxt Country Property
     - Wave Country Property
     - Wave Data Type


Business Nxt Currency to Wave Currency
--------------------------------------
Every Business Nxt Currency will be synchronized with a Wave Currency.

Once a link between a Business Nxt Currency and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - Wave Currency Property
     - Wave Data Type


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

