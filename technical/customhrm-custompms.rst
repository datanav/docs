================================
Custom HRM to CustomPMS Dataflow
================================

Generated: 2024-09-11 11:38:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom HRM to CustomPMS. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomHRM Department to CustomPMS Customer
------------------------------------------
Every CustomHRM Department will be synchronized with a CustomPMS Customer.

Once a link between a CustomHRM Department and a CustomPMS Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomHRM Department and a CustomPMS Customer:

.. list-table::
   :header-rows: 1

   * - CustomHRM Department Property
     - CustomPMS Customer Property
     - CustomPMS Data Type

