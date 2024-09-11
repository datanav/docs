===============================
Custom ERP to Invoiced Dataflow
===============================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Custom ERP to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CustomERP Customer to Invoiced Customers company
------------------------------------------------
Every CustomERP Customer will be synchronized with a Invoiced Customers company.

Once a link between a CustomERP Customer and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomERP Customer and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - CustomERP Customer Property
     - Invoiced Customers company Property
     - Invoiced Data Type


CustomERP Order to Invoiced Invoices
------------------------------------
Every CustomERP Order will be synchronized with a Invoiced Invoices.

Once a link between a CustomERP Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomERP Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - CustomERP Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type


CustomERP Product to Invoiced Items
-----------------------------------
Every CustomERP Product will be synchronized with a Invoiced Items.

Once a link between a CustomERP Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CustomERP Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - CustomERP Product Property
     - Invoiced Items Property
     - Invoiced Data Type

