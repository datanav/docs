==============================
Trello to Superoffice Dataflow
==============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Superoffice Person
------------------------------------
Every Trello Members will be synchronized with a Superoffice Person.

Once a link between a Trello Members and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - email
     - Emails.Value
     - "string"


Trello Organizations to Superoffice Contact
-------------------------------------------
Every Trello Organizations will be synchronized with a Superoffice Contact.

Once a link between a Trello Organizations and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"
   * - website
     - Urls.Value
     - "string"

