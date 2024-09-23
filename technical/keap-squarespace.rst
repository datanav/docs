=================
Keap to  Dataflow
=================

Generated: 2024-09-23 09:26:56

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to  Sesamproducts
------------------------------
Before any synchronization can take place, a link between a Keap Product and a  Sesamproducts must be established.

A Keap Product will merge with a  Sesamproducts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     -  Sesamproducts Property
   * - sku
     - variants.sku

Once a link between a Keap Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     -  Sesamproducts Property
     -  Data Type


Keap Product to  Inventory
--------------------------
Every Keap Product will be synchronized with a  Inventory.

Once a link between a Keap Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     -  Inventory Property
     -  Data Type


Keap Product to  Inventory
--------------------------
Every Keap Product will be synchronized with a  Inventory.

Once a link between a Keap Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     -  Inventory Property
     -  Data Type
   * - product_desc
     - descriptor
     - "string"


Keap Product to  Sesamproducts
------------------------------
Every Keap Product will be synchronized with a  Sesamproducts.

Once a link between a Keap Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     -  Sesamproducts Property
     -  Data Type
   * - product_name
     - name
     - "string"
   * - product_price
     - variants.pricing.salePrice.value
     - "string"

