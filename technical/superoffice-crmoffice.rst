=================================
SuperOffice to CRMOffice Dataflow
=================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to CRMOffice Contacts
----------------------------------------
Every SuperOffice Person will be synchronized with a CRMOffice Contacts.

Once a link between a SuperOffice Person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - Firstname
     - givenName
     - "string"
   * - Lastname
     - familyName
     - "string"
   * - MobilePhones.Value
     - mobilePhone
     - "string"
   * - OfficePhones.Value
     - directPhone
     - "string"


SuperOffice Product to CRMOffice Companies
------------------------------------------
Every SuperOffice Product will be synchronized with a CRMOffice Companies.

Once a link between a SuperOffice Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type

