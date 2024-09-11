=======================================
BusinessCentral to ExactOnline Dataflow
=======================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


BusinessCentral Contacts person to ExactOnline Addresses
--------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a ExactOnline Addresses.

Once a link between a BusinessCentral Contacts person and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


BusinessCentral Contacts person to ExactOnline Contacts
-------------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a ExactOnline Contacts.

Once a link between a BusinessCentral Contacts person and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


BusinessCentral Currencies to ExactOnline Currencies
----------------------------------------------------
Every BusinessCentral Currencies will be synchronized with a ExactOnline Currencies.

Once a link between a BusinessCentral Currencies and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Currencies and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Currencies Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - code
     - Code
     - "string"
   * - displayName
     - Description
     - "string"


BusinessCentral Customers company to ExactOnline Accounts
---------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a ExactOnline Accounts.

Once a link between a BusinessCentral Customers company and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


BusinessCentral Customers person to ExactOnline Addresses
---------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a ExactOnline Addresses.

Once a link between a BusinessCentral Customers person and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


BusinessCentral Employees to ExactOnline Employees
--------------------------------------------------
Every BusinessCentral Employees will be synchronized with a ExactOnline Employees.

Once a link between a BusinessCentral Employees and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
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


BusinessCentral Items to ExactOnline Items
------------------------------------------
Every BusinessCentral Items will be synchronized with a ExactOnline Items.

Once a link between a BusinessCentral Items and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - ExactOnline Items Property
     - ExactOnline Data Type


BusinessCentral Salesorderlines to ExactOnline Salesorderlines
--------------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a ExactOnline Salesorderlines.

Once a link between a BusinessCentral Salesorderlines and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - documentId
     - OrderID
     - "string"
   * - itemId
     - Item
     - "string"


BusinessCentral Salesorderlines to ExactOnline Vatcodes
-------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a ExactOnline Vatcodes.

Once a link between a BusinessCentral Salesorderlines and a ExactOnline Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a ExactOnline Vatcodes:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - ExactOnline Vatcodes Property
     - ExactOnline Data Type


BusinessCentral Salesorders to ExactOnline Salesorders
------------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a ExactOnline Salesorders.

Once a link between a BusinessCentral Salesorders and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - currencyId
     - Currency
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"

