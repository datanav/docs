================================
Wix.com to Business Nxt Dataflow
================================

Generated: 2024-09-12 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to Business Nxt Currency
-------------------------------------------
Every Wix.com Currencies will be synchronized with a Business Nxt Currency.

Once a link between a Wix.com Currencies and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Business Nxt Currency Property
     - Business Nxt Data Type


Wix.com Orders to Business Nxt Order
------------------------------------
Every Wix.com Orders will be synchronized with a Business Nxt Order.

Once a link between a Wix.com Orders and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - billingInfo.paidDate
     - settlementDate
     - "string"
   * - dateCreated
     - invoiceDate
     - "string"


Wix.com Orders to Business Nxt Orderline
----------------------------------------
Every Wix.com Orders will be synchronized with a Business Nxt Orderline.

Once a link between a Wix.com Orders and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - id
     - orderNo
     - "string"


Wix.com Products to Business Nxt Product
----------------------------------------
Every Wix.com Products will be synchronized with a Business Nxt Product.

Once a link between a Wix.com Products and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - priceData.price
     - priceQuantity
     - "string"

