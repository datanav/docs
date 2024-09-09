============================
Exact to Salesforce Dataflow
============================

Generated: 2024-09-09 08:42:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Salesforce Division
-------------------------------------
Every Exact Accounts will be synchronized with a Salesforce Division.

Once a link between a Exact Accounts and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


Exact Departments to Salesforce Division
----------------------------------------
Every Exact Departments will be synchronized with a Salesforce Division.

Once a link between a Exact Departments and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Salesforce Division Property
     - Salesforce Data Type


Exact Quotations to Salesforce Invoice
--------------------------------------
Every Exact Quotations will be synchronized with a Salesforce Invoice.

Once a link between a Exact Quotations and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


Exact Salesorderlines to Salesforce Invoice
-------------------------------------------
Every Exact Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a Exact Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Exact Salesorders to Salesforce Invoice
---------------------------------------
Every Exact Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a Exact Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


Exact Units to Salesforce Currencytype
--------------------------------------
Every Exact Units will be synchronized with a Salesforce Currencytype.

Once a link between a Exact Units and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Exact Vatcodes to Salesforce Currencytype
-----------------------------------------
Every Exact Vatcodes will be synchronized with a Salesforce Currencytype.

Once a link between a Exact Vatcodes and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Exact Contacts to Salesforce Contact
------------------------------------
Every Exact Contacts will be synchronized with a Salesforce Contact.

Once a link between a Exact Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - BirthDate
     - Birthdate
     - "string"
   * - FirstName
     - Name
     - "string"
   * - FullName
     - Name
     - "string"
   * - LastName
     - Name
     - "string"


Exact Currencies to Salesforce Currencytype
-------------------------------------------
Every Exact Currencies will be synchronized with a Salesforce Currencytype.

Once a link between a Exact Currencies and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - Code
     - IsoCode
     - "string"


Exact Divisions to Salesforce Division
--------------------------------------
Every Exact Divisions will be synchronized with a Salesforce Division.

Once a link between a Exact Divisions and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Salesforce Division Property
     - Salesforce Data Type


Exact Items to Salesforce Product2
----------------------------------
Every Exact Items will be synchronized with a Salesforce Product2.

Once a link between a Exact Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Exact Salesinvoices to Salesforce Invoice
-----------------------------------------
Every Exact Salesinvoices will be synchronized with a Salesforce Invoice.

Once a link between a Exact Salesinvoices and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


Exact Salesorderlines to Salesforce Invoiceline
-----------------------------------------------
Every Exact Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a Exact Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - CostPriceFC
     - Description
     - "string"


Exact Salesorders to Salesforce Order
-------------------------------------
Every Exact Salesorders will be synchronized with a Salesforce Order.

Once a link between a Exact Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


Exact Salesorders to Salesforce Orderitem
-----------------------------------------
Every Exact Salesorders will be synchronized with a Salesforce Orderitem.

Once a link between a Exact Salesorders and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"


Exact Salesorders to Salesforce Quote
-------------------------------------
Every Exact Salesorders will be synchronized with a Salesforce Quote.

Once a link between a Exact Salesorders and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Salesforce Quote Property
     - Salesforce Data Type

