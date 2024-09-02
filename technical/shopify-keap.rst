====================
Shopify to  Dataflow
====================

Generated: 2024-09-02 11:17:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to  Product
---------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a  Product must be established.

A Shopify Inventoryitem will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Product Property
   * - sku
     - sku

Once a link between a Shopify Inventoryitem and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Product Property
     -  Data Type


Shopify Inventoryitem to  Products
----------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a  Products must be established.

A Shopify Inventoryitem will merge with a  Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Products Property
   * - sku
     - sku

Once a link between a Shopify Inventoryitem and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Products Property
     -  Data Type


Shopify Sesamproduct to  Product
--------------------------------
Every Shopify Sesamproduct will be synchronized with a  Product.

If a matching  Product already exists, the Shopify Sesamproduct will be merged with the existing one.
If no matching  Product is found, a new  Product will be created.

A Shopify Sesamproduct will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Product Property
   * - variants.sku
     - sku

Once a link between a Shopify Sesamproduct and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Product Property
     -  Data Type
   * - sesam_priceExclVAT
     - product_price
     - "string"
   * - title
     - product_name
     - "string"
   * - variants.title
     - product_desc
     - "string"


Shopify Sesamproduct to  Products
---------------------------------
Every Shopify Sesamproduct will be synchronized with a  Products.

If a matching  Products already exists, the Shopify Sesamproduct will be merged with the existing one.
If no matching  Products is found, a new  Products will be created.

A Shopify Sesamproduct will merge with a  Products if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Products Property
   * - variants.sku
     - sku

Once a link between a Shopify Sesamproduct and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Products Property
     -  Data Type
   * - sesam_priceExclVAT
     - product_price
     - "string"
   * - title
     - product_name
     - "string"
   * - variants.sku
     - sku
     - "string"
   * - variants.title
     - product_desc
     - "string"

