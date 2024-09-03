==========================
Chargebee to Keap Dataflow
==========================

Generated: 2024-09-03 08:57:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Item to Keap Product
------------------------------
Every Chargebee Item will be synchronized with a Keap Product.

Once a link between a Chargebee Item and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Keap Product Property
     - Keap Data Type

