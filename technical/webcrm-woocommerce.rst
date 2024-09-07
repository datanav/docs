==============================
Webcrm to Woocommerce Dataflow
==============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Products to Woocommerce Product
--------------------------------------
Every Webcrm Products will be synchronized with a Woocommerce Product.

Once a link between a Webcrm Products and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - ProductCostPrice
     - price
     - "string"
   * - ProductPrice
     - sale_price
     - "string"

