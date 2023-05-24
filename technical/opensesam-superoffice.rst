=================================
Opensesam to SuperOffice Dataflow
=================================

Generated: 2023-05-24 08:54:50

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Opensesam to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Opensesam Organisation to SuperOffice Contact
---------------------------------------------
Every Opensesam Organisation will be synchronized with a SuperOffice Contact.

Once a link between a Opensesam Organisation and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Opensesam Organisation and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Opensesam Organisation Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - p:P4649.ps:P4649
     - OrgNr (Dependant on having p:P4649.ps:P3864 in Country.ThreeLetterISOCountry)
     - "string"

