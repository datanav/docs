====================================
HubSpot to Business Central Dataflow
====================================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Business Central Companies
---------------------------------------------
Every HubSpot Company will be synchronized with a Business Central Companies.

Once a link between a HubSpot Company and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Business Central Companies Property
     - Business Central Data Type


HubSpot Deal to Business Central Salesorders
--------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Business Central Salesorders.

Once a link between a HubSpot Deal and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - properties.closedate
     - orderDate
     - N/A
   * - properties.closedate
     - requestedDeliveryDate
     - N/A
   * - properties.deal_currency_code
     - currencyId
     - "string"


HubSpot Lineitem to Business Central Salesorderlines
----------------------------------------------------
Every HubSpot Lineitem will be synchronized with a Business Central Salesorderlines.

Once a link between a HubSpot Lineitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - properties.hs_discount_percentage
     - discountPercent
     - N/A
   * - properties.hs_product_id
     - itemId
     - "string"
   * - properties.name
     - description
     - "string"
   * - properties.price
     - unitPrice
     - "float"
   * - properties.quantity
     - quantity
     - N/A


HubSpot Lineitemdealassociationtype to Business Central Salesorderlines
-----------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Business Central Salesorderlines.

Once a link between a HubSpot Lineitemdealassociationtype and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


HubSpot Lineitemquoteassociationtype to Business Central Salesorderlines
------------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Business Central Salesorderlines.

Once a link between a HubSpot Lineitemquoteassociationtype and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


HubSpot Product to Business Central Items
-----------------------------------------
Every HubSpot Product will be synchronized with a Business Central Items.

Once a link between a HubSpot Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - properties.hs_cost_of_goods_sold
     - unitCost
     - N/A
   * - properties.name
     - displayName
     - "string"
   * - properties.price
     - unitPrice
     - N/A

