===========================
Wave Financial to  Dataflow
===========================

Generated: 2023-11-29 23:38:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Contactperson
--------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Contactperson must be established.

A Wave Customer person will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer person and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contactperson Property
     -  Data Type
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
   * - id
     - id
     - "integer"
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


Wave Vendor to  Contactperson
-----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Contactperson must be established.

A Wave Vendor will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contactperson Property
     -  Data Type
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
   * - id
     - id
     - "integer"


Wave Customer to PowerOfficeGo Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, or Customer-person that is synchronized into PowerOfficeGo.

Once a link between a Wave Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Customers person Property
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


Wave Currency to  Currency
--------------------------
Every Wave Currency will be synchronized with a  Currency.

If a matching  Currency already exists, the Wave Currency will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A Wave Currency will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     -  Currency Property
   * - code
     - code

Once a link between a Wave Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     -  Currency Property
     -  Data Type


Wave Customer to PowerOfficeGo Contactperson
--------------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Contactperson.

If a matching PowerOfficeGo Contactperson already exists, the Wave Customer will be merged with the existing one.
If no matching PowerOfficeGo Contactperson is found, a new PowerOfficeGo Contactperson will be created.

A Wave Customer will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Contactperson Property
   * - email
     - emailAddress

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


Wave Invoice to  Salesorderlines
--------------------------------
Every Wave Invoice will be synchronized with a  Salesorderlines.

Once a link between a Wave Invoice and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorderlines Property
     -  Data Type
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
     - "if", "is-decimal", "decimal", "integer"]
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
     - "integer"
   * - total.value
     - TotalAmount
     - "string"


Wave Invoice to  Salesorders
----------------------------
Every Wave Invoice will be synchronized with a  Salesorders.

Once a link between a Wave Invoice and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorders Property
     -  Data Type
   * - createdAt
     - CreatedDateTimeOffset
     - "string"
   * - currency.code
     - CurrencyCode
     - "string"
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


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
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
     - "if", "is-decimal", "decimal", "integer"]

