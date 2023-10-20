========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-10-20 08:13:06

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to PowerOfficeGo Contactperson
---------------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a PowerOfficeGo Contactperson must be established.

A Wave Customer person will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - PowerOfficeGo Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Customer person and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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


Wave Vendor to PowerOfficeGo Contactperson
------------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGo Contactperson must be established.

A Wave Vendor will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Contactperson Property
   * - email
     - emailAddress

Once a link between a Wave Vendor and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - id
     - id
     - "integer"


Wave Customer to PowerOfficeGo Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wave Customer if it is connected to a Wave Invoice, or Customer that is synchronized into PowerOfficeGo.

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
   * - address.countryCode
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
   * - address.countryCode
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


Wave Invoice to PowerOfficeGo Salesorderlines
---------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Salesorderlines.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorderlines Property
     - PowerOfficeGo Data Type
   * - id
     - sesam_SalesOrdersId
     - "string"
   * - items.description
     - Description
     - "string"
   * - items.price
     - ProductUnitPrice
     - "string"
   * - items.price
     - SalesOrderLineUnitPrice
     - "string"
   * - items.product.id
     - ProductCode
     - "string"
   * - items.quantity
     - Quantity
     - "string"
   * - total.value
     - TotalAmount
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

