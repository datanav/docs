==================================
Wave Financial to Shopify Dataflow
==================================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Product to Shopify Inventoryitem
-------------------------------------
Every Wave Product will be synchronized with a Shopify Inventoryitem.

Once a link between a Wave Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type


Wave Customer person to Shopify Customer
----------------------------------------
Every Wave Customer person will be synchronized with a Shopify Customer.

Once a link between a Wave Customer person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - address.addressLine1
     - addresses.address1
     - "string"
   * - address.addressLine2
     - addresses.address2
     - "string"
   * - address.city
     - addresses.city
     - "string"
   * - address.country.code
     - addresses.country
     - "string"
   * - address.postalCode
     - addresses.zip
     - "string"
   * - address.province.code
     - addresses.province_code
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phone
     - phone
     - "string"
   * - shippingDetails.address.addressLine1
     - addresses.address1
     - "string"
   * - shippingDetails.address.addressLine2
     - addresses.address2
     - "string"
   * - shippingDetails.address.city
     - addresses.city
     - "string"
   * - shippingDetails.address.country.code
     - addresses.country
     - "string"
   * - shippingDetails.address.postalCode
     - addresses.zip
     - "string"
   * - shippingDetails.address.province.code
     - addresses.province_code
     - "string"
   * - shippingDetails.phone
     - phone
     - "string"


Wave Invoice to Shopify Order
-----------------------------
Every Wave Invoice will be synchronized with a Shopify Order.

Once a link between a Wave Invoice and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Shopify Order Property
     - Shopify Data Type
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - customer.id
     - "string"
   * - items.price
     - line_items.price
     - "string"
   * - items.quantity
     - line_items.quantity
     - "string"
   * - poNumber
     - po_number
     - "string"
   * - title
     - name
     - "string"
   * - total.value
     - current_total_price
     - "string"
   * - total.value
     - total_price
     - "string"


Wave Product to Shopify Product
-------------------------------
Every Wave Product will be synchronized with a Shopify Product.

Once a link between a Wave Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - name
     - variants.title
     - "string"
   * - unitPrice
     - variants.price
     - "string"

