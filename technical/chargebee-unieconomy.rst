================================
Chargebee to Unieconomy Dataflow
================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to Unieconomy Companies
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Unieconomy Companies.

Once a link between a Chargebee Business_entity and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - name
     - Name
     - "string"

