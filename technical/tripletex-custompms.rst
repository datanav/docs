===============================
Tripletex to Custompms Dataflow
===============================

Generated: 2024-09-10 14:31:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Custompms. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Custompms Customer
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Custompms Customer.

Once a link between a Tripletex Customer and a Custompms Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Custompms Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Custompms Customer Property
     - Custompms Data Type

