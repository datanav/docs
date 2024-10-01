======================================
Chargebee to Business Central Dataflow
======================================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Chargebee Address to Business Central Customers (organisation data)
-------------------------------------------------------------------
Every Chargebee Address will be synchronized with a Business Central Customers (organisation data).

Once a link between a Chargebee Address and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type
   * - addr
     - addressLine1
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - subscription_id
     - id
     - "string"
   * - zip
     - postalCode
     - "string"


Chargebee Address to Business Central Customers (human data)
------------------------------------------------------------
Every Chargebee Address will be synchronized with a Business Central Customers (human data).

Once a link between a Chargebee Address and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
   * - addr
     - addressLine1
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - subscription_id
     - id
     - "string"
   * - zip
     - postalCode
     - "string"


Chargebee Business_entity to Business Central Customers (classification data)
-----------------------------------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Business Central Customers (classification data).

Once a link between a Chargebee Business_entity and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"


Chargebee Customer to Business Central Customers (organisation data)
--------------------------------------------------------------------
Every Chargebee Customer will be synchronized with a Business Central Customers (organisation data).

Once a link between a Chargebee Customer and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


Chargebee Customer to Business Central Customers (human data)
-------------------------------------------------------------
Every Chargebee Customer will be synchronized with a Business Central Customers (human data).

Once a link between a Chargebee Customer and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Business Central Customers (human data) Property
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

