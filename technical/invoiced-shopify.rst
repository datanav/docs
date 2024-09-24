============================
Invoiced to Shopify Dataflow
============================

Generated: 2024-09-24 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers (human data) to Shopify Customer
---------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Shopify Customer.

Once a link between a Invoiced Customers (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Shopify Customer Property
     - Shopify Data Type


Invoiced Customers (human data) to Shopify Customer
---------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Shopify Customer.

Once a link between a Invoiced Customers (human data) and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Shopify Customer Property
     - Shopify Data Type


Invoiced Invoices to Shopify Order
----------------------------------
Every Invoiced Invoices will be synchronized with a Shopify Order.

Once a link between a Invoiced Invoices and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Shopify Order Property
     - Shopify Data Type


Invoiced Items to Shopify Sesamproduct
--------------------------------------
Every Invoiced Items will be synchronized with a Shopify Sesamproduct.

Once a link between a Invoiced Items and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - description
     - variants.title
     - "string"
   * - name
     - title
     - "string"

