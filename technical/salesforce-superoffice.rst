==================================
Salesforce to SuperOffice Dataflow
==================================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Invoiceline to SuperOffice Quoteline
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Invoiceline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - Description
     - Description
     - "string"
   * - Quantity
     - Quantity
     - N/A
   * - TaxRate
     - VAT
     - "integer"
   * - UnitPrice
     - UnitListPrice
     - N/A


Salesforce Orderitem to SuperOffice Quoteline
---------------------------------------------
Every Salesforce Orderitem will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Orderitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - OrderId
     - QuoteAlternativeId
     - "integer"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPrice
     - UnitListPrice
     - N/A


Salesforce Product2 to SuperOffice Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a SuperOffice Product.

Once a link between a Salesforce Product2 and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - SuperOffice Product Property
     - SuperOffice Data Type


Salesforce Quote to SuperOffice Quotealternative
------------------------------------------------
Every Salesforce Quote will be synchronized with a SuperOffice Quotealternative.

Once a link between a Salesforce Quote and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"
   * - Tax
     - VAT
     - "integer"
   * - TotalPriceWithTax
     - TotalPrice
     - "float"


Salesforce Quotelineitem to SuperOffice Quoteline
-------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a SuperOffice Quoteline.

Once a link between a Salesforce Quotelineitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - Description
     - Description
     - "string"
   * - Discount
     - ERPDiscountPercent
     - "integer"
   * - Quantity
     - Quantity
     - N/A
   * - TotalPriceWithTax
     - UnitListPrice
     - N/A

