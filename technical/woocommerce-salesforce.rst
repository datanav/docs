==================================
Woocommerce to Salesforce Dataflow
==================================

Generated: 2024-09-06 11:53:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Salesforce Invoice
---------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Invoice.

Once a link between a Woocommerce Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"


Woocommerce Customer to Salesforce Customer
-------------------------------------------
Every Woocommerce Customer will be synchronized with a Salesforce Customer.

Once a link between a Woocommerce Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


Woocommerce Order to Salesforce Currencytype
--------------------------------------------
Every Woocommerce Order will be synchronized with a Salesforce Currencytype.

Once a link between a Woocommerce Order and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Woocommerce Product to Salesforce Product2
------------------------------------------
Every Woocommerce Product will be synchronized with a Salesforce Product2.

Once a link between a Woocommerce Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"

