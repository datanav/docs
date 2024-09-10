=====================
Invoiced to  Dataflow
=====================

Generated: 2024-09-10 13:18:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to  Customer
---------------------------------------
Every Invoiced Customers company will be synchronized with a  Customer.

Once a link between a Invoiced Customers company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a  Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     -  Customer Property
     -  Data Type
   * - name
     - Name
     - "string"

