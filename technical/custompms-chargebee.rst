===============================
Custompms to Chargebee Dataflow
===============================

Generated: 2024-09-10 15:43:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custompms to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Custompms Customer to Chargebee Business_entity
-----------------------------------------------
Every Custompms Customer will be synchronized with a Chargebee Business_entity.

Once a link between a Custompms Customer and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Custompms Customer and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Custompms Customer Property
     - Chargebee Business_entity Property
     - Chargebee Data Type

