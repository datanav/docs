===============================
Shopify to Businessnxt Dataflow
===============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Businessnxt Product
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Businessnxt Product.

Once a link between a Shopify Inventoryitem and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Businessnxt Product Property
     - Businessnxt Data Type


Shopify Product to Businessnxt Product
--------------------------------------
Every Shopify Product will be synchronized with a Businessnxt Product.

Once a link between a Shopify Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type


Shopify Customer to Businessnxt Country
---------------------------------------
Every Shopify Customer will be synchronized with a Businessnxt Country.

Once a link between a Shopify Customer and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to Businessnxt Currency
----------------------------------------
Every Shopify Customer will be synchronized with a Businessnxt Currency.

Once a link between a Shopify Customer and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to Businessnxt Country
------------------------------------
Every Shopify Order will be synchronized with a Businessnxt Country.

Once a link between a Shopify Order and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Businessnxt Country Property
     - Businessnxt Data Type
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


Shopify Order to Businessnxt Order
----------------------------------
Every Shopify Order will be synchronized with a Businessnxt Order.

Once a link between a Shopify Order and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - created_at
     - orderDate
     - "string"
   * - name
     - name
     - "string"


Shopify Order to Businessnxt Orderline
--------------------------------------
Every Shopify Order will be synchronized with a Businessnxt Orderline.

Once a link between a Shopify Order and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - id
     - orderNo
     - "string"


Shopify Sesamproduct to Businessnxt Product
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Businessnxt Product.

Once a link between a Shopify Sesamproduct and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - sesam_priceExclVAT
     - priceQuantity
     - "string"
   * - variants.inventory_quantity
     - quantityPerUnit
     - "string"
   * - variants.price
     - priceQuantity
     - "string"
   * - variants.title
     - description
     - "string"

