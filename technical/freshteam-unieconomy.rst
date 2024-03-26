================================
Freshteam to Unieconomy Dataflow
================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to  Departments
------------------------------------
Every Freshteam Department will be synchronized with a  Departments.

Once a link between a Freshteam Department and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a  Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     -  Departments Property
     -  Data Type
   * - name
     - Name
     - "string"

