========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-09-28 09:18:02

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGo Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into PowerOfficeGo.

Once a link between a Wave Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"


Wave Invoice to PowerOfficeGo Outgoinginvoices
----------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Wave Invoice and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - createdAt
     - createdDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - id
     - OrderNo
     - "string"
   * - total.value
     - NetAmount
     - "string"


Wave Currency to PowerOfficeGo Currency
---------------------------------------
Every Wave Currency will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the Wave Currency will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A Wave Currency will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Wave Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Wave Customer person to PowerOfficeGo Location
----------------------------------------------
Every Wave Customer person will be synchronized with a PowerOfficeGo Location.

Once a link between a Wave Customer person and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGo Location Property
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
   * - shippingDetails.address.addressLine1
     - address1
     - "string"
   * - shippingDetails.address.addressLine2
     - address2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - countryCode
     - "string"
   * - shippingDetails.address.postalCode
     - zipCode
     - "string"


Wave Customer to PowerOfficeGo Contactperson
--------------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Wave Customer and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Contactperson Property
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
     - residenceCountryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - id
     - partyId
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - address1
     - "string"
   * - shippingDetails.address.addressLine2
     - address2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - residenceCountryCode
     - "string"
   * - shippingDetails.address.postalCode
     - zipCode
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"


Wave Customer to PowerOfficeGo Customers
----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Customers.

Once a link between a Wave Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - name
     - Name
     - "string"
   * - phone
     - Number
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - shippingDetails.phone
     - Number
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Customer to PowerOfficeGo Location
---------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Location.

Once a link between a Wave Customer and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Location Property
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
   * - shippingDetails.address.addressLine1
     - address1
     - "string"
   * - shippingDetails.address.addressLine2
     - address2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - countryCode
     - "string"
   * - shippingDetails.address.postalCode
     - zipCode
     - "string"


Wave Customer to PowerOfficeGo Suppliers
----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Suppliers.

Once a link between a Wave Customer and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
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
   * - shippingDetails.address.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - shippingDetails.address.city
     - MailAddress.City
     - "string"
   * - shippingDetails.address.country.code
     - MailAddress.CountryCode
     - "string"
   * - shippingDetails.address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Invoice to PowerOfficeGo Salesorders
-----------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - createdAt
     - CreatedDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
   * - invoiceNumber
     - RelatedInvoiceNo
     - "string"
   * - poNumber
     - PurchaseOrderReference
     - "string"
   * - total.value
     - NetAmount
     - "string"
   * - total.value
     - TotalAmount
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
   * - description
     - description
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - modifiedAt
     - lastChanged
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - SalesPrice
     - "string"
   * - unitPrice
     - salesPrice
     - "string"


Wave Vendor to PowerOfficeGo Location
-------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Location.

Once a link between a Wave Vendor and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Location Property
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


Wave Vendor to PowerOfficeGo Suppliers
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Suppliers.

Once a link between a Wave Vendor and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Suppliers Property
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

