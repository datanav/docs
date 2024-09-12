=================================
Tripletex to WooCommerce Dataflow
=================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to WooCommerce Order
------------------------------------
Every Tripletex Order will be synchronized with a WooCommerce Order.

Once a link between a Tripletex Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Product to WooCommerce Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a WooCommerce Product.

Once a link between a Tripletex Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - costExcludingVatCurrency
     - price
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - sale_price
     - "string"

