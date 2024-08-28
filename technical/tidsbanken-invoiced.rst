=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-08-28 07:50:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to  Customers company
--------------------------------------
Every Tidsbanken Kunde will be synchronized with a  Customers company.

Once a link between a Tidsbanken Kunde and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Customers company Property
     -  Data Type
   * - Gateadresse
     - address1
     - "string"
   * - Id
     - id
     - "string"

