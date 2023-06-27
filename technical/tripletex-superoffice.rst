=================================
Tripletex to SuperOffice Dataflow
=================================

Generated: 2023-06-27 05:05:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to SuperOffice Quotealternative
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Order and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Tripletex Order if it is connected to a Tripletex Orderline that is synchronized into SuperOffice.

Once a link between a Tripletex Order and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type


Tripletex Orderline to SuperOffice Quoteline
--------------------------------------------
Every Tripletex Orderline will be synchronized with a SuperOffice Quoteline.

Once a link between a Tripletex Orderline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type

