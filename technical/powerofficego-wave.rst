==============================
Powerofficego to Wave Dataflow
==============================

Generated: 2023-10-05 08:39:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Wave Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customers, Employees, Suppliers, Salesorder, Departments, Salesorders, Contactperson, Salesorderlines, or Outgoinginvoices that is synchronized into Wave.

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


Powerofficego Departments to Wave Customer person
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Departments and a Wave Customer person must be established.

A new Wave Customer person will be created from a Powerofficego Departments if it is connected to a Powerofficego Customers, Employees, Suppliers, Departments, or Contactperson that is synchronized into Wave.

Once a link between a Powerofficego Departments and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Wave Customer person Property
     - Wave Data Type


Powerofficego Departments to Wave Customer
------------------------------------------
Every Powerofficego Departments will be synchronized with a Wave Customer.

Once a link between a Powerofficego Departments and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Wave Customer Property
     - Wave Data Type
   * - Name
     - name
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]


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


Powerofficego Outgoinginvoices to Wave Invoice
----------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a Wave Invoice.

Once a link between a Powerofficego Outgoinginvoices and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     - Wave Invoice Property
     - Wave Data Type


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


Powerofficego Salesorderlines to Wave Invoice
---------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Wave Invoice.

Once a link between a Powerofficego Salesorderlines and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Wave Invoice Property
     - Wave Data Type


Powerofficego Suppliers to Wave Customer
----------------------------------------
Every Powerofficego Suppliers will be synchronized with a Wave Customer.

Once a link between a Powerofficego Suppliers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Wave Customer Property
     - Wave Data Type

