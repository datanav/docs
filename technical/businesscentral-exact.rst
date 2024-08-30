============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-30 00:00:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to  Accounts
--------------------------------------
Every Businesscentral Companies will be synchronized with a  Accounts.

Once a link between a Businesscentral Companies and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Accounts Property
     -  Data Type


Businesscentral Customers person to  Contacts
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Contacts.

Once a link between a Businesscentral Customers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Contacts Property
     -  Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - FullName
     - "string"
   * - email
     - Email
     - "string"
   * - phoneNumber
     - Phone
     - "string"


Businesscentral Employees to  Contacts
--------------------------------------
Every Businesscentral Employees will be synchronized with a  Contacts.

Once a link between a Businesscentral Employees and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Contacts Property
     -  Data Type
   * - birthDate
     - BirthDate
     - "string"
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - FullName
     - "string"
   * - email
     - BusinessEmail
     - "string"
   * - givenName
     - FirstName
     - "string"
   * - mobilePhone
     - Mobile
     - "string"
   * - personalEmail
     - Email
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - surname
     - LastName
     - "string"


Businesscentral Salesorderlines to  Quotations
----------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Quotations.

Once a link between a Businesscentral Salesorderlines and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Quotations Property
     -  Data Type


Businesscentral Salesorders to  Quotations
------------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Quotations.

Once a link between a Businesscentral Salesorders and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Quotations Property
     -  Data Type
   * - currencyId
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"


Businesscentral Salesquotes to  Quotations
------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a  Quotations.

Once a link between a Businesscentral Salesquotes and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     -  Quotations Property
     -  Data Type
   * - id
     - DeliveryAddress
     - "string"


Businesscentral Contacts person to  Addresses
---------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Addresses.

Once a link between a Businesscentral Contacts person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Addresses Property
     -  Data Type
   * - addressLine1
     - AddressLine1
     - "string"
   * - addressLine2
     - AddressLine2
     - "string"
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"


Businesscentral Contacts person to  Contacts
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Contacts.

Once a link between a Businesscentral Contacts person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Contacts Property
     -  Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - FullName
     - "string"
   * - email
     - Email
     - "string"
   * - mobilePhoneNumber
     - Mobile
     - "string"
   * - phoneNumber
     - Phone
     - "string"


Businesscentral Currencies to  Currencies
-----------------------------------------
Every Businesscentral Currencies will be synchronized with a  Currencies.

Once a link between a Businesscentral Currencies and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currencies Property
     -  Data Type
   * - code
     - Code
     - "string"
   * - displayName
     - Description
     - "string"


Businesscentral Customers company to  Accounts
----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Accounts.

Once a link between a Businesscentral Customers company and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Accounts Property
     -  Data Type
   * - addressLine1
     - AddressLine1
     - "string"
   * - addressLine2
     - AddressLine2
     - "string"
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - Name
     - "string"
   * - email
     - Email
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - postalCode
     - Postcode
     - "string"
   * - website
     - Website
     - "string"


Businesscentral Customers person to  Addresses
----------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Addresses.

Once a link between a Businesscentral Customers person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Addresses Property
     -  Data Type
   * - addressLine1
     - AddressLine1
     - "string"
   * - addressLine2
     - AddressLine2
     - "string"
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"


Businesscentral Employees to  Employees
---------------------------------------
Every Businesscentral Employees will be synchronized with a  Employees.

Once a link between a Businesscentral Employees and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Employees:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Employees Property
     -  Data Type
   * - birthDate
     - BirthDate
     - "string"
   * - email
     - BusinessEmail
     - "string"
   * - givenName
     - FirstName
     - "string"
   * - mobilePhone
     - BusinessMobile
     - "string"
   * - personalEmail
     - Email
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - surname
     - LastName
     - "string"


Businesscentral Salesorderlines to  Salesorderlines
---------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Salesorderlines.

Once a link between a Businesscentral Salesorderlines and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Salesorderlines Property
     -  Data Type
   * - documentId
     - OrderID
     - "string"
   * - itemId
     - Item
     - "string"


Businesscentral Salesorders to  Salesorders
-------------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Salesorders.

Once a link between a Businesscentral Salesorders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Salesorders Property
     -  Data Type
   * - currencyId
     - Currency
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"

