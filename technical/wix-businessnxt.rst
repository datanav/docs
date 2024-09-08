===============================
Wix.com to Businessnxt Dataflow
===============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to Businessnxt Currency
------------------------------------------
Every Wix.com Currencies will be synchronized with a Businessnxt Currency.

Once a link between a Wix.com Currencies and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Businessnxt Currency Property
     - Businessnxt Data Type


Wix.com Orders to Businessnxt Order
-----------------------------------
Every Wix.com Orders will be synchronized with a Businessnxt Order.

Once a link between a Wix.com Orders and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - billingInfo.paidDate
     - settlementDate
     - "string"
   * - dateCreated
     - invoiceDate
     - "string"


Wix.com Orders to Businessnxt Orderline
---------------------------------------
Every Wix.com Orders will be synchronized with a Businessnxt Orderline.

Once a link between a Wix.com Orders and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - id
     - orderNo
     - "string"


Wix.com Products to Businessnxt Product
---------------------------------------
Every Wix.com Products will be synchronized with a Businessnxt Product.

Once a link between a Wix.com Products and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - priceData.price
     - priceQuantity
     - "string"

