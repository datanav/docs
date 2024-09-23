====================================
Shopify to Business Central Dataflow
====================================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Business Central Customers (organisation data)
------------------------------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Customers (organisation data).

Once a link between a Shopify Customer and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


Shopify Customer to Business Central Customers (human data)
-----------------------------------------------------------
Every Shopify Customer will be synchronized with a Business Central Customers (human data).

Once a link between a Shopify Customer and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
   * - default_address.phone
     - phoneNumber
     - "string"
   * - email
     - email
     - "string"


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
   * - sesam_priceExclVAT
     - unitPrice
     - N/A
   * - title
     - displayName
     - "string"

