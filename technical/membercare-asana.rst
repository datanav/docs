============================
Membercare to Asana Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Asana Workspaces
----------------------------------------
Every Membercare Companies will be synchronized with a Asana Workspaces.

Once a link between a Membercare Companies and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Asana Workspaces Property
     - Asana Data Type
   * - companyName
     - name
     - "string"
   * - url
     - email_domains
     - "string"

