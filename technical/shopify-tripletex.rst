=============================
Shopify to Tripletex Dataflow
=============================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Tripletex Contact
-------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Tripletex.

Once a link between a Shopify Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Shopify Customer to Tripletex Customer
--------------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Tripletex.

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
   * - title
     - name
     - "string"
   * - variants.price
     - priceExcludingVatCurrency
     - "float"
   * - variants.title
     - name
     - "string"

