========================
Wave to Shopify Dataflow
========================

Generated: 2024-09-21 00:00:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer (human data) to Shopify Customer
----------------------------------------------
Every Wave Customer (human data) will be synchronized with a Shopify Customer.

Once a link between a Wave Customer (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - Shopify Customer Property
     - Shopify Data Type
   * - address.addressLine1
     - default_address.address1
     - "string"
   * - address.addressLine2
     - default_address.address2
     - "string"
   * - address.city
     - default_address.city
     - "string"
   * - address.country.code
     - default_address.country
     - "string"
   * - address.postalCode
     - default_address.zip
     - "string"
   * - address.province.code
     - default_address.province_code
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - mobile
     - phone
     - "string"
   * - phone
     - default_address.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - default_address.address1
     - "string"
   * - shippingDetails.address.addressLine2
     - default_address.address2
     - "string"
   * - shippingDetails.address.city
     - default_address.city
     - "string"
   * - shippingDetails.address.country.code
     - default_address.country
     - "string"
   * - shippingDetails.address.postalCode
     - default_address.zip
     - "string"
   * - shippingDetails.address.province.code
     - default_address.province_code
     - "string"
   * - shippingDetails.phone
     - default_address.phone
     - "string"


Wave Customer to Shopify Customer
---------------------------------
Every Wave Customer will be synchronized with a Shopify Customer.

Once a link between a Wave Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Shopify Customer Property
     - Shopify Data Type
   * - address.addressLine1
     - default_address.address1
     - "string"
   * - address.addressLine2
     - default_address.address2
     - "string"
   * - address.city
     - default_address.city
     - "string"
   * - address.country.code
     - default_address.country
     - "string"
   * - address.postalCode
     - default_address.zip
     - "string"
   * - address.province.code
     - default_address.province_code
     - "string"
   * - shippingDetails.address.addressLine1
     - default_address.address1
     - "string"
   * - shippingDetails.address.addressLine2
     - default_address.address2
     - "string"
   * - shippingDetails.address.city
     - default_address.city
     - "string"
   * - shippingDetails.address.country.code
     - default_address.country
     - "string"
   * - shippingDetails.address.postalCode
     - default_address.zip
     - "string"
   * - shippingDetails.address.province.code
     - default_address.province_code
     - "string"


Wave Invoice to Shopify Order
-----------------------------
Every Wave Invoice will be synchronized with a Shopify Order.

Once a link between a Wave Invoice and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Shopify Order Property
     - Shopify Data Type


Wave Product to Shopify Sesamproduct
------------------------------------
Every Wave Product will be synchronized with a Shopify Sesamproduct.

Once a link between a Wave Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - description
     - variants.title
     - "string"
   * - name
     - title
     - "string"
   * - unitPrice
     - sesam_priceExclVAT
     - "string"

