===============================
Woocommerce to Hubspot Dataflow
===============================

Generated: 2024-09-03 08:16:35

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Hubspot Lineitem
-------------------------------------
Every Woocommerce Order will be synchronized with a Hubspot Lineitem.

Once a link between a Woocommerce Order and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Hubspot Lineitem Property
     - Hubspot Data Type


Woocommerce Product to Hubspot Product
--------------------------------------
Every Woocommerce Product will be synchronized with a Hubspot Product.

Once a link between a Woocommerce Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Hubspot Product Property
     - Hubspot Data Type

