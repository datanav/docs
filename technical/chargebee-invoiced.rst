==============================
Chargebee to Invoiced Dataflow
==============================

Generated: 2024-09-23 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Invoiced Customers (organisation data)
-----------------------------------------------------------
Every Chargebee Address will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Chargebee Address and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type
   * - addr
     - address1
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - subscription_id
     - id
     - "string"
   * - zip
     - postal_code
     - "string"


Chargebee Address to Invoiced Customers (human data)
----------------------------------------------------
Every Chargebee Address will be synchronized with a Invoiced Customers (human data).

Once a link between a Chargebee Address and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type
   * - addr
     - address1
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - subscription_id
     - id
     - "string"
   * - zip
     - postal_code
     - "string"


Chargebee Customer to Invoiced Customers (organisation data)
------------------------------------------------------------
Every Chargebee Customer will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Chargebee Customer and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


Chargebee Customer to Invoiced Customers (human data)
-----------------------------------------------------
Every Chargebee Customer will be synchronized with a Invoiced Customers (human data).

Once a link between a Chargebee Customer and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Invoiced Customers (human data) Property
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

