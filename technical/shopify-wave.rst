========================
Shopify to Wave Dataflow
========================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Wave Customer person
----------------------------------------
Every Shopify Customer will be synchronized with a Wave Customer person.

Once a link between a Shopify Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Wave Customer person Property
     - Wave Data Type
   * - addresses.address1
     - address.addressLine1
     - "string"
   * - addresses.address1
     - shippingDetails.address.addressLine1
     - "string"
   * - addresses.address2
     - address.addressLine2
     - "string"
   * - addresses.address2
     - shippingDetails.address.addressLine2
     - "string"
   * - addresses.city
     - address.city
     - "string"
   * - addresses.city
     - shippingDetails.address.city
     - "string"
   * - addresses.country
     - address.country.code
     - "string"
   * - addresses.country
     - shippingDetails.address.country.code
     - "string"
   * - addresses.province_code
     - address.province.code
     - "string"
   * - addresses.province_code
     - shippingDetails.address.province.code
     - "string"
   * - addresses.zip
     - address.postalCode
     - "string"
   * - addresses.zip
     - shippingDetails.address.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - phone
     - phone
     - "string"


Shopify Order to Wave Invoice
-----------------------------
Every Shopify Order will be synchronized with a Wave Invoice.

Once a link between a Shopify Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - currency
     - currency.code
     - "string"
   * - customer.id
     - customer.id
     - "string"
   * - line_items.price
     - items.price
     - "string"
   * - line_items.quantity
     - items.quantity
     - N/A
   * - name
     - title
     - "string"
   * - po_number
     - poNumber
     - "string"


Shopify Product to Wave Product
-------------------------------
Every Shopify Product will be synchronized with a Wave Product.

Once a link between a Shopify Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Wave Product Property
     - Wave Data Type
   * - variants.price
     - unitPrice
     - "string"
   * - variants.title
     - name
     - "string"

