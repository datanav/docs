========================
Asana to WebCRM Dataflow
========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to WebCRM Organisations
-----------------------------------
Every Asana Teams will be synchronized with a WebCRM Organisations.

Once a link between a Asana Teams and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - description
     - OrganisationCompanyDescription
     - "string"
   * - name
     - OrganisationName
     - "string"


Asana Workspaces to WebCRM Organisations
----------------------------------------
Every Asana Workspaces will be synchronized with a WebCRM Organisations.

Once a link between a Asana Workspaces and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"

