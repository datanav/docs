====================
HubSpot to  Dataflow
====================

Generated: 2024-05-03 12:07:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Product to  Inventoryitem
---------------------------------
Every HubSpot Product will be synchronized with a  Inventoryitem.

Once a link between a HubSpot Product and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Inventoryitem Property
     -  Data Type
   * - properties.hs_cost_of_goods_sold
     - cost
     - "string"


HubSpot Product to  Product
---------------------------
Every HubSpot Product will be synchronized with a  Product.

Once a link between a HubSpot Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Product Property
     -  Data Type

