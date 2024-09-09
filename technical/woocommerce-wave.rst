============================
Woocommerce to Wave Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to Wave Customer person
--------------------------------------------
Every Woocommerce Customer will be synchronized with a Wave Customer person.

Once a link between a Woocommerce Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Wave Customer person Property
     - Wave Data Type
   * - billing.address_1
     - address.addressLine1
     - "string"
   * - billing.address_1
     - shippingDetails.address.addressLine1
     - "string"
   * - billing.address_2
     - address.addressLine2
     - "string"
   * - billing.address_2
     - shippingDetails.address.addressLine2
     - "string"
   * - billing.city
     - address.city
     - "string"
   * - billing.city
     - shippingDetails.address.city
     - "string"
   * - billing.country
     - address.country.code
     - "string"
   * - billing.country
     - shippingDetails.address.country.code
     - "string"
   * - billing.postcode
     - address.postalCode
     - "string"
   * - billing.postcode
     - shippingDetails.address.postalCode
     - "string"
   * - billing.state
     - address.province.code
     - "string"
   * - billing.state
     - shippingDetails.address.province.code
     - "string"
   * - email
     - email
     - "string"
   * - last_name
     - lastName
     - N/A
   * - shipping.address_1
     - address.addressLine1
     - "string"
   * - shipping.address_1
     - shippingDetails.address.addressLine1
     - "string"
   * - shipping.address_2
     - address.addressLine2
     - "string"
   * - shipping.address_2
     - shippingDetails.address.addressLine2
     - "string"
   * - shipping.city
     - address.city
     - "string"
   * - shipping.city
     - shippingDetails.address.city
     - "string"
   * - shipping.country
     - address.country.code
     - "string"
   * - shipping.country
     - shippingDetails.address.country.code
     - "string"
   * - shipping.postcode
     - address.postalCode
     - "string"
   * - shipping.postcode
     - shippingDetails.address.postalCode
     - "string"
   * - shipping.state
     - address.province.code
     - "string"
   * - shipping.state
     - shippingDetails.address.province.code
     - "string"


Woocommerce Order to Wave Invoice
---------------------------------
Every Woocommerce Order will be synchronized with a Wave Invoice.

Once a link between a Woocommerce Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - currency
     - currency.code
     - "string"
   * - customer_id
     - customer.id
     - "string"
   * - line_items.price
     - items.price
     - "string"
   * - line_items.quantity
     - items.quantity
     - N/A


Woocommerce Product to Wave Product
-----------------------------------
Every Woocommerce Product will be synchronized with a Wave Product.

Once a link between a Woocommerce Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Wave Product Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - sale_price
     - unitPrice
     - "string"

