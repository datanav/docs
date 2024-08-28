====================
Shopify to  Dataflow
====================

Generated: 2024-08-28 12:18:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to  Customer
-----------------------------
Every Shopify Customer will be synchronized with a  Customer.

Once a link between a Shopify Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     -  Customer Property
     -  Data Type
   * - default_address.country_name
     - billing_address.country
     - "string"
   * - email
     - email
     - "string"
   * - first_name
     - first_name
     - "string"
   * - last_name
     - last_name
     - "string"


Shopify Order to  Order
-----------------------
Every Shopify Order will be synchronized with a  Order.

Once a link between a Shopify Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Order Property
     -  Data Type

