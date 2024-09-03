=======================
Webcrm to Keap Dataflow
=======================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Keap Opportunity
----------------------------------------
Every Webcrm Opportunities will be synchronized with a Keap Opportunity.

Once a link between a Webcrm Opportunities and a Keap Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Keap Opportunity:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Keap Opportunity Property
     - Keap Data Type


Webcrm Products to Keap Product
-------------------------------
Every Webcrm Products will be synchronized with a Keap Product.

Once a link between a Webcrm Products and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Keap Product Property
     - Keap Data Type
   * - ProductPrice
     - product_price
     - "string"

