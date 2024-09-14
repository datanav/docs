============================
Invoiced to Tilores Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers person to Tilores Human
------------------------------------------
Every Invoiced Customers person will be synchronized with a Tilores Human.

Once a link between a Invoiced Customers person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Tilores Human Property
     - Tilores Data Type
   * - city
     - city
     - "string"
   * - id
     - id
     - "string"
   * - postal_code
     - postalCode
     - "string"

