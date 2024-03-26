==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Projects to  Projects
-----------------------------------
Every Powerofficego Projects will be synchronized with a  Projects.

Once a link between a Powerofficego Projects and a  Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Projects:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Projects Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - ProjectManagerEmployeeId
     - owner.gid
     - "string"

