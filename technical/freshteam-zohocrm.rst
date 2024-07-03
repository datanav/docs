=============================
Freshteam to ZohoCRM Dataflow
=============================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to ZohoCRM Account
---------------------------------------
Every Freshteam Department will be synchronized with a ZohoCRM Account.

Once a link between a Freshteam Department and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

