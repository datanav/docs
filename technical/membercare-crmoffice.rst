================================
MemberCare to CRMOffice Dataflow
================================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Persons to Crmoffice Contacts
----------------------------------------
Every MemberCare Persons will be synchronized with a Crmoffice Contacts.

Once a link between a MemberCare Persons and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstname
     - givenName
     - "string"
   * - lastname
     - familyName
     - "string"


MemberCare Products to Crmoffice Companies
------------------------------------------
Every MemberCare Products will be synchronized with a Crmoffice Companies.

Once a link between a MemberCare Products and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Crmoffice Companies Property
     - Crmoffice Data Type

