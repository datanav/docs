===============================
HubSpot to Woocommerce Dataflow
===============================

Generated: 2024-09-10 00:00:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to Woocommerce Order
---------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Woocommerce Order.

Once a link between a HubSpot Deal and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Product to Woocommerce Product
--------------------------------------
Every HubSpot Product will be synchronized with a Woocommerce Product.

Once a link between a HubSpot Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
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

