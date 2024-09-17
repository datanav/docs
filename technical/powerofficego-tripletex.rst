====================================
PowerOffice GO to Tripletex Dataflow
====================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Tripletex Contact
-------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-projects, Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Tripletex.

A PowerOffice GO Contactperson will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Contact Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type


PowerOffice GO Contactperson to Tripletex Customer person
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-outgoinginvoice, Powerofficego-salesorderlines, or Powerofficego-outgoinginvoices that is synchronized into Tripletex.

A PowerOffice GO Contactperson will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Customer person Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - address1
     - deliveryAddress.addressLine1
     - "string"
   * - address1
     - physicalAddress.addressLine1
     - "string"
   * - address1
     - postalAddress.addressLine1
     - "string"
   * - address2
     - deliveryAddress.addressLine2
     - "string"
   * - address2
     - physicalAddress.addressLine2
     - "string"
   * - address2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - emailAddress
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - residenceCountryCode
     - deliveryAddress.country.id
     - "string"
   * - residenceCountryCode
     - physicalAddress.country.id
     - "integer"
   * - residenceCountryCode
     - postalAddress.country.id
     - "integer"
   * - zipCode
     - deliveryAddress.postalCode
     - "string"
   * - zipCode
     - physicalAddress.postalCode
     - "string"
   * - zipCode
     - postalAddress.postalCode
     - "string"


PowerOffice GO Contactperson to Tripletex Employee
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Tripletex Employee must be established.

A PowerOffice GO Contactperson will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Employee Property
   * - emailAddress
     - email
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a PowerOffice GO Contactperson and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - N/A
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - partyId
     - department.id (Dependant on having wd:Q703534 in  )
     - N/A
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - residenceCountryCode
     - address.country.id
     - "integer"
   * - zipCode
     - address.postalCode
     - "string"


PowerOffice GO Customers person to Tripletex Contact
----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tripletex Contact must be established.

A PowerOffice GO Customers person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Contact Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


PowerOffice GO Customers person to Tripletex Customer person
------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tripletex Customer person must be established.

A PowerOffice GO Customers person will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer person Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


PowerOffice GO Customers person to Tripletex Employee
-----------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Tripletex Employee must be established.

A PowerOffice GO Customers person will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Employee Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - DateOfBirth
     - dateOfBirth
     - N/A
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "integer"
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
     - address.country.id
     - "integer"
   * - MailAddress.ZipCode
     - address.postalCode
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-customer, Powerofficego-projects, Powerofficego-customers, Powerofficego-suppliers, Powerofficego-salesorder, Powerofficego-salesorders, Powerofficego-contactperson, Powerofficego-outgoinginvoice, Powerofficego-salesorderlines, Powerofficego-customers-person, Powerofficego-outgoinginvoices, or Powerofficego-suppliers-person that is synchronized into Tripletex.

A PowerOffice GO Customers will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


PowerOffice GO Departments to Tripletex Department
--------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Departments and a Tripletex Department must be established.

A new Tripletex Department will be created from a PowerOffice GO Departments if it is connected to a PowerOffice GO Powerofficego-employee, Powerofficego-projects, Powerofficego-employees, Powerofficego-contactperson, or Powerofficego-customers-person that is synchronized into Tripletex.

A PowerOffice GO Departments will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
   * - Code
     - departmentNumber

Once a link between a PowerOffice GO Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
     - Tripletex Data Type


PowerOffice GO Employees to Tripletex Employee
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Employees and a Tripletex Employee must be established.

A PowerOffice GO Employees will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
   * - Number
     - employeeNumber

Once a link between a PowerOffice GO Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type


PowerOffice GO Timetrackingactivity to Tripletex Activity
---------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Timetrackingactivity and a Tripletex Activity must be established.

A new Tripletex Activity will be created from a PowerOffice GO Timetrackingactivity if it is connected to a PowerOffice GO Powerofficego-projectactivity, or Powerofficego-timetrackingactivity that is synchronized into Tripletex.

A PowerOffice GO Timetrackingactivity will merge with a Tripletex Activity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Activity Property
   * - code
     - id

Once a link between a PowerOffice GO Timetrackingactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type


PowerOffice GO Timetrackingactivity to Tripletex Projectactivity
----------------------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Timetrackingactivity and a Tripletex Projectactivity must be established.

A PowerOffice GO Timetrackingactivity will merge with a Tripletex Projectactivity if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Projectactivity Property
   * - code
     - activity.id

