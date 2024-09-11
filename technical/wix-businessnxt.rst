======================================
Wix.com to Visma Business Nxt Dataflow
======================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to Visma Currency
------------------------------------
Every Wix.com Currencies will be synchronized with a Visma Currency.

Once a link between a Wix.com Currencies and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Visma Currency Property
     - Visma Data Type


Wix.com Orders to Visma Order
-----------------------------
Every Wix.com Orders will be synchronized with a Visma Order.

Once a link between a Wix.com Orders and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Visma Order Property
     - Visma Data Type
   * - billingInfo.paidDate
     - settlementDate
     - "string"
   * - dateCreated
     - invoiceDate
     - "string"


Wix.com Orders to Visma Orderline
---------------------------------
Every Wix.com Orders will be synchronized with a Visma Orderline.

Once a link between a Wix.com Orders and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Visma Orderline Property
     - Visma Data Type
   * - id
     - orderNo
     - "string"


Wix.com Products to Visma Product
---------------------------------
Every Wix.com Products will be synchronized with a Visma Product.

Once a link between a Wix.com Products and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Visma Product Property
     - Visma Data Type
   * - priceData.price
     - priceQuantity
     - "string"

