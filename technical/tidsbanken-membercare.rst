=================================
Tidsbanken to Membercare Dataflow
=================================

Generated: 2024-09-04 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to Membercare Companies
-------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Membercare Companies.

Once a link between a Tidsbanken Avdeling and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Navn
     - companyName
     - "string"


Tidsbanken Kunde to Membercare Companies
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Membercare Companies.

Once a link between a Tidsbanken Kunde and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Navn
     - companyName
     - "string"
   * - Url
     - url
     - "string"


Tidsbanken Avdeling to Membercare Organizations
-----------------------------------------------
Every Tidsbanken Avdeling will be synchronized with a Membercare Organizations.

Once a link between a Tidsbanken Avdeling and a Membercare Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a Membercare Organizations:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     - Membercare Organizations Property
     - Membercare Data Type

