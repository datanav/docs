======================
Tripletex to  Dataflow
======================

Generated: 2024-09-23 09:26:56

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to  Inventory
-------------------------------
Every Tripletex Product will be synchronized with a  Inventory.

Once a link between a Tripletex Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Inventory Property
     -  Data Type


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


Tripletex Product to  Inventory
-------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Inventory.

Once a link between a Tripletex Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Inventory Property
     -  Data Type
   * - description
     - descriptor
     - "string"
   * - stockOfGoods
     - quantity
     - "string"


Tripletex Product to  Sesamproducts
-----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Sesamproducts.

Once a link between a Tripletex Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Sesamproducts Property
     -  Data Type
   * - costExcludingVatCurrency
     - variants.pricing.basePrice.value
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - variants.pricing.salePrice.value
     - "string"
   * - stockOfGoods
     - variants.stock.quantity
     - "string"

