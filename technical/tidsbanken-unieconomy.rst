=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-03-26 14:23:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to  Companies
------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a  Companies must be established.

A Tidsbanken Kunde will merge with a  Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
   * - Organisasjonsnummer
     - OrganizationNumber

Once a link between a Tidsbanken Kunde and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
     -  Data Type


Tidsbanken Kunde to  Customers
------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a  Customers must be established.

A Tidsbanken Kunde will merge with a  Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Customers Property
   * - Organisasjonsnummer
     - OrgNumber

Once a link between a Tidsbanken Kunde and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Customers:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Customers Property
     -  Data Type

