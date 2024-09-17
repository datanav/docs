==================================
Salesforce to WooCommerce Dataflow
==================================

Generated: 2024-09-17 07:26:52

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Order to WooCommerce Order
-------------------------------------
Before any synchronization can take place, a link between a Salesforce Order and a WooCommerce Order must be established.

A new WooCommerce Order will be created from a Salesforce Order if it is connected to a Salesforce Order, Quote, or Orderitem that is synchronized into WooCommerce.

Once a link between a Salesforce Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type


Salesforce Product2 to WooCommerce Product
------------------------------------------
Before any synchronization can take place, a link between a Salesforce Product2 and a WooCommerce Product must be established.

A new WooCommerce Product will be created from a Salesforce Product2 if it is connected to a Salesforce Order, Quote, or Orderitem that is synchronized into WooCommerce.

Once a link between a Salesforce Product2 and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - WooCommerce Product Property
     - WooCommerce Data Type


Salesforce Order to WooCommerce Order
-------------------------------------
Every Salesforce Order will be synchronized with a WooCommerce Order.

Once a link between a Salesforce Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type


Salesforce Product2 to WooCommerce Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a WooCommerce Product.

Once a link between a Salesforce Product2 and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - WooCommerce Product Property
     - WooCommerce Data Type

