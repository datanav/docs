================================
Tidsbanken to Freshteam Dataflow
================================

Generated: 2024-03-26 14:23:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Freshteam Employee
---------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Freshteam Employee must be established.

A Tidsbanken Ansatt will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Freshteam Employee Property
   * - Id
     - employee_id

Once a link between a Tidsbanken Ansatt and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Freshteam Employee Property
     - Freshteam Data Type

