=========================================
Business Nxt to Business Central Dataflow
=========================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to Business Central Companies
--------------------------------------------------
Every Business Nxt Address will be synchronized with a Business Central Companies.

Once a link between a Business Nxt Address and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - Business Central Companies Property
     - Business Central Data Type


Business Nxt Company to Business Central Companies
--------------------------------------------------
Every Business Nxt Company will be synchronized with a Business Central Companies.

Once a link between a Business Nxt Company and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - Business Central Companies Property
     - Business Central Data Type


Business Nxt Order to Business Central Salesorders
--------------------------------------------------
Every Business Nxt Order will be synchronized with a Business Central Salesorders.

Once a link between a Business Nxt Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - dueDate
     - requestedDeliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A


Business Nxt Orderline to Business Central Salesorderlines
----------------------------------------------------------
Every Business Nxt Orderline will be synchronized with a Business Central Salesorderlines.

Once a link between a Business Nxt Orderline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - orderNo
     - documentId
     - "string"


Business Nxt Product to Business Central Items
----------------------------------------------
Every Business Nxt Product will be synchronized with a Business Central Items.

Once a link between a Business Nxt Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - priceQuantity
     - unitPrice
     - N/A

