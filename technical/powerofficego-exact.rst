==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-29 12:48:38

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers person to  Contacts
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Customers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contacts Property
     -  Data Type
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


Powerofficego Departments to  Accounts
--------------------------------------
Every Powerofficego Departments will be synchronized with a  Accounts.

Once a link between a Powerofficego Departments and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Accounts Property
     -  Data Type
   * - Name
     - Name
     - "string"


Powerofficego Employees to  Contacts
------------------------------------
Every Powerofficego Employees will be synchronized with a  Contacts.

Once a link between a Powerofficego Employees and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Contacts Property
     -  Data Type
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


Powerofficego Salesorderlines to  Quotations
--------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Quotations.

Once a link between a Powerofficego Salesorderlines and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Quotations Property
     -  Data Type


Powerofficego Salesorders to  Quotations
----------------------------------------
Every Powerofficego Salesorders will be synchronized with a  Quotations.

Once a link between a Powerofficego Salesorders and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Quotations Property
     -  Data Type
   * - CurrencyCode
     - Currency
     - "string"


Powerofficego Contactperson to  Addresses
-----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Addresses.

Once a link between a Powerofficego Contactperson and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Addresses Property
     -  Data Type
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


Powerofficego Contactperson to  Contacts
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contacts.

Once a link between a Powerofficego Contactperson and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contacts Property
     -  Data Type
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


Powerofficego Currency to  Currencies
-------------------------------------
Every Powerofficego Currency will be synchronized with a  Currencies.

Once a link between a Powerofficego Currency and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     -  Currencies Property
     -  Data Type


Powerofficego Customers to  Accounts
------------------------------------
Every Powerofficego Customers will be synchronized with a  Accounts.

Once a link between a Powerofficego Customers and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Accounts Property
     -  Data Type
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


Powerofficego Customers person to  Addresses
--------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Addresses.

Once a link between a Powerofficego Customers person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Addresses Property
     -  Data Type
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


Powerofficego Location to  Addresses
------------------------------------
Every Powerofficego Location will be synchronized with a  Addresses.

Once a link between a Powerofficego Location and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     -  Addresses Property
     -  Data Type
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


Powerofficego Quote to  Quotations
----------------------------------
Every Powerofficego Quote will be synchronized with a  Quotations.

Once a link between a Powerofficego Quote and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     -  Quotations Property
     -  Data Type


Powerofficego Suppliers person to  Contacts
-------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Suppliers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Contacts Property
     -  Data Type
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

