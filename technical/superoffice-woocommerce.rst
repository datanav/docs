========================
SuperOffice to  Dataflow
========================

Generated: 2024-07-04 09:43:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to  Products
--------------------------------
Every SuperOffice Product will be synchronized with a  Products.

Once a link between a SuperOffice Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Products Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - UnitCost
     - price
     - "string"
   * - UnitListPrice
     - sale_price
     - "string"

