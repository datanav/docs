===============================
Powerofficego to Exact Dataflow
===============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers person to Exact Contacts
------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Exact Contacts.

Once a link between a Powerofficego Customers person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Exact Contacts Property
     - Exact Data Type
   * - DateOfBirth
     - BirthDate
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"
   * - PhoneNumber
     - Phone
     - "string"


Powerofficego Departments to Exact Accounts
-------------------------------------------
Every Powerofficego Departments will be synchronized with a Exact Accounts.

Once a link between a Powerofficego Departments and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Exact Accounts Property
     - Exact Data Type
   * - Name
     - Name
     - "string"


Powerofficego Employees to Exact Contacts
-----------------------------------------
Every Powerofficego Employees will be synchronized with a Exact Contacts.

Once a link between a Powerofficego Employees and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Exact Contacts Property
     - Exact Data Type
   * - DateOfBirth
     - BirthDate
     - "string"
   * - EmailAddress
     - BusinessEmail
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"
   * - PhoneNumber
     - Mobile
     - "string"


Powerofficego Salesorderlines to Exact Quotations
-------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Exact Quotations.

Once a link between a Powerofficego Salesorderlines and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Exact Quotations Property
     - Exact Data Type


Powerofficego Salesorders to Exact Quotations
---------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Exact Quotations.

Once a link between a Powerofficego Salesorders and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyCode
     - Currency
     - "string"


Powerofficego Contactperson to Exact Addresses
----------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Exact Addresses.

Once a link between a Powerofficego Contactperson and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Exact Addresses Property
     - Exact Data Type
   * - address1
     - AddressLine1
     - "string"
   * - address2
     - AddressLine2
     - "string"
   * - city
     - City
     - "string"
   * - residenceCountryCode
     - Country
     - "string"


Powerofficego Contactperson to Exact Contacts
---------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Exact Contacts.

Once a link between a Powerofficego Contactperson and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Exact Contacts Property
     - Exact Data Type
   * - city
     - City
     - "string"
   * - dateOfBirth
     - BirthDate
     - "string"
   * - emailAddress
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - residenceCountryCode
     - Country
     - "string"


Powerofficego Currency to Exact Currencies
------------------------------------------
Every Powerofficego Currency will be synchronized with a Exact Currencies.

Once a link between a Powerofficego Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Exact Currencies Property
     - Exact Data Type


Powerofficego Customers to Exact Accounts
-----------------------------------------
Every Powerofficego Customers will be synchronized with a Exact Accounts.

Once a link between a Powerofficego Customers and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Exact Accounts Property
     - Exact Data Type
   * - MailAddress.AddressLine1
     - AddressLine1
     - "string"
   * - MailAddress.AddressLine2
     - AddressLine2
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"
   * - MailAddress.ZipCode
     - Postcode
     - "string"
   * - Name
     - Name
     - "string"
   * - PhoneNumber
     - Phone
     - "string"
   * - WebsiteUrl
     - Website
     - "string"


Powerofficego Customers person to Exact Addresses
-------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Exact Addresses.

Once a link between a Powerofficego Customers person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Exact Addresses Property
     - Exact Data Type
   * - MailAddress.AddressLine1
     - AddressLine1
     - "string"
   * - MailAddress.AddressLine2
     - AddressLine2
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"


Powerofficego Departments to Exact Departments
----------------------------------------------
Every Powerofficego Departments will be synchronized with a Exact Departments.

If a matching Exact Departments already exists, the Powerofficego Departments will be merged with the existing one.
If no matching Exact Departments is found, a new Exact Departments will be created.

A Powerofficego Departments will merge with a Exact Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Exact Departments Property
   * - Code
     - Code

Once a link between a Powerofficego Departments and a Exact Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Exact Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Exact Departments Property
     - Exact Data Type
   * - Code
     - Code
     - "string"


Powerofficego Employees to Exact Employees
------------------------------------------
Every Powerofficego Employees will be synchronized with a Exact Employees.

Once a link between a Powerofficego Employees and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Exact Employees Property
     - Exact Data Type
   * - DateOfBirth
     - BirthDate
     - "string"
   * - EmailAddress
     - BusinessEmail
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - PhoneNumber
     - BusinessMobile
     - "string"


Powerofficego Location to Exact Addresses
-----------------------------------------
Every Powerofficego Location will be synchronized with a Exact Addresses.

Once a link between a Powerofficego Location and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     - Exact Addresses Property
     - Exact Data Type
   * - address1
     - AddressLine1
     - "string"
   * - address2
     - AddressLine2
     - "string"
   * - address3
     - AddressLine3
     - "string"
   * - city
     - City
     - "string"
   * - countryCode
     - Country
     - "string"


Powerofficego Product to Exact Items
------------------------------------
Every Powerofficego Product will be synchronized with a Exact Items.

Once a link between a Powerofficego Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Exact Items Property
     - Exact Data Type


Powerofficego Product to Exact Units
------------------------------------
Every Powerofficego Product will be synchronized with a Exact Units.

Once a link between a Powerofficego Product and a Exact Units is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Exact Units:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Exact Units Property
     - Exact Data Type


Powerofficego Quote to Exact Quotations
---------------------------------------
Every Powerofficego Quote will be synchronized with a Exact Quotations.

Once a link between a Powerofficego Quote and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     - Exact Quotations Property
     - Exact Data Type


Powerofficego Salesorderlines to Exact Salesorderlines
------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Exact Salesorderlines.

Once a link between a Powerofficego Salesorderlines and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - ProductId
     - Item
     - "string"
   * - ProductUnitCost
     - CostPriceFC
     - "string"
   * - sesam_SalesOrderId
     - OrderID
     - "string"


Powerofficego Salesorders to Exact Salesorders
----------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Exact Salesorders.

Once a link between a Powerofficego Salesorders and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Exact Salesorders Property
     - Exact Data Type
   * - CurrencyCode
     - Currency
     - "string"
   * - SalesOrderDate
     - OrderDate
     - "string"


Powerofficego Suppliers person to Exact Contacts
------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Exact Contacts.

Once a link between a Powerofficego Suppliers person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Exact Contacts Property
     - Exact Data Type
   * - DateOfBirth
     - BirthDate
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"
   * - PhoneNumber
     - Phone
     - "string"


Powerofficego Vatcodes to Exact Vatcodes
----------------------------------------
Every Powerofficego Vatcodes will be synchronized with a Exact Vatcodes.

Once a link between a Powerofficego Vatcodes and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcodes and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcodes Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - Description
     - Description
     - "string"

