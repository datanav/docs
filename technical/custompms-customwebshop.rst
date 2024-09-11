===================================
CustomPMS to CustomWebshop Dataflow
===================================

Generated: 2024-09-11 07:56:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomPMS to CustomWebshop. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomPMS Customer to CustomWebshop Customer
--------------------------------------------
Every CustomPMS Customer will be synchronized with a CustomWebshop Customer.

Once a link between a CustomPMS Customer and a CustomWebshop Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomPMS Customer and a CustomWebshop Customer:

.. list-table::
   :header-rows: 1

   * - CustomPMS Customer Property
     - CustomWebshop Customer Property
     - CustomWebshop Data Type

