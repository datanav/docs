=============================
Tripletex to Shopify Dataflow
=============================

Generated: 2024-09-20 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer (human data) to Shopify Customer
---------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Shopify Customer.

Once a link between a Tripletex Customer (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Shopify Customer Property
     - Shopify Data Type


Tripletex Customer to Shopify Customer
--------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Shopify Customer.

Once a link between a Tripletex Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Shopify Customer Property
     - Shopify Data Type


Tripletex Order to Shopify Order
--------------------------------
Every Tripletex Order will be synchronized with a Shopify Order.

Once a link between a Tripletex Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Shopify Order Property
     - Shopify Data Type


Tripletex Product to Shopify Sesamproduct
-----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Shopify Sesamproduct.

Once a link between a Tripletex Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

