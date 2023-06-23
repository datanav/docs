======================================
Wave Financial to SuperOffice Dataflow
======================================

Generated: 2023-06-23 11:19:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to SuperOffice Contact
------------------------------------
Every Wave Customer will be synchronized with a SuperOffice Contact.

Once a link between a Wave Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"


Wave Invoice to SuperOffice Sale
--------------------------------
Every Wave Invoice will be synchronized with a SuperOffice Sale.

Once a link between a Wave Invoice and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - currency.code
     - Currency.Id
     - "integer"
   * - customer.id
     - Contact.ContactId
     - "integer"
   * - memo
     - SaleText
     - "string"
   * - total.value
     - Amount
     - "float"


Wave Product to SuperOffice Product
-----------------------------------
Every Wave Product will be synchronized with a SuperOffice Product.

Once a link between a Wave Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type


Wave Vendor to SuperOffice Contact
----------------------------------
Every Wave Vendor will be synchronized with a SuperOffice Contact.

Once a link between a Wave Vendor and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"

