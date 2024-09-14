=========================
WebCRM to Trello Dataflow
=========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Trello Organizations
--------------------------------------------
Every WebCRM Organisations will be synchronized with a Trello Organizations.

Once a link between a WebCRM Organisations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Trello Organizations Property
     - Trello Data Type
   * - OrganisationCompanyDescription
     - desc
     - "string"
   * - OrganisationName
     - name
     - "string"


WebCRM Persons to Trello Members
--------------------------------
Every WebCRM Persons will be synchronized with a Trello Members.

Once a link between a WebCRM Persons and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Trello Members:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Trello Members Property
     - Trello Data Type
   * - PersonName
     - fullName
     - "string"


WebCRM Users to Trello Members
------------------------------
Every WebCRM Users will be synchronized with a Trello Members.

Once a link between a WebCRM Users and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a Trello Members:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - Trello Members Property
     - Trello Data Type

