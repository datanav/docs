====================
HubSpot to  Dataflow
====================

Generated: 2024-08-29 08:03:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Deal to  Invoices
-------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Invoices.

Once a link between a HubSpot Deal and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Invoices Property
     -  Data Type
   * - properties.deal_currency_code
     - currency
     - "string"


HubSpot Lineitem to  Lineitem
-----------------------------
Every HubSpot Lineitem will be synchronized with a  Lineitem.

Once a link between a HubSpot Lineitem and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Lineitem Property
     -  Data Type
   * - properties.description
     - items.description
     - "string"
   * - properties.hs_discount_percentage
     - items.discounts
     - "string"
   * - properties.name
     - items.name
     - "string"
   * - properties.price
     - items.amount
     - "string"
   * - properties.quantity
     - items.quantity
     - "string"


HubSpot Product to  Items
-------------------------
Every HubSpot Product will be synchronized with a  Items.

Once a link between a HubSpot Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Items Property
     -  Data Type
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - unit_cost
     - "string"
   * - properties.name
     - name
     - "string"

