==============================
Wave to PowerOfficeGO Dataflow
==============================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to PowerOfficeGO Contactperson
---------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a PowerOfficeGO Contactperson must be established.

A Wave Customer person will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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
   * - address.countryCode
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


WaveWave Financial Customer to PowerOfficeGOPowerofficego Customers person
--------------------------------------------------------------------------
Before any synchronization can take place, a link between a WaveWave Financial Customer and a PowerOfficeGOPowerofficego Customers person must be established.

A new PowerOfficeGOPowerofficego Customers person will be created from a WaveWave Financial Customer if it is connected to a WaveWave Financial Wave-vendor, Wave-invoice, Wave-customer, Wave-customer-person, or Wave-customer-contact that is synchronized into PowerOfficeGOPowerofficego.

A WaveWave Financial Customer will merge with a PowerOfficeGOPowerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
     - PowerOfficeGOPowerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a WaveWave Financial Customer and a PowerOfficeGOPowerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Customer and a PowerOfficeGOPowerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
     - PowerOfficeGOPowerofficego Customers person Property
     - PowerOfficeGOPowerofficego Data Type
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
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - LastName
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


WaveWave Financial Vendor to PowerOfficeGOPowerofficego Customers person
------------------------------------------------------------------------
Before any synchronization can take place, a link between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers person must be established.

A new PowerOfficeGOPowerofficego Customers person will be created from a WaveWave Financial Vendor if it is connected to a WaveWave Financial Wave-vendor, Wave-customer, Wave-customer-person, or Wave-customer-contact that is synchronized into PowerOfficeGOPowerofficego.

A WaveWave Financial Vendor will merge with a PowerOfficeGOPowerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Vendor Property
     - PowerOfficeGOPowerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Vendor Property
     - PowerOfficeGOPowerofficego Customers person Property
     - PowerOfficeGOPowerofficego Data Type
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
   * - id
     - Id
     - "integer"


WaveWave Financial Vendor to PowerOfficeGOPowerofficego Customers
-----------------------------------------------------------------
Before any synchronization can take place, a link between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers must be established.

A new PowerOfficeGOPowerofficego Customers will be created from a WaveWave Financial Vendor if it is connected to a WaveWave Financial Wave-vendor, Wave-customer, Wave-customer-person, or Wave-customer-contact that is synchronized into PowerOfficeGOPowerofficego.

Once a link between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Vendor and a PowerOfficeGOPowerofficego Customers:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Vendor Property
     - PowerOfficeGOPowerofficego Customers Property
     - PowerOfficeGOPowerofficego Data Type
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
   * - id
     - Id
     - "integer"
   * - name
     - Name
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Customer person to PowerOfficeGO Customers person
------------------------------------------------------
Every Wave Customer person will be synchronized with a PowerOfficeGO Customers person.

If a matching PowerOfficeGO Customers person already exists, the Wave Customer person will be merged with the existing one.
If no matching PowerOfficeGO Customers person is found, a new PowerOfficeGO Customers person will be created.

A Wave Customer person will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGO Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - LastName
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


Wave Customer to PowerOfficeGO Contactperson
--------------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGO Contactperson.

If a matching PowerOfficeGO Contactperson already exists, the Wave Customer will be merged with the existing one.
If no matching PowerOfficeGO Contactperson is found, a new PowerOfficeGO Contactperson will be created.

A Wave Customer will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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
   * - address.countryCode
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
     - "integer"
   * - lastName
     - lastName
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


WaveWave Financial Customer to PowerOfficeGOPowerofficego Customers
-------------------------------------------------------------------
Every WaveWave Financial Customer will be synchronized with a PowerOfficeGOPowerofficego Customers.

Once a link between a WaveWave Financial Customer and a PowerOfficeGOPowerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Customer and a PowerOfficeGOPowerofficego Customers:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
     - PowerOfficeGOPowerofficego Customers Property
     - PowerOfficeGOPowerofficego Data Type
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
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
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
     - Number
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Invoice to PowerOfficeGO Salesorderlines
---------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Wave Invoice and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - id
     - sesam_SalesOrderId
     - "string"
   * - id
     - sesam_SalesOrdersId
     - "string"
   * - items.description
     - Description
     - "string"
   * - items.price
     - ProductUnitPrice
     - N/A
   * - items.price
     - SalesOrderLineUnitPrice
     - "string"
   * - items.product.id
     - ProductCode
     - "string"
   * - items.product.id
     - ProductId
     - "integer"
   * - items.quantity
     - Quantity
     - N/A
   * - total.value
     - TotalAmount
     - "string"


Wave Invoice to PowerOfficeGO Salesorders
-----------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a Wave Invoice and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - createdAt
     - CreatedDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
   * - customer.id
     - CustomerId
     - "integer"
   * - customer.id
     - CustomerReferenceContactPersonId
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


Wave Product to PowerOfficeGO Product
-------------------------------------
Every Wave Product will be synchronized with a PowerOfficeGO Product.

Once a link between a Wave Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
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
     - N/A


Wave Vendor to PowerOfficeGO Contactperson
------------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGO Contactperson.

If a matching PowerOfficeGO Contactperson already exists, the Wave Vendor will be merged with the existing one.
If no matching PowerOfficeGO Contactperson is found, a new PowerOfficeGO Contactperson will be created.

A Wave Vendor will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGO Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - phone
     - phoneNumber
     - "string"

