==============================
Trello to SuperOffice Dataflow
==============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to SuperOffice Person
------------------------------------
Every Trello Members will be synchronized with a SuperOffice Person.

Once a link between a Trello Members and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - email
     - Emails.Value
     - "string"


Trello Organizations to SuperOffice Contact
-------------------------------------------
Every Trello Organizations will be synchronized with a SuperOffice Contact.

Once a link between a Trello Organizations and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - website
     - Urls.Value
     - "string"

