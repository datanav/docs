===============================
PowerOffice GO to Wave Dataflow
===============================

Generated: 2024-09-17 09:13:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Wave Customer person
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Wave Customer person must be established.

A new Wave Customer person will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Wave.

A PowerOffice GO Contactperson will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Wave Customer person Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Customers person to Wave Customer person
-------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Wave Customer person must be established.

A PowerOffice GO Customers person will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Wave Customer person Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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

A new Wave Customer person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customer, Customers, Employees, Suppliers, Salesorder, Departments, Salesorders, Contactperson, Salesorderlines, Customers-person, Outgoinginvoices, or Customers-organisation that is synchronized into Wave.

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


Powerofficego Customers to Wave Customer
----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wave Customer must be established.

A new Wave Customer will be created from a Powerofficego Customers if it is connected to a Powerofficego Customer, Customers, Employees, Suppliers, Salesorder, Departments, Salesorders, Contactperson, Salesorderlines, Customers-person, Outgoinginvoices, or Customers-organisation that is synchronized into Wave.

Once a link between a Powerofficego Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wave Customer Property
     - Wave Data Type
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
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Powerofficego Product to Wave Product
-------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product and a Wave Product must be established.

A new Wave Product will be created from a Powerofficego Product if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Wave.

Once a link between a Powerofficego Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Wave Product Property
     - Wave Data Type
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
Before any synchronization can take place, a link between a Powerofficego Salesorders and a Wave Invoice must be established.

A new Wave Invoice will be created from a Powerofficego Salesorders if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Wave.

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


PowerOffice GO Customers person to Wave Customer
------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Wave Customer.

Once a link between a PowerOffice GO Customers person and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Customers person to Wave Customer person
-------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Wave Customer person.

Once a link between a PowerOffice GO Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Wave Customer person Property
     - Wave Data Type


PowerOffice GO Customers to Wave Customer
-----------------------------------------
Every PowerOffice GO Customers will be synchronized with a Wave Customer.

Once a link between a PowerOffice GO Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Wave Customer Property
     - Wave Data Type
   * - Name
     - name
     - N/A
   * - PhoneNumber
     - phone
     - "string"
   * - WebsiteUrl
     - website
     - "string"


PowerOffice GO Customers to Wave Customer person
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Wave Customer person.

Once a link between a PowerOffice GO Customers and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Wave Customer person Property
     - Wave Data Type


PowerOffice GO Product to Wave Product
--------------------------------------
Every PowerOffice GO Product will be synchronized with a Wave Product.

Once a link between a PowerOffice GO Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Wave Product Property
     - Wave Data Type


PowerOffice GO Salesorders to Wave Invoice
------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Wave Invoice.

Once a link between a PowerOffice GO Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Wave Invoice Property
     - Wave Data Type

