============================
Businesscentral to  Dataflow
============================

Generated: 2024-01-10 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Workspaces
------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Workspaces.

Once a link between a Businesscentral Customers company and a  Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Workspaces:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Workspaces Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - website
     - email_domains
     - "string"

