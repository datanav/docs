=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-11-29 14:34:53

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Powerofficego Customer to PowerOfficeGo Departments
---------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee, or Customers that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Customer and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type


Powerofficego Customers to PowerOfficeGo Customers person
---------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Powerofficego Customers if it is connected to a Powerofficego Customers, Suppliers, Salesorder, Salesorders, Salesorderline, Outgoinginvoice, Salesorderlines, Customers-person, or Suppliers-person that is synchronized into PowerOfficeGo.

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


Powerofficego Customers to PowerOfficeGo Departments
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Powerofficego Customers if it is connected to a Powerofficego Employee, or Customers that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Customers and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - Name
     - Name
     - "string"


Powerofficego Departments to PowerOfficeGo Customers person
-----------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Departments and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Powerofficego Departments if it is connected to a Powerofficego Customers, Suppliers, Customers-person, or Suppliers-person that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Departments and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


Powerofficego Departments to PowerOfficeGo Customers
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Departments and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Powerofficego Departments if it is connected to a Powerofficego Customers, Suppliers, Customers-person, or Suppliers-person that is synchronized into PowerOfficeGo.

Once a link between a Powerofficego Departments and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - Name
     - Name
     - "string"


Powerofficego Salesorder to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------
Every Powerofficego Salesorder will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorder and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - Currency
     - CurrencyCode
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DeliveryDate
     - sentDateTimeOffset
     - "string"
   * - DepartmentCode
     - customerId
     - "string"
   * - OrderDate
     - OrderDate
     - "string"


Powerofficego Salesorderline to PowerOfficeGo Outgoinginvoices
--------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorderline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type


Powerofficego Salesorderlines to PowerOfficeGo Outgoinginvoices
---------------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorderlines and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - TotalAmount
     - NetAmount
     - "string"
   * - sesam_SalesOrderId
     - OrderNo
     - "string"
   * - sesam_SalesOrdersId
     - OrderNo
     - "string"


Powerofficego Salesorders to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------
Every Powerofficego Salesorders will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - CreatedDateTimeOffset
     - createdDateTimeOffset
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - CustomerReferenceContactPersonId
     - customerId
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - SalesOrderDate
     - OrderDate
     - "string"
   * - TotalAmount
     - NetAmount
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

