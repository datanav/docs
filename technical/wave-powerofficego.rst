========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-08-01 14:01:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGo Address
--------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Address.

Once a link between a Wave Customer and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Customer to PowerOfficeGo Customer
---------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Customer.

Once a link between a Wave Customer and a PowerOfficeGo Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customer Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - id
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Invoice to PowerOfficeGo Salesorder
----------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type
   * - currency.code
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"


Wave Product to PowerOfficeGo Product
-------------------------------------
Every Wave Product will be synchronized with a PowerOfficeGo Product.

Once a link between a Wave Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - description
     - Description
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - Name
     - "string"
   * - unitPrice
     - SalesPrice
     - "string"


Wave Vendor to PowerOfficeGo Address
------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Address.

Once a link between a Wave Vendor and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Vendor to PowerOfficeGo Supplier
-------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Supplier.

Once a link between a Wave Vendor and a PowerOfficeGo Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Supplier:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Supplier Property
     - PowerOfficeGo Data Type
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - website
     - WebsiteUrl
     - "string"

