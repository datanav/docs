================================
Shopify to Business Nxt Dataflow
================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Business Nxt Product
---------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Business Nxt Product.

Once a link between a Shopify Inventoryitem and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Business Nxt Product Property
     - Business Nxt Data Type


Shopify Product to Business Nxt Product
---------------------------------------
Every Shopify Product will be synchronized with a Business Nxt Product.

Once a link between a Shopify Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type


Shopify Customer to Business Nxt Country
----------------------------------------
Every Shopify Customer will be synchronized with a Business Nxt Country.

Once a link between a Shopify Customer and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to Business Nxt Currency
-----------------------------------------
Every Shopify Customer will be synchronized with a Business Nxt Currency.

Once a link between a Shopify Customer and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to Business Nxt Country
-------------------------------------
Every Shopify Order will be synchronized with a Business Nxt Country.

Once a link between a Shopify Order and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Nxt Country Property
     - Business Nxt Data Type
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


Shopify Order to Business Nxt Order
-----------------------------------
Every Shopify Order will be synchronized with a Business Nxt Order.

Once a link between a Shopify Order and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - created_at
     - orderDate
     - "string"
   * - name
     - name
     - "string"


Shopify Order to Business Nxt Orderline
---------------------------------------
Every Shopify Order will be synchronized with a Business Nxt Orderline.

Once a link between a Shopify Order and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - id
     - orderNo
     - "string"


Shopify Sesamproduct to Business Nxt Product
--------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Business Nxt Product.

Once a link between a Shopify Sesamproduct and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Business Nxt Product Property
     - Business Nxt Data Type
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

