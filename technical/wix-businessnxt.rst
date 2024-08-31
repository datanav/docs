====================
Wix.com to  Dataflow
====================

Generated: 2024-08-31 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to  Currency
-------------------------------
Every Wix.com Currencies will be synchronized with a  Currency.

Once a link between a Wix.com Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     -  Currency Property
     -  Data Type


Wix.com Orders to  Order
------------------------
Every Wix.com Orders will be synchronized with a  Order.

Once a link between a Wix.com Orders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Order Property
     -  Data Type
   * - billingInfo.paidDate
     - settlementDate
     - "string"
   * - dateCreated
     - invoiceDate
     - "string"


Wix.com Orders to  Orderline
----------------------------
Every Wix.com Orders will be synchronized with a  Orderline.

Once a link between a Wix.com Orders and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Orderline Property
     -  Data Type
   * - id
     - orderNo
     - "string"


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
   * - priceData.price
     - priceQuantity
     - "string"

