=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-08-15 10:40:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to PowerOfficeGo Employees
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a PowerOfficeGo Employees must be established.

A Powerofficego Customers will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Employees Property
   * - NationalIdNumber
     - NationalIdNumber

Once a link between a Powerofficego Customers and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.city
     - MailAddress.City
     - "string"
   * - MailAddress.countryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.lastChangedDateTimeOffset
     - MailAddress.LastChanged
     - "string"
   * - MailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - NationalIdNumber
     - NationalIdNumber
     - "string"
   * - id
     - Id
     - "string"
   * - mailAddress.lastChangedDateTimeOffset
     - MailAddress.LastChanged
     - "string"
   * - mailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"


Powerofficego Employees to PowerOfficeGo Customers
--------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employees and a PowerOfficeGo Customers must be established.

A Powerofficego Employees will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Customers Property
   * - NationalIdNumber
     - NationalIdNumber

Once a link between a Powerofficego Employees and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - MailAddress.city
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.LastChanged
     - MailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.LastChanged
     - mailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.zipCode
     - "string"
   * - MailAddress.ZipCode
     - mailAddress.zipCode
     - "string"
   * - NationalIdNumber
     - NationalIdNumber
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - streetAddresses.countryCode
     - "string"
   * - streetAddresses.lastChanged
     - streetAddresses.lastChanged
     - "string"
   * - streetAddresses.zipCode
     - streetAddresses.zipCode
     - "string"


Powerofficego Supplier to PowerOfficeGo Address
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Address must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


Powerofficego Suppliers to PowerOfficeGo Address
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGo Address must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


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
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - TotalAmount
     - NetAmount
     - "string"

