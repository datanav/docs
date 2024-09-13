==============================
Chargebee to Invoiced Dataflow
==============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Invoiced Customers person
-----------------------------------------------
Every Chargebee Customer will be synchronized with a Invoiced Customers person.

Once a link between a Chargebee Customer and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Invoiced Customers person Property
     - Invoiced Data Type


Chargebee Item to Invoiced Items
--------------------------------
Every Chargebee Item will be synchronized with a Invoiced Items.

Once a link between a Chargebee Item and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Invoiced Items Property
     - Invoiced Data Type


Chargebee Order to Invoiced Invoices
------------------------------------
Every Chargebee Order will be synchronized with a Invoiced Invoices.

Once a link between a Chargebee Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currency_code
     - currency
     - "string"
   * - customer_id
     - customer
     - "string"

