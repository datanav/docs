================================
Custom HRM to Chargebee Dataflow
================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom HRM to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomHRM Department to Chargebee Business_entity
-------------------------------------------------
Every CustomHRM Department will be synchronized with a Chargebee Business_entity.

Once a link between a CustomHRM Department and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomHRM Department and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - CustomHRM Department Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


CustomHRM Employee to Chargebee Customer
----------------------------------------
Every CustomHRM Employee will be synchronized with a Chargebee Customer.

Once a link between a CustomHRM Employee and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomHRM Employee and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - CustomHRM Employee Property
     - Chargebee Customer Property
     - Chargebee Data Type

