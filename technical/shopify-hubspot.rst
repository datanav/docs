===========================
Shopify to Hubspot Dataflow
===========================

Generated: 2024-06-28 00:00:01

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
   * - email
     - properties.email
     - "string"
   * - id
     - id
     - "string"
   * - phone
     - properties.phone
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
   * - variants.price
     - properties.price
     - "string"
   * - variants.title
     - properties.name
     - "string"

