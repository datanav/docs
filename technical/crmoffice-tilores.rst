=============================
CRMOffice to Tilores Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to Tilores Human
-----------------------------------
Every CRMOffice Contacts will be synchronized with a Tilores Human.

Once a link between a CRMOffice Contacts and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Tilores Human Property
     - Tilores Data Type
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"

