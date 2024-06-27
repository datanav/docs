========================================
Wave Financial to Powerofficego Dataflow
========================================

Generated: 2024-06-27 07:12:28

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer contact to Powerofficego Customers person
-------------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer contact and a Powerofficego Customers person must be established.

A Wave Customer contact will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Powerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer contact and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer contact and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type


Wave Customer person to Powerofficego Contactperson
---------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Powerofficego Contactperson must be established.

A Wave Customer person will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Powerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer person and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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


Wave Customer to Powerofficego Contactperson
--------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Powerofficego.

A Wave Customer will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Powerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


Wave Customer to Powerofficego Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, Customer-person, or Customer-contact that is synchronized into Powerofficego.

A Wave Customer will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Powerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Powerofficego Customers person Property
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


Wave Vendor to Powerofficego Customers person
---------------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, Customer-person, or Customer-contact that is synchronized into Powerofficego.

A Wave Vendor will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Powerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Vendor and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Powerofficego Customers person Property
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


Wave Customer to Powerofficego Customers
----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, Customer-person, or Customer-contact that is synchronized into Powerofficego.

Once a link between a Wave Customer and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
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
   * - shippingDetails.phone
     - Number
     - "string"
   * - website
     - WebsiteUrl
     - "string"


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


Wave Customer contact to Powerofficego Contactperson
----------------------------------------------------
Every Wave Customer contact will be synchronized with a Powerofficego Contactperson.

If a matching Powerofficego Contactperson already exists, the Wave Customer contact will be merged with the existing one.
If no matching Powerofficego Contactperson is found, a new Powerofficego Contactperson will be created.

A Wave Customer contact will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Powerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer contact and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer contact and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - partyId
     - "integer"
   * - lastName
     - lastName
     - "string"


Wave Customer organisation to Powerofficego Customers
-----------------------------------------------------
Every Wave Customer organisation will be synchronized with a Powerofficego Customers.

Once a link between a Wave Customer organisation and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer organisation and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer organisation Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - name
     - Name
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - shippingDetails.phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Customer person to Powerofficego Customers person
------------------------------------------------------
Every Wave Customer person will be synchronized with a Powerofficego Customers person.

If a matching Powerofficego Customers person already exists, the Wave Customer person will be merged with the existing one.
If no matching Powerofficego Customers person is found, a new Powerofficego Customers person will be created.

A Wave Customer person will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Powerofficego Customers person Property
   * - email
     - EmailAddress

Once a link between a Wave Customer person and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Powerofficego Customers person Property
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


Wave Invoice to Powerofficego Salesorderlines
---------------------------------------------
Every Wave Invoice will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Wave Invoice and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
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


Wave Invoice to Powerofficego Salesorders
-----------------------------------------
Every Wave Invoice will be synchronized with a Powerofficego Salesorders.

Once a link between a Wave Invoice and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
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


Wave Product to Powerofficego Product
-------------------------------------
Every Wave Product will be synchronized with a Powerofficego Product.

Once a link between a Wave Product and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Powerofficego Product Property
     - Powerofficego Data Type
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


Wave Vendor to Powerofficego Contactperson
------------------------------------------
Every Wave Vendor will be synchronized with a Powerofficego Contactperson.

If a matching Powerofficego Contactperson already exists, the Wave Vendor will be merged with the existing one.
If no matching Powerofficego Contactperson is found, a new Powerofficego Contactperson will be created.

A Wave Vendor will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Powerofficego Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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

