==============================
Shopify to Membercare Dataflow
==============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Membercare Persons
--------------------------------------
Every Shopify Customer will be synchronized with a Membercare Persons.

Once a link between a Shopify Customer and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Membercare Persons Property
     - Membercare Data Type
   * - first_name
     - firstname
     - "string"
   * - last_name
     - lastname
     - "string"


Shopify Inventoryitem to Membercare Products
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a Membercare Products.

Once a link between a Shopify Inventoryitem and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Membercare Products Property
     - Membercare Data Type


Shopify Order to Membercare Invoices
------------------------------------
Every Shopify Order will be synchronized with a Membercare Invoices.

Once a link between a Shopify Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - line_items.price
     - invoiceItems.unitPrice
     - "string"
   * - line_items.quantity
     - invoiceItems.quantity
     - "string"


Shopify Product to Membercare Products
--------------------------------------
Every Shopify Product will be synchronized with a Membercare Products.

Once a link between a Shopify Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Membercare Products Property
     - Membercare Data Type


Shopify Sesamproduct to Membercare Products
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a Membercare Products.

Once a link between a Shopify Sesamproduct and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Membercare Products Property
     - Membercare Data Type
   * - title
     - name
     - "string"


Shopify Customer to Membercare Countries
----------------------------------------
Every Shopify Customer will be synchronized with a Membercare Countries.

Once a link between a Shopify Customer and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Membercare Countries Property
     - Membercare Data Type
   * - currency
     - iso2Letter
     - "string"
   * - default_address.country_code
     - iso2Letter
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to Membercare Countries
-------------------------------------
Every Shopify Order will be synchronized with a Membercare Countries.

Once a link between a Shopify Order and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billing_address.country
     - name
     - "string"
   * - billing_address.country_code
     - iso2Letter
     - "string"
   * - shipping_address.country
     - name
     - "string"
   * - shipping_address.country_code
     - iso2Letter
     - "string"

