=============================
Trello to Salesforce Dataflow
=============================

Generated: 2024-09-09 11:17:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to Salesforce Division
-------------------------------------------
Every Trello Organizations will be synchronized with a Salesforce Division.

Once a link between a Trello Organizations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Trello Cards to Salesforce Task
-------------------------------
Every Trello Cards will be synchronized with a Salesforce Task.

Once a link between a Trello Cards and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Cards and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Trello Cards Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - due
     - ActivityDate
     - "string"
   * - dueComplete
     - CompletedDateTime
     - "string"
   * - name
     - Subject
     - "string"


Trello Organizations to Salesforce Organization
-----------------------------------------------
Every Trello Organizations will be synchronized with a Salesforce Organization.

Once a link between a Trello Organizations and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"

