========================
SuperOffice to  Dataflow
========================

Generated: 2024-05-14 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to  Inventoryitem
-------------------------------------
Every SuperOffice Product will be synchronized with a  Inventoryitem.

Once a link between a SuperOffice Product and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Inventoryitem Property
     -  Data Type
   * - UnitCost
     - cost
     - "string"


SuperOffice Product to  Product
-------------------------------
Every SuperOffice Product will be synchronized with a  Product.

Once a link between a SuperOffice Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
     -  Data Type
   * - Name
     - variants.title
     - "string"
   * - UnitListPrice
     - variants.price
     - "string"

