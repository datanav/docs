=============================
Shopify to Tripletex Dataflow
=============================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Tripletex Customer person
---------------------------------------------
Every Shopify Customer will be synchronized with a Tripletex Customer person.

Once a link between a Shopify Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - addresses.address1
     - deliveryAddress.addressLine1
     - "string"
   * - addresses.address1
     - physicalAddress.addressLine1
     - "string"
   * - addresses.address1
     - postalAddress.addressLine1
     - "string"
   * - addresses.address2
     - deliveryAddress.addressLine2
     - "string"
   * - addresses.address2
     - physicalAddress.addressLine2
     - "string"
   * - addresses.address2
     - postalAddress.addressLine2
     - "string"
   * - addresses.city
     - deliveryAddress.city
     - "string"
   * - addresses.city
     - physicalAddress.city
     - "string"
   * - addresses.city
     - postalAddress.city
     - "string"
   * - addresses.country
     - deliveryAddress.country.id
     - "string"
   * - addresses.country
     - physicalAddress.country.id
     - "integer"
   * - addresses.country
     - postalAddress.country.id
     - "integer"
   * - addresses.zip
     - deliveryAddress.postalCode
     - "string"
   * - addresses.zip
     - physicalAddress.postalCode
     - "string"
   * - addresses.zip
     - postalAddress.postalCode
     - "string"
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
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - phone
     - phoneNumber
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


Shopify Product to Tripletex Product
------------------------------------
Every Shopify Product will be synchronized with a Tripletex Product.

Once a link between a Shopify Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - variants.price
     - priceExcludingVatCurrency
     - "float"
   * - variants.title
     - name
     - "string"

