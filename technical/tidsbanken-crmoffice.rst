================================
Tidsbanken to Crmoffice Dataflow
================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Crmoffice Contacts
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a Crmoffice Contacts.

Once a link between a Tidsbanken Ansatt and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - Etternavn
     - familyName
     - "string"
   * - Fornavn
     - givenName
     - "string"
   * - Mobil
     - mobilePhone
     - "string"


Tidsbanken Prosjekt to Crmoffice Activities
-------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a Crmoffice Activities.

Once a link between a Tidsbanken Prosjekt and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - AnsvarligId
     - ownerId
     - "string"
   * - FerdigDato
     - endsAt
     - "string"
   * - Navn
     - subject
     - "string"
   * - StartDato
     - startsAt
     - "string"

