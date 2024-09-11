=======================================
BusinessNxt to BusinessCentral Dataflow
=======================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


BusinessNxt Order to BusinessCentral Salesorders
------------------------------------------------
Every BusinessNxt Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a BusinessNxt Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
   * - dueDate
     - requestedDeliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A


BusinessNxt Orderline to BusinessCentral Salesorderlines
--------------------------------------------------------
Every BusinessNxt Orderline will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a BusinessNxt Orderline and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
   * - orderNo
     - documentId
     - "string"


BusinessNxt Product to BusinessCentral Items
--------------------------------------------
Every BusinessNxt Product will be synchronized with a BusinessCentral Items.

Once a link between a BusinessNxt Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - priceQuantity
     - unitPrice
     - N/A

