================================
Freshteam to UniEconomy Dataflow
================================

Generated: 2023-06-19 11:57:32

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to UniEconomy Departments
----------------------------------------------
Every Freshteam Department will be synchronized with a UniEconomy Departments.

Once a link between a Freshteam Department and a UniEconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a UniEconomy Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - UniEconomy Departments Property
     - UniEconomy Data Type
   * - name
     - Name
     - "string"

