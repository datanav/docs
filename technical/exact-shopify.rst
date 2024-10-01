================================
Exact Online to Shopify Dataflow
================================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to Shopify Customer
-----------------------------------------
Every Exact Online Accounts will be synchronized with a Shopify Customer.

Once a link between a Exact Online Accounts and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - Shopify Customer Property
     - Shopify Data Type


Exact Online Items to Shopify Sesamproduct
------------------------------------------
Every Exact Online Items will be synchronized with a Shopify Sesamproduct.

Once a link between a Exact Online Items and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - Shopify Sesamproduct Property
     - Shopify Data Type


Exact Online Salesorders to Shopify Order
-----------------------------------------
Every Exact Online Salesorders will be synchronized with a Shopify Order.

Once a link between a Exact Online Salesorders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - Shopify Order Property
     - Shopify Data Type
   * - Currency
     - currency
     - "string"

