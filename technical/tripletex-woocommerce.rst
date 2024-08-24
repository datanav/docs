======================
Tripletex to  Dataflow
======================

Generated: 2024-08-24 08:14:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to  Order
-------------------------
Every Tripletex Order will be synchronized with a  Order.

Once a link between a Tripletex Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Order Property
     -  Data Type


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type

