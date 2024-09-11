====================================
WooCommerce to Exact Online Dataflow
====================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Exact Online Quotations
--------------------------------------------
Every WooCommerce Order will be synchronized with a Exact Online Quotations.

Once a link between a WooCommerce Order and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"


WooCommerce Order to Exact Online Currencies
--------------------------------------------
Every WooCommerce Order will be synchronized with a Exact Online Currencies.

Once a link between a WooCommerce Order and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Online Currencies Property
     - Exact Online Data Type


WooCommerce Order to Exact Online Salesorderlines
-------------------------------------------------
Every WooCommerce Order will be synchronized with a Exact Online Salesorderlines.

Once a link between a WooCommerce Order and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - line_items.sku
     - CostPriceFC
     - "string"


WooCommerce Order to Exact Online Salesorders
---------------------------------------------
Every WooCommerce Order will be synchronized with a Exact Online Salesorders.

Once a link between a WooCommerce Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currency
     - Currency
     - "string"
   * - discount_total
     - Discount
     - "string"


WooCommerce Product to Exact Online Items
-----------------------------------------
Every WooCommerce Product will be synchronized with a Exact Online Items.

Once a link between a WooCommerce Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Exact Online Items Property
     - Exact Online Data Type

