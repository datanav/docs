=====================
Invoiced to  Dataflow
=====================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Items to  Inventory
----------------------------
Every Invoiced Items will be synchronized with a  Inventory.

Once a link between a Invoiced Items and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     -  Inventory Property
     -  Data Type


Invoiced Invoices to  Order
---------------------------
Every Invoiced Invoices will be synchronized with a  Order.

Once a link between a Invoiced Invoices and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a  Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     -  Order Property
     -  Data Type


Invoiced Items to  Inventory
----------------------------
Every Invoiced Items will be synchronized with a  Inventory.

Once a link between a Invoiced Items and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     -  Inventory Property
     -  Data Type
   * - description
     - descriptor
     - "string"


Invoiced Items to  Sesamproducts
--------------------------------
Every Invoiced Items will be synchronized with a  Sesamproducts.

Once a link between a Invoiced Items and a  Sesamproducts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a  Sesamproducts:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     -  Sesamproducts Property
     -  Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - variants.pricing.basePrice.value
     - "string"

