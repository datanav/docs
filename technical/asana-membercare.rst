==================
Asana to  Dataflow
==================

Generated: 2024-09-02 13:32:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Workspaces to  Companies
------------------------------
Every Asana Workspaces will be synchronized with a  Companies.

Once a link between a Asana Workspaces and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Companies Property
     -  Data Type
   * - email_domains
     - url
     - "string"
   * - name
     - name
     - "string"

