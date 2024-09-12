=====================================
PowerOffice GO to MemberCare Dataflow
=====================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to MemberCare Persons
--------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice GO Contactperson and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


PowerOffice GO Customers to MemberCare Companies
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a MemberCare Companies.

Once a link between a PowerOffice GO Customers and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"
   * - WebsiteUrl
     - url
     - "string"


PowerOffice GO Customers person to MemberCare Persons
-----------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice GO Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


PowerOffice GO Departments to MemberCare Companies
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a MemberCare Companies.

Once a link between a PowerOffice GO Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"


PowerOffice GO Employees to MemberCare Persons
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice GO Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


PowerOffice GO Product to MemberCare Products
---------------------------------------------
Every PowerOffice GO Product will be synchronized with a MemberCare Products.

Once a link between a PowerOffice GO Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


PowerOffice GO Salesorderlines to MemberCare Invoices
-----------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a PowerOffice GO Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - ProductUnitPrice
     - invoiceItems.unitPrice
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"


PowerOffice GO Salesorders to MemberCare Invoices
-------------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a PowerOffice GO Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


PowerOffice GO Contactperson to MemberCare Countries
----------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Contactperson and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - residenceCountryCode
     - iso2Letter
     - "string"


PowerOffice GO Customers to MemberCare Countries
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Customers and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - MailAddress.CountryCode
     - iso2Letter
     - "string"


PowerOffice GO Location to MemberCare Countries
-----------------------------------------------
Every PowerOffice GO Location will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Location and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Location and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Location Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOffice GO Outgoinginvoices to MemberCare Countries
-------------------------------------------------------
Every PowerOffice GO Outgoinginvoices will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Outgoinginvoices and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Outgoinginvoices and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Outgoinginvoices Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOffice GO Suppliers to MemberCare Countries
------------------------------------------------
Every PowerOffice GO Suppliers will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Suppliers and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOffice GO Suppliers person to MemberCare Countries
-------------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a MemberCare Countries.

Once a link between a PowerOffice GO Suppliers person and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - MemberCare Countries Property
     - MemberCare Data Type

