======================================
PowerOffice GO to WooCommerce Dataflow
======================================

Generated: 2024-10-25 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Product to WooCommerce Product
---------------------------------------------
Every PowerOffice GO Product will be synchronized with a WooCommerce Product.

Once a link between a PowerOffice GO Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - costPrice
     - price
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - sale_price
     - "string"


PowerOffice GO Salesorders to WooCommerce Order
-----------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a WooCommerce Order.

Once a link between a PowerOffice GO Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

