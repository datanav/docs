========================
Shopify to Keap Dataflow
========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Keap Product
-------------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a Keap Product must be established.

A Shopify Inventoryitem will merge with a Keap Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Keap Product Property
   * - sku
     - sku

Once a link between a Shopify Inventoryitem and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Keap Product Property
     - Keap Data Type


Shopify Customer to Keap Contacts
---------------------------------
Every Shopify Customer will be synchronized with a Keap Contacts.

Once a link between a Shopify Customer and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Keap Contacts Property
     - Keap Data Type


Shopify Sesamproduct to Keap Product
------------------------------------
Every Shopify Sesamproduct will be synchronized with a Keap Product.

If a matching Keap Product already exists, the Shopify Sesamproduct will be merged with the existing one.
If no matching Keap Product is found, a new Keap Product will be created.

A Shopify Sesamproduct will merge with a Keap Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Keap Product Property
   * - variants.sku
     - sku

Once a link between a Shopify Sesamproduct and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Keap Product Property
     - Keap Data Type
   * - sesam_priceExclVAT
     - product_price
     - "string"
   * - title
     - product_name
     - "string"
   * - variants.title
     - product_desc
     - "string"

