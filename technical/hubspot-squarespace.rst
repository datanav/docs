====================
HubSpot to  Dataflow
====================

Generated: 2024-09-24 00:00:03

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


HubSpot Deal to  Order
----------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Order.

Once a link between a HubSpot Deal and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Order Property
     -  Data Type


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


HubSpot Product to  Sesamproducts
---------------------------------
Every HubSpot Product will be synchronized with a  Sesamproducts.

Once a link between a HubSpot Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Sesamproducts Property
     -  Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - variants.pricing.basePrice.value
     - "string"
   * - properties.hs_sku
     - variants.sku
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - variants.pricing.salePrice.value
     - "string"

