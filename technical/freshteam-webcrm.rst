============================
Freshteam to Webcrm Dataflow
============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Webcrm Organisations
--------------------------------------------
Every Freshteam Department will be synchronized with a Webcrm Organisations.

Once a link between a Freshteam Department and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"

