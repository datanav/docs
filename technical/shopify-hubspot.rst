===========================
Shopify to Hubspot Dataflow
===========================

Generated: 2024-07-06 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Hubspot Contact
-----------------------------------
Every Shopify Customer will be synchronized with a Hubspot Contact.

Once a link between a Shopify Customer and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Hubspot Contact Property
     - Hubspot Data Type
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
     - properties.phone
     - "string"


Shopify Order to Hubspot Lineitem
---------------------------------
Every Shopify Order will be synchronized with a Hubspot Lineitem.

Once a link between a Shopify Order and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
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


Shopify Product to Hubspot Product
----------------------------------
Every Shopify Product will be synchronized with a Hubspot Product.

Once a link between a Shopify Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - title
     - properties.name
     - "string"
   * - variants.price
     - properties.price
     - "string"
   * - variants.title
     - properties.name
     - "string"

