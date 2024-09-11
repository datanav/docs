==============================
CustomPMS to Invoiced Dataflow
==============================

Generated: 2024-09-11 07:55:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomPMS to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomPMS Customer to Invoiced Customers company
------------------------------------------------
Every CustomPMS Customer will be synchronized with a Invoiced Customers company.

Once a link between a CustomPMS Customer and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomPMS Customer and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - CustomPMS Customer Property
     - Invoiced Customers company Property
     - Invoiced Data Type

