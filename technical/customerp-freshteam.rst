================================
Custom ERP to Freshteam Dataflow
================================

Generated: 2024-09-11 07:43:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom ERP to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Employee to Freshteam Employee
-------------------------------------
Every Custom Employee will be synchronized with a Freshteam Employee.

Once a link between a Custom Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Custom Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type

