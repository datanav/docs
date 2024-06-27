==============================
Powerofficego to Wave Dataflow
==============================

Generated: 2024-06-27 07:16:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Wave Customer person
---------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Wave Customer person must be established.

A new Wave Customer person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Wave.

A Powerofficego Contactperson will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wave Customer person Property
   * - emailAddress
     - email

Once a link between a Powerofficego Contactperson and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wave Customer person Property
     - Wave Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address1
     - shippingDetails.address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - address2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - N/A
   * - phoneNumber
     - phone
     - "string"
   * - residenceCountryCode
     - address.country.code
     - "string"
   * - residenceCountryCode
     - shippingDetails.address.country.code
     - "string"
   * - zipCode
     - address.postalCode
     - "string"
   * - zipCode
     - shippingDetails.address.postalCode
     - "string"


Powerofficego Contactperson to Wave Customer organisation
---------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Wave Customer organisation must be established.

A new Wave Customer organisation will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorders that is synchronized into Wave.

Once a link between a Powerofficego Contactperson and a Wave Customer organisation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wave Customer organisation:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wave Customer organisation Property
     - Wave Data Type


Powerofficego Contactperson to Wave Customer
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Wave Customer must be established.

A new Wave Customer will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Wave.

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
   * - address1
     - shippingDetails.address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - address2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
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
   * - residenceCountryCode
     - address.country.code
     - "string"
   * - residenceCountryCode
     - shippingDetails.address.country.code
     - "string"
   * - zipCode
     - address.postalCode
     - "string"
   * - zipCode
     - shippingDetails.address.postalCode
     - "string"


Powerofficego Customers to Wave Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customer, Customers, Employees, Suppliers, Salesorder, Departments, Salesorders, Contactperson, Salesorderlines, Outgoinginvoices, or Customers-organisation that is synchronized into Wave.

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


Powerofficego Customers person to Wave Customer person
------------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Wave Customer person.

If a matching Wave Customer person already exists, the Powerofficego Customers person will be merged with the existing one.
If no matching Wave Customer person is found, a new Wave Customer person will be created.

A Powerofficego Customers person will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wave Customer person Property
   * - EmailAddress
     - email

Once a link between a Powerofficego Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
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
     - N/A
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - shippingDetails.address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.CountryCode
     - shippingDetails.address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - shippingDetails.address.postalCode
     - "string"
   * - PhoneNumber
     - phone
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
   * - MailAddress.AddressLine1
     - address.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - address.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - shippingDetails.address.city
     - "string"
   * - MailAddress.CountryCode
     - address.country.code
     - "string"
   * - MailAddress.CountryCode
     - shippingDetails.address.country.code
     - "string"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - MailAddress.ZipCode
     - shippingDetails.address.postalCode
     - "string"
   * - Name
     - name
     - N/A
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
   * - CustomerId
     - customer.id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer.id
     - "string"
   * - PurchaseOrderReference
     - poNumber
     - "string"

