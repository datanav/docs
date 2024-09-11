========================================
BusinessCentral to Exact Online Dataflow
========================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Business Contacts person to Exact Addresses
-------------------------------------------
Every Business Contacts person will be synchronized with a Exact Addresses.

Once a link between a Business Contacts person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
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


Business Contacts person to Exact Contacts
------------------------------------------
Every Business Contacts person will be synchronized with a Exact Contacts.

Once a link between a Business Contacts person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
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


Business Currencies to Exact Currencies
---------------------------------------
Every Business Currencies will be synchronized with a Exact Currencies.

Once a link between a Business Currencies and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Currencies and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Business Currencies Property
     - Exact Currencies Property
     - Exact Data Type
   * - code
     - Code
     - "string"
   * - displayName
     - Description
     - "string"


Business Customers company to Exact Accounts
--------------------------------------------
Every Business Customers company will be synchronized with a Exact Accounts.

Once a link between a Business Customers company and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
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


Business Customers person to Exact Addresses
--------------------------------------------
Every Business Customers person will be synchronized with a Exact Addresses.

Once a link between a Business Customers person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
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


Business Employees to Exact Employees
-------------------------------------
Every Business Employees will be synchronized with a Exact Employees.

Once a link between a Business Employees and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
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


Business Items to Exact Items
-----------------------------
Every Business Items will be synchronized with a Exact Items.

Once a link between a Business Items and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - Exact Items Property
     - Exact Data Type


Business Salesorderlines to Exact Salesorderlines
-------------------------------------------------
Every Business Salesorderlines will be synchronized with a Exact Salesorderlines.

Once a link between a Business Salesorderlines and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - documentId
     - OrderID
     - "string"
   * - itemId
     - Item
     - "string"


Business Salesorderlines to Exact Vatcodes
------------------------------------------
Every Business Salesorderlines will be synchronized with a Exact Vatcodes.

Once a link between a Business Salesorderlines and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - Exact Vatcodes Property
     - Exact Data Type


Business Salesorders to Exact Salesorders
-----------------------------------------
Every Business Salesorders will be synchronized with a Exact Salesorders.

Once a link between a Business Salesorders and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
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

