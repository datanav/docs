============================
Salesforce to Asana Dataflow
============================

Generated: 2024-09-12 00:00:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to Asana Workspaces
-------------------------------------------
Every Salesforce Organization will be synchronized with a Asana Workspaces.

Once a link between a Salesforce Organization and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Asana Workspaces Property
     - Asana Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Task to Asana Tasks
------------------------------
Every Salesforce Task will be synchronized with a Asana Tasks.

Once a link between a Salesforce Task and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Task and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - Salesforce Task Property
     - Asana Tasks Property
     - Asana Data Type
   * - ActivityDate
     - due_on
     - "string"
   * - CompletedDateTime
     - completed_at
     - "string"
   * - Subject
     - name
     - "string"

