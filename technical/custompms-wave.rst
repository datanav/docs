===========================
Custom PMS to Wave Dataflow
===========================

Generated: 2024-09-11 07:43:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom PMS to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Customer to Wave Customer
--------------------------------
Every Custom Customer will be synchronized with a Wave Customer.

Once a link between a Custom Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Custom Customer Property
     - Wave Customer Property
     - Wave Data Type

