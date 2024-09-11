===============================
Wix.com to BusinessNxt Dataflow
===============================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to BusinessNxt Currency
------------------------------------------
Every Wix.com Currencies will be synchronized with a BusinessNxt Currency.

Once a link between a Wix.com Currencies and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type


Wix.com Orders to BusinessNxt Order
-----------------------------------
Every Wix.com Orders will be synchronized with a BusinessNxt Order.

Once a link between a Wix.com Orders and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - billingInfo.paidDate
     - settlementDate
     - "string"
   * - dateCreated
     - invoiceDate
     - "string"


Wix.com Orders to BusinessNxt Orderline
---------------------------------------
Every Wix.com Orders will be synchronized with a BusinessNxt Orderline.

Once a link between a Wix.com Orders and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - id
     - orderNo
     - "string"


Wix.com Products to BusinessNxt Product
---------------------------------------
Every Wix.com Products will be synchronized with a BusinessNxt Product.

Once a link between a Wix.com Products and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - priceData.price
     - priceQuantity
     - "string"

