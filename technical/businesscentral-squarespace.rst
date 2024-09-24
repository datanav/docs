=============================
Business Central to  Dataflow
=============================

Generated: 2024-09-24 00:00:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Items to  Inventory
------------------------------------
Every Business Central Items will be synchronized with a  Inventory.

Once a link between a Business Central Items and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     -  Inventory Property
     -  Data Type
   * - inventory
     - quantity
     - "string"


Business Central Items to  Inventory
------------------------------------
Every Business Central Items will be synchronized with a  Inventory.

Once a link between a Business Central Items and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     -  Inventory Property
     -  Data Type


Business Central Items to  Sesamproducts
----------------------------------------
Every Business Central Items will be synchronized with a  Sesamproducts.

Once a link between a Business Central Items and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     -  Sesamproducts Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - inventory
     - variants.stock.quantity
     - "string"
   * - unitCost
     - variants.pricing.basePrice.value
     - "string"
   * - unitPrice
     - variants.pricing.salePrice.value
     - "string"


Business Central Salesorders to  Order
--------------------------------------
Every Business Central Salesorders will be synchronized with a  Order.

Once a link between a Business Central Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     -  Order Property
     -  Data Type

