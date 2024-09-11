======================================
Shopify to Visma Business Nxt Dataflow
======================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Shopify Customer to Visma Country
---------------------------------
Every Shopify Customer will be synchronized with a Visma Country.

Once a link between a Shopify Customer and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Visma Country Property
     - Visma Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Customer to Visma Currency
----------------------------------
Every Shopify Customer will be synchronized with a Visma Currency.

Once a link between a Shopify Customer and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Visma Currency Property
     - Visma Data Type
   * - currency
     - isoCode
     - "string"
   * - default_address.country_code
     - isoCode
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to Visma Country
------------------------------
Every Shopify Order will be synchronized with a Visma Country.

Once a link between a Shopify Order and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Visma Country Property
     - Visma Data Type
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


Shopify Order to Visma Order
----------------------------
Every Shopify Order will be synchronized with a Visma Order.

Once a link between a Shopify Order and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Visma Order Property
     - Visma Data Type
   * - created_at
     - orderDate
     - "string"
   * - name
     - name
     - "string"


Shopify Order to Visma Orderline
--------------------------------
Every Shopify Order will be synchronized with a Visma Orderline.

Once a link between a Shopify Order and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Visma Orderline Property
     - Visma Data Type
   * - id
     - orderNo
     - "string"


Shopify Sesamproduct to Visma Product
-------------------------------------
Every Shopify Sesamproduct will be synchronized with a Visma Product.

Once a link between a Shopify Sesamproduct and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Visma Product Property
     - Visma Data Type
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

