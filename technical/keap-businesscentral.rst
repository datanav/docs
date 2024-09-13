=================================
Keap to Business Central Dataflow
=================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Business Central Companies
--------------------------------------------
Every Keap Companies will be synchronized with a Business Central Companies.

Once a link between a Keap Companies and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Business Central Companies Property
     - Business Central Data Type


Keap Product to Business Central Items
--------------------------------------
Every Keap Product will be synchronized with a Business Central Items.

Once a link between a Keap Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - product_name
     - displayName
     - "string"
   * - product_price
     - unitPrice
     - N/A

