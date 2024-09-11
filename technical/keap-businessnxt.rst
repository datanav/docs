============================
Keap to BusinessNxt Dataflow
============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to Visma Address
-------------------------------
Every Keap Companies will be synchronized with a Visma Address.

Once a link between a Keap Companies and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - Visma Address Property
     - Visma Data Type
   * - company_name
     - name
     - "string"


Keap Opportunity to Visma Order
-------------------------------
Every Keap Opportunity will be synchronized with a Visma Order.

Once a link between a Keap Opportunity and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - Visma Order Property
     - Visma Data Type
   * - opportunity_title
     - name
     - "string"


Keap Product to BusinessNxt Product
-----------------------------------
Every Keap Product will be synchronized with a BusinessNxt Product.

Once a link between a Keap Product and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - product_desc
     - description
     - "string"
   * - product_price
     - priceQuantity
     - "string"

