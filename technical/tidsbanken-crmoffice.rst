=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-08-23 13:09:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to  Contacts
------------------------------
Every Tidsbanken Ansatt will be synchronized with a  Contacts.

Once a link between a Tidsbanken Ansatt and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Contacts Property
     -  Data Type
   * - Etternavn
     - familyName
     - "string"
   * - Fornavn
     - givenName
     - "string"
   * - Mobil
     - mobilePhone
     - "string"


Tidsbanken Prosjekt to  Activities
----------------------------------
Every Tidsbanken Prosjekt will be synchronized with a  Activities.

Once a link between a Tidsbanken Prosjekt and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a  Activities:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     -  Activities Property
     -  Data Type

