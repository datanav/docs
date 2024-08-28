====================
Wix.com to  Dataflow
====================

Generated: 2024-08-28 08:12:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Orders to  Invoices
---------------------------
Every Wix.com Orders will be synchronized with a  Invoices.

Once a link between a Wix.com Orders and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Invoices Property
     -  Data Type
   * - buyerInfo.id
     - customer
     - "string"
   * - currency
     - currency
     - "string"

