====================
Shopify to  Dataflow
====================

Generated: 2024-08-28 08:12:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Customers person
-------------------------------------
Every Shopify Customer will be synchronized with a  Customers person.

Once a link between a Shopify Customer and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Customers person Property
     -  Data Type


Shopify Order to  Invoices
--------------------------
Every Shopify Order will be synchronized with a  Invoices.

Once a link between a Shopify Order and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Invoices Property
     -  Data Type
   * - currency
     - currency
     - "string"
   * - customer.id
     - customer
     - "string"

