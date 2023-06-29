============================
Asana to UniEconomy Dataflow
============================

Generated: 2023-06-29 21:29:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Workspaces to UniEconomy Companies
----------------------------------------
Every Asana Workspaces will be synchronized with a UniEconomy Companies.

Once a link between a Asana Workspaces and a UniEconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a UniEconomy Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - UniEconomy Companies Property
     - UniEconomy Data Type
   * - name
     - Name
     - "string"

