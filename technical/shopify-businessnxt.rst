===============================
Shopify to BusinessNxt Dataflow
===============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Visma Product
--------------------------------------
Every Shopify Inventoryitem will be synchronized with a Visma Product.

Once a link between a Shopify Inventoryitem and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Visma Product Property
     - Visma Data Type


Shopify Product to Visma Product
--------------------------------
Every Shopify Product will be synchronized with a Visma Product.

Once a link between a Shopify Product and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Visma Product Property
     - Visma Data Type


Shopify Customer to BusinessNxt Country
---------------------------------------
Every Shopify Customer will be synchronized with a BusinessNxt Country.

Once a link between a Shopify Customer and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to BusinessNxt Currency
----------------------------------------
Every Shopify Customer will be synchronized with a BusinessNxt Currency.

Once a link between a Shopify Customer and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to BusinessNxt Country
------------------------------------
Every Shopify Order will be synchronized with a BusinessNxt Country.

Once a link between a Shopify Order and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
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


Shopify Order to BusinessNxt Order
----------------------------------
Every Shopify Order will be synchronized with a BusinessNxt Order.

Once a link between a Shopify Order and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - created_at
     - orderDate
     - "string"
   * - name
     - name
     - "string"


Shopify Order to BusinessNxt Orderline
--------------------------------------
Every Shopify Order will be synchronized with a BusinessNxt Orderline.

Once a link between a Shopify Order and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - id
     - orderNo
     - "string"


Shopify Sesamproduct to BusinessNxt Product
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a BusinessNxt Product.

Once a link between a Shopify Sesamproduct and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
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

