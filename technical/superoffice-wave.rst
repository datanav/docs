============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-06-25 06:03:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Pricelist to Wave Currency
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a Wave Currency must be established.

A SuperOffice Pricelist will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wave Currency Property
   * - Currency
     - code

Once a link between a SuperOffice Pricelist and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wave Currency Property
     - Wave Data Type
   * - Name
     - name
     - "string"


SuperOffice Contact to Wave Customer
------------------------------------
Every SuperOffice Contact will be synchronized with a Wave Customer.

Once a link between a SuperOffice Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - Domains
     - website
     - "string"
   * - Name
     - name
     - "string"
   * - Phones.Value
     - phone
     - "string"


SuperOffice Quotealternative to Wave Invoice
--------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Wave Invoice.

Once a link between a SuperOffice Quotealternative and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Wave Invoice Property
     - Wave Data Type
   * - Description
     - memo
     - "string"
   * - Name
     - title
     - "string"


SuperOffice Quote to Wave Invoice
---------------------------------
Every SuperOffice Quote will be synchronized with a Wave Invoice.

Once a link between a SuperOffice Quote and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - Wave Invoice Property
     - Wave Data Type
   * - PoNumber
     - poNumber
     - "string"


SuperOffice Quoteline to Wave Invoice
-------------------------------------
Every SuperOffice Quoteline will be synchronized with a Wave Invoice.

Once a link between a SuperOffice Quoteline and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Wave Invoice Property
     - Wave Data Type
   * - ERPProductKey
     - items.product.id
     - "string"
   * - Name
     - items.description
     - "string"
   * - Quantity
     - items.quantity
     - "float"
   * - UnitListPrice
     - items.price
     - "float"


SuperOffice Sale to Wave Invoice
--------------------------------
Every SuperOffice Sale will be synchronized with a Wave Invoice.

Once a link between a SuperOffice Sale and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Wave Invoice Property
     - Wave Data Type
   * - Contact.ContactId
     - customer.id
     - "string"
   * - Currency.Id
     - currency.code
     - "string"
   * - SaleText
     - memo
     - "string"


SuperOffice Product to Wave Product
-----------------------------------
Every SuperOffice Product will be synchronized with a Wave Product.

Once a link between a SuperOffice Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - UnitListPrice
     - unitPrice
     - "string"

