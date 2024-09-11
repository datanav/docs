======================================
Chargebee to Business Central Dataflow
======================================

Generated: 2024-09-11 07:54:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Business Customers company
------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Business Customers company must be established.

A new Business Customers company will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Business.

Once a link between a Chargebee Customer and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Customers company Property
     - Business Data Type


Chargebee Business_entity to Businesscentral Companies
------------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Businesscentral Companies.

Once a link between a Chargebee Business_entity and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Chargebee Customer to Business Customers person
-----------------------------------------------
Every Chargebee Customer will be synchronized with a Business Customers person.

Once a link between a Chargebee Customer and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Customers person Property
     - Business Data Type
   * - email
     - email
     - "string"


Chargebee Item to Business Items
--------------------------------
Every Chargebee Item will be synchronized with a Business Items.

Once a link between a Chargebee Item and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Business Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Business Items Property
     - Business Data Type


Chargebee Order to Business Salesorders
---------------------------------------
Every Chargebee Order will be synchronized with a Business Salesorders.

Once a link between a Chargebee Order and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Business Salesorders Property
     - Business Data Type
   * - currency_code
     - currencyId
     - "string"
   * - customer_id
     - customerId
     - "string"

