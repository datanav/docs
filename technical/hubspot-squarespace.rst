====================
HubSpot to  Dataflow
====================

Generated: 2024-09-20 13:15:54

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Product to  Inventory
-----------------------------
Every HubSpot Product will be synchronized with a  Inventory.

Once a link between a HubSpot Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Inventory Property
     -  Data Type
   * - properties.description
     - descriptor
     - "string"
   * - properties.hs_sku
     - sku
     - "string"

