====================
Wix.com to  Dataflow
====================

Generated: 2023-11-30 13:24:08

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Orders to  Salesorders
------------------------------
Every Wix.com Orders will be synchronized with a  Salesorders.

Once a link between a Wix.com Orders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorders Property
     -  Data Type
   * - buyerInfo.id
     - customerId
     - "string"

