==================
Exact to  Dataflow
==================

Generated: 2024-09-03 08:16:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Customers company
------------------------------------
Every Exact Accounts will be synchronized with a  Customers company.

Once a link between a Exact Accounts and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Customers company Property
     -  Data Type
   * - Name
     - name
     - "string"


Exact Items to  Items
---------------------
Every Exact Items will be synchronized with a  Items.

Once a link between a Exact Items and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Items:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Items Property
     -  Data Type


Exact Salesorderlines to  Lineitem
----------------------------------
Every Exact Salesorderlines will be synchronized with a  Lineitem.

Once a link between a Exact Salesorderlines and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Lineitem Property
     -  Data Type


Exact Salesorders to  Invoices
------------------------------
Every Exact Salesorders will be synchronized with a  Invoices.

Once a link between a Exact Salesorders and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     -  Invoices Property
     -  Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discounts
     - "string"

