===========================
Webcrm to Invoiced Dataflow
===========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Products to Invoiced Items
---------------------------------
Every Webcrm Products will be synchronized with a Invoiced Items.

Once a link between a Webcrm Products and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - ProductCostPrice
     - unit_cost
     - "string"


Webcrm Quotationline to Invoiced Lineitem
-----------------------------------------
Every Webcrm Quotationline will be synchronized with a Invoiced Lineitem.

Once a link between a Webcrm Quotationline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type

