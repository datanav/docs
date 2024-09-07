=========================
Exact to Shopify Dataflow
=========================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Items to Shopify Product
------------------------------
Before any synchronization can take place, a link between a Exact Items and a Shopify Product must be established.

A new Shopify Product will be created from a Exact Items if it is connected to a Exact Salesorders that is synchronized into Shopify.

Once a link between a Exact Items and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Shopify Product Property
     - Shopify Data Type


Exact Items to Shopify Sesamproduct
-----------------------------------
Every Exact Items will be synchronized with a Shopify Sesamproduct.

Once a link between a Exact Items and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Shopify Sesamproduct Property
     - Shopify Data Type


Exact Salesorders to Shopify Order
----------------------------------
Every Exact Salesorders will be synchronized with a Shopify Order.

Once a link between a Exact Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Shopify Order Property
     - Shopify Data Type
   * - Currency
     - currency
     - "string"

