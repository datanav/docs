========================================
Business Central to ExactOnline Dataflow
========================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Companies to ExactOnline Accounts
-------------------------------------------------
Every BusinessCentral Companies will be synchronized with a ExactOnline Accounts.

Once a link between a BusinessCentral Companies and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Companies and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Companies Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type


BusinessCentral Customers person to ExactOnline Contacts
--------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a ExactOnline Contacts.

Once a link between a BusinessCentral Customers person and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
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
   * - phoneNumber
     - Phone
     - "string"


BusinessCentral Employees to ExactOnline Contacts
-------------------------------------------------
Every BusinessCentral Employees will be synchronized with a ExactOnline Contacts.

Once a link between a BusinessCentral Employees and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


BusinessCentral Salesorderlines to ExactOnline Quotations
---------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a ExactOnline Quotations.

Once a link between a BusinessCentral Salesorderlines and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


BusinessCentral Salesorders to ExactOnline Quotations
-----------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a ExactOnline Quotations.

Once a link between a BusinessCentral Salesorders and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - currencyId
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"
   * - requestedDeliveryDate
     - DeliveryDate
     - "string"


BusinessCentral Salesquotes to ExactOnline Quotations
-----------------------------------------------------
Every BusinessCentral Salesquotes will be synchronized with a ExactOnline Quotations.

Once a link between a BusinessCentral Salesquotes and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesquotes and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesquotes Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
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

