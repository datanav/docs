=====================================
Chargebee to Businesscentral Dataflow
=====================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Businesscentral Customers company
-------------------------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Businesscentral.

Once a link between a Chargebee Customer and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type


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


Chargebee Customer to Businesscentral Customers person
------------------------------------------------------
Every Chargebee Customer will be synchronized with a Businesscentral Customers person.

Once a link between a Chargebee Customer and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
   * - email
     - email
     - "string"


Chargebee Item to Businesscentral Items
---------------------------------------
Every Chargebee Item will be synchronized with a Businesscentral Items.

Once a link between a Chargebee Item and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Businesscentral Items Property
     - Businesscentral Data Type


Chargebee Order to Businesscentral Salesorders
----------------------------------------------
Every Chargebee Order will be synchronized with a Businesscentral Salesorders.

Once a link between a Chargebee Order and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
   * - currency_code
     - currencyId
     - "string"
   * - customer_id
     - customerId
     - "string"

