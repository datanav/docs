=========================================
Business Central to Exact Online Dataflow
=========================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to Exact Online Accounts
---------------------------------------------------
Every Business Central Companies will be synchronized with a Exact Online Accounts.

Once a link between a Business Central Companies and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Exact Online Accounts Property
     - Exact Online Data Type


Business Central Customers person to Exact Online Contacts
----------------------------------------------------------
Every Business Central Customers person will be synchronized with a Exact Online Contacts.

Once a link between a Business Central Customers person and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Business Central Employees to Exact Online Contacts
---------------------------------------------------
Every Business Central Employees will be synchronized with a Exact Online Contacts.

Once a link between a Business Central Employees and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Business Central Salesorderlines to Exact Online Quotations
-----------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Exact Online Quotations.

Once a link between a Business Central Salesorderlines and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Exact Online Quotations Property
     - Exact Online Data Type


Business Central Salesorders to Exact Online Quotations
-------------------------------------------------------
Every Business Central Salesorders will be synchronized with a Exact Online Quotations.

Once a link between a Business Central Salesorders and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currencyId
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"


Business Central Salesquotes to Exact Online Quotations
-------------------------------------------------------
Every Business Central Salesquotes will be synchronized with a Exact Online Quotations.

Once a link between a Business Central Salesquotes and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - id
     - DeliveryAddress
     - "string"


Business Central Contacts person to Exact Online Addresses
----------------------------------------------------------
Every Business Central Contacts person will be synchronized with a Exact Online Addresses.

Once a link between a Business Central Contacts person and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


Business Central Contacts person to Exact Online Contacts
---------------------------------------------------------
Every Business Central Contacts person will be synchronized with a Exact Online Contacts.

Once a link between a Business Central Contacts person and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Business Central Currencies to Exact Online Currencies
------------------------------------------------------
Every Business Central Currencies will be synchronized with a Exact Online Currencies.

Once a link between a Business Central Currencies and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - code
     - Code
     - "string"
   * - displayName
     - Description
     - "string"


Business Central Customers company to Exact Online Accounts
-----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Exact Online Accounts.

Once a link between a Business Central Customers company and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


Business Central Customers person to Exact Online Addresses
-----------------------------------------------------------
Every Business Central Customers person will be synchronized with a Exact Online Addresses.

Once a link between a Business Central Customers person and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


Business Central Employees to Exact Online Employees
----------------------------------------------------
Every Business Central Employees will be synchronized with a Exact Online Employees.

Once a link between a Business Central Employees and a Exact Online Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Exact Online Employees:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Exact Online Employees Property
     - Exact Online Data Type
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


Business Central Items to Exact Online Items
--------------------------------------------
Every Business Central Items will be synchronized with a Exact Online Items.

Once a link between a Business Central Items and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Exact Online Items Property
     - Exact Online Data Type


Business Central Salesorderlines to Exact Online Salesorderlines
----------------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Exact Online Salesorderlines.

Once a link between a Business Central Salesorderlines and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - documentId
     - OrderID
     - "string"
   * - itemId
     - Item
     - "string"


Business Central Salesorderlines to Exact Online Vatcodes
---------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Exact Online Vatcodes.

Once a link between a Business Central Salesorderlines and a Exact Online Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Exact Online Vatcodes:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Exact Online Vatcodes Property
     - Exact Online Data Type


Business Central Salesorders to Exact Online Salesorders
--------------------------------------------------------
Every Business Central Salesorders will be synchronized with a Exact Online Salesorders.

Once a link between a Business Central Salesorders and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currencyId
     - Currency
     - "string"
   * - orderDate
     - OrderDate
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"

