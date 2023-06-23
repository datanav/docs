============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-06-23 07:30:52

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
Before any synchronization can take place, a link between a SuperOffice Contact and a Wave Customer must be established.

A new Wave Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wave Customer Property
     - Wave Data Type


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


SuperOffice Quotealternative to Wave Invoice
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Wave Invoice must be established.

A new Wave Invoice will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Sale, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Quotealternative and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Wave Invoice Property
     - Wave Data Type


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

