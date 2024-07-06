====================
HubSpot to  Dataflow
====================

Generated: 2024-07-06 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to  Orders
-----------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Orders.

Once a link between a HubSpot Deal and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Orders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Orders Property
     -  Data Type
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Product to  Products
----------------------------
Every HubSpot Product will be synchronized with a  Products.

Once a link between a HubSpot Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Products Property
     -  Data Type
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

