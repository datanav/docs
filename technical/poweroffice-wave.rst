============================
Poweroffice to Wave Dataflow
============================

Generated: 2023-06-25 06:00:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Customer to Wave Customer
-------------------------------------
Every Poweroffice Customer will be synchronized with a Wave Customer.

Once a link between a Poweroffice Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Poweroffice Product to Wave Product
-----------------------------------
Every Poweroffice Product will be synchronized with a Wave Product.

Once a link between a Poweroffice Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Poweroffice Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - SalesPrice
     - unitPrice
     - "string"


Poweroffice Salesorder to Wave Invoice
--------------------------------------
Every Poweroffice Salesorder will be synchronized with a Wave Invoice.

Once a link between a Poweroffice Salesorder and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Salesorder and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Poweroffice Salesorder Property
     - Wave Invoice Property
     - Wave Data Type
   * - Currency
     - currency.code
     - "string"
   * - DepartmentCode
     - customer.id
     - "string"


Poweroffice Supplier to Wave Vendor
-----------------------------------
Every Poweroffice Supplier will be synchronized with a Wave Vendor.

Once a link between a Poweroffice Supplier and a Wave Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a Wave Vendor:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - Wave Vendor Property
     - Wave Data Type
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"

