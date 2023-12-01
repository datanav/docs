============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-01 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Product
---------------------------------
Before any synchronization can take place, a link between a Businesscentral Items and a  Product must be established.

A new  Product will be created from a Businesscentral Items if it is connected to a Businesscentral Salesorders that is synchronized into .

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type


Businesscentral Salesorders to  Invoice
---------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Invoice.

Once a link between a Businesscentral Salesorders and a  Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Invoice:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Invoice Property
     -  Data Type
   * - customerId
     - customer.id
     - "string"

