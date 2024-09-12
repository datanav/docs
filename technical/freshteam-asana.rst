===========================
Freshteam to Asana Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Asana Users
---------------------------------
Every Freshteam Employee will be synchronized with a Asana Users.

Once a link between a Freshteam Employee and a Asana Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Asana Users:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Asana Users Property
     - Asana Data Type
   * - first_name
     - name
     - "string"

