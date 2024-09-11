====================================
WooCommerce to Exact Online Dataflow
====================================

Generated: 2024-09-11 07:46:45

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Exact Quotations
-------------------------------------
Every WooCommerce Order will be synchronized with a Exact Quotations.

Once a link between a WooCommerce Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"


WooCommerce Order to Exact Currencies
-------------------------------------
Every WooCommerce Order will be synchronized with a Exact Currencies.

Once a link between a WooCommerce Order and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Currencies Property
     - Exact Data Type


WooCommerce Order to Exact Salesorderlines
------------------------------------------
Every WooCommerce Order will be synchronized with a Exact Salesorderlines.

Once a link between a WooCommerce Order and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - line_items.sku
     - CostPriceFC
     - "string"


WooCommerce Order to Exact Salesorders
--------------------------------------
Every WooCommerce Order will be synchronized with a Exact Salesorders.

Once a link between a WooCommerce Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - discount_total
     - Discount
     - "string"


WooCommerce Product to Exact Items
----------------------------------
Every WooCommerce Product will be synchronized with a Exact Items.

Once a link between a WooCommerce Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Exact Items Property
     - Exact Data Type

