=================================
Salesforce to Salesforce Dataflow
=================================

Generated: 2024-09-06 12:31:25

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Invoice to Salesforce Division
-----------------------------------------
Every Salesforce Invoice will be synchronized with a Salesforce Division.

Once a link between a Salesforce Invoice and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Salesforce Division Property
     - Salesforce Data Type


Salesforce Invoice to Salesforce Invoiceline
--------------------------------------------
Every Salesforce Invoice will be synchronized with a Salesforce Invoiceline.

Once a link between a Salesforce Invoice and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - CurrencyIsoCode
     - CurrencyIsoCode
     - "string"


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

