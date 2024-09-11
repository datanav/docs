==================================
Business Nxt to Tripletex Dataflow
==================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to Tripletex Order
------------------------------------
Every BusinessNxt Order will be synchronized with a Tripletex Order.

Once a link between a BusinessNxt Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - dueDate
     - deliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A


BusinessNxt Orderline to Tripletex Orderline
--------------------------------------------
Every BusinessNxt Orderline will be synchronized with a Tripletex Orderline.

Once a link between a BusinessNxt Orderline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - orderNo
     - order.id
     - "integer"


BusinessNxt Product to Tripletex Product
----------------------------------------
Every BusinessNxt Product will be synchronized with a Tripletex Product.

Once a link between a BusinessNxt Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - priceExcludingVatCurrency
     - "float"
   * - quantityPerUnit
     - stockOfGoods
     - "integer"

