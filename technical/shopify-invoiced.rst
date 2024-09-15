============================
Shopify to Invoiced Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Invoiced Customers person
---------------------------------------------
Every Shopify Customer will be synchronized with a Invoiced Customers person.

Once a link between a Shopify Customer and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Invoiced Customers person Property
     - Invoiced Data Type


Shopify Order to Invoiced Invoices
----------------------------------
Every Shopify Order will be synchronized with a Invoiced Invoices.

Once a link between a Shopify Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currency
     - currency
     - "string"
   * - customer.id
     - customer
     - "string"


Shopify Order to Invoiced Lineitem
----------------------------------
Every Shopify Order will be synchronized with a Invoiced Lineitem.

Once a link between a Shopify Order and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - line_items.price
     - items.amount
     - "string"
   * - line_items.quantity
     - items.quantity
     - "string"
   * - line_items.title
     - items.name
     - "string"
   * - line_items.total_discount
     - items.discounts
     - "string"


Shopify Sesamproduct to Invoiced Items
--------------------------------------
Every Shopify Sesamproduct will be synchronized with a Invoiced Items.

Once a link between a Shopify Sesamproduct and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - title
     - name
     - "string"
   * - variants.title
     - description
     - "string"

