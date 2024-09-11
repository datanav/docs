===============================
Wave to PowerOffice GO Dataflow
===============================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to PowerOffice Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a PowerOffice Contactperson must be established.

A Wave Customer person will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer person and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Wave Customer to PowerOffice Customers person
---------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, Customer-person, or Customer-contact that is synchronized into PowerOffice.

A Wave Customer will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Wave Vendor to PowerOffice Customers person
-------------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, Customer-person, or Customer-contact that is synchronized into PowerOffice.

A Wave Vendor will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Vendor and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Wave Vendor to Powerofficego Customers
--------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, Customer-person, or Customer-contact that is synchronized into Powerofficego.

Once a link between a Wave Vendor and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
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


Wave Customer person to PowerOffice Customers person
----------------------------------------------------
Every Wave Customer person will be synchronized with a PowerOffice Customers person.

If a matching PowerOffice Customers person already exists, the Wave Customer person will be merged with the existing one.
If no matching PowerOffice Customers person is found, a new PowerOffice Customers person will be created.

A Wave Customer person will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOffice Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Wave Customer to PowerOffice Contactperson
------------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Contactperson.

If a matching PowerOffice Contactperson already exists, the Wave Customer will be merged with the existing one.
If no matching PowerOffice Contactperson is found, a new PowerOffice Contactperson will be created.

A Wave Customer will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Wave Customer to PowerOffice Customers
--------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Customers.

Once a link between a Wave Customer and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
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


Wave Invoice to PowerOffice Salesorderlines
-------------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Wave Invoice and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
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


Wave Invoice to PowerOffice Salesorders
---------------------------------------
Every Wave Invoice will be synchronized with a PowerOffice Salesorders.

Once a link between a Wave Invoice and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
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


Wave Vendor to PowerOffice Contactperson
----------------------------------------
Every Wave Vendor will be synchronized with a PowerOffice Contactperson.

If a matching PowerOffice Contactperson already exists, the Wave Vendor will be merged with the existing one.
If no matching PowerOffice Contactperson is found, a new PowerOffice Contactperson will be created.

A Wave Vendor will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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

