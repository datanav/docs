=============================
Freshteam to Zendesk Dataflow
=============================

Generated: 2023-10-10 21:05:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Zendesk Organisations
---------------------------------------------
Every Freshteam Department will be synchronized with a Zendesk Organisations.

Once a link between a Freshteam Department and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


Freshteam Department to Zendesk Organizations
---------------------------------------------
Every Freshteam Department will be synchronized with a Zendesk Organizations.

Once a link between a Freshteam Department and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"


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
   * - designation
     - organization_id
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.name)
     - phone
     - "string"

