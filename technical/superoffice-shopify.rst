===============================
SuperOffice to Shopify Dataflow
===============================

Generated: 2024-07-03 06:58:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quotealternative to Shopify Order
---------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Shopify Order must be established.

A new Shopify Order will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Shopify.

Once a link between a SuperOffice Quotealternative and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Shopify Order Property
     - Shopify Data Type


SuperOffice Product to Shopify Inventoryitem
--------------------------------------------
Every SuperOffice Product will be synchronized with a Shopify Inventoryitem.

Once a link between a SuperOffice Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - UnitCost
     - cost
     - "string"


SuperOffice Product to Shopify Product
--------------------------------------
Every SuperOffice Product will be synchronized with a Shopify Product.

Once a link between a SuperOffice Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - Name
     - variants.title
     - "string"
   * - UnitListPrice
     - variants.price
     - "string"

