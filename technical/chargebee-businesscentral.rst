======================================
Chargebee to Business Central Dataflow
======================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Business Central Customers company
--------------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Business Central.

Once a link between a Chargebee Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Chargebee Business_entity to Business Central Companies
-------------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Business Central Companies.

Once a link between a Chargebee Business_entity and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Business Central Companies Property
     - Business Central Data Type


Chargebee Customer to Business Central Customers person
-------------------------------------------------------
Every Chargebee Customer will be synchronized with a Business Central Customers person.

Once a link between a Chargebee Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - email
     - email
     - "string"


Chargebee Item to Business Central Items
----------------------------------------
Every Chargebee Item will be synchronized with a Business Central Items.

Once a link between a Chargebee Item and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Business Central Items Property
     - Business Central Data Type


Chargebee Order to Business Central Salesorders
-----------------------------------------------
Every Chargebee Order will be synchronized with a Business Central Salesorders.

Once a link between a Chargebee Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - currency_code
     - currencyId
     - "string"
   * - customer_id
     - customerId
     - "string"

