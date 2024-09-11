==================================
Salesforce to ExactOnline Dataflow
==================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Salesforce Orderitem to Exact Quotations
----------------------------------------
Every Salesforce Orderitem will be synchronized with a Exact Quotations.

Once a link between a Salesforce Orderitem and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
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
   * - ID
     - ID
     - "string"
   * - Name
     - Name
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
   * - PostalCode	
     - Postcode
     - "string"


Salesforce Quotelineitem to Exact Quotations
--------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Exact Quotations.

Once a link between a Salesforce Quotelineitem and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Exact Quotations Property
     - Exact Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"


Salesforce Seller to Exact Contacts
-----------------------------------
Every Salesforce Seller will be synchronized with a Exact Contacts.

Once a link between a Salesforce Seller and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Exact Contacts Property
     - Exact Data Type


Salesforce User to Exact Contacts
---------------------------------
Every Salesforce User will be synchronized with a Exact Contacts.

Once a link between a Salesforce User and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Exact Contacts Property
     - Exact Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Contact to ExactOnline Contacts
------------------------------------------
Every Salesforce Contact will be synchronized with a ExactOnline Contacts.

Once a link between a Salesforce Contact and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Salesforce Currencytype to ExactOnline Currencies
-------------------------------------------------
Every Salesforce Currencytype will be synchronized with a ExactOnline Currencies.

Once a link between a Salesforce Currencytype and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - IsoCode
     - Code
     - "string"


Salesforce Division to ExactOnline Divisions
--------------------------------------------
Every Salesforce Division will be synchronized with a ExactOnline Divisions.

Once a link between a Salesforce Division and a ExactOnline Divisions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a ExactOnline Divisions:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - ExactOnline Divisions Property
     - ExactOnline Data Type


Salesforce Invoice to ExactOnline Salesinvoices
-----------------------------------------------
Every Salesforce Invoice will be synchronized with a ExactOnline Salesinvoices.

Once a link between a Salesforce Invoice and a ExactOnline Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a ExactOnline Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - ExactOnline Salesinvoices Property
     - ExactOnline Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Invoiceline to ExactOnline Salesorderlines
-----------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Salesforce Invoiceline and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - Description
     - CostPriceFC
     - "string"


Salesforce Order to ExactOnline Salesorders
-------------------------------------------
Every Salesforce Order will be synchronized with a ExactOnline Salesorders.

Once a link between a Salesforce Order and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Orderitem to ExactOnline Salesorderlines
---------------------------------------------------
Every Salesforce Orderitem will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Salesforce Orderitem and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type


Salesforce Organization to ExactOnline Addresses
------------------------------------------------
Every Salesforce Organization will be synchronized with a ExactOnline Addresses.

Once a link between a Salesforce Organization and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Product2 to ExactOnline Items
----------------------------------------
Every Salesforce Product2 will be synchronized with a ExactOnline Items.

Once a link between a Salesforce Product2 and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - ExactOnline Items Property
     - ExactOnline Data Type


Salesforce Quote to ExactOnline Quotations
------------------------------------------
Every Salesforce Quote will be synchronized with a ExactOnline Quotations.

Once a link between a Salesforce Quote and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - ID
     - DeliveryAddress
     - "string"


Salesforce Quotelineitem to ExactOnline Salesorderlines
-------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Salesforce Quotelineitem and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type


Salesforce User to ExactOnline Addresses
----------------------------------------
Every Salesforce User will be synchronized with a ExactOnline Addresses.

Once a link between a Salesforce User and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - Country
     - CountryName
     - "string"


Salesforce User to ExactOnline Employees
----------------------------------------
Every Salesforce User will be synchronized with a ExactOnline Employees.

Once a link between a Salesforce User and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - ID
     - ID
     - "string"
   * - PostalCode
     - Postcode
     - "string"

