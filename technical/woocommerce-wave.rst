============================
WooCommerce to Wave Dataflow
============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Wave Country
------------------------------------
Before any synchronization can take place, a link between a WooCommerce Customer and a Wave Country must be established.

A WooCommerce Customer will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wave Country Property
   * - billing.country
     - code
   * - shipping.country
     - code

Once a link between a WooCommerce Customer and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Wave Country:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wave Country Property
     - Wave Data Type


WooCommerce Order to Wave Country
---------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Wave Country must be established.

A WooCommerce Order will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Country Property
   * - billing.country
     - code
   * - shipping.country
     - code

Once a link between a WooCommerce Order and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wave Country:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Country Property
     - Wave Data Type


WooCommerce Customer to Wave Customer person
--------------------------------------------
Every WooCommerce Customer will be synchronized with a Wave Customer person.

Once a link between a WooCommerce Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
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


WooCommerce Order to Wave Currency
----------------------------------
Every WooCommerce Order will be synchronized with a Wave Currency.

If a matching Wave Currency already exists, the WooCommerce Order will be merged with the existing one.
If no matching Wave Currency is found, a new Wave Currency will be created.

A WooCommerce Order will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Currency Property
   * - currency
     - code

Once a link between a WooCommerce Order and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Currency Property
     - Wave Data Type


WooCommerce Order to Wave Invoice
---------------------------------
Every WooCommerce Order will be synchronized with a Wave Invoice.

Once a link between a WooCommerce Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
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


WooCommerce Product to Wave Product
-----------------------------------
Every WooCommerce Product will be synchronized with a Wave Product.

Once a link between a WooCommerce Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Wave Product Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - sale_price
     - unitPrice
     - "string"

