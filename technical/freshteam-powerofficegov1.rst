=====================================
Freshteam to PowerOfficeGov1 Dataflow
=====================================

Generated: 2023-08-14 08:48:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to PowerOfficeGov1 Employee
----------------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a PowerOfficeGov1 Employee must be established.

A Freshteam Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGov1 Employee Property
   * - employee_id
     - employeeNumber

Once a link between a Freshteam Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type

