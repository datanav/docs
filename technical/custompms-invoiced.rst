===============================
Custom PMS to Invoiced Dataflow
===============================

Generated: 2024-09-17 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom PMS to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom PMS Customer to Invoiced Customers company
-------------------------------------------------
Every Custom PMS Customer will be synchronized with a Invoiced Customers company.

Once a link between a Custom PMS Customer and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom PMS Customer and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - Custom PMS Customer Property
     - Invoiced Customers company Property
     - Invoiced Data Type

