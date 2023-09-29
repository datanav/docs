==============================
Powerofficego to Wave Dataflow
==============================

Generated: 2023-09-29 14:08:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Wave Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, or Salesorders that is synchronized into Wave.

Once a link between a Powerofficego Customers and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wave Customer person Property
     - Wave Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Powerofficego Salesorder to Wave Invoice
----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorder and a Wave Invoice must be established.

A new Wave Invoice will be created from a Powerofficego Salesorder if it is connected to a Powerofficego Salesorder, or Salesorders that is synchronized into Wave.

Once a link between a Powerofficego Salesorder and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - Wave Invoice Property
     - Wave Data Type


Powerofficego Contactperson to Wave Customer
--------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Wave Customer.

Once a link between a Powerofficego Contactperson and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wave Customer Property
     - Wave Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - partyId
     - id
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - residenceCountryCode
     - address.country.code
     - "string"
   * - zipCode
     - address.postalCode
     - "string"


Powerofficego Employees to Wave Customer
----------------------------------------
Every Powerofficego Employees will be synchronized with a Wave Customer.

Once a link between a Powerofficego Employees and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Wave Customer Property
     - Wave Data Type
   * - DepartmentId
     - id
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PhoneNumber
     - mobile
     - "string"


Powerofficego Customers to Wave Customer
----------------------------------------
Every Powerofficego Customers will be synchronized with a Wave Customer.

Once a link between a Powerofficego Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wave Customer Property
     - Wave Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Name
     - name
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - Number
     - phone
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - legalName
     - name
     - "string"
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
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
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - unitPrice
     - "string"


Powerofficego Salesorders to Wave Invoice
-----------------------------------------
Every Powerofficego Salesorders will be synchronized with a Wave Invoice.

Once a link between a Powerofficego Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - CurrencyCode
     - currency.code
     - "string"
   * - PurchaseOrderReference
     - poNumber
     - "string"


Powerofficego Suppliers to Wave Vendor
--------------------------------------
Every Powerofficego Suppliers will be synchronized with a Wave Vendor.

Once a link between a Powerofficego Suppliers and a Wave Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Wave Vendor:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Wave Vendor Property
     - Wave Data Type
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - firstName
     - "string"
   * - LegalName
     - name
     - "string"
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"

