=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-11-23 14:48:49

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to PowerOfficeGo Customers
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a PowerOfficeGo Customers must be established.

A Powerofficego Customer will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Customers Property
   * - id
     - Id

Once a link between a Powerofficego Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Customers Property
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
     - "datetime-format","%Y-%m-%d","_."]
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.AddressLine1
     - MailAddress.address1
     - "string"
   * - MailAddress.AddressLine2
     - MailAddress.address2
     - "string"
   * - MailAddress.City
     - MailAddress.city
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.CountryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.LastChangedDateTimeOffset
     - MailAddress.lastChanged
     - "string"
   * - MailAddress.ZipCode
     - MailAddress.zipCode
     - "string"
   * - MailAddress.addressLine1
     - MailAddress.Address1
     - "string"
   * - MailAddress.addressLine1
     - MailAddress.address1
     - "string"
   * - MailAddress.addressLine2
     - MailAddress.Address2
     - "string"
   * - MailAddress.addressLine2
     - MailAddress.address2
     - "string"
   * - MailAddress.city
     - MailAddress.City
     - "string"
   * - MailAddress.city
     - MailAddress.city
     - "string"
   * - MailAddress.countryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.countryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.lastChangedDateTimeOffset
     - MailAddress.LastChanged
     - "string"
   * - MailAddress.lastChangedDateTimeOffset
     - MailAddress.lastChanged
     - "string"
   * - MailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - MailAddress.zipCode
     - MailAddress.zipCode
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
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
     - "string"
   * - streetAddresses.city
     - streetAddresses.city
     - "string"
   * - streetAddresses.countryCode
     - MailAddress.countryCode
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


Powerofficego Employee to PowerOfficeGo Employees
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employee and a PowerOfficeGo Employees must be established.

A Powerofficego Employee will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGo Employees Property
   * - Id
     - Id
   * - id
     - Id

Once a link between a Powerofficego Employee and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type


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
     - "datetime-format","%Y-%m-%d","_."]
   * - FirstName
     - FirstName
     - "string"
   * - Id
     - Id
     - "string"
   * - Id
     - id
     - "string"
   * - InternationalIdNumber (Dependant on having wd:Q56404156 in InternationalIdType)
     - NationalIdNumber
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.Address1
     - MailAddress.addressLine1
     - "string"
   * - MailAddress.Address2
     - MailAddress.addressLine2
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
   * - MailAddress.address1
     - MailAddress.AddressLine1
     - "string"
   * - MailAddress.address1
     - MailAddress.addressLine1
     - "string"
   * - MailAddress.address2
     - MailAddress.AddressLine2
     - "string"
   * - MailAddress.address2
     - MailAddress.addressLine2
     - "string"
   * - MailAddress.city
     - MailAddress.City
     - "string"
   * - MailAddress.city
     - MailAddress.city
     - "string"
   * - MailAddress.countryCode
     - MailAddress.CountryCode
     - "string"
   * - MailAddress.countryCode
     - MailAddress.countryCode
     - "string"
   * - MailAddress.countryCode
     - streetAddresses.countryCode
     - "string"
   * - MailAddress.lastChanged
     - MailAddress.LastChangedDateTimeOffset
     - "string"
   * - MailAddress.lastChanged
     - MailAddress.lastChangedDateTimeOffset
     - "string"
   * - MailAddress.zipCode
     - MailAddress.ZipCode
     - "string"
   * - MailAddress.zipCode
     - MailAddress.zipCode
     - "string"
   * - NationalIdNumber
     - NationalIdNumber
     - "string"
   * - streetAddresses.address1
     - streetAddresses.address1
     - "string"
   * - streetAddresses.address2
     - streetAddresses.address2
     - "string"
   * - streetAddresses.address3
     - streetAddresses.address3
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


Powerofficego Outgoinginvoice to PowerOfficeGo Outgoinginvoices
---------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices must be established.

A Powerofficego Outgoinginvoice will merge with a PowerOfficeGo Outgoinginvoices if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGo Outgoinginvoices Property
   * - Id
     - Id

Once a link between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoice and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoice Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - CreatedDate
     - createdDateTimeOffset
     - "string"
   * - CurrencyCode
     - CurrencyCode
     - "string"
   * - CustomerCode
     - customerId
     - "string"
   * - CustomerEmail
     - customerNo
     - "string"
   * - DeliveryAddress1
     - DeliveryAddress1
     - "string"
   * - DeliveryAddress2
     - DeliveryAddress2
     - "string"
   * - DeliveryAddressCity
     - DeliveryAddressCity
     - "string"
   * - DeliveryAddressCountryCode
     - DeliveryAddressCountryCode
     - "string"
   * - DeliveryAddressZipCode
     - DeliveryAddressZipCode
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - DeliveryDate
     - sentDateTimeOffset
     - "string"
   * - Id
     - Id
     - "string"
   * - LastChanged
     - lastChangedDateTimeOffset
     - "string"
   * - NetAmount
     - NetAmount
     - "string"
   * - OrderDate
     - OrderDate
     - "string"
   * - OrderNo
     - OrderNo
     - "string"
   * - SentDate
     - DeliveryDate
     - "string"
   * - SentDate
     - sentDateTimeOffset
     - "string"


Powerofficego Salesorders to PowerOfficeGo Currency
---------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorders and a PowerOfficeGo Currency must be established.

A Powerofficego Salesorders will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Currency Property
   * - CurrencyCode
     - Code

Once a link between a Powerofficego Salesorders and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Powerofficego Supplier to PowerOfficeGo Location
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Location must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type


Powerofficego Supplier to PowerOfficeGo Suppliers
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Suppliers must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Suppliers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Suppliers Property
   * - Id
     - Id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type


Powerofficego Suppliers person to PowerOfficeGo Location
--------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers person and a PowerOfficeGo Location must be established.

A Powerofficego Suppliers person will merge with a PowerOfficeGo Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - PowerOfficeGo Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers person and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type
   * - MailAddress.CountryCode
     - countryCode
     - "string"


Powerofficego Suppliers to PowerOfficeGo Location
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Suppliers and a PowerOfficeGo Location must be established.

A Powerofficego Suppliers will merge with a PowerOfficeGo Location if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Location Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Suppliers and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type
   * - MailAddress.CountryCode
     - countryCode
     - "string"


Powerofficego Vatcode to PowerOfficeGo Vatcodes
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Vatcode and a PowerOfficeGo Vatcodes must be established.

A Powerofficego Vatcode will merge with a PowerOfficeGo Vatcodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGo Vatcodes Property
   * - id
     - Id

Once a link between a Powerofficego Vatcode and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcode and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcode Property
     - PowerOfficeGo Vatcodes Property
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
   * - id
     - Id
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

