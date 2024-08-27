====================
Shopify to  Dataflow
====================

Generated: 2024-08-27 10:30:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to  Product
---------------------------------
Every Shopify Inventoryitem will be synchronized with a  Product.

Once a link between a Shopify Inventoryitem and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Product Property
     -  Data Type


Shopify Product to  Product
---------------------------
Every Shopify Product will be synchronized with a  Product.

Once a link between a Shopify Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Product Property
     -  Data Type


Shopify Customer to  Country
----------------------------
Every Shopify Customer will be synchronized with a  Country.

Once a link between a Shopify Customer and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Country Property
     -  Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to  Currency
-----------------------------
Every Shopify Customer will be synchronized with a  Currency.

Once a link between a Shopify Customer and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Currency Property
     -  Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to  Country
-------------------------
Every Shopify Order will be synchronized with a  Country.

Once a link between a Shopify Order and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Country Property
     -  Data Type
   * - billing_address.country
     - name
     - "string"
   * - billing_address.country_code
     - isoCode
     - "string"
   * - shipping_address.country
     - name
     - "string"
   * - shipping_address.country_code
     - isoCode
     - "string"


Shopify Order to  Order
-----------------------
Every Shopify Order will be synchronized with a  Order.

Once a link between a Shopify Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Order Property
     -  Data Type


Shopify Sesamproduct to  Product
--------------------------------
Every Shopify Sesamproduct will be synchronized with a  Product.

Once a link between a Shopify Sesamproduct and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Product Property
     -  Data Type
   * - variants.inventory_quantity
     - quantityPerUnit
     - "string"
   * - variants.price
     - priceQuantity
     - "string"
   * - variants.title
     - description
     - "string"

