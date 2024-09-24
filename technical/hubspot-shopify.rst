===========================
HubSpot to Shopify Dataflow
===========================

Generated: 2024-09-24 00:00:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to Shopify Order
-----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Shopify Order.

Once a link between a HubSpot Deal and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Shopify Order Property
     - Shopify Data Type


HubSpot Product to Shopify Sesamproduct
---------------------------------------
Every HubSpot Product will be synchronized with a Shopify Sesamproduct.

Once a link between a HubSpot Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - properties.description
     - variants.title
     - "string"
   * - properties.hs_sku
     - variants.sku
     - "string"
   * - properties.name
     - title
     - "string"
   * - properties.price
     - sesam_priceExclVAT
     - "string"

