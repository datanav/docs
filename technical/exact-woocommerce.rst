===================================
ExactOnline to WooCommerce Dataflow
===================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnlineExact OnlineExact Items to WooCommerceWoocommerce Product
--------------------------------------------------------------------
Every ExactOnlineExact OnlineExact Items will be synchronized with a WooCommerceWoocommerce Product.

Once a link between a ExactOnlineExact OnlineExact Items and a WooCommerceWoocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnlineExact OnlineExact Items and a WooCommerceWoocommerce Product:

.. list-table::
   :header-rows: 1

   * - ExactOnlineExact OnlineExact Items Property
     - WooCommerceWoocommerce Product Property
     - WooCommerceWoocommerce Data Type


ExactOnlineExact OnlineExact Salesorders to WooCommerceWoocommerce Order
------------------------------------------------------------------------
Every ExactOnlineExact OnlineExact Salesorders will be synchronized with a WooCommerceWoocommerce Order.

Once a link between a ExactOnlineExact OnlineExact Salesorders and a WooCommerceWoocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnlineExact OnlineExact Salesorders and a WooCommerceWoocommerce Order:

.. list-table::
   :header-rows: 1

   * - ExactOnlineExact OnlineExact Salesorders Property
     - WooCommerceWoocommerce Order Property
     - WooCommerceWoocommerce Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discount_total
     - "string"

