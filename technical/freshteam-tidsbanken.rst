================================
Freshteam to Tidsbanken Dataflow
================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Tidsbanken Ansatt
---------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Tidsbanken Ansatt must be established.

A Freshteam Employee will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tidsbanken Ansatt Property
   * - employee_id
     - Id

Once a link between a Freshteam Employee and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type


Freshteam Department to Tidsbanken Avdeling
-------------------------------------------
Every Freshteam Department will be synchronized with a Tidsbanken Avdeling.

Once a link between a Freshteam Department and a Tidsbanken Avdeling is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Tidsbanken Avdeling:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Tidsbanken Avdeling Property
     - Tidsbanken Data Type


Freshteam Employee to Tidsbanken Ansatt
---------------------------------------
Every Freshteam Employee will be synchronized with a Tidsbanken Ansatt.

Once a link between a Freshteam Employee and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type

