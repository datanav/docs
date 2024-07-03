=======================================
Powerofficego to Powerofficego Dataflow
=======================================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Powerofficego Contactperson
----------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Powerofficego Contactperson must be established.

A Powerofficego Contactperson will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Powerofficego Contactperson Property
   * - emailAddress
     - emailAddress
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a Powerofficego Contactperson and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


Powerofficego Contactperson to Powerofficego Customers person
-------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderline, Outgoinginvoice, or Salesorderlines that is synchronized into Powerofficego.

A Powerofficego Contactperson will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Powerofficego Customers person Property
   * - emailAddress
     - EmailAddress

Once a link between a Powerofficego Contactperson and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
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


Powerofficego Customers person to Powerofficego Contactperson
-------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a Powerofficego Contactperson must be established.

A Powerofficego Customers person will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Powerofficego Contactperson Property
   * - EmailAddress
     - emailAddress

Once a link between a Powerofficego Customers person and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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


Powerofficego Customers person to Powerofficego Customers person
----------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a Powerofficego Customers person must be established.

A Powerofficego Customers person will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Powerofficego Customers person Property
   * - EmailAddress
     - EmailAddress

Once a link between a Powerofficego Customers person and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type


Powerofficego Customers to Powerofficego Customers
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Powerofficego Customers must be established.

A Powerofficego Customers will merge with a Powerofficego Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Powerofficego Customers Property
   * - EmailAddress
     - EmailAddress

Once a link between a Powerofficego Customers and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - Number
     - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - "string"
   * - OrganizationNumber (Dependant on having wd:Q852835 in MailAddress.CountryCodeDependant on having wd:Q852835 in MailAddress.CountryCode)
     - Number
     - "string"


Powerofficego Departments to Powerofficego Departments
------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Departments and a Powerofficego Departments must be established.

A Powerofficego Departments will merge with a Powerofficego Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Powerofficego Departments Property
   * - Code
     - Code

Once a link between a Powerofficego Departments and a Powerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Powerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Powerofficego Departments Property
     - Powerofficego Data Type


Powerofficego Employees to Powerofficego Employees
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employees and a Powerofficego Employees must be established.

A Powerofficego Employees will merge with a Powerofficego Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Powerofficego Employees Property
   * - Id
     - Id
   * - Number
     - Number

Once a link between a Powerofficego Employees and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
   * - DepartmentId (Dependant on having  in JobTitle)
     - JobTitle
     - "string"
   * - IsArchived
     - IsArchived
     - "boolean"
   * - JobTitle
     - DepartmentId (Dependant on having  in JobTitle)
     - "string"


Powerofficego Salesorders to Powerofficego Salesorders
------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorders and a Powerofficego Salesorders must be established.

A Powerofficego Salesorders will merge with a Powerofficego Salesorders if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Powerofficego Salesorders Property
   * - Id
     - Id

Once a link between a Powerofficego Salesorders and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
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


Powerofficego Customers person to Powerofficego Customers
---------------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Powerofficego Customers.

Once a link between a Powerofficego Customers person and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Powerofficego Customers Property
     - Powerofficego Data Type


Powerofficego Customers to Powerofficego Customers person
---------------------------------------------------------
Every Powerofficego Customers will be synchronized with a Powerofficego Customers person.

Once a link between a Powerofficego Customers and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
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


Powerofficego Suppliers person to Powerofficego Contactperson
-------------------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Powerofficego Contactperson.

Once a link between a Powerofficego Suppliers person and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
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

