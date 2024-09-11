================================
Custom PMS to CustomCRM Dataflow
================================

Generated: 2024-09-11 11:38:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom PMS to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomPMS Customer to CustomCRM Customer
----------------------------------------
Every CustomPMS Customer will be synchronized with a CustomCRM Customer.

Once a link between a CustomPMS Customer and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomPMS Customer and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - CustomPMS Customer Property
     - CustomCRM Customer Property
     - CustomCRM Data Type

