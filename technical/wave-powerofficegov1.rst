==========================================
Wave Financial to PowerOfficeGov1 Dataflow
==========================================

Generated: 2023-08-14 08:51:46

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGov1 Employee
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Employee must be established.

A Wave Customer will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Customer and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"


Wave Customer to PowerOfficeGov1 Person
---------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a PowerOfficeGov1 Person must be established.

A Wave Customer will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"


Wave Vendor to PowerOfficeGov1 Employee
---------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Employee must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Wave Vendor and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - MailAddress.Address1
     - "string"
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - MailAddress.Address2
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - MailAddress.CountryCode
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - MailAddress.ZipCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - Id
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Wave Vendor to PowerOfficeGov1 Person
-------------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a PowerOfficeGov1 Person must be established.

A Wave Vendor will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"


Wave Account to PowerOfficeGov1 Account
---------------------------------------
Every Wave Account will be synchronized with a PowerOfficeGov1 Account.

Once a link between a Wave Account and a PowerOfficeGov1 Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Account and a PowerOfficeGov1 Account:

.. list-table::
   :header-rows: 1

   * - Wave Account Property
     - PowerOfficeGov1 Account Property
     - PowerOfficeGov1 Data Type
   * - business.id
     - business.id
     - "string"
   * - currency.code
     - currency.code
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"


Wave Business to PowerOfficeGov1 Teams
--------------------------------------
Every Wave Business will be synchronized with a PowerOfficeGov1 Teams.

Once a link between a Wave Business and a PowerOfficeGov1 Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a PowerOfficeGov1 Teams:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - PowerOfficeGov1 Teams Property
     - PowerOfficeGov1 Data Type
   * - name
     - name
     - "string"
   * - website
     - permalink_url
     - "string"


Wave Customer to PowerOfficeGov1 Customer
-----------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGov1 Customer.

Once a link between a Wave Customer and a PowerOfficeGov1 Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Customer Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - address.country.code
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - address.province
     - address.province
     - "string"
   * - email
     - email
     - "string"
   * - email
     - emailAddress
     - "string"
   * - fax
     - fax
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - internalNotes
     - internalNotes
     - "string"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - mobile
     - "string"
   * - modifiedAt
     - lastChanged
     - "string"
   * - name
     - legalName
     - "string"
   * - name
     - name
     - "string"
   * - phone
     - phone
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - shippingDetails.address.city
     - deliveryAddress.city
     - "string"
   * - shippingDetails.address.country.code
     - deliveryAddress.country.id
     - "string"
   * - shippingDetails.address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - shippingDetails.phone
     - phone
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"
   * - tollFree
     - tollFree
     - "string"
   * - website
     - website
     - "string"
   * - website
     - websiteUrl
     - "string"


Wave Customer to PowerOfficeGov1 Customers
------------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGov1 Customers.

Once a link between a Wave Customer and a PowerOfficeGov1 Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGov1 Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGov1 Customers Property
     - PowerOfficeGov1 Data Type
   * - website
     - WebUrl
     - "string"


Wave Invoice to PowerOfficeGov1 Invoice
---------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGov1 Invoice.

Once a link between a Wave Invoice and a PowerOfficeGov1 Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGov1 Invoice:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGov1 Invoice Property
     - PowerOfficeGov1 Data Type
   * - currency.code
     - currency.code
     - "string"
   * - currency.code
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "string"
   * - dueDate
     - dueDate
     - "datetime-format","%Y-%m-%d","_."]
   * - dueDate
     - invoiceDueDate
     - "datetime-format","%Y-%m-%d","_."]
   * - invoiceDate
     - invoiceDate
     - "datetime-format","%Y-%m-%d","_."]
   * - items.description
     - items.description
     - "string"
   * - items.price
     - items.price
     - "float"
   * - items.product.id
     - items.product.id
     - "string"
   * - items.quantity
     - items.quantity
     - "float"
   * - memo
     - memo
     - "string"
   * - poNumber
     - poNumber
     - "string"
   * - title
     - title
     - "string"
   * - total.value
     - amountExcludingVat
     - "integer"


Wave Invoice to PowerOfficeGov1 Order
-------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGov1 Order.

Once a link between a Wave Invoice and a PowerOfficeGov1 Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGov1 Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGov1 Order Property
     - PowerOfficeGov1 Data Type
   * - currency.code
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "integer"
   * - poNumber
     - reference
     - "string"
   * - title
     - invoiceComment
     - "string"


Wave Invoice to PowerOfficeGov1 Salesorder
------------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGov1 Salesorder.

Once a link between a Wave Invoice and a PowerOfficeGov1 Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGov1 Salesorder:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGov1 Salesorder Property
     - PowerOfficeGov1 Data Type
   * - currency.code
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"


Wave Product to PowerOfficeGov1 Product
---------------------------------------
Every Wave Product will be synchronized with a PowerOfficeGov1 Product.

Once a link between a Wave Product and a PowerOfficeGov1 Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOfficeGov1 Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOfficeGov1 Product Property
     - PowerOfficeGov1 Data Type
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - expenseAccount.id
     - expenseAccount.id
     - "string"
   * - incomeAccount.id
     - incomeAccount.id
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
     - UnitListPrice
     - "decimal"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"
   * - unitPrice
     - salesPrice
     - "string"
   * - unitPrice
     - unitPrice
     - "string"


Wave Vendor to PowerOfficeGov1 Supplier
---------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Supplier.

Once a link between a Wave Vendor and a PowerOfficeGov1 Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Supplier:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Supplier Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - name
     - name
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Vendor to PowerOfficeGov1 Vendor
-------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGov1 Vendor.

Once a link between a Wave Vendor and a PowerOfficeGov1 Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGov1 Vendor:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGov1 Vendor Property
     - PowerOfficeGov1 Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country.code
     - address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.province.name
     - address.province.name
     - "string"
   * - email
     - email
     - "string"
   * - fax
     - fax
     - "string"
   * - firstName
     - firstName
     - "string"
   * - internalNotes
     - internalNotes
     - "string"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - mobile
     - "string"
   * - name
     - name
     - "string"
   * - phone
     - phone
     - "string"
   * - tollFree
     - tollFree
     - "string"
   * - website
     - website
     - "string"

