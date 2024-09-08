========================
Asana to Webcrm Dataflow
========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Webcrm Organisations
-----------------------------------
Every Asana Teams will be synchronized with a Webcrm Organisations.

Once a link between a Asana Teams and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - description
     - OrganisationCompanyDescription
     - "string"
   * - name
     - OrganisationName
     - "string"


Asana Workspaces to Webcrm Organisations
----------------------------------------
Every Asana Workspaces will be synchronized with a Webcrm Organisations.

Once a link between a Asana Workspaces and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"

