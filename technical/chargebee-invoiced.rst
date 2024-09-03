======================
Chargebee to  Dataflow
======================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to  Customers person
---------------------------------------
Every Chargebee Customer will be synchronized with a  Customers person.

Once a link between a Chargebee Customer and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     -  Customers person Property
     -  Data Type


Chargebee Item to  Items
------------------------
Every Chargebee Item will be synchronized with a  Items.

Once a link between a Chargebee Item and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a  Items:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     -  Items Property
     -  Data Type


Chargebee Order to  Invoices
----------------------------
Every Chargebee Order will be synchronized with a  Invoices.

Once a link between a Chargebee Order and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     -  Invoices Property
     -  Data Type
   * - currency_code
     - currency
     - "string"
   * - customer_id
     - customer
     - "string"

