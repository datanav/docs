========================
SuperOffice to  Dataflow
========================

Generated: 2024-09-23 11:15:53

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to  Inventory
---------------------------------
Every SuperOffice Product will be synchronized with a  Inventory.

Once a link between a SuperOffice Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Inventory Property
     -  Data Type


SuperOffice Product to  Inventory
---------------------------------
Every SuperOffice Product will be synchronized with a  Inventory.

Once a link between a SuperOffice Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Inventory Property
     -  Data Type
   * - Description
     - descriptor
     - "string"


SuperOffice Product to  Sesamproducts
-------------------------------------
Every SuperOffice Product will be synchronized with a  Sesamproducts.

Once a link between a SuperOffice Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Sesamproducts Property
     -  Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - ProductTypeKey
     - type
     - "string"
   * - UnitCost
     - variants.pricing.basePrice.value
     - "string"
   * - UnitListPrice
     - variants.pricing.salePrice.value
     - "string"

