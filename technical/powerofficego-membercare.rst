====================================
PowerOfficeGO to MemberCare Dataflow
====================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to MemberCare Persons
-----------------------------------------------
Every PowerOffice Contactperson will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice Contactperson and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
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


PowerOffice Customers to MemberCare Companies
---------------------------------------------
Every PowerOffice Customers will be synchronized with a MemberCare Companies.

Once a link between a PowerOffice Customers and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"
   * - WebsiteUrl
     - url
     - "string"


PowerOffice Customers person to MemberCare Persons
--------------------------------------------------
Every PowerOffice Customers person will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
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


PowerOffice Departments to MemberCare Companies
-----------------------------------------------
Every PowerOffice Departments will be synchronized with a MemberCare Companies.

Once a link between a PowerOffice Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"


PowerOffice Employees to MemberCare Persons
-------------------------------------------
Every PowerOffice Employees will be synchronized with a MemberCare Persons.

Once a link between a PowerOffice Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
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


PowerOffice Product to MemberCare Products
------------------------------------------
Every PowerOffice Product will be synchronized with a MemberCare Products.

Once a link between a PowerOffice Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"


PowerOffice Salesorderlines to MemberCare Invoices
--------------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a PowerOffice Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - ProductUnitPrice
     - invoiceItems.unitPrice
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"


PowerOffice Salesorders to MemberCare Invoices
----------------------------------------------
Every PowerOffice Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a PowerOffice Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
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

