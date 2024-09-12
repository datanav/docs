===========================
Shopify to HubSpot Dataflow
===========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Product to HubSpot Product
----------------------------------
Before any synchronization can take place, a link between a Shopify Product and a HubSpot Product must be established.

A new HubSpot Product will be created from a Shopify Product if it is connected to a Shopify Order that is synchronized into HubSpot.

Once a link between a Shopify Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - HubSpot Product Property
     - HubSpot Data Type


Shopify Customer to HubSpot Contact
-----------------------------------
Every Shopify Customer will be synchronized with a HubSpot Contact.

Once a link between a Shopify Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - addresses.address1
     - properties.address
     - "string"
   * - addresses.city
     - properties.city
     - "string"
   * - addresses.country
     - properties.country
     - "string"
   * - addresses.province_code
     - properties.state
     - "string"
   * - addresses.zip
     - properties.zip
     - "string"
   * - default_address.address1
     - properties.address
     - "string"
   * - default_address.city
     - properties.city
     - "string"
   * - default_address.country
     - properties.country
     - "string"
   * - default_address.phone
     - properties.phone
     - "string"
   * - default_address.province_code
     - properties.state
     - "string"
   * - default_address.zip
     - properties.zip
     - "string"
   * - email
     - properties.email
     - "string"
   * - first_name
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - properties.lastname
     - "string"
   * - phone
     - properties.mobilephone
     - "string"
   * - phone
     - properties.phone
     - "string"


Shopify Order to HubSpot Lineitem
---------------------------------
Every Shopify Order will be synchronized with a HubSpot Lineitem.

Once a link between a Shopify Order and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - line_items.price
     - properties.price
     - "string"
   * - line_items.quantity
     - properties.quantity
     - N/A
   * - line_items.title
     - properties.name
     - "string"
   * - line_items.total_discount
     - properties.hs_discount_percentage
     - "string"


Shopify Sesamproduct to HubSpot Product
---------------------------------------
Every Shopify Sesamproduct will be synchronized with a HubSpot Product.

Once a link between a Shopify Sesamproduct and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - sesam_priceExclVAT
     - properties.price
     - "string"
   * - title
     - properties.name
     - "string"
   * - variants..sku
     - properties.hs_sku
     - "string"
   * - variants.price
     - properties.price
     - "string"
   * - variants.sku
     - properties.hs_sku
     - "string"
   * - variants.title
     - properties.description
     - "string"

