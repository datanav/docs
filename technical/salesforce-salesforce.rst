=================================
Salesforce to Salesforce Dataflow
=================================

Generated: 2024-09-14 00:00:01

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


Salesforce Orderitem to Salesforce Invoice
------------------------------------------
Every Salesforce Orderitem will be synchronized with a Salesforce Invoice.

Once a link between a Salesforce Orderitem and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
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
   * - Name	
     - Name
     - "string"


Salesforce Quote to Salesforce Invoice
--------------------------------------
Every Salesforce Quote will be synchronized with a Salesforce Invoice.

Once a link between a Salesforce Quote and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"
   * - TotalPriceWithTax
     - TotalAmount
     - "string"


Salesforce Quotelineitem to Salesforce Invoice
----------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Salesforce Invoice.

Once a link between a Salesforce Quotelineitem and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"


Salesforce Invoiceline to Salesforce Orderitem
----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Salesforce Orderitem.

Once a link between a Salesforce Invoiceline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - UnitPrice
     - TotalPrice
     - "string"


Salesforce Invoiceline to Salesforce Quotelineitem
--------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Salesforce Invoiceline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - UnitPrice
     - TotalPriceWithTax
     - "string"


Salesforce Orderitem to Salesforce Invoiceline
----------------------------------------------
Every Salesforce Orderitem will be synchronized with a Salesforce Invoiceline.

Once a link between a Salesforce Orderitem and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - TotalPrice
     - UnitPrice
     - "string"


Salesforce Orderitem to Salesforce Quotelineitem
------------------------------------------------
Every Salesforce Orderitem will be synchronized with a Salesforce Quotelineitem.

Once a link between a Salesforce Orderitem and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - TotalPrice
     - TotalPriceWithTax
     - "string"


Salesforce Quotelineitem to Salesforce Invoiceline
--------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Salesforce Invoiceline.

Once a link between a Salesforce Quotelineitem and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Description
     - Description
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - TotalPriceWithTax
     - UnitPrice
     - "string"


Salesforce Quotelineitem to Salesforce Orderitem
------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Salesforce Orderitem.

Once a link between a Salesforce Quotelineitem and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - TotalPriceWithTax
     - TotalPrice
     - "string"

