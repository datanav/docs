=====================================
Powerofficego to Woocommerce Dataflow
=====================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to Woocommerce Product
--------------------------------------------
Every Powerofficego Product will be synchronized with a Woocommerce Product.

Once a link between a Powerofficego Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - costPrice
     - price
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - sale_price
     - "string"


Powerofficego Salesorders to Woocommerce Order
----------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Woocommerce Order.

Once a link between a Powerofficego Salesorders and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

