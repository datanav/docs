=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-11-29 15:05:23

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to PowerOfficeGo Contactperson
----------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a PowerOfficeGo Contactperson must be established.

A Powerofficego Contactperson will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Contactperson Property
   * - emailAddress
     - emailAddress
   * - SocialSecurityNumber
     - SocialSecurityNumber

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type


Powerofficego Currency to PowerOfficeGo Currency
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Currency and a PowerOfficeGo Currency must be established.

A Powerofficego Currency will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - PowerOfficeGo Currency Property
   * - code
     - code

Once a link between a Powerofficego Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Powerofficego Customers person to PowerOfficeGo Contactperson
-------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a PowerOfficeGo Contactperson must be established.

A Powerofficego Customers person will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - PowerOfficeGo Contactperson Property
   * - EmailAddress
     - emailAddress

Once a link between a Powerofficego Customers person and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - Id
     - id
     - "integer"
   * - IsPerson
     - residenceCountryCode
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


Powerofficego Customers to PowerOfficeGo Customers
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Customers must be established.

A Powerofficego Customers will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Customers Property
   * - EmailAddress
     - EmailAddress
   * - EmailAddress
     - InvoiceEmailAddress
   * - InvoiceEmailAddress
     - EmailAddress
   * - InvoiceEmailAddress
     - InvoiceEmailAddress
   * - EmailAddress
     - PaymentReminderEmailAddress
   * - PaymentReminderEmailAddress
     - EmailAddress
   * - InvoiceEmailAddress
     - PaymentReminderEmailAddress
   * - PaymentReminderEmailAddress
     - InvoiceEmailAddress
   * - PaymentReminderEmailAddress
     - PaymentReminderEmailAddress

Once a link between a Powerofficego Customers and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Powerofficego Employees to PowerOfficeGo Employees
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employees and a PowerOfficeGo Employees must be established.

A Powerofficego Employees will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Employees Property
   * - Id
     - Id
   * - Number
     - Number

Once a link between a Powerofficego Employees and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type


Powerofficego Salesorders to PowerOfficeGo Salesorders
------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorders and a PowerOfficeGo Salesorders must be established.

A Powerofficego Salesorders will merge with a PowerOfficeGo Salesorders if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Salesorders Property
   * - Id
     - Id

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type


Powerofficego Contactperson to PowerOfficeGo Customers person
-------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Salesorder, Salesorders, Salesorderline, Outgoinginvoice, or Salesorderlines that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Contactperson and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
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
     - "datetime-format","%Y-%m-%d","_."]
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


Powerofficego Customers to PowerOfficeGo Customers person
---------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customer, Customers, Suppliers, Salesorder, Salesorders, Contactperson, Salesorderline, Outgoinginvoice, Salesorderlines, Customers-person, or Suppliers-person that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Customers and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
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


Powerofficego Suppliers person to PowerOfficeGo Contactperson
-------------------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Suppliers person and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"

