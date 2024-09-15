==========================
Trello to HubSpot Dataflow
==========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to HubSpot Contact
---------------------------------
Every Trello Members will be synchronized with a HubSpot Contact.

Once a link between a Trello Members and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - email
     - properties.email
     - "string"


Trello Organizations to HubSpot Company
---------------------------------------
Every Trello Organizations will be synchronized with a HubSpot Company.

Once a link between a Trello Organizations and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - desc
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - website
     - properties.website
     - "string"

