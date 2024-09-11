=================================
Custom PMS to Custom HRM Dataflow
=================================

Generated: 2024-09-11 07:44:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom PMS to Custom HRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Customer to Custom Department
------------------------------------
Every Custom Customer will be synchronized with a Custom Department.

Once a link between a Custom Customer and a Custom Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Customer and a Custom Department:

.. list-table::
   :header-rows: 1

   * - Custom Customer Property
     - Custom Department Property
     - Custom Data Type

