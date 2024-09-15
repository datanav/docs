=======================
Trello to Keap Dataflow
=======================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Keap Contacts
-------------------------------
Every Trello Members will be synchronized with a Keap Contacts.

Once a link between a Trello Members and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Keap Contacts Property
     - Keap Data Type


Trello Organizations to Keap Companies
--------------------------------------
Every Trello Organizations will be synchronized with a Keap Companies.

Once a link between a Trello Organizations and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Keap Companies Property
     - Keap Data Type
   * - name
     - company_name
     - "string"

