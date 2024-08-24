====================
Shopify to  Dataflow
====================

Generated: 2024-08-24 08:14:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to  Product
---------------------------
Before any synchronization can take place, a link between a Shopify Product and a  Product must be established.

A new  Product will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into .

Once a link between a Shopify Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Product Property
     -  Data Type


Shopify Product to  Products
----------------------------
Before any synchronization can take place, a link between a Shopify Product and a  Products must be established.

A new  Products will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into .

Once a link between a Shopify Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Products Property
     -  Data Type


Shopify Order to  Order
-----------------------
Every Shopify Order will be synchronized with a  Order.

Once a link between a Shopify Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Order Property
     -  Data Type


Shopify Sesamproduct to  Product
--------------------------------
Every Shopify Sesamproduct will be synchronized with a  Product.

Once a link between a Shopify Sesamproduct and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Product Property
     -  Data Type

