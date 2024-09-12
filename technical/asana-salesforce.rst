============================
Asana to Salesforce Dataflow
============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to Salesforce Task
---------------------------------
Every Asana Projects will be synchronized with a Salesforce Task.

Once a link between a Asana Projects and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - completed_at
     - CompletedDateTime
     - "string"
   * - due_on
     - ActivityDate
     - "string"
   * - name
     - Subject
     - "string"
   * - owner.gid
     - OwnerId
     - "string"


Asana Teams to Salesforce Division
----------------------------------
Every Asana Teams will be synchronized with a Salesforce Division.

Once a link between a Asana Teams and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Asana Workspaces to Salesforce Division
---------------------------------------
Every Asana Workspaces will be synchronized with a Salesforce Division.

Once a link between a Asana Workspaces and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Asana Tasks to Salesforce Task
------------------------------
Every Asana Tasks will be synchronized with a Salesforce Task.

Once a link between a Asana Tasks and a Salesforce Task is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a Salesforce Task:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - Salesforce Task Property
     - Salesforce Data Type
   * - completed_at
     - CompletedDateTime
     - "string"
   * - due_on
     - ActivityDate
     - "string"
   * - name
     - Subject
     - "string"


Asana Users to Salesforce User
------------------------------
Every Asana Users will be synchronized with a Salesforce User.

Once a link between a Asana Users and a Salesforce User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Salesforce User:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Salesforce User Property
     - Salesforce Data Type
   * - email
     - Email
     - "string"
   * - name
     - Name
     - "string"
   * - workspaces.gid
     - EmployeeNumber
     - "string"


Asana Workspaces to Salesforce Organization
-------------------------------------------
Every Asana Workspaces will be synchronized with a Salesforce Organization.

Once a link between a Asana Workspaces and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"

