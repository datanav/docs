========================
Wix.com to Wave Dataflow
========================

Generated: 2023-09-05 14:08:56

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Inventory to Wave Product
---------------------------------
Every Wix.com Inventory will be synchronized with a Wave Product.

Once a link between a Wix.com Inventory and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - Wave Product Property
     - Wave Data Type


Wix.com Products to Wave Product
--------------------------------
Every Wix.com Products will be synchronized with a Wave Product.

Once a link between a Wix.com Products and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - price.price
     - unitPrice
     - "string"

