=================================
Woocommerce to Tripletex Dataflow
=================================

Generated: 2024-09-11 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to Tripletex Customer person
-------------------------------------------------
Every Woocommerce Customer will be synchronized with a Tripletex Customer person.

Once a link between a Woocommerce Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - billing.address_1
     - deliveryAddress.addressLine1
     - "string"
   * - billing.address_1
     - physicalAddress.addressLine1
     - "string"
   * - billing.address_1
     - postalAddress.addressLine1
     - "string"
   * - billing.address_2
     - deliveryAddress.addressLine2
     - "string"
   * - billing.address_2
     - physicalAddress.addressLine2
     - "string"
   * - billing.address_2
     - postalAddress.addressLine2
     - "string"
   * - billing.city
     - deliveryAddress.city
     - "string"
   * - billing.city
     - physicalAddress.city
     - "string"
   * - billing.city
     - postalAddress.city
     - "string"
   * - billing.country
     - deliveryAddress.country.id
     - "string"
   * - billing.country
     - physicalAddress.country.id
     - "integer"
   * - billing.country
     - postalAddress.country.id
     - "integer"
   * - billing.postcode
     - deliveryAddress.postalCode
     - "string"
   * - billing.postcode
     - physicalAddress.postalCode
     - "string"
   * - billing.postcode
     - postalAddress.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - shipping.address_1
     - deliveryAddress.addressLine1
     - "string"
   * - shipping.address_1
     - physicalAddress.addressLine1
     - "string"
   * - shipping.address_1
     - postalAddress.addressLine1
     - "string"
   * - shipping.address_2
     - deliveryAddress.addressLine2
     - "string"
   * - shipping.address_2
     - physicalAddress.addressLine2
     - "string"
   * - shipping.address_2
     - postalAddress.addressLine2
     - "string"
   * - shipping.city
     - deliveryAddress.city
     - "string"
   * - shipping.city
     - physicalAddress.city
     - "string"
   * - shipping.city
     - postalAddress.city
     - "string"
   * - shipping.country
     - deliveryAddress.country.id
     - "string"
   * - shipping.country
     - physicalAddress.country.id
     - "integer"
   * - shipping.country
     - postalAddress.country.id
     - "integer"
   * - shipping.postcode
     - deliveryAddress.postalCode
     - "string"
   * - shipping.postcode
     - physicalAddress.postalCode
     - "string"
   * - shipping.postcode
     - postalAddress.postalCode
     - "string"


Woocommerce Order to Tripletex Order
------------------------------------
Every Woocommerce Order will be synchronized with a Tripletex Order.

Once a link between a Woocommerce Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - currency
     - currency.id
     - "integer"
   * - customer_id
     - contact.id
     - "integer"
   * - customer_id
     - customer.id
     - "integer"


Woocommerce Order to Tripletex Orderline
----------------------------------------
Every Woocommerce Order will be synchronized with a Tripletex Orderline.

Once a link between a Woocommerce Order and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
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


Woocommerce Product to Tripletex Product
----------------------------------------
Every Woocommerce Product will be synchronized with a Tripletex Product.

Once a link between a Woocommerce Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - name
     - name
     - "string"
   * - price
     - costExcludingVatCurrency
     - "float"
   * - sale_price
     - priceExcludingVatCurrency
     - "float"

