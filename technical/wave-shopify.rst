===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-05-16 10:07:49

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Product to  Inventoryitem
------------------------------
Every Wave Product will be synchronized with a  Inventoryitem.

Once a link between a Wave Product and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Inventoryitem Property
     -  Data Type


Wave Customer person to  Customer
---------------------------------
Every Wave Customer person will be synchronized with a  Customer.

Once a link between a Wave Customer person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Customer Property
     -  Data Type
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


Wave Invoice to  Order
----------------------
Every Wave Invoice will be synchronized with a  Order.

Once a link between a Wave Invoice and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Order Property
     -  Data Type
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


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
   * - name
     - variants.title
     - "string"
   * - unitPrice
     - variants.price
     - "string"

