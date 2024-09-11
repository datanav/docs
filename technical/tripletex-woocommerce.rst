=================================
Tripletex to WooCommerce Dataflow
=================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to WooCommerceWoocommerce Order
-----------------------------------------------
Every Tripletex Order will be synchronized with a WooCommerceWoocommerce Order.

Once a link between a Tripletex Order and a WooCommerceWoocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a WooCommerceWoocommerce Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - WooCommerceWoocommerce Order Property
     - WooCommerceWoocommerce Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Product to WooCommerceWoocommerce Product
---------------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a WooCommerceWoocommerce Product.

Once a link between a Tripletex Product and a WooCommerceWoocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a WooCommerceWoocommerce Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - WooCommerceWoocommerce Product Property
     - WooCommerceWoocommerce Data Type
   * - costExcludingVatCurrency
     - price
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - sale_price
     - "string"

