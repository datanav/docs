============================
Freshteam to WebCRM Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to WebCRM Organisations
--------------------------------------------
Every Freshteam Department will be synchronized with a WebCRM Organisations.

Once a link between a Freshteam Department and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"

