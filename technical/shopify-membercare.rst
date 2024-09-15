==============================
Shopify to MemberCare Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to MemberCare Persons
--------------------------------------
Every Shopify Customer will be synchronized with a MemberCare Persons.

Once a link between a Shopify Customer and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - first_name
     - firstname
     - "string"
   * - last_name
     - lastname
     - "string"


Shopify Inventoryitem to MemberCare Products
--------------------------------------------
Every Shopify Inventoryitem will be synchronized with a MemberCare Products.

Once a link between a Shopify Inventoryitem and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - MemberCare Products Property
     - MemberCare Data Type


Shopify Order to MemberCare Invoices
------------------------------------
Every Shopify Order will be synchronized with a MemberCare Invoices.

Once a link between a Shopify Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - line_items.price
     - invoiceItems.unitPrice
     - "string"
   * - line_items.quantity
     - invoiceItems.quantity
     - "string"


Shopify Product to MemberCare Products
--------------------------------------
Every Shopify Product will be synchronized with a MemberCare Products.

Once a link between a Shopify Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - MemberCare Products Property
     - MemberCare Data Type


Shopify Sesamproduct to MemberCare Products
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a MemberCare Products.

Once a link between a Shopify Sesamproduct and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - title
     - name
     - "string"


Shopify Customer to MemberCare Countries
----------------------------------------
Every Shopify Customer will be synchronized with a MemberCare Countries.

Once a link between a Shopify Customer and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - currency
     - iso2Letter
     - "string"
   * - default_address.country_code
     - iso2Letter
     - "string"
   * - default_address.country_name
     - name
     - "string"


Shopify Order to MemberCare Countries
-------------------------------------
Every Shopify Order will be synchronized with a MemberCare Countries.

Once a link between a Shopify Order and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - MemberCare Countries Property
     - MemberCare Data Type
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

