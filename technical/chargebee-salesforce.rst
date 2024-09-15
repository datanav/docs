================================
Chargebee to Salesforce Dataflow
================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Salesforce Division
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Salesforce Division.

Once a link between a Chargebee Business_entity and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Chargebee Currency to Salesforce Currencytype
---------------------------------------------
Every Chargebee Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Chargebee Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Chargebee Item_family to Salesforce Currencytype
------------------------------------------------
Every Chargebee Item_family will be synchronized with a Salesforce Currencytype.

Once a link between a Chargebee Item_family and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Chargebee Order to Salesforce Invoice
-------------------------------------
Every Chargebee Order will be synchronized with a Salesforce Invoice.

Once a link between a Chargebee Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency_code
     - CurrencyIsoCode
     - "string"


Chargebee Business_entity to Salesforce Organization
----------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Salesforce Organization.

Once a link between a Chargebee Business_entity and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"


Chargebee Customer to Salesforce Customer
-----------------------------------------
Every Chargebee Customer will be synchronized with a Salesforce Customer.

Once a link between a Chargebee Customer and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Salesforce Customer Property
     - Salesforce Data Type


Chargebee Item to Salesforce Product2
-------------------------------------
Every Chargebee Item will be synchronized with a Salesforce Product2.

Once a link between a Chargebee Item and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Salesforce Product2 Property
     - Salesforce Data Type


Chargebee Order to Salesforce Order
-----------------------------------
Every Chargebee Order will be synchronized with a Salesforce Order.

Once a link between a Chargebee Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - currency_code
     - CurrencyIsoCode
     - "string"

