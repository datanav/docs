==================
Asana to  Dataflow
==================

Generated: 2024-09-04 13:26:45

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to  Boards
-------------------------
Every Asana Projects will be synchronized with a  Boards.

Once a link between a Asana Projects and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a  Boards:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     -  Boards Property
     -  Data Type
   * - name
     - name
     - "string"


Asana Users to  Members
-----------------------
Every Asana Users will be synchronized with a  Members.

Once a link between a Asana Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Members:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Members Property
     -  Data Type
   * - name
     - fullName
     - "string"


Asana Workspaces to  Organizations
----------------------------------
Every Asana Workspaces will be synchronized with a  Organizations.

Once a link between a Asana Workspaces and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Organizations Property
     -  Data Type
   * - email_domains
     - website
     - "string"
   * - name
     - name
     - "string"

