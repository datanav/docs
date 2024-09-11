=======================================
PowerOfficeGO to PowerOfficeGO Dataflow
=======================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to PowerOfficeGO Contactperson
----------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a PowerOfficeGO Contactperson must be established.

A PowerOfficeGO Contactperson will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Contactperson Property
   * - emailAddress
     - emailAddress
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a PowerOfficeGO Contactperson and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type


PowerOfficeGOPowerofficego Contactperson to PowerOfficeGOPowerOfficeGo Customers person
---------------------------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGOPowerofficego Contactperson and a PowerOfficeGOPowerOfficeGo Customers person must be established.

A new PowerOfficeGOPowerOfficeGo Customers person will be created from a PowerOfficeGOPowerofficego Contactperson if it is connected to a PowerOfficeGOPowerofficego Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderline, Powerofficego-outgoinginvoice, or Powerofficego-salesorderlines that is synchronized into PowerOfficeGOPowerOfficeGo.

A PowerOfficeGOPowerofficego Contactperson will merge with a PowerOfficeGOPowerOfficeGo Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficego Contactperson Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
   * - emailAddress
     - EmailAddress

Once a link between a PowerOfficeGOPowerofficego Contactperson and a PowerOfficeGOPowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficego Contactperson and a PowerOfficeGOPowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficego Contactperson Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
     - PowerOfficeGOPowerOfficeGo Data Type
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


PowerOfficeGO Customers person to PowerOfficeGO Contactperson
-------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers person and a PowerOfficeGO Contactperson must be established.

A PowerOfficeGO Customers person will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - PowerOfficeGO Contactperson Property
   * - EmailAddress
     - emailAddress

Once a link between a PowerOfficeGO Customers person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


PowerOfficeGO Customers person to PowerOfficeGO Customers person
----------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers person and a PowerOfficeGO Customers person must be established.

A PowerOfficeGO Customers person will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - PowerOfficeGO Customers person Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOfficeGO Customers person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type


PowerOfficeGO Customers to PowerOfficeGO Customers
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers and a PowerOfficeGO Customers must be established.

A PowerOfficeGO Customers will merge with a PowerOfficeGO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - PowerOfficeGO Customers Property
   * - EmailAddress
     - EmailAddress

Once a link between a PowerOfficeGO Customers and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
   * - Number
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - Number
     - "string"


PowerOfficeGO Departments to PowerOfficeGO Departments
------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Departments and a PowerOfficeGO Departments must be established.

A PowerOfficeGO Departments will merge with a PowerOfficeGO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - PowerOfficeGO Departments Property
   * - Code
     - Code

Once a link between a PowerOfficeGO Departments and a PowerOfficeGO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a PowerOfficeGO Departments:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - PowerOfficeGO Departments Property
     - PowerOfficeGO Data Type


PowerOfficeGO Employees to PowerOfficeGO Employees
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Employees and a PowerOfficeGO Employees must be established.

A PowerOfficeGO Employees will merge with a PowerOfficeGO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - PowerOfficeGO Employees Property
   * - Id
     - Id
   * - Number
     - Number

Once a link between a PowerOfficeGO Employees and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
   * - DepartmentId (Dependant on having  in JobTitle)
     - JobTitle
     - "string"
   * - IsArchived
     - IsArchived
     - "boolean"
   * - JobTitle
     - DepartmentId (Dependant on having  in JobTitle)
     - "string"


PowerOfficeGO Projectactivity to PowerOfficeGO Projectactivity
--------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Projectactivity and a PowerOfficeGO Projectactivity must be established.

A PowerOfficeGO Projectactivity will merge with a PowerOfficeGO Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Projectactivity Property
   * - activityCode
     - activityCode

Once a link between a PowerOfficeGO Projectactivity and a PowerOfficeGO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projectactivity and a PowerOfficeGO Projectactivity:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Data Type


PowerOfficeGO Salesorders to PowerOfficeGO Salesorders
------------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Salesorders and a PowerOfficeGO Salesorders must be established.

A PowerOfficeGO Salesorders will merge with a PowerOfficeGO Salesorders if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Salesorders Property
   * - Id
     - Id

Once a link between a PowerOfficeGO Salesorders and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorders and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - CustomerId
     - CustomerReferenceContactPersonId
     - "integer"
   * - CustomerReferenceContactPersonId
     - CustomerId
     - "integer"


PowerofficegoPowerOfficeGO Contactperson to PowerOfficeGoPowerOfficeGO Customers
--------------------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerofficegoPowerOfficeGO Contactperson and a PowerOfficeGoPowerOfficeGO Customers must be established.

A new PowerOfficeGoPowerOfficeGO Customers will be created from a PowerofficegoPowerOfficeGO Contactperson if it is connected to a PowerofficegoPowerOfficeGO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderline, Powerofficego-outgoinginvoice, or Powerofficego-salesorderlines that is synchronized into PowerOfficeGoPowerOfficeGO.

Once a link between a PowerofficegoPowerOfficeGO Contactperson and a PowerOfficeGoPowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerofficegoPowerOfficeGO Contactperson and a PowerOfficeGoPowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - PowerofficegoPowerOfficeGO Contactperson Property
     - PowerOfficeGoPowerOfficeGO Customers Property
     - PowerOfficeGoPowerOfficeGO Data Type
   * - residenceCountryCode
     - MailAddress.CountryCode
     - "string"


PowerofficegoPowerOfficeGO Customers to PowerOfficeGoPowerOfficeGO Contactperson
--------------------------------------------------------------------------------
Before any synchronization can take place, a link between a PowerofficegoPowerOfficeGO Customers and a PowerOfficeGoPowerOfficeGO Contactperson must be established.

A new PowerOfficeGoPowerOfficeGO Contactperson will be created from a PowerofficegoPowerOfficeGO Customers if it is connected to a PowerofficegoPowerOfficeGO Powerofficego-salesorder, or Powerofficego-salesorders that is synchronized into PowerOfficeGoPowerOfficeGO.

Once a link between a PowerofficegoPowerOfficeGO Customers and a PowerOfficeGoPowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerofficegoPowerOfficeGO Customers and a PowerOfficeGoPowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerofficegoPowerOfficeGO Customers Property
     - PowerOfficeGoPowerOfficeGO Contactperson Property
     - PowerOfficeGoPowerOfficeGO Data Type
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"


PowerOfficeGO Customers person to PowerOfficeGO Customers
---------------------------------------------------------
Every PowerOfficeGO Customers person will be synchronized with a PowerOfficeGO Customers.

Once a link between a PowerOfficeGO Customers person and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type


PowerOfficeGOPowerofficego Customers to PowerOfficeGOPowerOfficeGo Customers person
-----------------------------------------------------------------------------------
Every PowerOfficeGOPowerofficego Customers will be synchronized with a PowerOfficeGOPowerOfficeGo Customers person.

Once a link between a PowerOfficeGOPowerofficego Customers and a PowerOfficeGOPowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerofficego Customers and a PowerOfficeGOPowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerofficego Customers Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
     - PowerOfficeGOPowerOfficeGo Data Type
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


PowerOfficeGO Suppliers person to PowerOfficeGO Contactperson
-------------------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a PowerOfficeGO Suppliers person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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

