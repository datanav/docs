=================================
SuperOffice to Crmoffice Dataflow
=================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Crmoffice Contacts
----------------------------------------
Every SuperOffice Person will be synchronized with a Crmoffice Contacts.

Once a link between a SuperOffice Person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
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


SuperOffice Product to Crmoffice Companies
------------------------------------------
Every SuperOffice Product will be synchronized with a Crmoffice Companies.

Once a link between a SuperOffice Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type

