====================================
Business Central to Shopify Dataflow
====================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers to Shopify Customer
----------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a Shopify Customer must be established.

A new Shopify Customer will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-salesorders, or Businesscentral-salesorderlines that is synchronized into Shopify.

Once a link between a Business Central Customers and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - Shopify Customer Property
     - Shopify Data Type


Business Central Items to Shopify Product
-----------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Shopify Product must be established.

A new Shopify Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorders, or Businesscentral-salesorderlines that is synchronized into Shopify.

Once a link between a Business Central Items and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Shopify Product Property
     - Shopify Data Type


Business Central Salesorders to Shopify Order
---------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a Shopify Order must be established.

A new Shopify Order will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorders, or Businesscentral-salesorderlines that is synchronized into Shopify.

Once a link between a Business Central Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Shopify Order Property
     - Shopify Data Type


Business Central Customers company to Shopify Customer
------------------------------------------------------
Every Business Central Customers company will be synchronized with a Shopify Customer.

Once a link between a Business Central Customers company and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Shopify Customer Property
     - Shopify Data Type


Business Central Customers person to Shopify Customer
-----------------------------------------------------
Every Business Central Customers person will be synchronized with a Shopify Customer.

Once a link between a Business Central Customers person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Shopify Customer Property
     - Shopify Data Type


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

