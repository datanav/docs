=============================
Shopify to Tripletex Dataflow
=============================

Generated: 2024-09-24 13:16:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Tripletex Customer
--------------------------------------
Every Shopify Customer will be synchronized with a Tripletex Customer.

Once a link between a Shopify Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - default_address.address1
     - deliveryAddress.addressLine1
     - "string"
   * - default_address.address1
     - physicalAddress.addressLine1
     - "string"
   * - default_address.address1
     - postalAddress.addressLine1
     - "string"
   * - default_address.address2
     - deliveryAddress.addressLine2
     - "string"
   * - default_address.address2
     - physicalAddress.addressLine2
     - "string"
   * - default_address.address2
     - postalAddress.addressLine2
     - "string"
   * - default_address.city
     - deliveryAddress.city
     - "string"
   * - default_address.city
     - physicalAddress.city
     - "string"
   * - default_address.city
     - postalAddress.city
     - "string"
   * - default_address.country
     - deliveryAddress.country.id
     - "string"
   * - default_address.country
     - physicalAddress.country.id
     - "integer"
   * - default_address.country
     - postalAddress.country.id
     - "integer"
   * - default_address.zip
     - deliveryAddress.postalCode
     - "string"
   * - default_address.zip
     - physicalAddress.postalCode
     - "string"
   * - default_address.zip
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"


Shopify Customer to Tripletex Customer (human data)
---------------------------------------------------
Every Shopify Customer will be synchronized with a Tripletex Customer (human data).

Once a link between a Shopify Customer and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type
   * - default_address.address1
     - deliveryAddress.addressLine1
     - "string"
   * - default_address.address1
     - physicalAddress.addressLine1
     - "string"
   * - default_address.address1
     - postalAddress.addressLine1
     - "string"
   * - default_address.address2
     - deliveryAddress.addressLine2
     - "string"
   * - default_address.address2
     - physicalAddress.addressLine2
     - "string"
   * - default_address.address2
     - postalAddress.addressLine2
     - "string"
   * - default_address.city
     - deliveryAddress.city
     - "string"
   * - default_address.city
     - physicalAddress.city
     - "string"
   * - default_address.city
     - postalAddress.city
     - "string"
   * - default_address.country
     - deliveryAddress.country.id
     - "string"
   * - default_address.country
     - physicalAddress.country.id
     - "integer"
   * - default_address.country
     - postalAddress.country.id
     - "integer"
   * - default_address.phone
     - phoneNumber
     - "string"
   * - default_address.zip
     - deliveryAddress.postalCode
     - "string"
   * - default_address.zip
     - physicalAddress.postalCode
     - "string"
   * - default_address.zip
     - postalAddress.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - phone
     - phoneNumberMobile
     - "string"


Shopify Order to Tripletex Order
--------------------------------
Every Shopify Order will be synchronized with a Tripletex Order.

Once a link between a Shopify Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - created_at
     - orderDate
     - N/A
   * - currency
     - currency.id
     - "integer"
   * - customer.id
     - contact.id
     - "integer"
   * - customer.id
     - customer.id
     - "integer"
   * - po_number
     - reference
     - "string"


Shopify Order to Tripletex Orderline
------------------------------------
Every Shopify Order will be synchronized with a Tripletex Orderline.

Once a link between a Shopify Order and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - id
     - order.id
     - "integer"
   * - line_items.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - line_items.quantity
     - count
     - N/A
   * - line_items.total_discount
     - discount
     - "float"


Shopify Sesamproduct to Tripletex Product
-----------------------------------------
Every Shopify Sesamproduct will be synchronized with a Tripletex Product.

Once a link between a Shopify Sesamproduct and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - sesam_priceExclVAT
     - priceExcludingVatCurrency
     - "float"
   * - title
     - name
     - "string"
   * - variants.inventory_quantity
     - stockOfGoods
     - "integer"
   * - variants.title
     - description
     - "string"

