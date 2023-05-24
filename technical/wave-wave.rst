===============================
Wave Financial to Wave Dataflow
===============================

Generated: 2023-05-24 13:06:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to Wave Customer
-----------------------------
Every Wave Invoice will be synchronized with a Wave Customer.

Once a link between a Wave Invoice and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Wave Customer Property
     - Wave Data Type

