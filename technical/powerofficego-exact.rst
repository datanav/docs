======================================
PowerOfficeGO to Exact Online Dataflow
======================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


PowerOffice Contactperson to Exact Addresses
--------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Exact Addresses.

Once a link between a PowerOffice Contactperson and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
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


PowerOffice Contactperson to Exact Contacts
-------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Exact Contacts.

Once a link between a PowerOffice Contactperson and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
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


PowerOffice Currency to Exact Currencies
----------------------------------------
Every PowerOffice Currency will be synchronized with a Exact Currencies.

Once a link between a PowerOffice Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - PowerOffice Currency Property
     - Exact Currencies Property
     - Exact Data Type


PowerOffice Customers to Exact Accounts
---------------------------------------
Every PowerOffice Customers will be synchronized with a Exact Accounts.

Once a link between a PowerOffice Customers and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
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


PowerOffice Customers person to Exact Addresses
-----------------------------------------------
Every PowerOffice Customers person will be synchronized with a Exact Addresses.

Once a link between a PowerOffice Customers person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
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


PowerOffice Departments to Exact Departments
--------------------------------------------
Every PowerOffice Departments will be synchronized with a Exact Departments.

If a matching Exact Departments already exists, the PowerOffice Departments will be merged with the existing one.
If no matching Exact Departments is found, a new Exact Departments will be created.

A PowerOffice Departments will merge with a Exact Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - Exact Departments Property
   * - Code
     - Code

Once a link between a PowerOffice Departments and a Exact Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a Exact Departments:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - Exact Departments Property
     - Exact Data Type
   * - Code
     - Code
     - "string"


PowerOffice Employees to Exact Employees
----------------------------------------
Every PowerOffice Employees will be synchronized with a Exact Employees.

Once a link between a PowerOffice Employees and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
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


PowerOffice Location to Exact Addresses
---------------------------------------
Every PowerOffice Location will be synchronized with a Exact Addresses.

Once a link between a PowerOffice Location and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Location and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - PowerOffice Location Property
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


PowerOffice Product to Exact Items
----------------------------------
Every PowerOffice Product will be synchronized with a Exact Items.

Once a link between a PowerOffice Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - Exact Items Property
     - Exact Data Type


PowerOffice Product to Exact Units
----------------------------------
Every PowerOffice Product will be synchronized with a Exact Units.

Once a link between a PowerOffice Product and a Exact Units is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Exact Units:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - Exact Units Property
     - Exact Data Type


PowerOffice Quote to Exact Quotations
-------------------------------------
Every PowerOffice Quote will be synchronized with a Exact Quotations.

Once a link between a PowerOffice Quote and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Quote and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - PowerOffice Quote Property
     - Exact Quotations Property
     - Exact Data Type


PowerOffice Salesorderlines to Exact Salesorderlines
----------------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Exact Salesorderlines.

Once a link between a PowerOffice Salesorderlines and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
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


PowerOffice Salesorders to Exact Salesorders
--------------------------------------------
Every PowerOffice Salesorders will be synchronized with a Exact Salesorders.

Once a link between a PowerOffice Salesorders and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorders and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorders Property
     - Exact Salesorders Property
     - Exact Data Type
   * - CurrencyCode
     - Currency
     - "string"
   * - SalesOrderDate
     - OrderDate
     - "string"


PowerOffice Suppliers person to Exact Contacts
----------------------------------------------
Every PowerOffice Suppliers person will be synchronized with a Exact Contacts.

Once a link between a PowerOffice Suppliers person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Suppliers person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice Suppliers person Property
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


PowerOffice Vatcodes to Exact Vatcodes
--------------------------------------
Every PowerOffice Vatcodes will be synchronized with a Exact Vatcodes.

Once a link between a PowerOffice Vatcodes and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Vatcodes and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - PowerOffice Vatcodes Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - Description
     - Description
     - "string"

