======================
Tripletex to  Dataflow
======================

Generated: 2024-09-20 13:11:59

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to  Inventory
-------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Inventory.

Once a link between a Tripletex Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Inventory Property
     -  Data Type
   * - description
     - descriptor
     - "string"

