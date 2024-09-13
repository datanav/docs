===============================
Chargebee to Chargebee Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Item_family to Chargebee Currency
-------------------------------------------
Every Chargebee Item_family will be synchronized with a Chargebee Currency.

Once a link between a Chargebee Item_family and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Chargebee Currency Property
     - Chargebee Data Type

