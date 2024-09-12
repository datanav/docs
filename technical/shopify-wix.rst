=======================
Shopify to Wix Dataflow
=======================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a Shopify Customer and a Wix Contacts must be established.

A new Wix Contacts will be created from a Shopify Customer if it is connected to a Shopify Order that is synchronized into Wix.

Once a link between a Shopify Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Wix Contacts Property
     - Wix Data Type
   * - default_address.phone
     - primaryInfo.phone
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - first_name
     - info.name.first
     - "string"
   * - last_name
     - info.name.last
     - "string"


Shopify Product to Wix Products
-------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Wix Products must be established.

A new Wix Products will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into Wix.

Once a link between a Shopify Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Wix Products Property
     - Wix Data Type


Shopify Sesamproduct to Wix Products
------------------------------------
Every Shopify Sesamproduct will be synchronized with a Wix Products.

Once a link between a Shopify Sesamproduct and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Wix Products Property
     - Wix Data Type
   * - sesam_priceExclVAT
     - priceData.price
     - N/A
   * - title
     - name
     - "string"
   * - variants..sku
     - sku
     - "string"
   * - variants.price
     - priceData.price
     - N/A
   * - variants.sku
     - sku
     - "string"

