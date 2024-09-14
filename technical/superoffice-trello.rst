==============================
SuperOffice to Trello Dataflow
==============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Trello Organizations
-------------------------------------------
Every SuperOffice Contact will be synchronized with a Trello Organizations.

Once a link between a SuperOffice Contact and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Trello Organizations Property
     - Trello Data Type
   * - Name
     - name
     - "string"
   * - Urls.Value
     - website
     - "string"


SuperOffice Person to Trello Members
------------------------------------
Every SuperOffice Person will be synchronized with a Trello Members.

Once a link between a SuperOffice Person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Trello Members Property
     - Trello Data Type
   * - Emails.Value
     - email
     - "string"

