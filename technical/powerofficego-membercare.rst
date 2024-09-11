=====================================
PowerOffice GO to MemberCare Dataflow
=====================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to MemberCare Persons
-------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a MemberCare Persons.

Once a link between a PowerOfficeGO Contactperson and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
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


PowerOfficeGO Customers to MemberCare Companies
-----------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a MemberCare Companies.

Once a link between a PowerOfficeGO Customers and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"
   * - WebsiteUrl
     - url
     - "string"


PowerOfficeGO Customers person to MemberCare Persons
----------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a MemberCare Persons.

Once a link between a PowerOfficeGO Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
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


PowerOfficeGO Departments to MemberCare Companies
-------------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a MemberCare Companies.

Once a link between a PowerOfficeGO Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"


PowerOfficeGO Employees to MemberCare Persons
---------------------------------------------
Every PowerOfficeGO Employees will be synchronized with a MemberCare Persons.

Once a link between a PowerOfficeGO Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
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


PowerOfficeGO Product to MemberCare Products
--------------------------------------------
Every PowerOfficeGO Product will be synchronized with a MemberCare Products.

Once a link between a PowerOfficeGO Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


PowerOfficeGO Salesorderlines to MemberCare Invoices
----------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a PowerOfficeGO Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - ProductUnitPrice
     - invoiceItems.unitPrice
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"


PowerOfficeGO Salesorders to MemberCare Invoices
------------------------------------------------
Every PowerOfficeGO Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a PowerOfficeGO Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


PowerOfficeGO Contactperson to MemberCare Countries
---------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Contactperson and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - residenceCountryCode
     - iso2Letter
     - "string"


PowerOfficeGO Customers to MemberCare Countries
-----------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Customers and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - MailAddress.CountryCode
     - iso2Letter
     - "string"


PowerOfficeGO Location to MemberCare Countries
----------------------------------------------
Every PowerOfficeGO Location will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Location and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Location and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Location Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOfficeGO Outgoinginvoices to MemberCare Countries
------------------------------------------------------
Every PowerOfficeGO Outgoinginvoices will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Outgoinginvoices and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Outgoinginvoices and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Outgoinginvoices Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOfficeGO Suppliers to MemberCare Countries
-----------------------------------------------
Every PowerOfficeGO Suppliers will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Suppliers and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers Property
     - MemberCare Countries Property
     - MemberCare Data Type


PowerOfficeGO Suppliers person to MemberCare Countries
------------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a MemberCare Countries.

Once a link between a PowerOfficeGO Suppliers person and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - MemberCare Countries Property
     - MemberCare Data Type

