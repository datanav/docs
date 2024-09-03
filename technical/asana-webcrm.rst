==================
Asana to  Dataflow
==================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to  Organisations
-----------------------------
Every Asana Teams will be synchronized with a  Organisations.

Once a link between a Asana Teams and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     -  Organisations Property
     -  Data Type
   * - description
     - OrganisationCompanyDescription
     - "string"
   * - name
     - OrganisationName
     - "string"


Asana Workspaces to  Organisations
----------------------------------
Every Asana Workspaces will be synchronized with a  Organisations.

Once a link between a Asana Workspaces and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Organisations Property
     -  Data Type
   * - name
     - OrganisationName
     - "string"

