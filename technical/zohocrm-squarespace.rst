====================
ZohoCRM to  Dataflow
====================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Deal to  Order
----------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Order.

Once a link between a ZohoCRM Deal and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Order Property
     -  Data Type

