==================================
SuperOffice to Salesforce Dataflow
==================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to Salesforce Order
------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Salesforce Order must be established.

A new Salesforce Order will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Salesforce.

Once a link between a SuperOffice Quotealternative and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - Name
     - Description
     - "string"
   * - TotalPrice
     - TotalAmount
     - "string"


SuperOffice Contact to Salesforce Division
------------------------------------------
Every SuperOffice Contact will be synchronized with a Salesforce Division.

Once a link between a SuperOffice Contact and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - Name
     - Name
     - "string"


SuperOffice Quotealternative to Salesforce Invoice
--------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Salesforce Invoice.

Once a link between a SuperOffice Quotealternative and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Name
     - Description
     - "string"
   * - TotalPrice
     - TotalAmount
     - "string"


SuperOffice Quoteline to Salesforce Invoice
-------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Salesforce Invoice.

Once a link between a SuperOffice Quoteline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


SuperOffice Sale to Salesforce Invoice
--------------------------------------
Every SuperOffice Sale will be synchronized with a Salesforce Invoice.

Once a link between a SuperOffice Sale and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - Amount
     - TotalAmount
     - "string"
   * - Currency.Id
     - CurrencyIsoCode
     - "string"
   * - Saledate
     - FullSettlementDate
     - "string"


SuperOffice Listcurrencyitems to Salesforce Currencytype
--------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Salesforce Currencytype.

Once a link between a SuperOffice Listcurrencyitems and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - Name
     - IsoCode
     - "string"


SuperOffice Product to Salesforce Product2
------------------------------------------
Every SuperOffice Product will be synchronized with a Salesforce Product2.

Once a link between a SuperOffice Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - Description
     - Description
     - "string"
   * - Description
     - Description	
     - "string"
   * - Name
     - Name
     - "string"
   * - Name
     - Name	
     - "string"
   * - Url
     - DisplayUrl
     - "string"
   * - Url
     - DisplayUrl	
     - "string"


SuperOffice Quotealternative to Salesforce Quote
------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Salesforce Quote.

Once a link between a SuperOffice Quotealternative and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - DiscountPercent
     - Discount
     - "string"
   * - Name
     - Description
     - "string"
   * - TotalPrice
     - TotalPriceWithTax
     - "string"
   * - VAT
     - Tax
     - "string"


SuperOffice Quoteline to Salesforce Invoiceline
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Salesforce Invoiceline.

Once a link between a SuperOffice Quoteline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - Description
     - Description
     - "string"
   * - Name
     - Name
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - UnitListPrice
     - UnitPrice
     - "string"
   * - VAT
     - TaxRate
     - "string"


SuperOffice Quoteline to Salesforce Orderitem
---------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Salesforce Orderitem.

Once a link between a SuperOffice Quoteline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - Quantity
     - Quantity
     - "string"
   * - QuoteAlternativeId
     - OrderId
     - "string"
   * - UnitListPrice
     - TotalPrice
     - "string"


SuperOffice Quoteline to Salesforce Quotelineitem
-------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Salesforce Quotelineitem.

Once a link between a SuperOffice Quoteline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - Description
     - Description
     - "string"
   * - DiscountPercent
     - Discount
     - "string"
   * - ERPDiscountPercent
     - Discount
     - "string"
   * - Quantity
     - Quantity
     - "string"
   * - UnitListPrice
     - TotalPriceWithTax
     - "string"

