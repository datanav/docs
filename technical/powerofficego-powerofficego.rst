========================================
PowerOfficeGO to PowerOffice GO Dataflow
========================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to PowerOffice Contactperson
------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a PowerOffice Contactperson must be established.

A PowerOffice Contactperson will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - PowerOffice Contactperson Property
   * - emailAddress
     - emailAddress
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a PowerOffice Contactperson and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type


PowerOffice Contactperson to PowerOffice Customers person
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a PowerOffice Contactperson if it is connected to a PowerOffice Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderline, Powerofficego-outgoinginvoice, or Powerofficego-salesorderlines that is synchronized into PowerOffice.

A PowerOffice Contactperson will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - PowerOffice Customers person Property
   * - emailAddress
     - EmailAddress

Once a link between a PowerOffice Contactperson and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - address1
     - MailAddress.AddressLine1
     - "string"
   * - address2
     - MailAddress.AddressLine2
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - N/A
   * - emailAddress
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - LastName
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - residenceCountryCode
     - MailAddress.CountryCode
     - "string"
   * - zipCode
     - MailAddress.ZipCode
     - "string"


PowerOffice Customers person to PowerOffice Contactperson
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers person and a PowerOffice Contactperson must be established.

A PowerOffice Customers person will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - PowerOffice Contactperson Property
   * - EmailAddress
     - emailAddress

Once a link between a PowerOffice Customers person and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - DateOfBirth
     - dateOfBirth
     - N/A
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
   * - IsPerson
     - residenceCountryCode
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.AddressLine1
     - address1
     - "string"
   * - MailAddress.AddressLine2
     - address2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"
   * - MailAddress.ZipCode
     - zipCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


PowerOffice Customers person to PowerOffice Customers person
------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers person and a PowerOffice Customers person must be established.

A PowerOffice Customers person will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - PowerOffice Customers person Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOffice Customers person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type


PowerOffice Customers to PowerOffice Customers
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers and a PowerOffice Customers must be established.

A PowerOffice Customers will merge with a PowerOffice Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - PowerOffice Customers Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOffice Customers and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
   * - Number
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - Number
     - "string"


PowerOffice Departments to PowerOffice Departments
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Departments and a PowerOffice Departments must be established.

A PowerOffice Departments will merge with a PowerOffice Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - PowerOffice Departments Property
   * - Code
     - Code

Once a link between a PowerOffice Departments and a PowerOffice Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a PowerOffice Departments:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - PowerOffice Departments Property
     - PowerOffice Data Type


PowerOffice Employees to PowerOffice Employees
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Employees and a PowerOffice Employees must be established.

A PowerOffice Employees will merge with a PowerOffice Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
     - PowerOffice Employees Property
   * - Id
     - Id
   * - Number
     - Number

Once a link between a PowerOffice Employees and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
   * - DepartmentId (Dependant on having  in JobTitle)
     - JobTitle
     - "string"
   * - IsArchived
     - IsArchived
     - "boolean"
   * - JobTitle
     - DepartmentId (Dependant on having  in JobTitle)
     - "string"


PowerOffice Salesorders to PowerOffice Salesorders
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Salesorders and a PowerOffice Salesorders must be established.

A PowerOffice Salesorders will merge with a PowerOffice Salesorders if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
     - PowerOffice Salesorders Property
   * - Id
     - Id

Once a link between a PowerOffice Salesorders and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - CustomerId
     - CustomerReferenceContactPersonId
     - "integer"
   * - CustomerReferenceContactPersonId
     - CustomerId
     - "integer"


Powerofficego Contactperson to PowerOfficeGo Customers
------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderline, Outgoinginvoice, or Salesorderlines that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - residenceCountryCode
     - MailAddress.CountryCode
     - "string"


Powerofficego Customers to PowerOfficeGo Contactperson
------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Contactperson must be established.

A new PowerOfficeGo Contactperson will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, or Salesorders that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Customers and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"


PowerOffice Customers person to PowerOffice Customers
-----------------------------------------------------
Every PowerOffice Customers person will be synchronized with a PowerOffice Customers.

Once a link between a PowerOffice Customers person and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - PowerOffice Customers Property
     - PowerOffice Data Type


PowerOffice Customers to PowerOffice Customers person
-----------------------------------------------------
Every PowerOffice Customers will be synchronized with a PowerOffice Customers person.

Once a link between a PowerOffice Customers and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - Id
     - Id
     - "string"
   * - IsPerson
     - IsPerson
     - "string"
   * - IsPerson
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.AddressLine1
     - MailAddress.AddressLine1
     - "string"
   * - MailAddress.AddressLine2
     - MailAddress.AddressLine2
     - "string"
   * - MailAddress.City
     - MailAddress.City
     - "string"
   * - MailAddress.CountryCode
     - IsPerson
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.LastChangedDateTimeOffset
     - MailAddress.LastChangedDateTimeOffset
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.ZipCode
     - "string"


PowerOffice Suppliers person to PowerOffice Contactperson
---------------------------------------------------------
Every PowerOffice Suppliers person will be synchronized with a PowerOffice Contactperson.

Once a link between a PowerOffice Suppliers person and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Suppliers person and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice Suppliers person Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - DateOfBirth
     - dateOfBirth
     - N/A
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

