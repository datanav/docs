========================
Keap to Shopify Dataflow
========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Shopify Inventoryitem
-------------------------------------
Before any synchronization can take place, a link between a Keap Product and a Shopify Inventoryitem must be established.

A Keap Product will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Shopify Inventoryitem Property
   * - sku
     - sku

Once a link between a Keap Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type


Keap Product to Shopify Sesamproduct
------------------------------------
Every Keap Product will be synchronized with a Shopify Sesamproduct.

If a matching Shopify Sesamproduct already exists, the Keap Product will be merged with the existing one.
If no matching Shopify Sesamproduct is found, a new Shopify Sesamproduct will be created.

A Keap Product will merge with a Shopify Sesamproduct if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Shopify Sesamproduct Property
   * - sku
     - variants.sku

Once a link between a Keap Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - product_desc
     - variants.title
     - "string"
   * - product_name
     - title
     - "string"
   * - product_price
     - sesam_priceExclVAT
     - "string"

