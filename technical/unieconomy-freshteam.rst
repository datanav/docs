================================
Unieconomy to Freshteam Dataflow
================================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Departments to Freshteam Department
----------------------------------------------
Every Unieconomy Departments will be synchronized with a Freshteam Department.

Once a link between a Unieconomy Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - Name
     - name
     - "string"

