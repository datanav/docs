============================
Invoiced to Hubspot Dataflow
============================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Items to Hubspot Product
---------------------------------
Every Invoiced Items will be synchronized with a Hubspot Product.

Once a link between a Invoiced Items and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - unit_cost
     - properties.hs_cost_of_goods_sold
     - "string"


Invoiced Lineitem to Hubspot Lineitem
-------------------------------------
Every Invoiced Lineitem will be synchronized with a Hubspot Lineitem.

Once a link between a Invoiced Lineitem and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - items.amount
     - properties.price
     - "string"
   * - items.description
     - properties.description
     - "string"
   * - items.discounts
     - properties.hs_discount_percentage
     - "string"
   * - items.name
     - properties.name
     - "string"
   * - items.quantity
     - properties.quantity
     - N/A

