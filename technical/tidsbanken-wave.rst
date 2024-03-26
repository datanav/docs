===========================
Tidsbanken to Wave Dataflow
===========================

Generated: 2024-03-26 14:23:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Wave Customer
---------------------------------
Every Tidsbanken Kunde will be synchronized with a Wave Customer.

Once a link between a Tidsbanken Kunde and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Wave Customer Property
     - Wave Data Type

