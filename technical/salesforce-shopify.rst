==============================
Salesforce to Shopify Dataflow
==============================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to Shopify Order
---------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a Shopify Order must be established.

A new Shopify Order will be created from a Salesforce Order if it is connected to a Salesforce Order, Quote, or Orderitem that is synchronized into Shopify.

Once a link between a Salesforce Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Shopify Order Property
     - Shopify Data Type


Salesforce Product2 to Shopify Product
--------------------------------------
Before any synchronization can take place, a link between a Salesforce Product2 and a Shopify Product must be established.

A new Shopify Product will be created from a Salesforce Product2 if it is connected to a Salesforce Order, Quote, or Orderitem that is synchronized into Shopify.

Once a link between a Salesforce Product2 and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Shopify Product Property
     - Shopify Data Type


Salesforce Customer to Shopify Customer
---------------------------------------
Every Salesforce Customer will be synchronized with a Shopify Customer.

Once a link between a Salesforce Customer and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Shopify Customer Property
     - Shopify Data Type


Salesforce Order to Shopify Order
---------------------------------
Every Salesforce Order will be synchronized with a Shopify Order.

Once a link between a Salesforce Order and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Shopify Order Property
     - Shopify Data Type


Salesforce Product2 to Shopify Sesamproduct
-------------------------------------------
Every Salesforce Product2 will be synchronized with a Shopify Sesamproduct.

Once a link between a Salesforce Product2 and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

