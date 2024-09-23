===================
WebCRM to  Dataflow
===================

Generated: 2024-09-23 09:25:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Products to  Inventory
-----------------------------
Every WebCRM Products will be synchronized with a  Inventory.

Once a link between a WebCRM Products and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a  Inventory:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     -  Inventory Property
     -  Data Type


WebCRM Products to  Inventory
-----------------------------
Every WebCRM Products will be synchronized with a  Inventory.

Once a link between a WebCRM Products and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a  Inventory:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     -  Inventory Property
     -  Data Type
   * - ProductQuantity
     - quantity
     - "string"


WebCRM Products to  Sesamproducts
---------------------------------
Every WebCRM Products will be synchronized with a  Sesamproducts.

Once a link between a WebCRM Products and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     -  Sesamproducts Property
     -  Data Type
   * - ProductCostPrice
     - variants.pricing.basePrice.value
     - "string"
   * - ProductPrice
     - variants.pricing.salePrice.value
     - "string"

