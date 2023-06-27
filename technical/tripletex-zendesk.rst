=============================
Tripletex to Zendesk Dataflow
=============================

Generated: 2023-06-27 05:12:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to Zendesk Users
-----------------------------------
Every Tripletex Employee will be synchronized with a Zendesk Users.

Once a link between a Tripletex Employee and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - phoneNumberHome
     - phone
     - "string"

