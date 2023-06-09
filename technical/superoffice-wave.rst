============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-06-09 09:07:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to Wave Product
-----------------------------------
Every SuperOffice Product will be synchronized with a Wave Product.

Once a link between a SuperOffice Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - UnitListPrice
     - unitPrice
     - "string"

