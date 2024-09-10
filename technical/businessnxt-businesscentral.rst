=======================================
Businessnxt to Businesscentral Dataflow
=======================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Businesscentral Companies
------------------------------------------------
Every Businessnxt Address will be synchronized with a Businesscentral Companies.

Once a link between a Businessnxt Address and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Businessnxt Company to Businesscentral Companies
------------------------------------------------
Every Businessnxt Company will be synchronized with a Businesscentral Companies.

Once a link between a Businessnxt Company and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Businessnxt Order to Businesscentral Salesorders
------------------------------------------------
Every Businessnxt Order will be synchronized with a Businesscentral Salesorders.

Once a link between a Businessnxt Order and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
   * - dueDate
     - requestedDeliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A


Businessnxt Orderline to Businesscentral Salesorderlines
--------------------------------------------------------
Every Businessnxt Orderline will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Businessnxt Orderline and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - orderNo
     - documentId
     - "string"


Businessnxt Product to Businesscentral Items
--------------------------------------------
Every Businessnxt Product will be synchronized with a Businesscentral Items.

Once a link between a Businessnxt Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - priceQuantity
     - unitPrice
     - N/A

