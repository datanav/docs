=============================
Tripletex to Shopify Dataflow
=============================

Generated: 2024-07-03 06:56:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to Shopify Inventoryitem
------------------------------------------
Every Tripletex Product will be synchronized with a Shopify Inventoryitem.

Once a link between a Tripletex Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - costExcludingVatCurrency
     - cost
     - "string"


Tripletex Customer person to Shopify Customer
---------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Shopify Customer.

Once a link between a Tripletex Customer person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - deliveryAddress.addressLine1
     - addresses.address1
     - "string"
   * - deliveryAddress.addressLine1
     - default_address.address1
     - "string"
   * - deliveryAddress.addressLine2
     - addresses.address2
     - "string"
   * - deliveryAddress.addressLine2
     - default_address.address2
     - "string"
   * - deliveryAddress.city
     - addresses.city
     - "string"
   * - deliveryAddress.city
     - default_address.city
     - "string"
   * - deliveryAddress.country.id
     - addresses.country
     - "string"
   * - deliveryAddress.country.id
     - default_address.country
     - "string"
   * - deliveryAddress.postalCode
     - addresses.zip
     - "string"
   * - deliveryAddress.postalCode
     - default_address.zip
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - physicalAddress.addressLine1
     - addresses.address1
     - "string"
   * - physicalAddress.addressLine1
     - default_address.address1
     - "string"
   * - physicalAddress.addressLine2
     - addresses.address2
     - "string"
   * - physicalAddress.addressLine2
     - default_address.address2
     - "string"
   * - physicalAddress.city
     - addresses.city
     - "string"
   * - physicalAddress.city
     - default_address.city
     - "string"
   * - physicalAddress.country.id
     - addresses.country
     - "string"
   * - physicalAddress.country.id
     - default_address.country
     - "string"
   * - physicalAddress.postalCode
     - addresses.zip
     - "string"
   * - physicalAddress.postalCode
     - default_address.zip
     - "string"
   * - postalAddress.addressLine1
     - addresses.address1
     - "string"
   * - postalAddress.addressLine1
     - default_address.address1
     - "string"
   * - postalAddress.addressLine2
     - addresses.address2
     - "string"
   * - postalAddress.addressLine2
     - default_address.address2
     - "string"
   * - postalAddress.city
     - addresses.city
     - "string"
   * - postalAddress.city
     - default_address.city
     - "string"
   * - postalAddress.country.id
     - addresses.country
     - "string"
   * - postalAddress.country.id
     - default_address.country
     - "string"
   * - postalAddress.postalCode
     - addresses.zip
     - "string"
   * - postalAddress.postalCode
     - default_address.zip
     - "string"


Tripletex Order to Shopify Order
--------------------------------
Every Tripletex Order will be synchronized with a Shopify Order.

Once a link between a Tripletex Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Shopify Order Property
     - Shopify Data Type
   * - contact.id
     - customer.id
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer.id
     - "string"
   * - reference
     - po_number
     - "string"


Tripletex Orderline to Shopify Order
------------------------------------
Every Tripletex Orderline will be synchronized with a Shopify Order.

Once a link between a Tripletex Orderline and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Shopify Order Property
     - Shopify Data Type


Tripletex Product to Shopify Product
------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Shopify Product.

Once a link between a Tripletex Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - name
     - variants.title
     - "string"
   * - priceExcludingVatCurrency
     - variants.price
     - "string"

