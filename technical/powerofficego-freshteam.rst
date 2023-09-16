===================================
Powerofficego to Freshteam Dataflow
===================================

Generated: 2023-09-16 14:59:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Departments to Freshteam Department
-------------------------------------------------
Every Powerofficego Departments will be synchronized with a Freshteam Department.

Once a link between a Powerofficego Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - CreatedDateTimeOffset
     - created_at
     - "string"
   * - Name
     - name
     - "string"

