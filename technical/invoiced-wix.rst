========================
Invoiced to Wix Dataflow
========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to Wix Contacts
---------------------------------
Every Invoiced Contacts will be synchronized with a Wix Contacts.

Once a link between a Invoiced Contacts and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - primaryInfo.email
     - "string"


Invoiced Invoices to Wix Orders
-------------------------------
Every Invoiced Invoices will be synchronized with a Wix Orders.

Once a link between a Invoiced Invoices and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Wix Orders Property
     - Wix Data Type


Invoiced Items to Wix Products
------------------------------
Every Invoiced Items will be synchronized with a Wix Products.

Once a link between a Invoiced Items and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Wix Products Property
     - Wix Data Type
   * - currency
     - priceData.currency
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costAndProfitData.itemCost
     - N/A

