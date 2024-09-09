=================================
Tripletex to Woocommerce Dataflow
=================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Order to Woocommerce Order
------------------------------------
Every Tripletex Order will be synchronized with a Woocommerce Order.

Once a link between a Tripletex Order and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Product to Woocommerce Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Woocommerce Product.

Once a link between a Tripletex Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - costExcludingVatCurrency
     - price
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - sale_price
     - "string"

