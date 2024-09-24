===============================
WooCommerce to HubSpot Dataflow
===============================

Generated: 2024-09-24 13:16:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to HubSpot Deal
---------------------------------
Every WooCommerce Order will be synchronized with a HubSpot Deal.

Once a link between a WooCommerce Order and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - currency
     - properties.deal_currency_code
     - "string"


WooCommerce Order to HubSpot Lineitem
-------------------------------------
Every WooCommerce Order will be synchronized with a HubSpot Lineitem.

Once a link between a WooCommerce Order and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - line_items.name
     - properties.name
     - "string"
   * - line_items.price
     - properties.price
     - "string"
   * - line_items.quantity
     - properties.quantity
     - N/A


WooCommerce Order to HubSpot Lineitemdealassociationtype
--------------------------------------------------------
Every WooCommerce Order will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a WooCommerce Order and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


WooCommerce Order to HubSpot Lineitemquoteassociationtype
---------------------------------------------------------
Every WooCommerce Order will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a WooCommerce Order and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


WooCommerce Product to HubSpot Product
--------------------------------------
Every WooCommerce Product will be synchronized with a HubSpot Product.

Once a link between a WooCommerce Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"
   * - price
     - properties.hs_cost_of_goods_sold
     - "string"
   * - sale_price
     - properties.price
     - "string"
   * - sku
     - properties.hs_sku
     - "string"

