===========================
HubSpot to Shopify Dataflow
===========================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Product to Shopify Inventoryitem
----------------------------------------
Every HubSpot Product will be synchronized with a Shopify Inventoryitem.

Once a link between a HubSpot Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - properties.hs_cost_of_goods_sold
     - cost
     - "string"
   * - properties.hs_sku
     - sku
     - "string"


HubSpot Deal to Shopify Order
-----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Shopify Order.

Once a link between a HubSpot Deal and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Shopify Order Property
     - Shopify Data Type
   * - properties.amount
     - current_total_price
     - "string"
   * - properties.amount
     - total_price
     - "string"
   * - properties.deal_currency_code
     - currency
     - "string"
   * - properties.dealname
     - name
     - "string"


HubSpot Product to Shopify Product
----------------------------------
Every HubSpot Product will be synchronized with a Shopify Product.

Once a link between a HubSpot Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - properties.name
     - variants.title
     - "string"
   * - properties.price
     - variants.price
     - "string"

