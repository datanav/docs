=============================
HubSpot to Chargebee Dataflow
=============================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to Chargebee Order
-------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Chargebee Order.

Once a link between a HubSpot Deal and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Chargebee Order Property
     - Chargebee Data Type


HubSpot Product to Chargebee Item
---------------------------------
Every HubSpot Product will be synchronized with a Chargebee Item.

Once a link between a HubSpot Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Chargebee Item Property
     - Chargebee Data Type

