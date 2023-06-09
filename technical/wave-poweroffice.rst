======================================
Wave Financial to PowerOffice Dataflow
======================================

Generated: 2023-06-09 09:07:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Business to PowerOffice Address
------------------------------------
Every Wave Business will be synchronized with a PowerOffice Address.

Once a link between a Wave Business and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - address.addressLine1
     - Address1
     - "string"
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - Address2
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country
     - CountryCode
     - "string"
   * - address.country
     - countryCode
     - "string"
   * - address.postalCode
     - ZipCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Customer to PowerOffice Address
------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Address.

Once a link between a Wave Customer and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - address.addressLine1
     - Address1
     - "string"
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - Address2
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - CountryCode
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - ZipCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Customer to PowerOffice Customer
-------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Customer.

Once a link between a Wave Customer and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
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
   * - phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Invoice to PowerOffice Outgoinginvoice
-------------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice Outgoinginvoice.

Once a link between a Wave Invoice and a PowerOffice Outgoinginvoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice Outgoinginvoice:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice Outgoinginvoice Property
     - PowerOffice Data Type
   * - amountDue.value
     - NetAmount
     - "string"
   * - createdAt
     - CreatedDate
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"


Wave Invoice to PowerOffice Salesorder
--------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice Salesorder.

Once a link between a Wave Invoice and a PowerOffice Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice Salesorder:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice Salesorder Property
     - PowerOffice Data Type
   * - currency.code
     - Currency
     - "string"


Wave Product to PowerOffice Product
-----------------------------------
Every Wave Product will be synchronized with a PowerOffice Product.

Once a link between a Wave Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
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

