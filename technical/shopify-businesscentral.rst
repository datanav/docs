====================================
Shopify to Business Central Dataflow
====================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Business Central Customers company
------------------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Shopify Customer to Business Central Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers person Property
     - Business Central Data Type


Shopify Order to Business Central Salesorders
---------------------------------------------
Before any synchronization can take place, a link between a Shopify Order and a Business Central Salesorders must be established.

A new Business Central Salesorders will be created from a Shopify Order if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Central Salesorders Property
     - Business Central Data Type


Shopify Product to Business Central Items
-----------------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Business Central Items must be established.

A new Business Central Items will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into Business Central.

Once a link between a Shopify Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Business Central Items Property
     - Business Central Data Type


Shopify Customer to Business Central Customers company
------------------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Customers company.

Once a link between a Shopify Customer and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers company Property
     - Business Central Data Type


Shopify Customer to Business Central Customers person
-----------------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Customers person.

Once a link between a Shopify Customer and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers person Property
     - Business Central Data Type


Shopify Order to Business Central Salesorderlines
-------------------------------------------------
Every Shopify Order will be synchronized with a Business Central Salesorderlines.

Once a link between a Shopify Order and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Shopify Order to Business Central Salesorders
---------------------------------------------
Every Shopify Order will be synchronized with a Business Central Salesorders.

Once a link between a Shopify Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Central Salesorders Property
     - Business Central Data Type


Shopify Sesamproduct to Business Central Items
----------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Business Central Items.

Once a link between a Shopify Sesamproduct and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Business Central Items Property
     - Business Central Data Type

