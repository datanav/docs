=================================
Tidsbanken to Membercare Dataflow
=================================

Generated: 2024-09-03 09:00:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to  Companies
---------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Companies.

Once a link between a Tidsbanken Avdeling and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Companies Property
     -  Data Type
   * - Navn
     - companyName
     - "string"


Tidsbanken Kunde to  Companies
------------------------------
Every Tidsbanken Kunde will be synchronized with a  Companies.

Once a link between a Tidsbanken Kunde and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Companies Property
     -  Data Type
   * - Navn
     - companyName
     - "string"
   * - Url
     - url
     - "string"

