==========================
Freshteam to Keap Dataflow
==========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Keap Companies
--------------------------------------
Every Freshteam Department will be synchronized with a Keap Companies.

Once a link between a Freshteam Department and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"


Freshteam Employee to Keap Contacts
-----------------------------------
Every Freshteam Employee will be synchronized with a Keap Contacts.

Once a link between a Freshteam Employee and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Keap Contacts Property
     - Keap Data Type
   * - date_of_birth
     - birthday
     - "string"

