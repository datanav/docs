====================================
Powerofficego to Membercare Dataflow
====================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Membercare Persons
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Membercare Persons.

Once a link between a Powerofficego Contactperson and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Membercare Persons Property
     - Membercare Data Type
   * - SocialSecurityNumber
     - socialSecurityNumber.number (Dependant on having wd:Q1140371 in socialSecurityNumber.iso2Letter)
     - "string"
   * - city
     - addresses.postalCode.city
     - "string"
   * - dateOfBirth
     - birthDate
     - "string"
   * - emailAddress
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - firstName
     - firstname
     - "string"
   * - id
     - addresses.id
     - "string"
   * - lastName
     - lastname
     - "string"
   * - residenceCountryCode
     - addresses.country.id
     - "string"
   * - zipCode
     - addresses.postalCode.zipCode
     - "string"


Powerofficego Customers to Membercare Companies
-----------------------------------------------
Every Powerofficego Customers will be synchronized with a Membercare Companies.

Once a link between a Powerofficego Customers and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Name
     - companyName
     - "string"
   * - WebsiteUrl
     - url
     - "string"


Powerofficego Customers person to Membercare Persons
----------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Membercare Persons.

Once a link between a Powerofficego Customers person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Membercare Persons Property
     - Membercare Data Type
   * - DateOfBirth
     - birthDate
     - "string"
   * - EmailAddress
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - Id
     - addresses.id
     - "string"
   * - LastName
     - lastname
     - "string"
   * - MailAddress.City
     - addresses.postalCode.city
     - "string"
   * - MailAddress.CountryCode
     - addresses.country.id
     - "string"
   * - MailAddress.ZipCode
     - addresses.postalCode.zipCode
     - "string"


Powerofficego Departments to Membercare Companies
-------------------------------------------------
Every Powerofficego Departments will be synchronized with a Membercare Companies.

Once a link between a Powerofficego Departments and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Name
     - companyName
     - "string"


Powerofficego Employees to Membercare Persons
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Membercare Persons.

Once a link between a Powerofficego Employees and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Membercare Persons Property
     - Membercare Data Type
   * - DateOfBirth
     - birthDate
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - Id
     - socialSecurityNumber.number (Dependant on having poweroffice-employee in socialSecurityNumber.iso2Letter)
     - "string"
   * - LastName
     - lastname
     - "string"
   * - Number
     - socialSecurityNumber.number (Dependant on having wd:Q36218176 in socialSecurityNumber.iso2Letter)
     - "string"


Powerofficego Product to Membercare Products
--------------------------------------------
Every Powerofficego Product will be synchronized with a Membercare Products.

Once a link between a Powerofficego Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"


Powerofficego Salesorderlines to Membercare Invoices
----------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Membercare Invoices.

Once a link between a Powerofficego Salesorderlines and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - ProductUnitPrice
     - invoiceItems.unitPrice
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"


Powerofficego Salesorders to Membercare Invoices
------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Membercare Invoices.

Once a link between a Powerofficego Salesorders and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Membercare Invoices Property
     - Membercare Data Type


Powerofficego Contactperson to Membercare Countries
---------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Contactperson and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Membercare Countries Property
     - Membercare Data Type
   * - residenceCountryCode
     - iso2Letter
     - "string"


Powerofficego Customers to Membercare Countries
-----------------------------------------------
Every Powerofficego Customers will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Customers and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Membercare Countries Property
     - Membercare Data Type
   * - MailAddress.CountryCode
     - iso2Letter
     - "string"


Powerofficego Location to Membercare Countries
----------------------------------------------
Every Powerofficego Location will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Location and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     - Membercare Countries Property
     - Membercare Data Type


Powerofficego Outgoinginvoices to Membercare Countries
------------------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Outgoinginvoices and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     - Membercare Countries Property
     - Membercare Data Type


Powerofficego Suppliers to Membercare Countries
-----------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Suppliers and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Membercare Countries Property
     - Membercare Data Type


Powerofficego Suppliers person to Membercare Countries
------------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Membercare Countries.

Once a link between a Powerofficego Suppliers person and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Membercare Countries Property
     - Membercare Data Type

