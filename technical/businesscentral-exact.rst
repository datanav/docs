=================================
Businesscentral to Exact Dataflow
=================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Exact Accounts
-------------------------------------------
Every Businesscentral Companies will be synchronized with a Exact Accounts.

Once a link between a Businesscentral Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Exact Accounts Property
     - Exact Data Type


Businesscentral Customers person to Exact Contacts
--------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Exact Contacts.

Once a link between a Businesscentral Customers person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Exact Contacts Property
     - Exact Data Type
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


Businesscentral Employees to Exact Contacts
-------------------------------------------
Every Businesscentral Employees will be synchronized with a Exact Contacts.

Once a link between a Businesscentral Employees and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Exact Contacts Property
     - Exact Data Type
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


Businesscentral Salesorderlines to Exact Quotations
---------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Exact Quotations.

Once a link between a Businesscentral Salesorderlines and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Exact Quotations Property
     - Exact Data Type


Businesscentral Salesorders to Exact Quotations
-----------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Exact Quotations.

Once a link between a Businesscentral Salesorders and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Exact Quotations Property
     - Exact Data Type
   * - currencyId
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"


Businesscentral Salesquotes to Exact Quotations
-----------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Exact Quotations.

Once a link between a Businesscentral Salesquotes and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Exact Quotations Property
     - Exact Data Type
   * - id
     - DeliveryAddress
     - "string"


Businesscentral Contacts person to Exact Addresses
--------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Exact Addresses.

Once a link between a Businesscentral Contacts person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Exact Addresses Property
     - Exact Data Type
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


Businesscentral Contacts person to Exact Contacts
-------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Exact Contacts.

Once a link between a Businesscentral Contacts person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Exact Contacts Property
     - Exact Data Type
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


Businesscentral Currencies to Exact Currencies
----------------------------------------------
Every Businesscentral Currencies will be synchronized with a Exact Currencies.

Once a link between a Businesscentral Currencies and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     - Exact Currencies Property
     - Exact Data Type
   * - code
     - Code
     - "string"
   * - displayName
     - Description
     - "string"


Businesscentral Customers company to Exact Accounts
---------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Exact Accounts.

Once a link between a Businesscentral Customers company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Exact Accounts Property
     - Exact Data Type
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


Businesscentral Customers person to Exact Addresses
---------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Exact Addresses.

Once a link between a Businesscentral Customers person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Exact Addresses Property
     - Exact Data Type
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


Businesscentral Employees to Exact Employees
--------------------------------------------
Every Businesscentral Employees will be synchronized with a Exact Employees.

Once a link between a Businesscentral Employees and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Exact Employees Property
     - Exact Data Type
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


Businesscentral Items to Exact Items
------------------------------------
Every Businesscentral Items will be synchronized with a Exact Items.

Once a link between a Businesscentral Items and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Exact Items Property
     - Exact Data Type


Businesscentral Salesorderlines to Exact Salesorderlines
--------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Exact Salesorderlines.

Once a link between a Businesscentral Salesorderlines and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - documentId
     - OrderID
     - "string"
   * - itemId
     - Item
     - "string"


Businesscentral Salesorderlines to Exact Vatcodes
-------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Exact Vatcodes.

Once a link between a Businesscentral Salesorderlines and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Exact Vatcodes Property
     - Exact Data Type


Businesscentral Salesorders to Exact Salesorders
------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Exact Salesorders.

Once a link between a Businesscentral Salesorders and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currencyId
     - Currency
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"

