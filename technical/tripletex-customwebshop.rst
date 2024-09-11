===================================
Tripletex to CustomWebshop Dataflow
===================================

Generated: 2024-09-11 07:56:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to CustomWebshop. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Department to Custom Customer
---------------------------------------
Every Tripletex Department will be synchronized with a Custom Customer.

Once a link between a Tripletex Department and a Custom Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Custom Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Custom Customer Property
     - Custom Data Type


Tripletex Orderline to Custom Order
-----------------------------------
Every Tripletex Orderline will be synchronized with a Custom Order.

Once a link between a Tripletex Orderline and a Custom Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Custom Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Custom Order Property
     - Custom Data Type


Tripletex Customer to CustomWebshop Customer
--------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a CustomWebshop Customer.

Once a link between a Tripletex Customer and a CustomWebshop Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a CustomWebshop Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - CustomWebshop Customer Property
     - CustomWebshop Data Type


Tripletex Order to CustomWebshop Order
--------------------------------------
Every Tripletex Order will be synchronized with a CustomWebshop Order.

Once a link between a Tripletex Order and a CustomWebshop Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a CustomWebshop Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - CustomWebshop Order Property
     - CustomWebshop Data Type


Tripletex Product to CustomWebshop Product
------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a CustomWebshop Product.

Once a link between a Tripletex Product and a CustomWebshop Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a CustomWebshop Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - CustomWebshop Product Property
     - CustomWebshop Data Type

