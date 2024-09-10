=================================
HubSpot to Customwebshop Dataflow
=================================

Generated: 2024-09-10 14:35:47

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Customwebshop. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to Customwebshop Order
-----------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Customwebshop Order.

Once a link between a HubSpot Deal and a Customwebshop Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Customwebshop Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Customwebshop Order Property
     - Customwebshop Data Type


HubSpot Product to Customwebshop Product
----------------------------------------
Every HubSpot Product will be synchronized with a Customwebshop Product.

Once a link between a HubSpot Product and a Customwebshop Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Customwebshop Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Customwebshop Product Property
     - Customwebshop Data Type

