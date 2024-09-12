================================
Chargebee to Custom PMS Dataflow
================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Custom PMS. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Custom PMS Customer
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Custom PMS Customer.

Once a link between a Chargebee Business_entity and a Custom PMS Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Custom PMS Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Custom PMS Customer Property
     - Custom PMS Data Type

