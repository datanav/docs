============================
Asana to Membercare Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Membercare Companies
-----------------------------------
Every Asana Teams will be synchronized with a Membercare Companies.

Once a link between a Asana Teams and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"
   * - name
     - name
     - "string"
   * - permalink_url
     - url
     - "string"


Asana Workspaces to Membercare Companies
----------------------------------------
Every Asana Workspaces will be synchronized with a Membercare Companies.

Once a link between a Asana Workspaces and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Membercare Companies Property
     - Membercare Data Type
   * - email_domains
     - url
     - "string"
   * - name
     - companyName
     - "string"
   * - name
     - name
     - "string"

