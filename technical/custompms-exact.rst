==================================
CustomPMS to Exact Online Dataflow
==================================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CustomPMS to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custom Customer to Exact Accounts
---------------------------------
Every Custom Customer will be synchronized with a Exact Accounts.

Once a link between a Custom Customer and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custom Customer and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Custom Customer Property
     - Exact Accounts Property
     - Exact Data Type

