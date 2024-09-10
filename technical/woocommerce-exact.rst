=============================
Woocommerce to Exact Dataflow
=============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Exact Quotations
-------------------------------------
Every Woocommerce Order will be synchronized with a Exact Quotations.

Once a link between a Woocommerce Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - id
     - DeliveryAddress
     - "string"


Woocommerce Order to Exact Currencies
-------------------------------------
Every Woocommerce Order will be synchronized with a Exact Currencies.

Once a link between a Woocommerce Order and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Exact Currencies Property
     - Exact Data Type


Woocommerce Order to Exact Salesorderlines
------------------------------------------
Every Woocommerce Order will be synchronized with a Exact Salesorderlines.

Once a link between a Woocommerce Order and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - line_items.sku
     - CostPriceFC
     - "string"


Woocommerce Order to Exact Salesorders
--------------------------------------
Every Woocommerce Order will be synchronized with a Exact Salesorders.

Once a link between a Woocommerce Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency
     - Currency
     - "string"
   * - discount_total
     - Discount
     - "string"


Woocommerce Product to Exact Items
----------------------------------
Every Woocommerce Product will be synchronized with a Exact Items.

Once a link between a Woocommerce Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Exact Items Property
     - Exact Data Type

