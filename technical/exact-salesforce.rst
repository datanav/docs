==================================
ExactOnline to Salesforce Dataflow
==================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Salesforce Division
-------------------------------------------
Every ExactOnline Accounts will be synchronized with a Salesforce Division.

Once a link between a ExactOnline Accounts and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


ExactOnline Departments to Salesforce Division
----------------------------------------------
Every ExactOnline Departments will be synchronized with a Salesforce Division.

Once a link between a ExactOnline Departments and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Salesforce Division Property
     - Salesforce Data Type


ExactOnline Quotations to Salesforce Invoice
--------------------------------------------
Every ExactOnline Quotations will be synchronized with a Salesforce Invoice.

Once a link between a ExactOnline Quotations and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


ExactOnline Salesorderlines to Salesforce Invoice
-------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Salesforce Invoice.

Once a link between a ExactOnline Salesorderlines and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Salesforce Invoice Property
     - Salesforce Data Type


ExactOnline Salesorders to Salesforce Invoice
---------------------------------------------
Every ExactOnline Salesorders will be synchronized with a Salesforce Invoice.

Once a link between a ExactOnline Salesorders and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


ExactOnline Units to Salesforce Currencytype
--------------------------------------------
Every ExactOnline Units will be synchronized with a Salesforce Currencytype.

Once a link between a ExactOnline Units and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Units and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - ExactOnline Units Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


ExactOnline Vatcodes to Salesforce Currencytype
-----------------------------------------------
Every ExactOnline Vatcodes will be synchronized with a Salesforce Currencytype.

Once a link between a ExactOnline Vatcodes and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Vatcodes and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - ExactOnline Vatcodes Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


ExactOnline Contacts to Salesforce Contact
------------------------------------------
Every ExactOnline Contacts will be synchronized with a Salesforce Contact.

Once a link between a ExactOnline Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
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


ExactOnline Currencies to Salesforce Currencytype
-------------------------------------------------
Every ExactOnline Currencies will be synchronized with a Salesforce Currencytype.

Once a link between a ExactOnline Currencies and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Currencies and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - ExactOnline Currencies Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - Code
     - IsoCode
     - "string"


ExactOnline Divisions to Salesforce Division
--------------------------------------------
Every ExactOnline Divisions will be synchronized with a Salesforce Division.

Once a link between a ExactOnline Divisions and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - Salesforce Division Property
     - Salesforce Data Type


ExactOnline Employees to Salesforce User
----------------------------------------
Every ExactOnline Employees will be synchronized with a Salesforce User.

Once a link between a ExactOnline Employees and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - Salesforce User Property
     - Salesforce Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - ID
     - ID
     - "string"
   * - Postcode
     - PostalCode
     - "string"


ExactOnlineExact Items to Salesforce Product2
---------------------------------------------
Every ExactOnlineExact Items will be synchronized with a Salesforce Product2.

Once a link between a ExactOnlineExact Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnlineExact Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - ExactOnlineExact Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type


ExactOnline Quotations to Salesforce Quote
------------------------------------------
Every ExactOnline Quotations will be synchronized with a Salesforce Quote.

Once a link between a ExactOnline Quotations and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - DeliveryAddress
     - ID
     - "string"
   * - Description
     - Description
     - "string"


ExactOnline Salesinvoices to Salesforce Invoice
-----------------------------------------------
Every ExactOnline Salesinvoices will be synchronized with a Salesforce Invoice.

Once a link between a ExactOnline Salesinvoices and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesinvoices and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesinvoices Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"


ExactOnline Salesorderlines to Salesforce Invoiceline
-----------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Salesforce Invoiceline.

Once a link between a ExactOnline Salesorderlines and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - CostPriceFC
     - Description
     - "string"


ExactOnline Salesorderlines to Salesforce Orderitem
---------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Salesforce Orderitem.

Once a link between a ExactOnline Salesorderlines and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Salesforce Orderitem Property
     - Salesforce Data Type


ExactOnline Salesorderlines to Salesforce Quotelineitem
-------------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Salesforce Quotelineitem.

Once a link between a ExactOnline Salesorderlines and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


ExactOnlineExact Salesorders to Salesforce Order
------------------------------------------------
Every ExactOnlineExact Salesorders will be synchronized with a Salesforce Order.

Once a link between a ExactOnlineExact Salesorders and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnlineExact Salesorders and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - ExactOnlineExact Salesorders Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - Currency
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"

