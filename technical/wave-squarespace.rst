=================
Wave to  Dataflow
=================

Generated: 2024-09-24 13:32:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Product to  Inventory
--------------------------
Every Wave Product will be synchronized with a  Inventory.

Once a link between a Wave Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Inventory Property
     -  Data Type


Wave Invoice to  Order
----------------------
Every Wave Invoice will be synchronized with a  Order.

Once a link between a Wave Invoice and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Order Property
     -  Data Type


Wave Product to  Inventory
--------------------------
Every Wave Product will be synchronized with a  Inventory.

Once a link between a Wave Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Inventory Property
     -  Data Type
   * - description
     - descriptor
     - "string"


Wave Product to  Sesamproducts
------------------------------
Every Wave Product will be synchronized with a  Sesamproducts.

Once a link between a Wave Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Sesamproducts Property
     -  Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - variants.pricing.salePrice.value
     - "string"

