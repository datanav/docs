=================================
Salesforce to Salesforce Dataflow
=================================

Generated: 2024-09-09 08:42:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Invoiceline to Salesforce Invoice
--------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Salesforce Invoice.

Once a link between a Salesforce Invoiceline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"


Salesforce Order to Salesforce Invoice
--------------------------------------
Every Salesforce Order will be synchronized with a Salesforce Invoice.

Once a link between a Salesforce Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"
   * - EffectiveDate
     - FullSettlementDate
     - "string"
   * - TotalAmount
     - TotalAmount
     - "string"


Salesforce Organization to Salesforce Division
----------------------------------------------
Every Salesforce Organization will be synchronized with a Salesforce Division.

Once a link between a Salesforce Organization and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name	
     - Name
     - "string"


Salesforce Order to Salesforce Orderitem
----------------------------------------
Every Salesforce Order will be synchronized with a Salesforce Orderitem.

Once a link between a Salesforce Order and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"


Salesforce Order to Salesforce Quote
------------------------------------
Every Salesforce Order will be synchronized with a Salesforce Quote.

Once a link between a Salesforce Order and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Salesforce Quote Property
     - Salesforce Data Type


Salesforce Orderitem to Salesforce Order
----------------------------------------
Every Salesforce Orderitem will be synchronized with a Salesforce Order.

Once a link between a Salesforce Orderitem and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"


Salesforce Orderitem to Salesforce Quote
----------------------------------------
Every Salesforce Orderitem will be synchronized with a Salesforce Quote.

Once a link between a Salesforce Orderitem and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Salesforce Quote Property
     - Salesforce Data Type


Salesforce Quote to Salesforce Order
------------------------------------
Every Salesforce Quote will be synchronized with a Salesforce Order.

Once a link between a Salesforce Quote and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Salesforce Order Property
     - Salesforce Data Type


Salesforce Quote to Salesforce Orderitem
----------------------------------------
Every Salesforce Quote will be synchronized with a Salesforce Orderitem.

Once a link between a Salesforce Quote and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Salesforce Orderitem Property
     - Salesforce Data Type

