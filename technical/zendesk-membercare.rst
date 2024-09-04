==============================
Zendesk to Membercare Dataflow
==============================

Generated: 2024-09-04 10:50:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Membercare Companies
---------------------------------------------
Every Zendesk Organizations will be synchronized with a Membercare Companies.

Once a link between a Zendesk Organizations and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"


Zendesk Users to Membercare Persons
-----------------------------------
Every Zendesk Users will be synchronized with a Membercare Persons.

Once a link between a Zendesk Users and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Membercare Persons Property
     - Membercare Data Type

