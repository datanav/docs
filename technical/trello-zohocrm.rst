==========================
Trello to ZohoCRM Dataflow
==========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to ZohoCRM Account
---------------------------------------
Every Trello Organizations will be synchronized with a ZohoCRM Account.

Once a link between a Trello Organizations and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - desc
     - Created_Time
     - "string"
   * - name
     - Account_Name
     - "string"
   * - website
     - Website
     - "string"

