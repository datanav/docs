===============================
Salesforce to Invoiced Dataflow
===============================

Generated: 2024-09-23 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Customer to Invoiced Customers (organisation data)
-------------------------------------------------------------
Every Salesforce Customer will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Salesforce Customer and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


Salesforce Customer to Invoiced Customers (human data)
------------------------------------------------------
Every Salesforce Customer will be synchronized with a Invoiced Customers (human data).

Once a link between a Salesforce Customer and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type


Salesforce Invoiceline to Invoiced Lineitem
-------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Invoiced Lineitem.

Once a link between a Salesforce Invoiceline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Salesforce Order to Invoiced Invoices
-------------------------------------
Every Salesforce Order will be synchronized with a Invoiced Invoices.

Once a link between a Salesforce Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type


Salesforce Orderitem to Invoiced Lineitem
-----------------------------------------
Every Salesforce Orderitem will be synchronized with a Invoiced Lineitem.

Once a link between a Salesforce Orderitem and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Salesforce Product2 to Invoiced Items
-------------------------------------
Every Salesforce Product2 will be synchronized with a Invoiced Items.

Once a link between a Salesforce Product2 and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"


Salesforce Quotelineitem to Invoiced Lineitem
---------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Invoiced Lineitem.

Once a link between a Salesforce Quotelineitem and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Invoiced Lineitem Property
     - Invoiced Data Type

