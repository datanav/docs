================================
Freshteam to Unieconomy Dataflow
================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Unieconomy Countries
------------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Unieconomy Countries must be established.

A Freshteam Employee will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Unieconomy Countries Property
   * - address.country
     - Name
   * - communication_address.communication_country
     - Name

Once a link between a Freshteam Employee and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Freshteam Department to Unieconomy Departments
----------------------------------------------
Every Freshteam Department will be synchronized with a Unieconomy Departments.

Once a link between a Freshteam Department and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - name
     - Name
     - "string"

