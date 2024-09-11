=================================
Exact Online to Invoiced Dataflow
=================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Invoiced Customers company
--------------------------------------------------
Every ExactOnline Accounts will be synchronized with a Invoiced Customers company.

Once a link between a ExactOnline Accounts and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


ExactOnline Items to Invoiced Items
-----------------------------------
Every ExactOnline Items will be synchronized with a Invoiced Items.

Once a link between a ExactOnline Items and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - Invoiced Items Property
     - Invoiced Data Type


ExactOnline Salesorderlines to Invoiced Lineitem
------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a ExactOnline Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


ExactOnline Salesorders to Invoiced Invoices
--------------------------------------------
Every ExactOnline Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a ExactOnline Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discounts
     - "string"

