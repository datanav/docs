================================
MemberCare to CRMOffice Dataflow
================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Persons to CRMOffice Contacts
----------------------------------------
Every MemberCare Persons will be synchronized with a CRMOffice Contacts.

Once a link between a MemberCare Persons and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - firstname
     - givenName
     - "string"
   * - lastname
     - familyName
     - "string"


MemberCare Products to CRMOffice Companies
------------------------------------------
Every MemberCare Products will be synchronized with a CRMOffice Companies.

Once a link between a MemberCare Products and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


MemberCare Companies to CRMOffice Companies
-------------------------------------------
Every MemberCare Companies will be synchronized with a CRMOffice Companies.

Once a link between a MemberCare Companies and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - CRMOffice Companies Property
     - CRMOffice Data Type
   * - addresses.country.id
     - postAddress.country
     - "string"
   * - addresses.country.id
     - visitAddress.country
     - "string"
   * - addresses.id
     - id
     - "string"
   * - addresses.postalCode.city
     - postAddress.postalArea
     - "string"
   * - addresses.postalCode.city
     - visitAddress.postalArea
     - "string"
   * - addresses.postalCode.zipCode
     - postAddress.postCode
     - "string"
   * - addresses.postalCode.zipCode
     - visitAddress.postCode
     - "string"

