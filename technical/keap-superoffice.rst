============================
Keap to Superoffice Dataflow
============================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Opportunity to Superoffice Sale
------------------------------------
Every Keap Opportunity will be synchronized with a Superoffice Sale.

Once a link between a Keap Opportunity and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Superoffice Sale Property
     - Superoffice Data Type
   * - opportunity_title
     - Heading
     - "string"


Keap Product to Superoffice Product
-----------------------------------
Every Keap Product will be synchronized with a Superoffice Product.

Once a link between a Keap Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - product_desc
     - Description
     - "string"
   * - product_name
     - Name
     - "string"
   * - product_price
     - UnitListPrice
     - N/A

