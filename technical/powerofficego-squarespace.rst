===========================
PowerOffice GO to  Dataflow
===========================

Generated: 2024-09-24 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Product to  Inventory
------------------------------------
Every PowerOffice GO Product will be synchronized with a  Inventory.

Once a link between a PowerOffice GO Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     -  Inventory Property
     -  Data Type


PowerOffice GO Product to  Inventory
------------------------------------
Every PowerOffice GO Product will be synchronized with a  Inventory.

Once a link between a PowerOffice GO Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     -  Inventory Property
     -  Data Type
   * - availableStock
     - quantity
     - "string"
   * - description
     - descriptor
     - "string"


PowerOffice GO Product to  Sesamproducts
----------------------------------------
Every PowerOffice GO Product will be synchronized with a  Sesamproducts.

Once a link between a PowerOffice GO Product and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     -  Sesamproducts Property
     -  Data Type
   * - availableStock
     - variants.stock.quantity
     - "string"
   * - costPrice
     - variants.pricing.basePrice.value
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - variants.pricing.salePrice.value
     - "string"
   * - type
     - type
     - "string"


PowerOffice GO Salesorders to  Order
------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a  Order.

Once a link between a PowerOffice GO Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     -  Order Property
     -  Data Type

