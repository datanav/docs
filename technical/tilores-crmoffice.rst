=============================
Tilores to Crmoffice Dataflow
=============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Crmoffice Contacts
-----------------------------------
Every Tilores Human will be synchronized with a Crmoffice Contacts.

Once a link between a Tilores Human and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"

