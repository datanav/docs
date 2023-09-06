==========================
Freshteam to Wave Dataflow
==========================

Generated: 2023-09-06 12:00:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Wave Customer
-----------------------------------
Every Freshteam Employee will be synchronized with a Wave Customer.

Once a link between a Freshteam Employee and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Wave Customer Property
     - Wave Data Type
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - mobile
     - "string"

