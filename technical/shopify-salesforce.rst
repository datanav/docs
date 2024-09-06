==============================
Shopify to Salesforce Dataflow
==============================

Generated: 2024-09-06 11:56:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Salesforce Product2
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Salesforce Product2.

Once a link between a Shopify Inventoryitem and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Shopify Order to Salesforce Invoice
-----------------------------------
Every Shopify Order will be synchronized with a Salesforce Invoice.

Once a link between a Shopify Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"
   * - current_total_price
     - TotalAmount
     - "string"
   * - total_price
     - TotalAmount
     - "string"


Shopify Product to Salesforce Product2
--------------------------------------
Every Shopify Product will be synchronized with a Salesforce Product2.

Once a link between a Shopify Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Shopify Customer to Salesforce Currencytype
-------------------------------------------
Every Shopify Customer will be synchronized with a Salesforce Currencytype.

Once a link between a Shopify Customer and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Shopify Customer to Salesforce Customer
---------------------------------------
Every Shopify Customer will be synchronized with a Salesforce Customer.

Once a link between a Shopify Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


Shopify Order to Salesforce Invoiceline
---------------------------------------
Every Shopify Order will be synchronized with a Salesforce Invoiceline.

Once a link between a Shopify Order and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


Shopify Sesamproduct to Salesforce Product2
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Salesforce Product2.

Once a link between a Shopify Sesamproduct and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - title
     - Name	
     - "string"
   * - variants.title
     - Description	
     - "string"

