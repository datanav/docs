===================================
Salesforce to Exact Online Dataflow
===================================

Generated: 2024-09-12 00:00:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Exact Online Contacts
--------------------------------------------
Every Salesforce Customer will be synchronized with a Exact Online Contacts.

Once a link between a Salesforce Customer and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Exact Online Contacts Property
     - Exact Online Data Type


Salesforce Division to Exact Online Accounts
--------------------------------------------
Every Salesforce Division will be synchronized with a Exact Online Accounts.

Once a link between a Salesforce Division and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - Name
     - Name
     - "string"


Salesforce Invoice to Exact Online Quotations
---------------------------------------------
Every Salesforce Invoice will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Invoice and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Invoiceline to Exact Online Quotations
-------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Invoiceline and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"


Salesforce Order to Exact Online Quotations
-------------------------------------------
Every Salesforce Order will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Order and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - ID
     - DeliveryAddress
     - "string"


Salesforce Orderitem to Exact Online Quotations
-----------------------------------------------
Every Salesforce Orderitem will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Orderitem and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"


Salesforce Organization to Exact Online Accounts
------------------------------------------------
Every Salesforce Organization will be synchronized with a Exact Online Accounts.

Once a link between a Salesforce Organization and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


Salesforce Quotelineitem to Exact Online Quotations
---------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Quotelineitem and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"


Salesforce Seller to Exact Online Contacts
------------------------------------------
Every Salesforce Seller will be synchronized with a Exact Online Contacts.

Once a link between a Salesforce Seller and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Exact Online Contacts Property
     - Exact Online Data Type


Salesforce User to Exact Online Contacts
----------------------------------------
Every Salesforce User will be synchronized with a Exact Online Contacts.

Once a link between a Salesforce User and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Contact to Exact Online Contacts
-------------------------------------------
Every Salesforce Contact will be synchronized with a Exact Online Contacts.

Once a link between a Salesforce Contact and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Salesforce Currencytype to Exact Online Currencies
--------------------------------------------------
Every Salesforce Currencytype will be synchronized with a Exact Online Currencies.

Once a link between a Salesforce Currencytype and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - IsoCode
     - Code
     - "string"


Salesforce Division to Exact Online Divisions
---------------------------------------------
Every Salesforce Division will be synchronized with a Exact Online Divisions.

Once a link between a Salesforce Division and a Exact Online Divisions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Exact Online Divisions:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Exact Online Divisions Property
     - Exact Online Data Type


Salesforce Invoice to Exact Online Salesinvoices
------------------------------------------------
Every Salesforce Invoice will be synchronized with a Exact Online Salesinvoices.

Once a link between a Salesforce Invoice and a Exact Online Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Exact Online Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Exact Online Salesinvoices Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Invoiceline to Exact Online Salesorderlines
------------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Exact Online Salesorderlines.

Once a link between a Salesforce Invoiceline and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - Description
     - CostPriceFC
     - "string"


Salesforce Order to Exact Online Salesorders
--------------------------------------------
Every Salesforce Order will be synchronized with a Exact Online Salesorders.

Once a link between a Salesforce Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"


Salesforce Orderitem to Exact Online Salesorderlines
----------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Exact Online Salesorderlines.

Once a link between a Salesforce Orderitem and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


Salesforce Organization to Exact Online Addresses
-------------------------------------------------
Every Salesforce Organization will be synchronized with a Exact Online Addresses.

Once a link between a Salesforce Organization and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Product2 to Exact Online Items
-----------------------------------------
Every Salesforce Product2 will be synchronized with a Exact Online Items.

Once a link between a Salesforce Product2 and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Exact Online Items Property
     - Exact Online Data Type


Salesforce Quote to Exact Online Quotations
-------------------------------------------
Every Salesforce Quote will be synchronized with a Exact Online Quotations.

Once a link between a Salesforce Quote and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - CurrencyIsoCode
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - ID
     - DeliveryAddress
     - "string"


Salesforce Quotelineitem to Exact Online Salesorderlines
--------------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Exact Online Salesorderlines.

Once a link between a Salesforce Quotelineitem and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


Salesforce User to Exact Online Addresses
-----------------------------------------
Every Salesforce User will be synchronized with a Exact Online Addresses.

Once a link between a Salesforce User and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - Country
     - CountryName
     - "string"


Salesforce User to Exact Online Employees
-----------------------------------------
Every Salesforce User will be synchronized with a Exact Online Employees.

Once a link between a Salesforce User and a Exact Online Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Exact Online Employees:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Exact Online Employees Property
     - Exact Online Data Type
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

