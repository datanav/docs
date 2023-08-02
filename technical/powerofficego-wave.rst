==============================
Powerofficego to Wave Dataflow
==============================

Generated: 2023-08-02 12:47:40

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to Wave Customer
---------------------------------------
Every Powerofficego Customer will be synchronized with a Wave Customer.

Once a link between a Powerofficego Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - LastName
     - lastName
     - "string"
   * - LegalName
     - name
     - "string"
   * - WebsiteUrl
     - website
     - "string"
   * - firstName
     - firstName
     - "string"
   * - legalName
     - name
     - "string"
   * - streetAddresses.address1
     - address.addressLine1
     - "string"
   * - streetAddresses.address2
     - address.addressLine2
     - "string"
   * - streetAddresses.city
     - address.city
     - "string"
   * - streetAddresses.countryCode
     - address.country.code
     - "string"
   * - streetAddresses.zipCode
     - address.postalCode
     - "string"
   * - websiteUrl
     - website
     - "string"


Powerofficego Product to Wave Product
-------------------------------------
Every Powerofficego Product will be synchronized with a Wave Product.

Once a link between a Powerofficego Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
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


Powerofficego Salesorder to Wave Invoice
----------------------------------------
Every Powerofficego Salesorder will be synchronized with a Wave Invoice.

Once a link between a Powerofficego Salesorder and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - Wave Invoice Property
     - Wave Data Type
   * - Currency
     - currency.code
     - "string"
   * - DepartmentCode
     - customer.id
     - "string"


Powerofficego Supplier to Wave Vendor
-------------------------------------
Every Powerofficego Supplier will be synchronized with a Wave Vendor.

Once a link between a Powerofficego Supplier and a Wave Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a Wave Vendor:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - Wave Vendor Property
     - Wave Data Type
   * - LegalName
     - name
     - "string"
   * - WebsiteUrl
     - website
     - "string"