Once a link between a PowerOffice GO Timetrackingactivity and a Tripletex Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Tripletex Projectactivity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Projectactivity Property
     - Tripletex Data Type


Powerofficego Contactperson to Tripletex Customer
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Outgoinginvoice, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Contactperson and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - residenceCountryCode
     - invoiceSendMethod
     - "string"


Powerofficego Customers to Tripletex Contact
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Customer person
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customer, Projects, Customers, Suppliers, Salesorder, Salesorders, Contactperson, Outgoinginvoice, Salesorderlines, Customers-person, Outgoinginvoices, or Suppliers-person that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Powerofficego Product to Tripletex Product
------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product and a Tripletex Product must be established.

A new Tripletex Product will be created from a Powerofficego Product if it is connected to a Powerofficego Salesorderline, or Salesorderlines that is synchronized into Tripletex.

Once a link between a Powerofficego Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Product Property
     - Tripletex Data Type


PowerOffice GO Projects to Tripletex Project
--------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Projects and a Tripletex Project must be established.

A new Tripletex Project will be created from a PowerOffice GO Projects if it is connected to a PowerOffice GO Powerofficego-projects, Powerofficego-projectactivity, or Powerofficego-timetrackingactivity that is synchronized into Tripletex.

Once a link between a PowerOffice GO Projects and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Tripletex Project Property
     - Tripletex Data Type


Powerofficego Salesorders to Tripletex Order
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorders and a Tripletex Order must be established.

A new Tripletex Order will be created from a Powerofficego Salesorders if it is connected to a Powerofficego Salesorderline, Outgoinginvoice, Salesorderlines, or Outgoinginvoices that is synchronized into Tripletex.

Once a link between a Powerofficego Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type


PowerOffice GO Contactperson to Tripletex Contact
-------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Tripletex Contact.

Once a link between a PowerOffice GO Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type


PowerOffice GO Customers person to Tripletex Customer
-----------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Tripletex Customer.

Once a link between a PowerOffice GO Customers person and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer Property
     - Tripletex Data Type


PowerOffice GO Customers person to Tripletex Customer person
------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Tripletex Customer person.

Once a link between a PowerOffice GO Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


PowerOffice GO Customers person to Tripletex Customer person
------------------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Tripletex Customer person.

Once a link between a PowerOffice GO Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer
----------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer.

Once a link between a PowerOffice GO Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer person
-----------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer person.

Once a link between a PowerOffice GO Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


PowerOffice GO Customers to Tripletex Customer person
-----------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Tripletex Customer person.

Once a link between a PowerOffice GO Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


PowerOffice GO Departments to Tripletex Department
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Tripletex Department.

Once a link between a PowerOffice GO Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Tripletex Department Property
     - Tripletex Data Type


PowerOffice GO Employees to Tripletex Employee
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Tripletex Employee.

Once a link between a PowerOffice GO Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type


PowerOffice GO Product to Tripletex Product
-------------------------------------------
Every PowerOffice GO Product will be synchronized with a Tripletex Product.

Once a link between a PowerOffice GO Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Tripletex Product Property
     - Tripletex Data Type


PowerOffice GO Projectactivity to Tripletex Activity
----------------------------------------------------
Every PowerOffice GO Projectactivity will be synchronized with a Tripletex Activity.

Once a link between a PowerOffice GO Projectactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type


PowerOffice GO Projects to Tripletex Project
--------------------------------------------
Every PowerOffice GO Projects will be synchronized with a Tripletex Project.

Once a link between a PowerOffice GO Projects and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Tripletex Project Property
     - Tripletex Data Type


PowerOffice GO Salesorderlines to Tripletex Orderline
-----------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a PowerOffice GO Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


PowerOffice GO Salesorders to Tripletex Order
---------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Tripletex Order.

Once a link between a PowerOffice GO Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type


PowerOffice GO Suppliers person to Tripletex Contact
----------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Tripletex Contact.

Once a link between a PowerOffice GO Suppliers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Tripletex Contact Property
     - Tripletex Data Type


PowerOffice GO Timetrackingactivity to Tripletex Activity
---------------------------------------------------------
Every PowerOffice GO Timetrackingactivity will be synchronized with a Tripletex Activity.

Once a link between a PowerOffice GO Timetrackingactivity and a Tripletex Activity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Tripletex Activity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Tripletex Activity Property
     - Tripletex Data Type

