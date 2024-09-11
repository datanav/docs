===================================
WooCommerce to ExactOnline Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to ExactOnline Quotations
-------------------------------------------
Every WooCommerce Order will be synchronized with a ExactOnline Quotations.

Once a link between a WooCommerce Order and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - currency
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"


WooCommerce Order to ExactOnline Currencies
-------------------------------------------
Every WooCommerce Order will be synchronized with a ExactOnline Currencies.

Once a link between a WooCommerce Order and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type


WooCommerce Order to ExactOnline Salesorderlines
------------------------------------------------
Every WooCommerce Order will be synchronized with a ExactOnline Salesorderlines.

Once a link between a WooCommerce Order and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - line_items.sku
     - CostPriceFC
     - "string"


WooCommerce Order to ExactOnline Salesorders
--------------------------------------------
Every WooCommerce Order will be synchronized with a ExactOnline Salesorders.

Once a link between a WooCommerce Order and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - currency
     - Currency
     - "string"
   * - discount_total
     - Discount
     - "string"


WooCommerce Product to ExactOnline Items
----------------------------------------
Every WooCommerce Product will be synchronized with a ExactOnline Items.

Once a link between a WooCommerce Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type

