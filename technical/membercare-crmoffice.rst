================================
Membercare to Crmoffice Dataflow
================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Persons to Crmoffice Contacts
----------------------------------------
Every Membercare Persons will be synchronized with a Crmoffice Contacts.

Once a link between a Membercare Persons and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstname
     - givenName
     - "string"
   * - lastname
     - familyName
     - "string"


Membercare Products to Crmoffice Companies
------------------------------------------
Every Membercare Products will be synchronized with a Crmoffice Companies.

Once a link between a Membercare Products and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Crmoffice Companies Property
     - Crmoffice Data Type

