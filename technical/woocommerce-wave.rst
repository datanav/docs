============================
WooCommerce to Wave Dataflow
============================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Wave Invoice
---------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a Wave Invoice must be established.

A new Wave Invoice will be created from a WooCommerce Order if it is connected to a WooCommerce Order that is synchronized into Wave.

Once a link between a WooCommerce Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Invoice Property
     - Wave Data Type


WooCommerce Product to Wave Product
-----------------------------------
Before any synchronization can take place, a link between a WooCommerce Product and a Wave Product must be established.

A new Wave Product will be created from a WooCommerce Product if it is connected to a WooCommerce Order that is synchronized into Wave.

Once a link between a WooCommerce Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Wave Product Property
     - Wave Data Type


WooCommerce Customer to Wave Customer
-------------------------------------
Every WooCommerce Customer will be synchronized with a Wave Customer.

Once a link between a WooCommerce Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wave Customer Property
     - Wave Data Type


WooCommerce Customer to Wave Customer person
--------------------------------------------
Every WooCommerce Customer will be synchronized with a Wave Customer person.

Once a link between a WooCommerce Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Wave Customer person Property
     - Wave Data Type


WooCommerce Order to Wave Invoice
---------------------------------
Every WooCommerce Order will be synchronized with a Wave Invoice.

Once a link between a WooCommerce Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Wave Invoice Property
     - Wave Data Type


WooCommerce Product to Wave Product
-----------------------------------
Every WooCommerce Product will be synchronized with a Wave Product.

Once a link between a WooCommerce Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Wave Product Property
     - Wave Data Type

