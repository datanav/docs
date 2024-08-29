============================
Salesforce to Asana Dataflow
============================

Generated: 2024-08-29 08:03:18

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

