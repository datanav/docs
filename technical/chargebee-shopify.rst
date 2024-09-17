=============================
Chargebee to Shopify Dataflow
=============================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Shopify Customer
--------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Shopify Customer must be established.

A new Shopify Customer will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Shopify.

Once a link between a Chargebee Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Shopify Customer Property
     - Shopify Data Type


Chargebee Address to Shopify Customer
-------------------------------------
Every Chargebee Address will be synchronized with a Shopify Customer.

Once a link between a Chargebee Address and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Shopify Customer Property
     - Shopify Data Type


Chargebee Customer to Shopify Customer
--------------------------------------
Every Chargebee Customer will be synchronized with a Shopify Customer.

Once a link between a Chargebee Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Shopify Customer Property
     - Shopify Data Type


Chargebee Item to Shopify Sesamproduct
--------------------------------------
Every Chargebee Item will be synchronized with a Shopify Sesamproduct.

Once a link between a Chargebee Item and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Shopify Sesamproduct Property
     - Shopify Data Type


Chargebee Order to Shopify Order
--------------------------------
Every Chargebee Order will be synchronized with a Shopify Order.

Once a link between a Chargebee Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Shopify Order Property
     - Shopify Data Type

