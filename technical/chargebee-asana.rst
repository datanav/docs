===========================
Chargebee to Asana Dataflow
===========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Asana Workspaces
---------------------------------------------
Every Chargebee Business_entity will be synchronized with a Asana Workspaces.

Once a link between a Chargebee Business_entity and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Asana Workspaces Property
     - Asana Data Type
   * - name
     - name
     - "string"

