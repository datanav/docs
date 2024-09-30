===========================
Invoiced to Trello Dataflow
===========================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers (organisation data) to Trello Organizations
--------------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Trello Organizations.

Once a link between a Invoiced Customers (organisation data) and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"


Invoiced Customers (human data) to Trello Members
-------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Trello Members.

Once a link between a Invoiced Customers (human data) and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Trello Members Property
     - Trello Data Type
   * - name
     - fullName
     - "string"

