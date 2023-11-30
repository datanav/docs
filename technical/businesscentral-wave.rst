============================
Businesscentral to  Dataflow
============================

Generated: 2023-11-30 13:24:08

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

