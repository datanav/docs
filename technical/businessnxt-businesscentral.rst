========================================
BusinessNxt to Business Central Dataflow
========================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Businesscentral Companies
------------------------------------------
Every Visma Address will be synchronized with a Businesscentral Companies.

Once a link between a Visma Address and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Visma Company to Businesscentral Companies
------------------------------------------
Every Visma Company will be synchronized with a Businesscentral Companies.

Once a link between a Visma Company and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Visma Order to Business Salesorders
-----------------------------------
Every Visma Order will be synchronized with a Business Salesorders.

Once a link between a Visma Order and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Business Salesorders Property
     - Business Data Type
   * - dueDate
     - requestedDeliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A


Visma Orderline to Business Salesorderlines
-------------------------------------------
Every Visma Orderline will be synchronized with a Business Salesorderlines.

Once a link between a Visma Orderline and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Business Salesorderlines Property
     - Business Data Type
   * - orderNo
     - documentId
     - "string"


Visma Product to Business Items
-------------------------------
Every Visma Product will be synchronized with a Business Items.

Once a link between a Visma Product and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Business Items:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Business Items Property
     - Business Data Type
   * - priceQuantity
     - unitPrice
     - N/A

