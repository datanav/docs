==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to  Products
----------------------------------
Every Powerofficego Product will be synchronized with a  Products.

Once a link between a Powerofficego Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Products Property
     -  Data Type
   * - costPrice
     - price
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - sale_price
     - "string"


Powerofficego Salesorders to  Orders
------------------------------------
Every Powerofficego Salesorders will be synchronized with a  Orders.

Once a link between a Powerofficego Salesorders and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Orders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Orders Property
     -  Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

