=============================
Zendesk to Chargebee Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Chargebee Business_entity
--------------------------------------------------
Every Zendesk Organizations will be synchronized with a Chargebee Business_entity.

Once a link between a Zendesk Organizations and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Zendesk Users to Chargebee Customer
-----------------------------------
Every Zendesk Users will be synchronized with a Chargebee Customer.

Once a link between a Zendesk Users and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"

