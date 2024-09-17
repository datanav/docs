===============================
WooCommerce to Shopify Dataflow
===============================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Shopify Order
----------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Shopify Order must be established.

A new Shopify Order will be created from a WooCommerce Order if it is connected to a WooCommerce Order that is synchronized into Shopify.

Once a link between a WooCommerce Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Shopify Order Property
     - Shopify Data Type


WooCommerce Product to Shopify Product
--------------------------------------
Before any synchronization can take place, a link between a WooCommerce Product and a Shopify Product must be established.

A new Shopify Product will be created from a WooCommerce Product if it is connected to a WooCommerce Order that is synchronized into Shopify.

Once a link between a WooCommerce Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Shopify Product Property
     - Shopify Data Type


WooCommerce Customer to Shopify Customer
----------------------------------------
Every WooCommerce Customer will be synchronized with a Shopify Customer.

Once a link between a WooCommerce Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Shopify Customer Property
     - Shopify Data Type


WooCommerce Order to Shopify Order
----------------------------------
Every WooCommerce Order will be synchronized with a Shopify Order.

Once a link between a WooCommerce Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Shopify Order Property
     - Shopify Data Type


WooCommerce Product to Shopify Sesamproduct
-------------------------------------------
Every WooCommerce Product will be synchronized with a Shopify Sesamproduct.

Once a link between a WooCommerce Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

