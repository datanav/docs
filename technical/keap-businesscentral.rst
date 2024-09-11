================================
Keap to BusinessCentral Dataflow
================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to BusinessCentral Companies
-------------------------------------------
Every Keap Companies will be synchronized with a BusinessCentral Companies.

Once a link between a Keap Companies and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Keap Product to BusinessCentral Items
-------------------------------------
Every Keap Product will be synchronized with a BusinessCentral Items.

Once a link between a Keap Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - product_name
     - displayName
     - "string"
   * - product_price
     - unitPrice
     - N/A

