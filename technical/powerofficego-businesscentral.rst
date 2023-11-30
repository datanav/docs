==========================
Powerofficego to  Dataflow
==========================

Generated: 2023-11-30 20:49:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Product to  Items
-------------------------------
Every Powerofficego Product will be synchronized with a  Items.

Once a link between a Powerofficego Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Items Property
     -  Data Type


Powerofficego Customers to  Company
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Company.

Once a link between a Powerofficego Customers and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Company Property
     -  Data Type


Powerofficego Departments to  Company
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Company.

Once a link between a Powerofficego Departments and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Company Property
     -  Data Type


Powerofficego Salesorderlines to  Salesorderlines
-------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Salesorderlines.

Once a link between a Powerofficego Salesorderlines and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Salesorderlines Property
     -  Data Type
   * - Allowance
     - discountPercent
     - "string"
   * - ProductId
     - itemId
     - "string"
   * - ProductUnitPrice
     - amountExcludingTax
     - "string"
   * - Quantity
     - invoiceQuantity
     - "string"
   * - Quantity
     - quantity
     - "string"


Powerofficego Salesorders to  Salesorders
-----------------------------------------
Every Powerofficego Salesorders will be synchronized with a  Salesorders.

Once a link between a Powerofficego Salesorders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Salesorders Property
     -  Data Type
   * - CustomerReferenceContactPersonId
     - customerId
     - "string"
   * - SalesOrderDate
     - orderDate
     - "string"
   * - TotalAmount
     - totalAmountExcludingTax
     - "string"

