===============================
HubSpot to WooCommerce Dataflow
===============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to WooCommerce Order
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a WooCommerce Order.

Once a link between a HubSpot Deal and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Product to WooCommerce Product
--------------------------------------
Every HubSpot Product will be synchronized with a WooCommerce Product.

Once a link between a HubSpot Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - properties.hs_cost_of_goods_sold
     - price
     - "string"
   * - properties.hs_sku
     - sku
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - sale_price
     - "string"

