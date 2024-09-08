================================
Keap to Businesscentral Dataflow
================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Businesscentral Companies
-------------------------------------------
Every Keap Companies will be synchronized with a Businesscentral Companies.

Once a link between a Keap Companies and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Keap Product to Businesscentral Items
-------------------------------------
Every Keap Product will be synchronized with a Businesscentral Items.

Once a link between a Keap Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - product_name
     - displayName
     - "string"
   * - product_price
     - unitPrice
     - N/A

