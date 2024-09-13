=========================================
PowerOffice GO to PowerOffice GO Dataflow
=========================================

Generated: 2024-09-13 00:00:27

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to PowerOffice GO Contactperson
------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a PowerOffice GO Contactperson must be established.

A PowerOffice GO Contactperson will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - PowerOffice GO Contactperson Property
   * - emailAddress
     - emailAddress
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a PowerOffice GO Contactperson and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


PowerOffice GO Contactperson to PowerOffice GO Customers person
---------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderline, Powerofficego-outgoinginvoice, or Powerofficego-salesorderlines that is synchronized into PowerOffice GO.

A PowerOffice GO Contactperson will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - PowerOffice GO Customers person Property
   * - emailAddress
     - EmailAddress

Once a link between a PowerOffice GO Contactperson and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
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


PowerOffice GO Customers person to PowerOffice GO Contactperson
---------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a PowerOffice GO Contactperson must be established.

A PowerOffice GO Customers person will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - PowerOffice GO Contactperson Property
   * - EmailAddress
     - emailAddress

Once a link between a PowerOffice GO Customers person and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


PowerOffice GO Customers person to PowerOffice GO Customers person
------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a PowerOffice GO Customers person must be established.

A PowerOffice GO Customers person will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - PowerOffice GO Customers person Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOffice GO Customers person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type


PowerOffice GO Customers to PowerOffice GO Customers
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a PowerOffice GO Customers must be established.

A PowerOffice GO Customers will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - PowerOffice GO Customers Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOffice GO Customers and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - Number
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - Number
     - "string"


PowerOffice GO Departments to PowerOffice GO Departments
--------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Departments and a PowerOffice GO Departments must be established.

A PowerOffice GO Departments will merge with a PowerOffice GO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - PowerOffice GO Departments Property
   * - Code
     - Code

Once a link between a PowerOffice GO Departments and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type


PowerOffice GO Employees to PowerOffice GO Employees
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Employees and a PowerOffice GO Employees must be established.

A PowerOffice GO Employees will merge with a PowerOffice GO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - PowerOffice GO Employees Property
   * - Id
     - Id
   * - Number
     - Number

Once a link between a PowerOffice GO Employees and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - DepartmentId (Dependant on having  in JobTitle)
     - JobTitle
     - "string"
   * - IsArchived
     - IsArchived
     - "boolean"
   * - JobTitle
     - DepartmentId (Dependant on having  in JobTitle)
     - "string"


PowerOffice GO Projectactivity to PowerOffice GO Projectactivity
----------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Projectactivity and a PowerOffice GO Projectactivity must be established.

A PowerOffice GO Projectactivity will merge with a PowerOffice GO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - PowerOffice GO Projectactivity Property
   * - activityCode
     - activityCode

Once a link between a PowerOffice GO Projectactivity and a PowerOffice GO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a PowerOffice GO Projectactivity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - PowerOffice GO Projectactivity Property
     - PowerOffice GO Data Type


PowerOffice GO Salesorders to PowerOffice GO Salesorders
--------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Salesorders and a PowerOffice GO Salesorders must be established.

A PowerOffice GO Salesorders will merge with a PowerOffice GO Salesorders if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - PowerOffice GO Salesorders Property
   * - Id
     - Id

Once a link between a PowerOffice GO Salesorders and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
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


PowerOffice GO Customers person to PowerOffice GO Customers
-----------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a PowerOffice GO Customers.

Once a link between a PowerOffice GO Customers person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


PowerOffice GO Customers to PowerOffice GO Customers person
-----------------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a PowerOffice GO Customers person.

Once a link between a PowerOffice GO Customers and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
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


PowerOffice GO Suppliers person to PowerOffice GO Contactperson
---------------------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a PowerOffice GO Contactperson.

Once a link between a PowerOffice GO Suppliers person and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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

