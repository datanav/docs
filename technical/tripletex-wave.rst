==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-05-31 11:44:30

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Wave Customer
-----------------------------------
Every Tripletex Customer will be synchronized with a Wave Customer.

Once a link between a Tripletex Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"


Tripletex Invoice to Wave Invoice
---------------------------------
Every Tripletex Invoice will be synchronized with a Wave Invoice.

Once a link between a Tripletex Invoice and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - Wave Invoice Property
     - Wave Data Type
   * - amountExcludingVat
     - amountDue.value
     - "string"


Tripletex Product to Wave Product
---------------------------------
Every Tripletex Product will be synchronized with a Wave Product.

Once a link between a Tripletex Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Wave Product Property
     - Wave Data Type

