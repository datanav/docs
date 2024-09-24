====================================
Business Central to Shopify Dataflow
====================================

Generated: 2024-09-24 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers (human data) to Shopify Customer
-----------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Shopify Customer.

Once a link between a Business Central Customers (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Shopify Customer Property
     - Shopify Data Type


Business Central Customers (human data) to Shopify Customer
-----------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Shopify Customer.

Once a link between a Business Central Customers (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Shopify Customer Property
     - Shopify Data Type
   * - email
     - email
     - "string"
   * - phoneNumber
     - default_address.phone
     - "string"


Business Central Items to Shopify Sesamproduct
----------------------------------------------
Every Business Central Items will be synchronized with a Shopify Sesamproduct.

Once a link between a Business Central Items and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - displayName
     - title
     - "string"
   * - inventory
     - variants.inventory_quantity
     - "integer"
   * - unitPrice
     - sesam_priceExclVAT
     - "string"


Business Central Salesorders to Shopify Order
---------------------------------------------
Every Business Central Salesorders will be synchronized with a Shopify Order.

Once a link between a Business Central Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Shopify Order Property
     - Shopify Data Type

