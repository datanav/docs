=============================
Tilores to CRMOffice Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to CRMOffice Contacts
-----------------------------------
Every Tilores Human will be synchronized with a CRMOffice Contacts.

Once a link between a Tilores Human and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"

