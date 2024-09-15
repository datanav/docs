===========================
WebCRM to Invoiced Dataflow
===========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Products to Invoiced Items
---------------------------------
Every WebCRM Products will be synchronized with a Invoiced Items.

Once a link between a WebCRM Products and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - ProductCostPrice
     - unit_cost
     - "string"


WebCRM Quotationline to Invoiced Lineitem
-----------------------------------------
Every WebCRM Quotationline will be synchronized with a Invoiced Lineitem.

Once a link between a WebCRM Quotationline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type

