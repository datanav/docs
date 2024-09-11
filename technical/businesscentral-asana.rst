==================================
Business Central to Asana Dataflow
==================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Customers company to Asana Workspaces
-----------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Asana Workspaces.

Once a link between a BusinessCentral Customers company and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - Asana Workspaces Property
     - Asana Data Type
   * - displayName
     - name
     - "string"
   * - website
     - email_domains
     - "string"

