============================
Salesforce to Exact Dataflow
============================

Generated: 2024-09-07 00:00:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Exact Contacts
-------------------------------------
Every Salesforce Customer will be synchronized with a Exact Contacts.

Once a link between a Salesforce Customer and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Exact Contacts Property
     - Exact Data Type


Salesforce Division to Exact Accounts
-------------------------------------
Every Salesforce Division will be synchronized with a Exact Accounts.

Once a link between a Salesforce Division and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Exact Accounts Property
     - Exact Data Type
   * - Name
     - Name
     - "string"


Salesforce Division to Exact Contacts
-------------------------------------
Every Salesforce Division will be synchronized with a Exact Contacts.

Once a link between a Salesforce Division and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Exact Contacts Property
     - Exact Data Type


Salesforce Invoice to Exact Accounts
------------------------------------
Every Salesforce Invoice will be synchronized with a Exact Accounts.

Once a link between a Salesforce Invoice and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Exact Accounts Property
     - Exact Data Type


Salesforce Invoice to Exact Quotations
--------------------------------------
Every Salesforce Invoice will be synchronized with a Exact Quotations.

Once a link between a Salesforce Invoice and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Invoiceline to Exact Quotations
------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Exact Quotations.

Once a link between a Salesforce Invoiceline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"


Salesforce Order to Exact Quotations
------------------------------------
Every Salesforce Order will be synchronized with a Exact Quotations.

Once a link between a Salesforce Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - ID
     - DeliveryAddress
     - "string"


Salesforce Organization to Exact Accounts
-----------------------------------------
Every Salesforce Organization will be synchronized with a Exact Accounts.

Once a link between a Salesforce Organization and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Accounts Property
     - Exact Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - Name	
     - Name
     - "string"
   * - Phone	
     - Phone
     - "string"
   * - PostalCode	
     - Postcode
     - "string"


Salesforce Contact to Exact Contacts
------------------------------------
Every Salesforce Contact will be synchronized with a Exact Contacts.

Once a link between a Salesforce Contact and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Exact Contacts Property
     - Exact Data Type
   * - Birthdate
     - BirthDate
     - "string"
   * - Email
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailingCity
     - City
     - "string"
   * - MailingCountry
     - Country
     - "string"
   * - MobilePhone
     - Mobile
     - "string"
   * - Name
     - FirstName
     - "string"
   * - Name
     - FullName
     - "string"
   * - Name
     - LastName
     - "string"
   * - Phone
     - Phone
     - "string"


Salesforce Currencytype to Exact Currencies
-------------------------------------------
Every Salesforce Currencytype will be synchronized with a Exact Currencies.

Once a link between a Salesforce Currencytype and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Exact Currencies Property
     - Exact Data Type
   * - IsoCode
     - Code
     - "string"


Salesforce Division to Exact Divisions
--------------------------------------
Every Salesforce Division will be synchronized with a Exact Divisions.

Once a link between a Salesforce Division and a Exact Divisions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Exact Divisions:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Exact Divisions Property
     - Exact Data Type


Salesforce Invoice to Exact Salesinvoices
-----------------------------------------
Every Salesforce Invoice will be synchronized with a Exact Salesinvoices.

Once a link between a Salesforce Invoice and a Exact Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Exact Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Exact Salesinvoices Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Invoiceline to Exact Salesorderlines
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Exact Salesorderlines.

Once a link between a Salesforce Invoiceline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - Description
     - CostPriceFC
     - "string"


Salesforce Order to Exact Salesorders
-------------------------------------
Every Salesforce Order will be synchronized with a Exact Salesorders.

Once a link between a Salesforce Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Organization to Exact Addresses
------------------------------------------
Every Salesforce Organization will be synchronized with a Exact Addresses.

Once a link between a Salesforce Organization and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Addresses Property
     - Exact Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Product2 to Exact Items
----------------------------------
Every Salesforce Product2 will be synchronized with a Exact Items.

Once a link between a Salesforce Product2 and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Exact Items Property
     - Exact Data Type

