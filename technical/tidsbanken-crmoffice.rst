================================
Tidsbanken to CRMOffice Dataflow
================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to CRMOffice Contacts
---------------------------------------
Every Tidsbanken Ansatt will be synchronized with a CRMOffice Contacts.

Once a link between a Tidsbanken Ansatt and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - Etternavn
     - familyName
     - "string"
   * - Fornavn
     - givenName
     - "string"
   * - Mobil
     - mobilePhone
     - "string"


Tidsbanken Prosjekt to CRMOffice Activities
-------------------------------------------
Every Tidsbanken Prosjekt will be synchronized with a CRMOffice Activities.

Once a link between a Tidsbanken Prosjekt and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Prosjekt and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Prosjekt Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
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

