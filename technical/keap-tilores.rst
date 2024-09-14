========================
Keap to Tilores Dataflow
========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Contacts to Tilores Human
------------------------------
Every Keap Contacts will be synchronized with a Tilores Human.

Once a link between a Keap Contacts and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Contacts and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Keap Contacts Property
     - Tilores Human Property
     - Tilores Data Type
   * - birthday
     - dateOfBirth
     - "string"

