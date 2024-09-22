========================
Shopify to Wave Dataflow
========================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Wave Customer
---------------------------------
Every Shopify Customer will be synchronized with a Wave Customer.

Once a link between a Shopify Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - default_address.address1
     - address.addressLine1
     - "string"
   * - default_address.address1
     - shippingDetails.address.addressLine1
     - "string"
   * - default_address.address2
     - address.addressLine2
     - "string"
   * - default_address.address2
     - shippingDetails.address.addressLine2
     - "string"
   * - default_address.city
     - address.city
     - "string"
   * - default_address.city
     - shippingDetails.address.city
     - "string"
   * - default_address.country
     - address.country.code
     - "string"
   * - default_address.country
     - shippingDetails.address.country.code
     - "string"
   * - default_address.province_code
     - address.province.code
     - "string"
   * - default_address.province_code
     - shippingDetails.address.province.code
     - "string"
   * - default_address.zip
     - address.postalCode
     - "string"
   * - default_address.zip
     - shippingDetails.address.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone
     - mobile
     - "string"


Shopify Customer to Wave Customer (human data)
----------------------------------------------
Every Shopify Customer will be synchronized with a Wave Customer (human data).

Once a link between a Shopify Customer and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Wave Customer (human data) Property
     - Wave Data Type
   * - default_address.address1
     - address.addressLine1
     - "string"
   * - default_address.address1
     - shippingDetails.address.addressLine1
     - "string"
   * - default_address.address2
     - address.addressLine2
     - "string"
   * - default_address.address2
     - shippingDetails.address.addressLine2
     - "string"
   * - default_address.city
     - address.city
     - "string"
   * - default_address.city
     - shippingDetails.address.city
     - "string"
   * - default_address.country
     - address.country.code
     - "string"
   * - default_address.country
     - shippingDetails.address.country.code
     - "string"
   * - default_address.phone
     - phone
     - "string"
   * - default_address.province_code
     - address.province.code
     - "string"
   * - default_address.province_code
     - shippingDetails.address.province.code
     - "string"
   * - default_address.zip
     - address.postalCode
     - "string"
   * - default_address.zip
     - shippingDetails.address.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - N/A
   * - phone
     - mobile
     - "string"


Shopify Order to Wave Invoice
-----------------------------
Every Shopify Order will be synchronized with a Wave Invoice.

Once a link between a Shopify Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Wave Invoice Property
     - Wave Data Type


Shopify Sesamproduct to Wave Product
------------------------------------
Every Shopify Sesamproduct will be synchronized with a Wave Product.

Once a link between a Shopify Sesamproduct and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Wave Product Property
     - Wave Data Type
   * - sesam_priceExclVAT
     - unitPrice
     - "string"
   * - title
     - name
     - "string"
   * - variants.title
     - description
     - "string"

