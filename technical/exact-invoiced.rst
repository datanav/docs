=================================
Exact Online to Invoiced Dataflow
=================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to Invoiced Customers company
---------------------------------------------------
Every Exact Online Accounts will be synchronized with a Invoiced Customers company.

Once a link between a Exact Online Accounts and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - Name
     - name
     - "string"


Exact Online Items to Invoiced Items
------------------------------------
Every Exact Online Items will be synchronized with a Invoiced Items.

Once a link between a Exact Online Items and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - Invoiced Items Property
     - Invoiced Data Type


Exact Online Salesorderlines to Invoiced Lineitem
-------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a Invoiced Lineitem.

Once a link between a Exact Online Salesorderlines and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Exact Online Salesorders to Invoiced Invoices
---------------------------------------------
Every Exact Online Salesorders will be synchronized with a Invoiced Invoices.

Once a link between a Exact Online Salesorders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discounts
     - "string"

