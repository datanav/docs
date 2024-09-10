=========================
Webcrm to Trello Dataflow
=========================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Trello Organizations
--------------------------------------------
Every Webcrm Organisations will be synchronized with a Trello Organizations.

Once a link between a Webcrm Organisations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Trello Organizations Property
     - Trello Data Type
   * - OrganisationCompanyDescription
     - desc
     - "string"
   * - OrganisationName
     - name
     - "string"


Webcrm Persons to Trello Members
--------------------------------
Every Webcrm Persons will be synchronized with a Trello Members.

Once a link between a Webcrm Persons and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Trello Members Property
     - Trello Data Type
   * - PersonName
     - fullName
     - "string"


Webcrm Users to Trello Members
------------------------------
Every Webcrm Users will be synchronized with a Trello Members.

Once a link between a Webcrm Users and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Trello Members Property
     - Trello Data Type

