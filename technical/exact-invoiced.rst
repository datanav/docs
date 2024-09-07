==========================
Exact to Invoiced Dataflow
==========================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Invoiced Customers company
--------------------------------------------
Every Exact Accounts will be synchronized with a Invoiced Customers company.

Once a link between a Exact Accounts and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


Exact Items to Invoiced Items
-----------------------------
Every Exact Items will be synchronized with a Invoiced Items.

Once a link between a Exact Items and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Invoiced Items Property
     - Invoiced Data Type


Exact Salesorderlines to Invoiced Lineitem
------------------------------------------
Every Exact Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a Exact Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Exact Salesorders to Invoiced Invoices
--------------------------------------
Every Exact Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a Exact Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discounts
     - "string"

