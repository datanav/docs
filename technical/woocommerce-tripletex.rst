=================================
WooCommerce to Tripletex Dataflow
=================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Tripletex Order
------------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Tripletex Order must be established.

A new Tripletex Order will be created from a WooCommerce Order if it is connected to a WooCommerce Order that is synchronized into Tripletex.

Once a link between a WooCommerce Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Tripletex Order Property
     - Tripletex Data Type


WooCommerce Product to Tripletex Product
----------------------------------------
Before any synchronization can take place, a link between a WooCommerce Product and a Tripletex Product must be established.

A new Tripletex Product will be created from a WooCommerce Product if it is connected to a WooCommerce Order that is synchronized into Tripletex.

Once a link between a WooCommerce Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Tripletex Product Property
     - Tripletex Data Type


WooCommerce Customer to Tripletex Customer
------------------------------------------
Every WooCommerce Customer will be synchronized with a Tripletex Customer.

Once a link between a WooCommerce Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type


WooCommerce Customer to Tripletex Customer person
-------------------------------------------------
Every WooCommerce Customer will be synchronized with a Tripletex Customer person.

Once a link between a WooCommerce Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Tripletex Customer person Property
     - Tripletex Data Type


WooCommerce Order to Tripletex Order
------------------------------------
Every WooCommerce Order will be synchronized with a Tripletex Order.

Once a link between a WooCommerce Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Tripletex Order Property
     - Tripletex Data Type


WooCommerce Order to Tripletex Orderline
----------------------------------------
Every WooCommerce Order will be synchronized with a Tripletex Orderline.

Once a link between a WooCommerce Order and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Tripletex Orderline Property
     - Tripletex Data Type


WooCommerce Product to Tripletex Product
----------------------------------------
Every WooCommerce Product will be synchronized with a Tripletex Product.

Once a link between a WooCommerce Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Tripletex Product Property
     - Tripletex Data Type

