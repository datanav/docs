================================
Tidsbanken to Customerp Dataflow
================================

Generated: 2024-09-10 14:20:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Customerp. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Customerp Customer
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a Customerp Customer.

Once a link between a Tidsbanken Kunde and a Customerp Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Customerp Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Customerp Customer Property
     - Customerp Data Type

