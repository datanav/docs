=============================
Freshteam to Zendesk Dataflow
=============================

Generated: 2023-08-17 09:11:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Zendesk Users
-----------------------------------
Every Freshteam Employee will be synchronized with a Zendesk Users.

Once a link between a Freshteam Employee and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - phone
     - "string"

