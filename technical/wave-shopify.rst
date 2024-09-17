========================
Wave to Shopify Dataflow
========================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Shopify Customer
---------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Shopify Customer must be established.

A new Shopify Customer will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Shopify.

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
Before any synchronization can take place, a link between a Wave Invoice and a Shopify Order must be established.

A new Shopify Order will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into Shopify.

Once a link between a Wave Invoice and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Shopify Order Property
     - Shopify Data Type


Wave Product to Shopify Product
-------------------------------
Before any synchronization can take place, a link between a Wave Product and a Shopify Product must be established.

A new Shopify Product will be created from a Wave Product if it is connected to a Wave Invoice that is synchronized into Shopify.

Once a link between a Wave Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Shopify Product Property
     - Shopify Data Type


Wave Customer person to Shopify Customer
----------------------------------------
Every Wave Customer person will be synchronized with a Shopify Customer.

Once a link between a Wave Customer person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Shopify Customer Property
     - Shopify Data Type


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

