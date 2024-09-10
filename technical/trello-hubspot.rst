==========================
Trello to Hubspot Dataflow
==========================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Hubspot Contact
---------------------------------
Every Trello Members will be synchronized with a Hubspot Contact.

Once a link between a Trello Members and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - email
     - properties.email
     - "string"


Trello Organizations to Hubspot Company
---------------------------------------
Every Trello Organizations will be synchronized with a Hubspot Company.

Once a link between a Trello Organizations and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - desc
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - website
     - properties.website
     - "string"

